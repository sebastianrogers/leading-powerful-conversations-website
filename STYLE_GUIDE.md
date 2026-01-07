# Style Guide - Leading Powerful Conversations Website

## Brand Identity

### Mission
Empowering leaders to have meaningful, impactful conversations that drive positive change in their organizations and communities.

### Brand Personality
- **Professional**: Credible and trustworthy
- **Approachable**: Warm and accessible
- **Empowering**: Inspiring confidence and action
- **Clear**: Simple and easy to understand

## Visual Design System

### Color Palette

#### Primary Colors
- **Deep Blue**: `#1e40af` - Trust, professionalism, stability
- **Warm Orange**: `#f97316` - Energy, enthusiasm, action
- **Dark Charcoal**: `#374151` - Authority, sophistication

#### Secondary Colors
- **Light Gray**: `#f3f4f6` - Backgrounds, subtle elements
- **Medium Gray**: `#6b7280` - Text, borders
- **Success Green**: `#10b981` - Success messages, positive actions
- **Warning Amber**: `#f59e0b` - Alerts, important notices

#### Usage Guidelines
- **Primary Blue**: Main headings, navigation, CTA buttons
- **Warm Orange**: Accent elements, hover states, highlights
- **Dark Charcoal**: Body text, secondary headings
- **Gray tones**: Backgrounds, borders, subtle text

### Typography

#### Primary Font: System Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, sans-serif;
```

#### Font Hierarchy
- **H1 (Main Headlines)**: 2.5rem (40px), Bold, Primary Blue
- **H2 (Section Headers)**: 2rem (32px), Bold, Dark Charcoal
- **H3 (Subsections)**: 1.5rem (24px), Semibold, Dark Charcoal
- **H4 (Minor Headers)**: 1.25rem (20px), Medium, Dark Charcoal
- **Body Text**: 1rem (16px), Regular, Dark Charcoal
- **Small Text**: 0.875rem (14px), Regular, Medium Gray

#### Typography Guidelines
- Line height: 1.6 for body text, 1.2 for headings
- Letter spacing: Normal for body, slight negative for large headings
- Text alignment: Left-aligned for body, center for hero sections

### Spacing System

#### Base Unit: 8px
- **XS**: 4px (0.25rem) - Fine details, borders
- **SM**: 8px (0.5rem) - Small gaps, padding
- **MD**: 16px (1rem) - Standard spacing
- **LG**: 24px (1.5rem) - Section separation
- **XL**: 32px (2rem) - Major sections
- **2XL**: 48px (3rem) - Large separations
- **3XL**: 64px (4rem) - Hero sections, major divisions

### Layout Grid

#### Breakpoints
- **Mobile**: 320px - 767px
- **Tablet**: 768px - 1023px
- **Desktop**: 1024px - 1439px
- **Large Desktop**: 1440px+

#### Container Widths
- **Mobile**: 100% with 16px margins
- **Tablet**: 90% with max-width 720px
- **Desktop**: 80% with max-width 1200px

#### Grid System
- **Columns**: 12-column grid
- **Gutters**: 24px between columns
- **Margins**: Responsive margins based on screen size

## Component Styles

### Buttons

#### Primary Button
```css
background: #1e40af;
color: white;
padding: 12px 24px;
border-radius: 6px;
font-weight: 600;
border: none;
cursor: pointer;
```

#### Secondary Button
```css
background: transparent;
color: #1e40af;
padding: 12px 24px;
border: 2px solid #1e40af;
border-radius: 6px;
font-weight: 600;
```

#### Button States
- **Hover**: Darken by 10%, add subtle shadow
- **Active**: Darken by 15%, inset shadow
- **Disabled**: 50% opacity, no cursor

### Cards

#### Standard Card
```css
background: white;
border: 1px solid #e5e7eb;
border-radius: 8px;
padding: 24px;
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
```

#### Card Hover State
```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
transform: translateY(-2px);
```

### Navigation

#### Main Navigation
- Clean, minimal design
- Clear visual hierarchy
- Responsive hamburger menu for mobile
- Active state indication
- Smooth transitions

#### Navigation Colors
- Background: White with subtle shadow
- Links: Dark Charcoal (#374151)
- Active/Hover: Primary Blue (#1e40af)
- Mobile menu: Clean overlay

### Forms

#### Input Fields
```css
border: 2px solid #d1d5db;
border-radius: 6px;
padding: 12px 16px;
font-size: 16px;
background: white;
```

#### Input States
- **Focus**: Border color changes to Primary Blue
- **Error**: Border color changes to red (#ef4444)
- **Success**: Border color changes to Success Green

#### Labels
- Position above input
- Font weight: 600
- Color: Dark Charcoal
- Required fields marked with asterisk

## Content Guidelines

### Voice and Tone

#### Voice Characteristics
- **Authoritative but approachable**: Expert knowledge delivered warmly
- **Clear and direct**: No jargon, straightforward communication
- **Encouraging**: Positive, supportive language
- **Professional**: Maintains credibility and trust

#### Tone Variations
- **Homepage**: Confident and inspiring
- **About/Bio**: Personal but professional
- **Resources**: Helpful and educational
- **Contact**: Welcoming and accessible

### Writing Style

#### Guidelines
- Use active voice when possible
- Keep sentences concise and clear
- Use bullet points for easy scanning
- Include clear calls-to-action
- Avoid industry jargon
- Use inclusive language

#### Content Structure
1. **Headlines**: Clear benefit or value proposition
2. **Subheadings**: Descriptive and scannable
3. **Body text**: Supportive details and explanation
4. **Call-to-action**: Clear next step

### Imagery

#### Photo Style
- **Professional**: High-quality, well-lit images
- **Authentic**: Real people, genuine moments
- **Diverse**: Inclusive representation
- **Consistent**: Similar lighting and color treatment

#### Image Guidelines
- Minimum 1200px width for hero images
- Optimize for web (WebP format preferred)
- Include alt text for accessibility
- Maintain consistent aspect ratios

## Accessibility Standards

### WCAG 2.1 AA Compliance

#### Color Contrast
- Text on background: Minimum 4.5:1 ratio
- Large text (18pt+): Minimum 3:1 ratio
- Interactive elements: Clear visual focus states

#### Typography
- Minimum 16px font size for body text
- Maximum 80 characters per line
- Sufficient line spacing (1.6 minimum)

#### Navigation
- Keyboard accessible
- Clear focus indicators
- Logical tab order
- Skip navigation links

### Testing Requirements
- Test with screen readers
- Verify keyboard navigation
- Check color contrast ratios
- Validate HTML markup
- Test on mobile devices

## Implementation Guidelines

### CSS Architecture
- Use CSS custom properties for colors and spacing
- Follow mobile-first approach
- Use semantic class names
- Maintain consistent naming conventions

### Performance
- Optimize images for web
- Minimize CSS and JavaScript
- Use system fonts to avoid loading delays
- Implement proper caching headers

### Browser Support
- Modern browsers (last 2 versions)
- Chrome, Firefox, Safari, Edge
- iOS Safari, Chrome Mobile
- Graceful degradation for older browsers

## Brand Application

### Logo Usage
- Maintain clear space around logo
- Use high-contrast backgrounds
- Provide alternative formats (light/dark)
- Never distort or modify proportions

### Marketing Materials
- Apply consistent color palette
- Use established typography hierarchy
- Maintain professional photography style
- Include clear calls-to-action

### Digital Presence
- Consistent visual identity across platforms
- Professional social media imagery
- Email templates following brand guidelines
- Presentation templates using brand elements

Last updated: January 7, 2026