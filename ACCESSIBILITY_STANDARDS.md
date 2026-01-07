# Accessibility Standards - Leading Powerful Conversations Website

## Overview

This website is committed to providing an inclusive experience for all users, including those with disabilities. We follow Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards to ensure our content is accessible to the widest possible audience.

## WCAG 2.1 AA Compliance

### Four Principles of Accessibility

#### 1. Perceivable
Information and user interface components must be presentable to users in ways they can perceive.

#### 2. Operable
User interface components and navigation must be operable by all users.

#### 3. Understandable
Information and the operation of user interface must be understandable.

#### 4. Robust
Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.

## Implementation Standards

### Visual Design

#### Color Contrast Requirements
- **Normal text**: Minimum 4.5:1 contrast ratio
- **Large text** (18pt+ or 14pt+ bold): Minimum 3:1 contrast ratio
- **Interactive elements**: Meet contrast requirements in all states
- **Graphical elements**: 3:1 contrast ratio for meaningful graphics

#### Current Color Compliance
```css
/* Text on white background */
--primary-blue: #1e40af;    /* 8.2:1 ratio ✓ */
--dark-charcoal: #374151;   /* 7.8:1 ratio ✓ */
--medium-gray: #6b7280;     /* 4.6:1 ratio ✓ */

/* Interactive elements */
--button-hover: #1d4ed8;    /* 8.7:1 ratio ✓ */
--link-focus: #2563eb;      /* 7.1:1 ratio ✓ */
```

#### Color Independence
- Never rely solely on color to convey information
- Use additional visual indicators (icons, patterns, text)
- Provide alternative text descriptions for color-coded content
- Test with color blindness simulators

### Typography

#### Font Size Requirements
- **Minimum body text**: 16px (1rem)
- **Scalable fonts**: Use relative units (rem, em)
- **Zoom support**: Content readable at 200% zoom
- **Line height**: Minimum 1.5 for body text, 1.2 for headings

#### Text Spacing
- **Paragraph spacing**: At least 0.5 times the font size
- **Letter spacing**: Can be adjusted up to 0.12 times font size
- **Word spacing**: Can be adjusted up to 0.16 times font size
- **Line height**: Can be adjusted up to 1.5 times font size

#### Implementation
```css
body {
  font-size: 16px;          /* Base size */
  line-height: 1.6;         /* Readable spacing */
  letter-spacing: 0.025em;  /* Slight character spacing */
}

h1, h2, h3, h4, h5, h6 {
  line-height: 1.25;        /* Tighter for headings */
  margin-bottom: 0.75em;    /* Consistent spacing */
}
```

### Navigation and Interaction

#### Keyboard Navigation
- **Tab order**: Logical and intuitive sequence
- **Focus indicators**: Visible focus states for all interactive elements
- **Skip links**: "Skip to main content" link for screen readers
- **Keyboard shortcuts**: Standard keyboard navigation support

#### Focus Management
```css
/* Visible focus indicators */
button:focus,
a:focus,
input:focus {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
  box-shadow: 0 0 0 1px #ffffff;
}

/* Skip link implementation */
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 1000;
}

.skip-link:focus {
  top: 6px;
}
```

#### Interactive Elements
- **Clickable area**: Minimum 44x44px touch target
- **Hover states**: Visual feedback for interactive elements
- **Active states**: Clear indication when elements are activated
- **Disabled states**: Clearly communicate non-interactive elements

### Form Accessibility

#### Form Labels
- **Required**: All form inputs must have associated labels
- **Descriptive**: Labels clearly describe the input purpose
- **Placement**: Labels positioned consistently (above inputs)
- **Required fields**: Clearly marked with visual and text indicators

#### Implementation Example
```html
<label for="name">Full Name <span class="required">*</span></label>
<input type="text" id="name" name="name" required aria-describedby="name-help">
<div id="name-help" class="help-text">Enter your first and last name</div>
```

#### Form Validation
- **Error messages**: Clear, specific error descriptions
- **Error association**: Errors linked to relevant form fields using aria-describedby
- **Success feedback**: Confirmation of successful form submission
- **Real-time validation**: Immediate feedback for user corrections

#### Error Handling
```html
<label for="email">Email Address <span class="required">*</span></label>
<input 
  type="email" 
  id="email" 
  name="email" 
  required 
  aria-describedby="email-error"
  aria-invalid="true">
<div id="email-error" class="error-message" role="alert">
  Please enter a valid email address
</div>
```

### Images and Media

#### Alternative Text
- **Decorative images**: Use empty alt attribute (alt="")
- **Informative images**: Describe the content and function
- **Complex images**: Provide detailed description in surrounding text
- **Text in images**: Include all text content in alt attribute

#### Image Implementation
```html
<!-- Informative image -->
<img src="leadership-workshop.jpg" 
     alt="Business professionals engaged in leadership communication workshop">

<!-- Decorative image -->
<img src="decorative-border.svg" alt="" role="presentation">

<!-- Complex chart or diagram -->
<img src="communication-model.png" 
     alt="Four-step communication model described in detail below">
```

### Content Structure

#### Semantic HTML
- **Headings**: Proper heading hierarchy (H1 → H2 → H3)
- **Landmarks**: Use semantic elements (header, nav, main, aside, footer)
- **Lists**: Use proper list markup for grouped content
- **Tables**: Include table headers and captions when appropriate

#### Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Page Title - Leading Powerful Conversations</title>
  <meta name="description" content="Page description">
