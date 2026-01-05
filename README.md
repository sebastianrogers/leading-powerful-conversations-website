# Leading Powerful Conversations Website

A static website for "Leading Powerful Conversations" - a leadership coaching and development service.

## GitHub Pages Deployment

This website is optimized for GitHub Pages hosting with automatic deployment. To set up:

1. **Repository Setup**: Ensure your repository is public (or have GitHub Pro for private repos)
2. **Access Settings**: Go to your repository settings on GitHub
3. **Pages Configuration**: Navigate to the "Pages" section in the left sidebar
4. **Source Selection**:
   - Select "Deploy from a branch" as source
   - Choose the `main` branch (recommended)
   - Select the root directory `/` as the folder
5. **Save & Deploy**: Click "Save" - GitHub will automatically build and deploy your site
6. **Access Your Site**: Your site will be available at `https://[username].github.io/[repository-name]`
7. **Custom Domain** (Optional): Add a CNAME file to use a custom domain

**Note**: Deployment typically takes 5-10 minutes. Check the Actions tab for build status.

## Website Structure

- `index.html` - Home page
- `bio.html` - Biography/About page
- `contact.html` - Contact page
- `resources.html` - Resources page
- `404.html` - Custom error page
- `css/style.css` - Main stylesheet
- `robots.txt` - Search engine crawler instructions
- `sitemap.xml` - Site structure for search engines
- `images/` - Image assets directory

## Local Development

To view the site locally, you can:

1. Open `index.html` directly in your browser, or
2. Use a local web server:

   ```bash
   python3 -m http.server 8000
   ```

   Then visit <http://localhost:8000>

## Customization

To customize the website:

1. Update the HTML content in each `.html` file
2. Modify colors and styles in `css/style.css`
3. Update the contact form action URL in `contact.html` with your own form service

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
- **GitHub Pages Ready**: Instant deployment with version control integration
- **Accessibility Focused**: Semantic markup and keyboard navigation support

## License

All rights reserved.
