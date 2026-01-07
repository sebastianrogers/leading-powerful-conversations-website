# Google Search Console Setup Guide

## Overview

This guide walks you through setting up Google Search Console for the Leading Powerful Conversations website to monitor search performance, indexing status, and technical SEO issues.

## Step 1: Verify Website Ownership

### Option 1: HTML File Verification (Recommended)

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add Property" → "URL prefix"
3. Enter your website URL (e.g., `https://leadingpowerfulconversations.com`)
4. Choose "HTML file" verification method
5. Download the verification file (it will be named something like `googleXXXXXXXXXXXXXXXX.html`)
6. Upload this file to your website's root directory (`/site/` folder)
7. Click "Verify" in Google Search Console

### Option 2: HTML Tag Verification

1. Follow steps 1-4 above
2. Choose "HTML tag" verification method
3. Copy the provided meta tag
4. Add the meta tag to the `<head>` section of all your HTML pages (after the existing meta tags)
5. Click "Verify" in Google Search Console

### Option 3: Google Analytics Verification

If you already have Google Analytics set up:

1. Follow steps 1-4 above
2. Choose "Google Analytics" verification method
3. Ensure you're using the same Google account for both services
4. Click "Verify"

## Step 2: Submit Your Sitemap

1. In Google Search Console, go to "Sitemaps" in the left sidebar
2. Click "Add a new sitemap"
3. Enter: `sitemap.xml`
4. Click "Submit"

Your sitemap is already properly configured with:

- All main pages included
- Appropriate priority levels
- Change frequency settings
- Proper last modified dates

## Step 3: Set Up URL Prefixes (if needed)

If your site is accessible via both www and non-www versions:

1. Add both properties to Google Search Console:
   - `https://leadingpowerfulconversations.com`
   - `https://www.leadingpowerfulconversations.com`
2. Set your preferred version in Search Console settings
3. Ensure proper 301 redirects are configured

## Step 4: Configure Notifications

1. Go to "Settings" → "Users and permissions"
2. Add email addresses that should receive alerts
3. Configure notification preferences:
   - Critical crawling issues
   - Manual actions
   - Security issues
   - New enhancements

## Step 5: Initial Monitoring

After setup, monitor these key areas:

### Performance Tab

- Query performance
- Click-through rates
- Average position
- Impressions

### Coverage Tab

- Valid pages
- Errors (404s, server errors)
- Excluded pages
- Warnings

### Enhancements

- Mobile usability
- Core Web Vitals
- Page experience

### Security Issues

- Hacking attempts
- Malware detection

## Expected Timeline

- **Verification**: Immediate
- **Initial data**: 24-48 hours
- **Full data population**: 7-14 days
- **Trend analysis**: 30+ days

## Troubleshooting

### Common Verification Issues

- **File not found**: Ensure the verification file is in the root directory and accessible
- **Permissions**: Check file permissions (should be readable)
- **Caching**: Clear any CDN or browser caches

### Sitemap Issues

- **Not found**: Verify the sitemap.xml is accessible at `/sitemap.xml`
- **Format errors**: Validate XML syntax
- **URL mismatches**: Ensure URLs in sitemap match your actual site structure

## Maintenance

### Weekly

- Check for new errors in Coverage report
- Monitor Core Web Vitals

### Monthly

- Review performance trends
- Check for manual actions
- Update sitemap if site structure changes

### Quarterly

- Audit search queries and optimize content
- Review and update meta descriptions based on performance data

## Next Steps After Setup

1. ✅ Complete verification process
2. ✅ Submit sitemap
3. ✅ Configure email notifications
4. 📊 Wait for initial data (24-48 hours)
5. 🔍 Begin monitoring performance and coverage reports
6. 📈 Use insights to optimize content and technical SEO

## Integration with Other Tools

This setup complements your existing:

- Google Analytics (GA4)
- XML Sitemap
- robots.txt
- Meta tags and structured data

---

**Next TODO Items to Complete:**

- [ ] Optimize page titles and meta descriptions (use GSC data for insights)
- [ ] Add local business schema if applicable
- [ ] Set up automated lighthouse scores monitoring

Last updated: January 7, 2026
