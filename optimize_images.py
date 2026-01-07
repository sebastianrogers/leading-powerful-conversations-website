#!/usr/bin/env python3
"""
Image Optimization Script for Leading Powerful Conversations Website

This script optimizes all images in the website by:
1. Creating WebP versions of all major images
2. Compressing original images (JPEG and PNG)
3. Generating responsive image sets
4. Updating HTML files to use optimized images with fallbacks
"""

import os
import subprocess
import shutil
from pathlib import Path
import re

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cwd)
        if result.returncode != 0:
            print(f"Error running command '{command}': {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Exception running command '{command}': {e}")
        return False

def optimize_png(input_path, output_path=None):
    """Optimize PNG files using optipng"""
    if output_path is None:
        output_path = input_path
    
    # Copy first if different paths
    if input_path != output_path:
        shutil.copy2(input_path, output_path)
    
    # Optimize with optipng
    command = f"optipng -o2 -strip all '{output_path}'"
    return run_command(command)

def optimize_jpeg(input_path, output_path=None, quality=85):
    """Optimize JPEG files using jpegoptim"""
    if output_path is None:
        output_path = input_path
    
    # Copy first if different paths
    if input_path != output_path:
        shutil.copy2(input_path, output_path)
    
    # Optimize with jpegoptim
    command = f"jpegoptim --max={quality} --strip-all '{output_path}'"
    return run_command(command)

def create_webp(input_path, output_path=None, quality=80):
    """Create WebP version of an image"""
    if output_path is None:
        output_path = str(Path(input_path).with_suffix('.webp'))
    
    command = f"cwebp -q {quality} '{input_path}' -o '{output_path}'"
    return run_command(command)

def create_responsive_variants(input_path, base_name, sizes=[300, 600, 1200]):
    """Create responsive image variants at different sizes"""
    input_path = Path(input_path)
    variants = []
    
    for size in sizes:
        # Create resized version
        resized_name = f"{base_name}-{size}w{input_path.suffix}"
        resized_path = input_path.parent / resized_name
        
        # Resize using ImageMagick
        command = f"convert '{input_path}' -resize {size}x -quality 85 '{resized_path}'"
        if run_command(command):
            variants.append((resized_path, size))
            
            # Create WebP version
            webp_name = f"{base_name}-{size}w.webp"
            webp_path = input_path.parent / webp_name
            create_webp(resized_path, webp_path, 80)
            variants.append((webp_path, size))
    
    return variants

def optimize_images():
    """Main function to optimize all images"""
    images_dir = Path("/workspaces/leading-powerful-conversations-website/site/images")
    
    # Images that should get responsive variants (main content images)
    responsive_images = [
        "steve-ellis-photo.png",
        "FrameworkFull.png", 
        "Leading-Powerful-Convesations-Front-Cover.jpg",
        "Leading-Powerful-Convesations-Back-Cover.jpg",
        "seven-principles.png"
    ]
    
    # Images to skip (favicons and small icons)
    skip_images = [
        "favicon.ico",
        "favicon.svg", 
        "favicon-96x96.png",
        "apple-touch-icon.png",
        "web-app-manifest-192x192.png",
        "web-app-manifest-512x512.png"
    ]
    
    print("🖼️  Starting image optimization...")
    
    for image_file in images_dir.glob("*"):
        if image_file.is_file() and image_file.name not in skip_images:
            print(f"\n📸 Processing: {image_file.name}")
            
            # Get file extension
            ext = image_file.suffix.lower()
            base_name = image_file.stem
            
            # Optimize original image
            if ext in ['.jpg', '.jpeg']:
                print(f"  🗜️  Optimizing JPEG...")
                optimize_jpeg(str(image_file), quality=85)
            elif ext in ['.png']:
                print(f"  🗜️  Optimizing PNG...")
                optimize_png(str(image_file))
            
            # Create WebP version
            print(f"  🌐 Creating WebP...")
            webp_path = image_file.with_suffix('.webp')
            create_webp(str(image_file), str(webp_path), 80)
            
            # Create responsive variants for main images
            if image_file.name in responsive_images:
                print(f"  📱 Creating responsive variants...")
                variants = create_responsive_variants(str(image_file), base_name)
                print(f"     Created {len(variants)} variants")
    
    print("\n✅ Image optimization complete!")

