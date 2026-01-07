#!/bin/bash

# Sitemap Update Script
# This script should be run during deployment or as part of a CI/CD pipeline

echo "🗺️  Updating sitemap.xml..."

# Navigate to the project directory
cd "$(dirname "$0")"

# Run the sitemap generator
python3 generate_sitemap.py

# Check if sitemap was generated successfully
if [ -f "site/sitemap.xml" ]; then
    echo "✅ Sitemap updated successfully"
    echo "📊 Sitemap location: site/sitemap.xml"
    
    # Display file stats
    echo "📈 Sitemap stats:"
    echo "   - File size: $(du -h site/sitemap.xml | cut -f1)"
    echo "   - Last modified: $(date -r site/sitemap.xml '+%Y-%m-%d %H:%M:%S')"
    echo "   - URL count: $(grep -c '<url>' site/sitemap.xml)"
else
    echo "❌ Failed to generate sitemap.xml"
    exit 1
fi

echo "🚀 Sitemap update complete!"