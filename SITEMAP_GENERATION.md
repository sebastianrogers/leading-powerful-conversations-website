# Dynamic Sitemap Generation

## Overview

The website now includes dynamic sitemap.xml generation that automatically discovers HTML pages and updates the sitemap with current modification dates and appropriate priorities.

## Files

- **`generate_sitemap.py`** - Main sitemap generator script
- **`update_sitemap.sh`** - Bash script for easy deployment updates
- **`site/sitemap.xml`** - Generated sitemap file

## How It Works

The sitemap generator:

1. **Scans** the `site/` directory for all `.html` files
2. **Determines** appropriate priority and change frequency for each page
3. **Gets** the last modification date from file system
4. **Generates** a properly formatted XML sitemap
5. **Validates** the output for compliance

## Page Priorities

- **Homepage** (`index.html`): Priority 1.0, Updated weekly
- **Main pages** (`bio.html`, `resources.html`, `contact.html`): Priority 0.8
- **Error pages** (`404.html`): Priority 0.1, Updated yearly
- **Other pages**: Priority 0.5, Updated monthly (default)

## Usage

### Automated Updates (GitHub Actions)

The sitemap is automatically generated and updated on every deployment via GitHub Actions. The workflow:

1. **Builds** the site normally
2. **Generates** fresh sitemap with current file dates
3. **Uses** the correct base URL for the deployment
4. **Includes** the updated sitemap in the deployed site

No manual intervention required! ✨

### Manual Update (Local Development)

```bash
# Run the Python script directly
python3 generate_sitemap.py

# Or use the bash wrapper script
./update_sitemap.sh
```

### Configuration for Different Environments

The sitemap generator automatically adapts based on environment:

- **Local development**: Uses relative URLs (no base URL)
- **GitHub Pages**: Uses full URLs with the repository's GitHub Pages domain
- **Custom domain**: Set `GITHUB_PAGES_URL` environment variable

### Configuration

To customize the sitemap generation, edit `generate_sitemap.py`:

- **`BASE_URL`**: Set your domain (leave empty for relative URLs)
- **`PAGE_PRIORITIES`**: Adjust priority values for specific pages
- **`CHANGE_FREQUENCIES`**: Set how often pages typically change

## Output

The generated sitemap includes:

- `<loc>` - Page URL (relative or absolute)
- `<lastmod>` - Last modification date (YYYY-MM-DD format)
- `<changefreq>` - How frequently the page changes
- `<priority>` - Relative importance (0.0 to 1.0)

## GitHub Actions Integration

The sitemap generation is integrated into the deployment workflow at [.github/workflows/pages.yml](.github/workflows/pages.yml):

```yaml
- name: Generate sitemap
  run: |
    echo "Generating dynamic sitemap.xml..."
    # Set the base URL for GitHub Pages
    export GITHUB_PAGES_URL="https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}"
    echo "Using base URL: $GITHUB_PAGES_URL"
    python3 generate_sitemap.py
    echo "Sitemap generated successfully"
```

This ensures:

- ✅ Sitemap is always current on deployment
- ✅ Absolute URLs are used for production
- ✅ No manual maintenance required
- ✅ Build fails if sitemap generation fails

## Benefits

1. **Automatic updates** - No manual maintenance required
2. **Current dates** - Last modified dates reflect actual file changes
3. **Proper priorities** - SEO-friendly page importance ranking
4. **Extensible** - Easy to add new pages or modify priorities
5. **Validated output** - Ensures compliance with sitemap standards

## SEO Impact

- Helps search engines discover all pages
- Provides hints about page importance and update frequency
- Ensures fresh modification dates for better crawling
- Compliant with sitemap protocol standards

## Deployment

The sitemap is automatically updated when you run the generation script. For production deployments:

1. Run `./update_sitemap.sh` as part of your build process
2. Ensure the generated `site/sitemap.xml` is deployed with your site
3. Update your `robots.txt` to reference the sitemap (already done)

## Future Enhancements

- Add support for news sitemaps if blog content is added
- Include image sitemaps for better image SEO
- Add automatic submission to search engines
- Integrate with content management workflow
