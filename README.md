# Leading Powerful Conversations Website

A static website for "Leading Powerful Conversations" - a leadership coaching and development service.

## GitHub Pages Deployment

This website is optimized for GitHub Pages hosting with automatic deployment using GitHub Actions. To set up:

1. **Repository Setup**: Ensure your repository is public (or have GitHub Pro for private repos)
2. **Access Settings**: Go to your repository settings on GitHub
3. **Pages Configuration**: Navigate to the "Pages" section in the left sidebar
4. **Source Selection**:
   - Select "GitHub Actions" as the source
   - The workflow will automatically deploy from the `site/` folder
5. **Automatic Deployment**: Push changes to the `main` branch to trigger deployment
6. **Access Your Site**: Your site will be available at `https://[username].github.io/[repository-name]`
7. **Custom Domain** (Optional): Add a CNAME file to the `site/` folder to use a custom domain

**Note**: Deployment typically takes 2-5 minutes. Check the Actions tab for build status.

## Website Structure

All website files are located in the `site/` directory:

- `site/index.html` - Home page
- `site/bio.html` - Biography/About page
- `site/contact.html` - Contact page
- `site/resources.html` - Resources page
- `site/404.html` - Custom error page
- `site/css/style.css` - Main stylesheet
- `site/robots.txt` - Search engine crawler instructions
- `site/sitemap.xml` - Site structure for search engines
- `site/images/` - Image assets directory

## Local Development

To view the site locally:

1. Navigate to the site directory:

   ```bash
   cd site
   ```

2. Start a local web server:

   ```bash
   python3 -m http.server 8000
   ```

   Then visit <http://localhost:8000>

## Customization

To customize the website:

1. Update the HTML content in each `.html` file in the `site/` directory
2. Modify colors and styles in `site/css/style.css`
3. Update the contact form action URL in `site/contact.html` with your own form service
4. Add new images to `site/images/` directory

## Contact Form Setup

The contact form uses [Formspree](https://formspree.io/) to handle form submissions and send emails to <sebastian@crazybearandraggedstaff.com>.

**First-time setup:**

1. When the first form submission is made, Formspree will send a confirmation email to <sebastian@crazybearandraggedstaff.com>
2. Click the confirmation link in that email to activate the form
3. After activation, all future form submissions will be forwarded to that email address

No additional configuration or API keys are required for basic functionality.

## Features

- **Fully Responsive**: Optimized for mobile, tablet, and desktop viewing
- **Professional Design**: Clean, modern styling that builds trust and credibility
- **SEO Optimized**: Includes sitemap.xml, robots.txt, and semantic HTML structure
- **Fast Loading**: Minimal dependencies and optimized assets for quick page loads
- **Easy Customization**: Simple HTML/CSS structure for quick modifications
- **Contact Integration**: Pre-configured Formspree contact form
- **Error Handling**: Custom 404 page for better user experience
- **Zero Dependencies**: No build process, frameworks, or external libraries required
- **GitHub Pages Ready**: Automated deployment with GitHub Actions from `site/` folder
- **Accessibility Focused**: Semantic markup and keyboard navigation support

## License

All rights reserved.
