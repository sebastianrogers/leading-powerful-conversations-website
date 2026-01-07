#!/bin/bash

# CSS Validation Script for Modular Architecture
# Validates CSS syntax and checks for common issues

echo "🎨 Validating Modular CSS Architecture..."
echo "=========================================="

CSS_DIR="/workspaces/leading-powerful-conversations-website/site/css"
ERRORS_FOUND=0

# List of CSS files to validate (excluding backup)
CSS_FILES=(
    "main.css"
    "variables.css"
    "base.css"
    "layout.css"
    "components.css"
    "accessibility.css"
    "responsive.css"
    "carousels.css"
    "error.css"
    "print.css"
)

echo "📁 Checking file existence..."
for file in "${CSS_FILES[@]}"; do
    if [ -f "$CSS_DIR/$file" ]; then
        echo "✅ $file - exists"
    else
        echo "❌ $file - missing"
        ((ERRORS_FOUND++))
    fi
done

echo ""
echo "🔍 Checking CSS syntax (basic validation)..."

for file in "${CSS_FILES[@]}"; do
    if [ -f "$CSS_DIR/$file" ]; then
        # Basic syntax checks
        
        # Check for unmatched braces
        OPEN_BRACES=$(grep -o '{' "$CSS_DIR/$file" | wc -l)
        CLOSE_BRACES=$(grep -o '}' "$CSS_DIR/$file" | wc -l)
        
        if [ $OPEN_BRACES -eq $CLOSE_BRACES ]; then
            echo "✅ $file - braces balanced ($OPEN_BRACES pairs)"
        else
            echo "❌ $file - unmatched braces (open: $OPEN_BRACES, close: $CLOSE_BRACES)"
            ((ERRORS_FOUND++))
        fi
        
        # Check for common CSS syntax errors
        if grep -q ';;' "$CSS_DIR/$file"; then
            echo "⚠️  $file - contains double semicolons"
        fi
        
        # Check for unclosed comments
        if [ $(grep -o '/\*' "$CSS_DIR/$file" | wc -l) -ne $(grep -o '\*/' "$CSS_DIR/$file" | wc -l) ]; then
            echo "❌ $file - unclosed comments"
            ((ERRORS_FOUND++))
        fi
    fi
done

echo ""
echo "📊 Summary:"
echo "==========="

if [ $ERRORS_FOUND -eq 0 ]; then
    echo "🎉 All CSS files passed validation!"
    echo "✨ Modular architecture is properly structured"
    exit 0
else
    echo "⚠️  Found $ERRORS_FOUND error(s)"
    echo "🔧 Please review and fix the issues above"
    exit 1
fi