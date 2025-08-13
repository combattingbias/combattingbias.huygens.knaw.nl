#!/usr/bin/env python3
"""
Auto-generate bias-config.js from markdown files
Run this script whenever you add new bias type pages
"""

import os
import re
import json
import yaml
from pathlib import Path

def extract_frontmatter_and_content(file_path):
    """Extract YAML frontmatter and content from markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file starts with ---
    if not content.startswith('---\n'):
        return None, content
    
    # Find the end of frontmatter
    try:
        end_index = content.index('\n---\n', 4)
        frontmatter_content = content[4:end_index]
        markdown_content = content[end_index + 5:]
        
        # Parse YAML frontmatter
        frontmatter = yaml.safe_load(frontmatter_content)
        return frontmatter, markdown_content
    except (ValueError, yaml.YAMLError) as e:
        print(f"Error parsing {file_path}: {e}")
        return None, content

def extract_definition(markdown_content):
    """Extract the first definition from markdown content"""
    # Look for ## Definition section
    definition_match = re.search(r'## Definition\s*\n(.*?)(?=\n## |$)', markdown_content, re.DOTALL)
    if definition_match:
        definition = definition_match.group(1).strip()
        # Remove quotes and clean up
        definition = re.sub(r'^["\'""]|["\'""]$', '', definition)
        # Remove markdown formatting and special characters
        definition = re.sub(r'\*\*(.*?)\*\*', r'\1', definition)
        definition = re.sub(r'\*(.*?)\*', r'\1', definition)
        definition = definition.replace('â€œ', '"').replace('â€', '"').replace('â€™', "'")
        # Take first sentence or first 200 chars
        sentences = definition.split('.')
        if len(sentences[0]) > 200:
            return definition[:200] + '...'
        return sentences[0] + '.'
    return "Definition not found"

def extract_stakes(markdown_content):
    """Extract stakes information from markdown content"""
    stakes_match = re.search(r'## Stakes\s*.*?\n(.*?)(?=\n## |$)', markdown_content, re.DOTALL)
    if stakes_match:
        stakes = stakes_match.group(1).strip()
        # Clean up formatting
        stakes = re.sub(r'\*\*(.*?)\*\*', r'\1', stakes)
        stakes = re.sub(r'_part of:.*?_\s*', '', stakes)
        stakes = re.sub(r'_related to:.*?_\s*', '', stakes)
        stakes = stakes.replace('\n', ' ').strip()
        stakes = stakes.replace('â€œ', '"').replace('â€', '"').replace('â€™', "'")
        return stakes
    return "Stakes not specified"

def get_icon_for_bias(title):
    """Get appropriate FontAwesome icon for bias type"""
    icon_map = {
        'positionality': 'fa-user-circle',
        'silences': 'fa-volume-xmark',
        'representation': 'fa-users',
        'collaboration': 'fa-handshake',
        'source selection': 'fa-filter',
        'algorithmic bias': 'fa-robot',
        'transparency': 'fa-eye',
        'fairness': 'fa-balance-scale',
        'ethics': 'fa-gavel',
        'data quality': 'fa-chart-line',
        'methodology': 'fa-microscope'
    }
    
    title_lower = title.lower()
    for key, icon in icon_map.items():
        if key in title_lower:
            return icon
    return 'fa-circle-question'  # Default icon

def process_bias_files(bias_types_dir):
    """Process all markdown files in the bias types directory"""
    bias_data = []
    
    for file_path in Path(bias_types_dir).glob('*.md'):
        print(f"Processing {file_path.name}...")
        
        frontmatter, content = extract_frontmatter_and_content(file_path)
        
        if not frontmatter:
            print(f"  Warning: No frontmatter found in {file_path.name}")
            continue
        
        # Extract required fields
        title = frontmatter.get('title', file_path.stem.replace('-', ' ').title())
        slug = file_path.stem
        types = frontmatter.get('type', [])
        stages = frontmatter.get('stages', [])
        keywords = frontmatter.get('keywords', [])
        
        # Ensure types and stages are lists
        if isinstance(types, str):
            types = [types]
        if isinstance(stages, str):
            stages = [stages]
            
        # Extract content
        definition = extract_definition(content)
        stakes = extract_stakes(content)
        icon = get_icon_for_bias(title)
        
        bias_entry = {
            'title': title,
            'slug': slug,
            'types': types,
            'stages': stages,
            'keywords': keywords,
            'definition': definition,
            'stakes': stakes,
            'icon': icon
        }
        
        bias_data.append(bias_entry)
        print(f"  ✓ Added {title}")
        print(f"    Types: {types}")
        print(f"    Stages: {stages}")
        print(f"    Keywords: {len(keywords)} found")
    
    return bias_data

def generate_config_file(bias_data, output_path):
    """Generate the bias-config.js file"""
    js_content = "// Auto-generated bias configuration\n"
    js_content += "// Run generate_bias_config.py to update this file\n\n"
    js_content += "window.biasConfig = "
    
    # Convert to JSON with proper formatting
    json_str = json.dumps(bias_data, indent=4, ensure_ascii=False)
    js_content += json_str + ";"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"\n✓ Generated {output_path}")
    print(f"  Found {len(bias_data)} bias concepts")

def main():
    # Configuration
    BIAS_TYPES_DIR = "bias/types"  # Adjust path as needed
    OUTPUT_FILE = "javascripts/bias-config.js"
    
    # Ensure directories exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    if not os.path.exists(BIAS_TYPES_DIR):
        print(f"Error: Directory {BIAS_TYPES_DIR} not found")
        print("Please adjust BIAS_TYPES_DIR in the script")
        return
    
    print(f"Scanning {BIAS_TYPES_DIR} for bias type files...")
    
    # Process files
    bias_data = process_bias_files(BIAS_TYPES_DIR)
    
    if not bias_data:
        print("No bias data found. Check your markdown files have proper frontmatter.")
        return
    
    # Generate config file
    generate_config_file(bias_data, OUTPUT_FILE)
    
    print(f"\n🎉 Success! Your mkdocs.yml should include:")
    print(f"extra_javascript:")
    print(f"  - javascripts/bias-config.js")
    print(f"\nNext steps:")
    print(f"1. Update your toolkitpage to use the config")
    print(f"2. Run 'mkdocs serve' to test")
    print(f"3. Run this script again whenever you add new bias types")

if __name__ == "__main__":
    main()