# Leading Powerful Conversations Website

A static website for "Leading Powerful Conversations" - a leadership coaching and development service.

## GitHub Pages Deployment

This website is designed to be hosted on GitHub Pages. To deploy:

1. Go to your repository settings
2. Navigate to the "Pages" section
3. Select the branch you want to deploy (e.g., `main` or `gh-pages`)
4. Select the root directory `/` as the source
5. Save and wait for GitHub Pages to deploy your site

## Website Structure

- `index.html` - Home page
- `about.html` - About page
- `services.html` - Services page
- `contact.html` - Contact page
- `css/style.css` - Stylesheet
- `_config.yml` - Jekyll configuration for GitHub Pages

## Local Development

To view the site locally, you can:

1. Open `index.html` directly in your browser, or
2. Use a local web server:
   ```bash
   python3 -m http.server 8000
   ```
   Then visit http://localhost:8000

## Customization

To customize the website:

1. Update the HTML content in each `.html` file
2. Modify colors and styles in `css/style.css`
3. Update the contact form action URL in `contact.html` with your own form service

## Features

- Responsive design that works on mobile, tablet, and desktop
- Clean, professional styling
- Easy to customize and extend
- GitHub Pages compatible
- No build process required

## License

All rights reserved.