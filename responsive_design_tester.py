#!/usr/bin/env python3
"""
Responsive Design Testing Script for Leading Powerful Conversations Website
This script performs automated checks for responsive design best practices.
"""

import os
import re

class ResponsiveDesignTester:
    def __init__(self, base_url="site"):
        self.base_url = base_url
        self.pages = [
            'index.html',
            'bio.html',
            'contact.html',
            'resources.html'
        ]
        self.results = {}
        
    def test_viewport_meta_tag(self, html_content):
        """Check for proper viewport meta tag"""
        if 'name="viewport"' in html_content and 'width=device-width' in html_content:
            return True, "Viewport meta tag properly configured"
        else:
            return False, "No proper viewport meta tag found"
    
    def test_responsive_images(self, html_content):
        """Check for responsive image practices"""
        images = html_content.count('<img')
        
        if images == 0:
            return True, "No images found to test"
        
        # Check for alt attributes
        alt_count = html_content.count('alt="')
        if alt_count < images:
            return False, f"Found {images - alt_count} images missing alt text"
        
        return True, f"All {images} images have alt text"
    
    def test_mobile_navigation(self, html_content):
        """Check for mobile navigation elements"""
        if 'nav-toggle' in html_content and 'aria-label' in html_content:
            return True, "Mobile navigation properly implemented"
        else:
            return False, "No mobile navigation toggle found"
    
    def test_text_readability(self, html_content):
        """Check for text readability best practices"""
        # Simple check for paragraph structure
        paragraphs = html_content.count('<p>')
        if paragraphs > 0:
            return True, f"Found {paragraphs} paragraphs with proper structure"
        else:
            return False, "No properly structured paragraphs found"
    
    def test_css_media_queries(self, css_content):
        """Check for media queries in CSS"""
        if not css_content:
            return False, "No CSS content found"
        
        # Count media queries
        media_queries = len(re.findall(r'@media', css_content, re.IGNORECASE))
        
        if media_queries == 0:
            return False, "No media queries found in CSS"
        
        return True, f"Found {media_queries} media queries in CSS"
    
    def load_page_content(self, page):
        """Load page content for testing"""
        try:
            file_path = os.path.join(self.base_url, page)
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading {page}: {e}")
            return None
    
    def load_css_content(self):
        """Load CSS content for testing"""
        try:
            css_path = os.path.join(self.base_url, 'css', 'style.css')
            with open(css_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading CSS: {e}")
            return None
    
    def run_tests(self):
        """Run all responsive design tests"""
        print("🔍 Running Responsive Design Tests...")
        print("=" * 60)
        
        # Test CSS first
        css_content = self.load_css_content()
        css_result = self.test_css_media_queries(css_content)
        print(f"📱 CSS Media Queries: {'✅' if css_result[0] else '❌'} {css_result[1]}")
        print()
        
        # Test each page
        for page in self.pages:
            print(f"📄 Testing {page}...")
            html_content = self.load_page_content(page)
            
            if not html_content:
                print(f"   ❌ Could not load {page}")
                continue
            
            # Run tests
            tests = [
                ("Viewport Meta Tag", self.test_viewport_meta_tag(html_content)),
                ("Responsive Images", self.test_responsive_images(html_content)),
                ("Mobile Navigation", self.test_mobile_navigation(html_content)),
                ("Text Readability", self.test_text_readability(html_content))
            ]
            
            page_results = []
            for test_name, (passed, message) in tests:
                status = "✅" if passed else "❌"
                print(f"   {status} {test_name}: {message}")
                page_results.append((test_name, passed, message))
            
            self.results[page] = page_results
            print()
        
        # Summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary"""
        print("📊 Test Summary")
        print("=" * 60)
        
        total_tests = 0
        passed_tests = 0
        
        for page, tests in self.results.items():
            page_passed = sum(1 for _, passed, _ in tests if passed)
            total_page_tests = len(tests)
            
            total_tests += total_page_tests
            passed_tests += page_passed
            
            percentage = (page_passed / total_page_tests * 100) if total_page_tests > 0 else 0
            print(f"{page}: {page_passed}/{total_page_tests} tests passed ({percentage:.1f}%)")
        
        overall_percentage = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        print(f"\n🎯 Overall Score: {passed_tests}/{total_tests} tests passed ({overall_percentage:.1f}%)")
        
        if overall_percentage >= 90:
            print("🌟 Excellent responsive design implementation!")
        elif overall_percentage >= 75:
            print("👍 Good responsive design, minor improvements possible")
        elif overall_percentage >= 50:
            print("⚠️  Moderate responsive design, several areas need attention")
        else:
            print("🚨 Responsive design needs significant improvement")

if __name__ == "__main__":
    tester = ResponsiveDesignTester('site')
    tester.run_tests()