#!/usr/bin/env python3
"""
Generate toolkit.md with embedded bias configuration data
Run this script to regenerate the complete toolkit page
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
    
    if not content.startswith('---\n'):
        return None, content
    
    try:
        end_index = content.index('\n---\n', 4)
        frontmatter_content = content[4:end_index]
        markdown_content = content[end_index + 5:]
        
        frontmatter = yaml.safe_load(frontmatter_content)
        return frontmatter, markdown_content
    except (ValueError, yaml.YAMLError) as e:
        print(f"Error parsing {file_path}: {e}")
        return None, content

def extract_definition(markdown_content):
    """Extract the first definition from markdown content"""
    definition_match = re.search(r'## Definition\s*\n(.*?)(?=\n## |$)', markdown_content, re.DOTALL)
    if definition_match:
        definition = definition_match.group(1).strip()
        definition = re.sub(r'^["\'""]|["\'""]$', '', definition)
        definition = re.sub(r'\*\*(.*?)\*\*', r'\1', definition)
        definition = re.sub(r'\*(.*?)\*', r'\1', definition)
        definition = definition.replace('â€œ', '"').replace('â€', '"').replace('â€™', "'")
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
    return 'fa-circle-question'

def process_bias_files(bias_types_dir):
    """Process all markdown files in the bias types directory"""
    bias_data = []
    
    for file_path in Path(bias_types_dir).glob('*.md'):
        print(f"Processing {file_path.name}...")
        
        frontmatter, content = extract_frontmatter_and_content(file_path)
        
        if not frontmatter:
            print(f"  Warning: No frontmatter found in {file_path.name}")
            continue
        
        title = frontmatter.get('title', file_path.stem.replace('-', ' ').title())
        slug = file_path.stem
        types = frontmatter.get('type', [])
        stages = frontmatter.get('stages', [])
        keywords = frontmatter.get('keywords', [])
        
        if isinstance(types, str):
            types = [types]
        if isinstance(stages, str):
            stages = [stages]
            
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
    
    return bias_data

def generate_toolkit_page(bias_data, output_path):
    """Generate the complete toolkit.md file with embedded data"""
    
    # Convert bias data to JavaScript
    bias_json = json.dumps(bias_data, indent=8, ensure_ascii=False)
    
    toolkit_content = f'''---
title: Bias Toolkit
hide:
  - toc
---

<style>
body {{
    font-family: 'Roboto', sans-serif;
    line-height: 1;
}}

.container-custom {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}}

.post-title {{
    color: #333;
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 10px;
    text-align: center;
}}

.post-description {{
    text-align: center;
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 20px;
}}

.filter-section {{
    margin-bottom: 30px;
    padding: 25px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    border: 2px solid #1d4066ff;
}}

.filter-section h3 {{
    color: #333;
    font-weight: 500;
    margin-bottom: 20px;
    margin-top: 10px;
    font-size: 1rem;
}}

.button-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 15px;
    margin-top: 15px;
}}

.filter-btn {{
    padding: 15px 20px;
    border: 2px solid #dee2e6;
    background: white;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}}

.filter-btn:hover {{
    border-color: #007bff;
    background-color: #f8f9fa;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,123,255,0.15);
}}

.filter-btn.active {{
    background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
    color: white;
    border-color: #007bff;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0,123,255,0.3);
}}

.search-container {{
    display: flex;
    gap: 10px;
    margin-top: 15px;
    flex-wrap: wrap;
}}

.search-container input {{
    flex: 1;
    min-width: 200px;
    padding: 12px 16px;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s ease;
}}

.search-container input:focus {{
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
}}

.search-btn {{
    padding: 12px 24px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}}

.search-btn:hover {{
    background: #0056b3;
    transform: translateY(-1px);
}}

.reset-btn {{
    padding: 12px 24px;
    background: #6c757d;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 8px;
}}

.reset-btn:hover {{
    background: #545b62;
    transform: translateY(-1px);
}}

.card {{
    border: 1px solid rgba(0,123,255,0.15);
    border-radius: 12px;
    margin-bottom: 25px;
    transition: all 0.3s ease;
    cursor: pointer;
    background: white;
    overflow: hidden;
}}

.card:hover {{
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transform: translateY(-3px);
    border-color: #007bff;
}}

.card-body {{
    padding: 25px;
}}

.card-title {{
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 15px;
    color: #333;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.card-title i {{
    color: #007bff;
    font-size: 1.2rem;
}}

.card-text {{
    color: #666;
    margin-bottom: 12px;
    line-height: 1.6;
}}

.card-text.keyword {{
    font-style: italic;
    color: #888;
    font-size: 0.8rem;
}}

.badge {{
    display: inline-block;
    padding: 6px 12px;
    background: #e9ecef;
    color: #495057;
    border-radius: 20px;
    font-size: 0.7rem;
    margin-right: 8px;
    margin-bottom: 8px;
    font-weight: 500;
}}

.badge.discrimination {{
    background: linear-gradient(135deg, #ca6a73ff 0%, #c82333 100%);
    color: white;
}}

.badge.opacity {{
    background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
    color: white;
}}

.badge.stage {{
    background: linear-gradient(135deg, #28a745 0%, #218838 100%);
    color: white;
}}

hr.solid {{
    border-top: 2px solid #e9ecef;
    margin: 20px 0;
    opacity: 1;
}}

#resource-count {{
    font-weight: 700;
    color: #007bff;
    font-size: 0.9rem;
}}

.results-header {{
    text-align: center;
    margin: 0px 0 10px 0;
    padding: 30px;
    background: #fffffdff;
    border-radius: 12px;
    border: 2px solid #e7ec54ff;
}}

.results-header h2 {{
    color: #333;
    font-weight: 400;
    margin-bottom: 10px;
}}

.results-header p {{
    color: #666;
    margin: 0;
}}

.intro-section {{
    background: #f1f5f8ff;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 40px;
    border: 1px solid #d8dbcbff;
}}

.intro-section p {{
    margin: 0;
    color: #333;
    font-size: 0.85rem;
    line-height: 1.7;
}}

.loading {{
    text-align: center;
    padding: 40px;
    color: #666;
}}

/* Responsive design */
@media (max-width: 768px) {{
    .search-container {{
        flex-direction: column;
    }}
    
    .search-container input {{
        min-width: 100%;
    }}
    
    .button-grid {{
        grid-template-columns: 1fr;
    }}
    
    .card-body {{
        padding: 20px;
    }}
    
    .post-title {{
        font-size: 2rem;
    }}
}}
</style>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" integrity="sha256-HtsXJanqjKTc8vVQjO4YMhiqFoXkfBsjBWcX91T1jr8=" crossorigin="anonymous">

<div class="container-custom">
    <header class="post-header">
        <h1 class="post-title">Bias Aware Toolkit</h1>
        <p class="post-description">
            Explore different types of bias and their manifestations throughout the research lifecycle. 
            Use the filters below to find concepts by category or research stage.
        </p>
    </header>

    <article>
        <div class="intro-section">
            <p>
                <strong>Use the filters below</strong> to explore types of biases by their <strong>category</strong> (discrimination or opacity) 
                or by the <strong>research stage</strong> where they commonly occur. You can also search for specific keywords across all bias concepts. 
                Each concept includes definitions, practical questions, and actionable guidance for dataset creators and users.
            </p>
        </div>
        
        <!-- Type Filter -->
        <div class="filter-section">
            <h3><i class="fa-solid fa-tags"></i> Types of Bias</h3>
            <div class="button-grid">
                <button class="filter-btn type-btn" data-filter="type" data-value="discrimination">
                    <i class="fa-solid fa-exclamation-triangle"></i>
                    Discrimination
                </button>
                <button class="filter-btn type-btn" data-filter="type" data-value="opacity">
                    <i class="fa-solid fa-eye-slash"></i>
                    Opacity 
                </button>
            </div>
        </div>

        <!-- Stage Filter -->
        <div class="filter-section">
            <h3><i class="fa-solid fa-project-diagram"></i> Research Stage</h3>
            <div class="button-grid">
                <button class="filter-btn stage-btn" data-filter="stage" data-value="setup">
                    <i class="fa-solid fa-cog"></i>
                    Set Up 
                </button>
                <button class="filter-btn stage-btn" data-filter="stage" data-value="collection">
                    <i class="fa-solid fa-database"></i>
                    Collection 
                </button>
                <button class="filter-btn stage-btn" data-filter="stage" data-value="process">
                    <i class="fa-solid fa-gears"></i>
                    Process 
                </button>
                <button class="filter-btn stage-btn" data-filter="stage" data-value="analyse">
                    <i class="fa-solid fa-chart-bar"></i>
                    Analyse 
                </button>
                <button class="filter-btn stage-btn" data-filter="stage" data-value="share">
                    <i class="fa-solid fa-share"></i>
                    Share & Preserve 
                </button>
            </div>
        </div>

        <!-- Search -->
        <div class="filter-section">
            <h3><i class="fa-solid fa-search"></i> Search Concepts</h3>
            <div class="search-container">
                <input type="text" id="search-input" placeholder="Search for bias concepts, definitions, keywords, or questions...">
                <button id="search-btn" class="search-btn">
                    <i class="fa-solid fa-search"></i> Search
                </button>
                <button id="clear-search-btn" class="search-btn" style="background: #6c757d;">
                    <i class="fa-solid fa-times"></i> Clear
                </button>
            </div>
        </div>

        <!-- Reset -->
        <div class="filter-section">
            <button class="reset-btn" data-reset="all">
                <i class="fa-solid fa-rotate-left"></i>
                Reset all filters
            </button>
        </div>

        <hr style="border-top: 3px solid #dee2e6; margin: 40px 0;">

        <!-- Results Header -->
        <div class="results-header">
            <h2>
                Bias Concepts (<span id="resource-count">0</span>)
            </h2>
            <p>
                <i class="fa-solid fa-info-circle"></i> 
                Click on any card to explore the concept in detail
            </p>
        </div>

        <!-- Cards Container -->
        <div id="card-list">
            <div class="loading">
                <i class="fa-solid fa-spinner fa-spin"></i> Loading bias concepts...
            </div>
        </div>

        <script>
            // Embedded bias configuration data - no async loading required
            const BIAS_DATA = {bias_json};

            class BiasToolkit {{
                constructor() {{
                    this.biasData = BIAS_DATA;
                    this.state = {{
                        type: null,
                        stage: null,
                        searchQuery: ""
                    }};
                    this.init();
                }}

                init() {{
                    this.renderCards();
                    this.bindEvents();
                    this.filterCards();
                    
                    // Handle URL parameters for SPA navigation
                    this.loadFromURL();
                    window.addEventListener('popstate', () => this.loadFromURL());
                }}

                renderCards() {{
                    const cardList = document.getElementById('card-list');
                    cardList.innerHTML = this.biasData.map(bias => this.createCardHTML(bias)).join('');
                }}

                createCardHTML(bias) {{
                    const typeBadges = bias.types.map(type => 
                        `<span class="badge ${{type}}">${{this.capitalizeFirst(type)}}</span>`
                    ).join('');
                    
                    const stageBadges = bias.stages.map(stage => 
                        `<span class="badge stage">${{this.formatStage(stage)}}</span>`
                    ).join('');

                    const keywordsText = bias.keywords.join(', ');

                    return `
                        <div class="card-wrapper" onclick="this.navigateToPage('${{bias.slug}}');" style="cursor: pointer;">
                            <div class="card" data-type="${{bias.types.join(',')}}" data-stage="${{bias.stages.join(',')}}">
                                <div class="card-body">
                                    <h5 class="card-title">
                                        <i class="fa-solid ${{bias.icon}}"></i>
                                        ${{bias.title}}
                                    </h5>
                                    <div style="margin-bottom: 15px;">
                                        ${{typeBadges}}
                                        ${{stageBadges}}
                                    </div>
                                    <p class="card-text">
                                        ${{bias.definition}}
                                    </p>
                                    <p class="card-text keyword">
                                        <i class="fa-solid fa-tags"></i>
                                        <strong>Keywords:</strong> ${{keywordsText}}
                                    </p>
                                    <hr class="solid">
                                    <p class="card-text">
                                        <i class="fa-solid fa-exclamation-triangle" style="color: #ffc107;"></i>
                                        <strong>Stakes:</strong> ${{bias.stakes}}
                                    </p>
                                </div>
                            </div>
                        </div>
                    `;
                }}

                navigateToPage(slug) {{
                    // SPA navigation - can be customized for your routing
                    window.open(`../types/${{slug}}/`, '_blank');
                }}

                capitalizeFirst(str) {{
                    return str.charAt(0).toUpperCase() + str.slice(1);
                }}

                formatStage(stage) {{
                    const stageMap = {{
                        'setup': 'Set Up',
                        'collection': 'Collection',
                        'process': 'Process',
                        'analyse': 'Analyse',
                        'share': 'Share & Preserve'
                    }};
                    return stageMap[stage] || this.capitalizeFirst(stage);
                }}

                bindEvents() {{
                    // Type filter buttons
                    document.querySelectorAll(".type-btn").forEach(btn => {{
                        btn.addEventListener("click", () => this.handleFilter("type", btn));
                    }});

                    // Stage filter buttons
                    document.querySelectorAll(".stage-btn").forEach(btn => {{
                        btn.addEventListener("click", () => this.handleFilter("stage", btn));
                    }});

                    // Reset buttons
                    document.querySelectorAll(".reset-btn").forEach(btn => {{
                        btn.addEventListener("click", () => {{
                            if (btn.dataset.reset === "all") {{
                                this.clearAllFilters();
                            }} else {{
                                this.handleReset(btn.dataset.reset);
                            }}
                        }});
                    }});

                    // Search functionality
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {{
                        searchInput.addEventListener("input", () => this.handleSearch());
                        searchInput.addEventListener("keypress", (e) => {{
                            if (e.key === "Enter") {{
                                e.preventDefault();
                                this.handleSearch();
                            }}
                        }});
                    }}

                    const searchBtn = document.getElementById("search-btn");
                    if (searchBtn) {{
                        searchBtn.addEventListener("click", () => this.handleSearch());
                    }}

                    const clearBtn = document.getElementById("clear-search-btn");
                    if (clearBtn) {{
                        clearBtn.addEventListener("click", () => this.clearSearch());
                    }}
                }}

                handleFilter(filterType, button) {{
                    const value = button.dataset.value;
                    
                    if (this.state[filterType] === value) {{
                        this.state[filterType] = null;
                        button.classList.remove("active");
                    }} else {{
                        document.querySelectorAll(`.${{filterType}}-btn`).forEach(btn => {{
                            btn.classList.remove("active");
                        }});
                        this.state[filterType] = value;
                        button.classList.add("active");
                    }}
                    
                    this.filterCards();
                    this.updateURL();
                }}

                filterCards() {{
                    const cards = document.querySelectorAll(".card");
                    let visibleCount = 0;

                    cards.forEach(card => {{
                        const cardTypes = card.dataset.type ? card.dataset.type.split(",") : [];
                        const cardStages = card.dataset.stage ? card.dataset.stage.split(",") : [];
                        const cardText = card.textContent.toLowerCase();

                        const typeMatch = !this.state.type || cardTypes.includes(this.state.type);
                        const stageMatch = !this.state.stage || cardStages.includes(this.state.stage);
                        const searchMatch = !this.state.searchQuery || cardText.includes(this.state.searchQuery);

                        const shouldShow = typeMatch && stageMatch && searchMatch;
                        
                        card.style.display = shouldShow ? "block" : "none";
                        if (shouldShow) visibleCount++;
                    }});

                    document.getElementById("resource-count").textContent = visibleCount;
                }}

                handleSearch() {{
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {{
                        this.state.searchQuery = searchInput.value.toLowerCase();
                        this.filterCards();
                        this.updateURL();
                    }}
                }}

                clearSearch() {{
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {{
                        searchInput.value = "";
                        this.state.searchQuery = "";
                        this.filterCards();
                        this.updateURL();
                    }}
                }}

                handleReset(filterType) {{
                    this.state[filterType] = null;
                    document.querySelectorAll(`.${{filterType}}-btn`).forEach(btn => {{
                        btn.classList.remove("active");
                    }});
                    this.filterCards();
                    this.updateURL();
                }}

                clearAllFilters() {{
                    this.state = {{
                        type: null,
                        stage: null,
                        searchQuery: ""
                    }};
                    
                    document.querySelectorAll(".filter-btn").forEach(btn => {{
                        btn.classList.remove("active");
                    }});
                    
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {{
                        searchInput.value = "";
                    }}
                    this.filterCards();
                    this.updateURL();
                }}

                // SPA Navigation with URL state
                updateURL() {{
                    const params = new URLSearchParams();
                    
                    if (this.state.type) params.set('type', this.state.type);
                    if (this.state.stage) params.set('stage', this.state.stage);
                    if (this.state.searchQuery) params.set('search', this.state.searchQuery);
                    
                    const newURL = window.location.pathname + (params.toString() ? '?' + params.toString() : '');
                    history.replaceState(null, '', newURL);
                }}

                loadFromURL() {{
                    const params = new URLSearchParams(window.location.search);
                    
                    this.state.type = params.get('type');
                    this.state.stage = params.get('stage');
                    this.state.searchQuery = params.get('search') || '';
                    
                    // Update UI to match URL
                    document.getElementById('search-input').value = this.state.searchQuery;
                    
                    // Update filter buttons
                    document.querySelectorAll('.filter-btn').forEach(btn => {{
                        btn.classList.remove('active');
                        if ((btn.dataset.filter === 'type' && btn.dataset.value === this.state.type) ||
                            (btn.dataset.filter === 'stage' && btn.dataset.value === this.state.stage)) {{
                            btn.classList.add('active');
                        }}
                    }});
                    
                    this.filterCards();
                }}
            }}
            // Initialize BiasToolkit function
            function initBiasToolkit() {{
                // Always re-initialize to handle MkDocs page navigation
                window.biasToolkitInstance = new BiasToolkit();
            }}
            
            // Initialize on DOM ready and MkDocs navigation events
            document.addEventListener('DOMContentLoaded', initBiasToolkit);
            document.addEventListener('navigation.loaded', initBiasToolkit);

        </script>
    </article>
</div>'''
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(toolkit_content)
    
    print(f"\n✓ Generated complete {output_path}")
    print(f"  Found {len(bias_data)} bias concepts")
    print(f"  Total file size: {len(toolkit_content)} characters")

def main():
    BIAS_TYPES_DIR = "bias/types"
    OUTPUT_FILE = "bias/toolkit.md"
    
    if not os.path.exists(BIAS_TYPES_DIR):
        print(f"Error: Directory {BIAS_TYPES_DIR} not found")
        return
    
    print(f"Scanning {BIAS_TYPES_DIR} for bias type files...")
    bias_data = process_bias_files(BIAS_TYPES_DIR)
    
    if not bias_data:
        print("No bias data found.")
        return
    
    generate_toolkit_page(bias_data, OUTPUT_FILE)
    
    print(f"\n🎉 Success! Generated self-contained toolkit.md")
    print(f"Benefits of this approach:")
    print(f"  - No async loading issues")
    print(f"  - Works offline")
    print(f"  - Single file deployment")
    print(f"  - SPA navigation with URL state")
    print(f"  - Fast initial page load")

if __name__ == "__main__":
    main()