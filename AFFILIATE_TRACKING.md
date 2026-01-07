# Affiliate Link Tracking Implementation

## Overview

Affiliate link tracking has been implemented for the Amazon book purchase button to monitor click-through rates, engagement, and potential conversions.

## Features Implemented

### 1. Affiliate URL Structure

- **Amazon Affiliate ID**: `leadpowconv-21` (placeholder - needs to be replaced with actual affiliate ID)
- **Tracking Parameters**: UTM parameters for campaign attribution
- **Reference Parameters**: Amazon-specific tracking parameters

### 2. Google Analytics Integration

The tracking sends the following events to Google Analytics:

- `affiliate_click` - Main tracking event with detailed metadata
- `conversion` - Conversion tracking for affiliate clicks
- `affiliate_hover` - Engagement tracking for button hover duration

### 3. Event Data Collected

- Platform (amazon)
- Click action (book_purchase)
- Element identifier
- Timestamp
- Source page
- Hover duration (engagement metric)

### 4. Enhanced Tracking Features

- Automatic tracking for all Amazon links on the page
- Hover duration tracking for engagement analytics
- Console logging for debugging
- Prepared endpoint for custom tracking server

## Setup Requirements

### 1. Amazon Affiliate Account

1. Sign up for Amazon Associates program
2. Replace `leadpowconv-21` with your actual affiliate tag
3. Update the affiliate ID in both:
   - Main Amazon button URL
   - Structured data URL

### 2. Google Analytics Configuration

1. Ensure Google Analytics 4 is properly configured
2. Replace `G-XXXXXXXXXX` with actual tracking ID
3. Set up conversion goals in GA4 dashboard

### 3. Optional: Custom Tracking Server

Uncomment and configure the fetch request in `trackAffiliateClick()` function if you want to send data to your own analytics endpoint.

## Files Modified

- `/site/index.html` - Added tracking JavaScript and updated URLs

## Testing

1. Open browser developer console
2. Click the Amazon button
3. Check console for tracking logs
4. Verify Google Analytics Real-Time events

## Compliance Notes

- All tracking respects user privacy
- Consider adding cookie consent if required by jurisdiction
- Amazon Associates program has specific guidelines - ensure compliance

## Analytics Dashboard

Monitor the following metrics in Google Analytics:

- Affiliate click rate
- Hover engagement time
- Conversion attribution
- Traffic source analysis

Last updated: January 7, 2026
