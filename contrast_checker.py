#!/usr/bin/env python3
"""
Contrast ratio calculator for WCAG compliance
"""

def hex_to_rgb(hex_color):
    """Convert hex color to RGB values"""
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_luminance(r, g, b):
    """Convert RGB to relative luminance"""
    def gamma_correct(c):
        c = c / 255.0
        if c <= 0.03928:
            return c / 12.92
        else:
            return ((c + 0.055) / 1.055) ** 2.4
    
    return 0.2126 * gamma_correct(r) + 0.7152 * gamma_correct(g) + 0.0722 * gamma_correct(b)

def contrast_ratio(color1, color2):
    """Calculate contrast ratio between two colors"""
    if isinstance(color1, str):
        color1 = hex_to_rgb(color1)
    if isinstance(color2, str):
        color2 = hex_to_rgb(color2)
    
    lum1 = rgb_to_luminance(*color1)
    lum2 = rgb_to_luminance(*color2)
    
    # Ensure the lighter color is in the numerator
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)

def wcag_compliance(ratio):
    """Check WCAG compliance levels"""
    if ratio >= 7.0:
        return "AAA (excellent)"
    elif ratio >= 4.5:
        return "AA (good)"
    elif ratio >= 3.0:
        return "A (minimal)"
    else:
        return "FAIL"

# Current color combinations from the website
print("=== Current Website Color Accessibility Analysis ===\n")

# Convert rgb(243, 203, 46) to hex for easier calculation
yellow_bg = (243, 203, 46)  # Main background color

# Calculate important contrasts
combinations = [
    ("Body text", "#333", "#ffffff", "Dark gray text on white background"),
    ("Nav links", "rgba(0,0,0,0.8)", yellow_bg, "Navigation links on yellow background"),
    ("Footer text", "rgba(0,0,0,0.85)", yellow_bg, "Footer text on yellow background"),
    ("Footer links", "#1a5490", yellow_bg, "Footer links on yellow background"),
    ("Skip link", "#ffffff", "#000000", "Skip link - white text on black"),
]

for desc, fg, bg, context in combinations:
    if fg.startswith('rgba'):
        # Handle rgba colors by approximating alpha blend
        if fg == "rgba(0,0,0,0.8)":
            fg_rgb = (51, 51, 51)  # Approximate 80% opacity black
        elif fg == "rgba(0,0,0,0.85)":
            fg_rgb = (38, 38, 38)  # Approximate 85% opacity black
    else:
        fg_rgb = hex_to_rgb(fg) if fg.startswith('#') else fg
    
    bg_rgb = hex_to_rgb(bg) if isinstance(bg, str) and bg.startswith('#') else bg
    
    ratio = contrast_ratio(fg_rgb, bg_rgb)
    compliance = wcag_compliance(ratio)
    
    print(f"{desc}:")
    print(f"  Context: {context}")
    print(f"  Contrast Ratio: {ratio:.2f}:1")
    print(f"  WCAG Level: {compliance}")
    print()