#!/usr/bin/env python3
"""
Automated Mermaid Diagram Renderer
Converts .mmd files to PNG images using mermaid-cli
"""

import subprocess
import os
import glob
from pathlib import Path

def render_mermaid_file(input_path, output_path=None, width=800, height=600, theme="default"):
    """
    Render a single mermaid file to PNG

    Args:
        input_path (str): Path to .mmd file
        output_path (str): Output PNG path (defaults to input_path with .png extension)
        width (int): Image width in pixels
        height (int): Image height in pixels
        theme (str): Mermaid theme (default, forest, dark, neutral)
    """
    if output_path is None:
        output_path = Path(input_path).with_suffix('.png')

    cmd = [
        'mmdc',
        '-i', str(input_path),
        '-o', str(output_path),
        '-w', str(width),
        '-H', str(height),
        '-t', theme,
        '-b', 'transparent'  # Transparent background
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Rendered: {input_path} → {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to render {input_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ mermaid-cli (mmdc) not found. Install with: npm install -g @mermaid-js/mermaid-cli")
        return False

def render_all_mermaid_files(directory=".", pattern="**/*.mmd"):
    """
    Find and render all .mmd files in a directory

    Args:
        directory (str): Directory to search
        pattern (str): Glob pattern for finding files
    """
    mmd_files = glob.glob(os.path.join(directory, pattern), recursive=True)

    if not mmd_files:
        print(f"No .mmd files found in {directory}")
        return

    print(f"Found {len(mmd_files)} mermaid files to render:")

    success_count = 0
    for mmd_file in mmd_files:
        if render_mermaid_file(mmd_file):
            success_count += 1

    print(f"\n🎉 Successfully rendered {success_count}/{len(mmd_files)} files")

def main():
    """Test the mermaid rendering with current files"""
    print("🔧 Testing Mermaid CLI Rendering")
    print("=" * 40)

    # Test with current directory and subdirectories
    render_all_mermaid_files(".", "**/*.mmd")

if __name__ == "__main__":
    main()