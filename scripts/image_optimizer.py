#!/usr/bin/env python3
"""
Image Optimizer for BigCommerce Auto Blog System
Optimizes images to under 100KB while maintaining quality
"""

from PIL import Image
import os
import sys

def optimize_image(input_path, output_path=None, target_size_kb=100, max_dimension=1200):
    """
    Optimize image to target file size while maintaining quality
    
    Args:
        input_path: Path to input image
        output_path: Path for optimized image (optional, defaults to overwrite)
        target_size_kb: Target file size in KB
        max_dimension: Maximum width or height in pixels
    """
    
    if output_path is None:
        output_path = input_path
    
    target_size_bytes = target_size_kb * 1024
    
    try:
        # Open and convert image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (for WebP compatibility)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparency
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate optimal dimensions
            width, height = img.size
            if width > max_dimension or height > max_dimension:
                if width > height:
                    new_width = max_dimension
                    new_height = int(height * (max_dimension / width))
                else:
                    new_height = max_dimension
                    new_width = int(width * (max_dimension / height))
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Start with high quality and reduce if needed
            quality = 95
            
            while quality > 20:
                # Save to temporary location to check size
                temp_path = output_path + '.temp'
                img.save(temp_path, 'WebP', quality=quality, optimize=True)
                
                # Check file size
                file_size = os.path.getsize(temp_path)
                
                if file_size <= target_size_bytes:
                    # Size is acceptable, move temp to final location
                    os.rename(temp_path, output_path)
                    print(f"✅ Optimized {os.path.basename(input_path)}: {file_size/1024:.1f}KB (quality: {quality})")
                    return True
                else:
                    # Remove temp file and try lower quality
                    os.remove(temp_path)
                    quality -= 5
            
            # If we can't get under target size, save at minimum quality
            img.save(output_path, 'WebP', quality=20, optimize=True)
            final_size = os.path.getsize(output_path)
            print(f"⚠️  {os.path.basename(input_path)}: {final_size/1024:.1f}KB (minimum quality)")
            return True
            
    except Exception as e:
        print(f"❌ Error optimizing {input_path}: {e}")
        return False

def optimize_all_images(directory=".", target_size_kb=100):
    """Optimize all WebP images in directory"""
    
    webp_files = [f for f in os.listdir(directory) if f.lower().endswith('.webp')]
    
    if not webp_files:
        print("No WebP files found in directory")
        return
    
    print(f"Found {len(webp_files)} WebP files to optimize")
    print(f"Target size: {target_size_kb}KB")
    print("-" * 50)
    
    success_count = 0
    for filename in webp_files:
        filepath = os.path.join(directory, filename)
        original_size = os.path.getsize(filepath)
        
        print(f"Processing {filename} ({original_size/1024:.1f}KB)...")
        
        if optimize_image(filepath, target_size_kb=target_size_kb):
            success_count += 1
            new_size = os.path.getsize(filepath)
            reduction = ((original_size - new_size) / original_size) * 100
            print(f"  Reduced by {reduction:.1f}% ({original_size/1024:.1f}KB → {new_size/1024:.1f}KB)")
        
        print()
    
    print(f"✅ Successfully optimized {success_count}/{len(webp_files)} images")

def test_optimization():
    """Test optimization on sample images"""
    
    print("🧪 Testing Image Optimization")
    print("=" * 40)
    
    # Test with different target sizes
    test_sizes = [100, 75, 50]
    
    # Find a test image
    webp_files = [f for f in os.listdir('.') if f.lower().endswith('.webp')]
    if not webp_files:
        print("No WebP files found for testing")
        return
    
    test_file = webp_files[0]
    original_size = os.path.getsize(test_file)
    
    print(f"Test file: {test_file} ({original_size/1024:.1f}KB)")
    print()
    
    for target_kb in test_sizes:
        output_file = f"test_{target_kb}kb_{test_file}"
        print(f"Testing {target_kb}KB target...")
        
        if optimize_image(test_file, output_file, target_size_kb=target_kb):
            final_size = os.path.getsize(output_file)
            reduction = ((original_size - final_size) / original_size) * 100
            print(f"  Result: {final_size/1024:.1f}KB (reduced {reduction:.1f}%)")
        
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            test_optimization()
        elif sys.argv[1] == "optimize":
            target_kb = int(sys.argv[2]) if len(sys.argv) > 2 else 100
            optimize_all_images(target_size_kb=target_kb)
        else:
            print("Usage: python3 image_optimizer.py [test|optimize] [target_kb]")
    else:
        # Default: optimize all images to 100KB
        optimize_all_images()

