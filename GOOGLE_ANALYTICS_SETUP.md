# Google Analytics Setup Instructions

## Implementation Status

✅ Google Analytics 4 tracking code has been added to all HTML pages on the website

## Next Steps to Activate Tracking

1. **Create Google Analytics Account**

   - Go to [Google Analytics](https://analytics.google.com)
   - Create an account if you don't have one
   - Set up a new GA4 property for your website

2. **Get Your Measurement ID**

   - In your GA4 property, go to Admin → Data Streams
   - Create a web data stream for `leadingpowerfulconversations.com`
   - Copy the Measurement ID (format: G-XXXXXXXXXX)

3. **Replace Placeholder ID**

   - Find and replace `G-XXXXXXXXXX` with your actual Measurement ID in these files:
     - `/site/index.html`
     - `/site/contact.html`
     - `/site/bio.html`
     - `/site/resources.html`
     - `/site/404.html`

4. **Verify Installation**
   - After replacing the ID and deploying the site, use Google Analytics Real-time reports
   - Or use the Google Analytics Debugger browser extension
   - Or check the browser developer console for gtag events

## What's Tracking

The current implementation tracks:

- Page views across all pages
- User sessions and engagement
- Traffic sources and referrals
- Basic user demographics (where permitted)
- Device and browser information

## Privacy Considerations

- The implementation respects user privacy settings
- No personally identifiable information is collected
- Consider adding a privacy policy page mentioning analytics usage
- You may want to implement cookie consent for EU visitors (GDPR compliance)

## Additional Setup Recommendations

1. Set up Goals in GA4 for:

   - Contact form submissions
   - Amazon book link clicks
   - Resource downloads (if implemented)

2. Connect Google Search Console for SEO insights

3. Set up custom events for specific interactions:
   - Book cover clicks
   - Email link clicks
   - Social media link clicks

## Files Modified

- `index.html` - Added GA4 tracking code
- `contact.html` - Added GA4 tracking code
- `bio.html` - Added GA4 tracking code
- `resources.html` - Added GA4 tracking code
- `404.html` - Added GA4 tracking code

All tracking code is placed in the `<head>` section for optimal loading and tracking accuracy.
