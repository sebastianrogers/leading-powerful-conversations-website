#!/usr/bin/env python3
"""
Dynamic Sitemap Generator for Leading Powerful Conversations Website

This script generates a sitemap.xml file based on the HTML files found in the site directory.
It automatically sets priorities and last modified dates based on file statistics and page types.
"""

import os
import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Configuration
SITE_DIR = "site"
# Base URL - will be set by environment variable in GitHub Actions, empty for local dev
BASE_URL = os.environ.get('GITHUB_PAGES_URL', '')  
SITEMAP_PATH = os.path.join(SITE_DIR, "sitemap.xml")

# Priority mapping for different page types
PAGE_PRIORITIES = {
    'index.html': '1.0',      # Homepage - highest priority
    'bio.html': '0.8',        # About/Bio page - high priority
    'resources.html': '0.8',  # Resources page - high priority
    'contact.html': '0.8',    # Contact page - high priority
    '404.html': '0.1',        # Error page - lowest priority
}

# Change frequency mapping
CHANGE_FREQUENCIES = {
    'index.html': 'weekly',
    'bio.html': 'monthly',
    'resources.html': 'weekly',
    'contact.html': 'monthly',
    '404.html': 'yearly',
}

def get_file_last_modified(file_path):
    """Get the last modified date of a file in ISO format."""
    timestamp = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def should_include_file(filename):
    """Determine if a file should be included in the sitemap."""
    # Include HTML files but exclude certain patterns
    if not filename.endswith('.html'):
        return False
    
    # Exclude files that shouldn't be indexed
    excluded_files = []  # Add any files to exclude here
    if filename in excluded_files:
        return False
    
    return True

def get_url_path(filename):
    """Convert filename to URL path."""
    if filename == 'index.html':
        return '/'
    return f'/{filename}'

def generate_sitemap():
    """Generate the sitemap.xml file."""
    print("Generating sitemap.xml...")
    
    if BASE_URL:
        print(f"Using base URL: {BASE_URL}")
    else:
        print("Using relative URLs (no base URL set)")
    
    # Create the root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Get all HTML files in the site directory
    site_path = Path(SITE_DIR)
    html_files = []
    
    for file_path in site_path.glob('*.html'):
        if should_include_file(file_path.name):
            html_files.append(file_path)
    
    # Sort files for consistent output
    html_files.sort(key=lambda x: x.name)
    
    # Add each page to the sitemap
    for file_path in html_files:
        filename = file_path.name
        
        # Create URL element
        url_elem = ET.SubElement(urlset, 'url')
        
        # Add location
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = BASE_URL + get_url_path(filename)
        
        # Add last modified date
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = get_file_last_modified(file_path)
        
        # Add change frequency
        changefreq = ET.SubElement(url_elem, 'changefreq')
        changefreq.text = CHANGE_FREQUENCIES.get(filename, 'monthly')
        
        # Add priority
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = PAGE_PRIORITIES.get(filename, '0.5')
        
        print(f"  Added: {get_url_path(filename)} (priority: {PAGE_PRIORITIES.get(filename, '0.5')})")
    
    # Create the XML tree
    tree = ET.ElementTree(urlset)
    
    # Pretty format the XML
    rough_string = ET.tostring(urlset, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent='  ')
    
    # Remove empty lines and fix formatting
    lines = [line for line in pretty_xml.split('\n') if line.strip()]
    pretty_xml = '\n'.join(lines)
    
    # Write to file
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"Sitemap generated successfully: {SITEMAP_PATH}")
    print(f"Total URLs: {len(html_files)}")

def validate_sitemap():
    """Basic validation of the generated sitemap."""
    try:
        tree = ET.parse(SITEMAP_PATH)
        root = tree.getroot()
        
        if root.tag != '{http://www.sitemaps.org/schemas/sitemap/0.9}urlset':
            print("Warning: Invalid root element in sitemap")
            return False
        
        url_count = len(root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'))
        print(f"Sitemap validation passed: {url_count} URLs found")
        return True
        
    except ET.ParseError as e:
        print(f"Sitemap validation failed: {e}")
        return False

if __name__ == "__main__":
    # Change to the project directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if site directory exists
    if not os.path.exists(SITE_DIR):
        print(f"Error: {SITE_DIR} directory not found!")
        exit(1)
    
    # Generate sitemap
    generate_sitemap()
    
    # Validate the generated sitemap
    validate_sitemap()
    
    print("\nTo update the sitemap in the future, simply run this script again.")
    print("Consider adding this to your deployment process for automatic updates.")