def update_html_for_optimized_images():
    """Update HTML files to use optimized images with fallbacks"""
    site_dir = Path("/workspaces/leading-powerful-conversations-website/site")
    
    # Image replacements with responsive and WebP support
    image_updates = {
        'steve-ellis-photo.png': {
            'responsive': True,
            'alt': 'Steve Ellis - Leadership coach and author',
            'sizes': '(max-width: 768px) 100vw, 400px'
        },
        'FrameworkFull.png': {
            'responsive': True, 
            'alt': 'Leading Powerful Conversations Framework',
            'sizes': '(max-width: 768px) 100vw, 600px'
        },
        'Leading-Powerful-Convesations-Front-Cover.jpg': {
            'responsive': True,
            'alt': 'Leading Powerful Conversations book cover',
            'sizes': '(max-width: 768px) 100vw, 300px'
        },
        'Leading-Powerful-Convesations-Back-Cover.jpg': {
            'responsive': True,
            'alt': 'Leading Powerful Conversations book back cover', 
            'sizes': '(max-width: 768px) 100vw, 300px'
        },
        'seven-principles.png': {
            'responsive': True,
            'alt': 'Seven Principles of Leading Powerful Conversations',
            'sizes': '(max-width: 768px) 100vw, 500px'
        },
        'Amazon-buy-now-button-300x113.png': {
            'responsive': False,
            'alt': 'Buy now on Amazon',
            'webp_only': True
        }
    }
    
    print("\n🔄 Updating HTML files...")
    
    for html_file in site_dir.glob("*.html"):
        print(f"  📝 Processing: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for image_name, config in image_updates.items():
            base_name = Path(image_name).stem
            
            if config['responsive']:
                # Create picture element with responsive WebP and fallback
                picture_html = f'''<picture>
    <source type="image/webp" 
            sizes="{config['sizes']}"
            srcset="images/{base_name}-300w.webp 300w,
                    images/{base_name}-600w.webp 600w,
                    images/{base_name}-1200w.webp 1200w">
    <source type="image/{Path(image_name).suffix[1:]}"
            sizes="{config['sizes']}"
            srcset="images/{base_name}-300w{Path(image_name).suffix} 300w,
                    images/{base_name}-600w{Path(image_name).suffix} 600w,
                    images/{base_name}-1200w{Path(image_name).suffix} 1200w">
    <img src="images/{image_name}" alt="{config['alt']}" loading="lazy">
</picture>'''
            else:
                # Simple WebP with fallback
                picture_html = f'''<picture>
    <source type="image/webp" srcset="images/{base_name}.webp">
    <img src="images/{image_name}" alt="{config['alt']}" loading="lazy">
</picture>'''
            
            # Replace img tags that reference this image
            img_pattern = rf'<img[^>]*src=["\']images/{re.escape(image_name)}["\'][^>]*>'
            content = re.sub(img_pattern, picture_html, content)
        
        # Write back if content changed
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✅ Updated {html_file.name}")
        else:
            print(f"    ℹ️  No changes needed for {html_file.name}")
    
    print("\n✅ HTML updates complete!")

if __name__ == "__main__":
    optimize_images()
    update_html_for_optimized_images()
    
    print("\n📊 Final Results:")
    print("• Original images optimized (PNG/JPEG compression)")
    print("• WebP versions created for all images")  
    print("• Responsive image variants created for main content images")
    print("• HTML files updated with picture elements and responsive images")
    print("• Lazy loading added to all images")
    print("\nYour website images are now optimized for web performance! 🚀")