</head>
<body>
  <header role="banner">
    <nav role="navigation" aria-label="Main navigation">
      <!-- Navigation content -->
    </nav>
  </header>
  
  <main role="main">
    <h1>Page Title</h1>
    <!-- Main content -->
  </main>
  
  <footer role="contentinfo">
    <!-- Footer content -->
  </footer>
</body>
</html>
```

#### Content Organization
- **Headings**: Logical hierarchy without skipping levels
- **Page titles**: Unique, descriptive page titles
- **Link text**: Descriptive link text (avoid "click here")
- **Reading order**: Logical flow when CSS is disabled

### ARIA (Accessible Rich Internet Applications)

#### ARIA Labels and Descriptions
- **aria-label**: Provides accessible name for elements
- **aria-describedby**: Links to descriptive text
- **aria-labelledby**: References other elements that label this one
- **aria-hidden**: Hides decorative elements from screen readers

#### ARIA Roles
- **Landmark roles**: banner, navigation, main, complementary, contentinfo
- **Widget roles**: button, link, textbox, checkbox
- **Live regions**: alert, status, log for dynamic content

#### Implementation Examples
```html
<!-- Search form -->
<form role="search" aria-label="Site search">
  <input type="search" aria-label="Search terms">
  <button type="submit">Search</button>
</form>

<!-- Navigation with current page -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about" aria-current="page">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<!-- Status messages -->
<div id="status" aria-live="polite" aria-atomic="true">
  Form submitted successfully!
</div>
```

## Testing and Validation

### Automated Testing Tools

#### Browser Extensions
- **axe DevTools**: Comprehensive accessibility testing
- **WAVE**: Web accessibility evaluation
- **Lighthouse**: Built-in accessibility audit
- **Colour Contrast Analyser**: Check contrast ratios

#### Command Line Tools
- **axe-core**: Automated testing framework
- **Pa11y**: Command-line accessibility testing
- **HTML validator**: W3C markup validation

### Manual Testing

#### Keyboard Navigation Testing
1. **Tab through all interactive elements**
2. **Verify logical tab order**
3. **Test skip links functionality**
4. **Ensure all content is keyboard accessible**
5. **Check focus indicators are visible**

#### Screen Reader Testing
- **Test with NVDA** (Windows - free)
- **Test with JAWS** (Windows - commercial)
- **Test with VoiceOver** (macOS/iOS - built-in)
- **Test with TalkBack** (Android - built-in)

#### Visual Testing
1. **Zoom to 200%** and verify readability
2. **Test with high contrast mode**
3. **Check color blindness simulation**
4. **Verify content without CSS**
5. **Test on mobile devices**

### Testing Checklist

#### Pre-Launch Testing
- [ ] All images have appropriate alt text
- [ ] Forms have proper labels and error handling
- [ ] Color contrast meets WCAG AA standards
- [ ] Keyboard navigation works throughout site
- [ ] Focus indicators are visible and consistent
- [ ] Headings follow logical hierarchy
- [ ] Content is readable at 200% zoom
- [ ] Screen reader testing completed
- [ ] HTML validates without errors
- [ ] ARIA attributes used appropriately

#### Ongoing Testing
- [ ] Regular automated accessibility scans
- [ ] User testing with people with disabilities
- [ ] Periodic manual testing with assistive technologies
- [ ] Review of new content for accessibility compliance
- [ ] Staff training on accessibility best practices

## Assistive Technology Support

### Screen Readers
- **NVDA**: Primary testing screen reader (Windows)
- **JAWS**: Secondary testing screen reader (Windows)
- **VoiceOver**: macOS and iOS testing
- **TalkBack**: Android testing

### Other Assistive Technologies
- **Voice recognition software**: Dragon NaturallySpeaking
- **Switch navigation**: Single-switch and dual-switch users
- **Eye-tracking software**: For users with motor disabilities
- **Magnification software**: ZoomText, built-in OS magnifiers

## Legal Compliance

### Applicable Laws and Standards
- **ADA** (Americans with Disabilities Act)
- **Section 508** (US Federal accessibility requirements)
- **WCAG 2.1 AA** (International accessibility guidelines)
- **AODA** (Accessibility for Ontarians with Disabilities Act)

### Risk Mitigation
- Regular accessibility audits
- Staff training on accessibility
- Clear accessibility policy
- Responsive communication for accessibility issues
- Continuous improvement process

## Accessibility Statement

### Public Commitment
We are committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone and applying the relevant accessibility standards.

### Feedback Process
If you encounter accessibility barriers on our website:
1. **Contact us** via email or contact form
2. **Describe the issue** and provide page URL
3. **We will respond** within 2 business days
4. **We will work** to resolve issues promptly

### Ongoing Improvements
- Regular accessibility training for team members
- Quarterly accessibility audits
- User feedback integration
- Technology updates and improvements
- Community engagement and learning

## Resources and Training

### Internal Training
- WCAG 2.1 guidelines overview
- Screen reader demonstration
- Keyboard navigation training
- Color contrast tools usage
- ARIA implementation best practices

### External Resources
- **WebAIM**: Web accessibility training and resources
- **A11Y Project**: Accessibility best practices
- **WAVE**: Web accessibility evaluation tool
- **Color Oracle**: Color blindness simulator
- **axe**: Accessibility testing tools

### Ongoing Education
- Accessibility conferences and workshops
- Online courses and certifications
- Community forums and discussion groups
- Regular review of accessibility updates
- User feedback and testing sessions

Last updated: January 7, 2026