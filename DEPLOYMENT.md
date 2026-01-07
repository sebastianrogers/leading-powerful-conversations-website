# Deployment Guide - Leading Powerful Conversations Website

## Overview

This website is designed for easy deployment to GitHub Pages with zero configuration required. The deployment process is fully automated using GitHub Actions.

## GitHub Pages Deployment (Recommended)

### Initial Setup

1. **Repository Requirements**:
   - Repository must be public (or have GitHub Pro/Enterprise for private repos)
   - Repository contains the website files in the `site/` directory

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Navigate to **Settings** > **Pages**
   - Under "Source", select **GitHub Actions**
   - The deployment workflow is already configured in `.github/workflows/deploy.yml`

3. **Domain Configuration**:
   - **Default Domain**: Your site will be available at `https://[username].github.io/[repository-name]`
   - **Custom Domain** (optional): Add your domain in Settings > Pages > Custom domain

### Deployment Process

1. **Automatic Deployment**:
   - Every push to the `main` branch triggers automatic deployment
   - Deployment typically takes 2-5 minutes
   - Monitor progress in the **Actions** tab

2. **Manual Deployment**:
   - Go to **Actions** tab
   - Select "Deploy to GitHub Pages" workflow
   - Click "Run workflow" > "Run workflow"

### Deployment Verification

1. **Check Build Status**:
   - Visit the **Actions** tab in your repository
   - Look for green checkmark on latest deployment
   - Red X indicates deployment failure - click to see error details

2. **Test Deployed Site**:
   - Visit your GitHub Pages URL
   - Test all pages and functionality
   - Verify contact form works (first submission requires email confirmation)

## Alternative Deployment Options

### Netlify

1. **Setup**:
   - Connect your GitHub repository to Netlify
   - Set publish directory to `site/`
   - Deploy automatically on push to main

2. **Configuration**:
   - Build command: (leave empty)
   - Publish directory: `site`
   - Environment variables: (none required)

### Vercel

1. **Setup**:
   - Import your GitHub repository
   - Framework preset: Other
   - Output directory: `site`

### Traditional Web Hosting

1. **File Upload**:
   - Upload contents of `site/` directory to your web root
   - Ensure `index.html` is in the root directory
   - Verify file permissions allow web access

2. **Required Files**:
   - All files in `site/` directory
   - Maintain directory structure
   - Ensure `.htaccess` rules if using Apache

## Custom Domain Setup

### DNS Configuration

1. **For GitHub Pages**:
   - Add CNAME record: `www` → `[username].github.io`
   - Add A records for apex domain:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`

2. **SSL Certificate**:
   - GitHub Pages provides free SSL automatically
   - Enable "Enforce HTTPS" in repository settings

### Domain Verification

1. **GitHub Settings**:
   - Add custom domain in Settings > Pages
   - Wait for DNS check (can take up to 24 hours)
   - Enable "Enforce HTTPS"

## Deployment Checklist

### Pre-deployment
- [ ] Test locally on multiple browsers
- [ ] Verify all links work
- [ ] Check responsive design on different screen sizes
- [ ] Validate HTML/CSS
- [ ] Optimize images for web
- [ ] Update sitemap.xml if needed

### Post-deployment
- [ ] Verify site loads at deployed URL
- [ ] Test all navigation and internal links
- [ ] Submit contact form to test email delivery
- [ ] Check Google Analytics (if configured)
- [ ] Submit sitemap to Google Search Console

## Troubleshooting

### Common Issues

1. **404 Page Not Found**:
   - Verify files are in `site/` directory
   - Check GitHub Pages source configuration
   - Ensure `index.html` exists

2. **CSS/Images Not Loading**:
   - Verify relative paths in HTML
   - Check file case sensitivity
   - Ensure files exist in correct directories

3. **Contact Form Not Working**:
   - First submission requires email confirmation
   - Check Formspree endpoint URL
   - Verify email address is correct

4. **Custom Domain Issues**:
   - Verify DNS configuration
   - Wait up to 24 hours for propagation
   - Check GitHub Pages custom domain settings

### Getting Help

- Check GitHub Actions logs for deployment errors
- Verify repository settings
- Test locally before pushing changes
- Check GitHub Pages status page for service issues

## Rollback Procedure

1. **Quick Rollback**:
   - Revert commit in GitHub
   - Push to main branch
   - Wait for automatic redeployment

2. **Manual Rollback**:
   - Go to Actions > Previous successful deployment
   - Click "Re-run jobs"

Last updated: January 7, 2026