---
title: Bias Toolkit
hide:
  - toc
---

<style>
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
}

.container-custom {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.post-title {
    color: #333;
    font-size: 2.5rem;
    font-weight: 300;
    margin-bottom: 10px;
    text-align: center;
}

.post-description {
    text-align: center;
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 40px;
}

.filter-section {
    margin-bottom: 30px;
    padding: 25px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    border-left: 4px solid #007bff;
}

.filter-section h3 {
    color: #333;
    font-weight: 500;
    margin-bottom: 20px;
    font-size: 1.3rem;
}

.button-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 15px;
    margin-top: 15px;
}

.filter-btn {
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
}

.filter-btn:hover {
    border-color: #007bff;
    background-color: #f8f9fa;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,123,255,0.15);
}

.filter-btn.active {
    background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
    color: white;
    border-color: #007bff;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0,123,255,0.3);
}

.search-container {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    flex-wrap: wrap;
}

.search-container input {
    flex: 1;
    min-width: 200px;
    padding: 12px 16px;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s ease;
}

.search-container input:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
}

.search-btn {
    padding: 12px 24px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.search-btn:hover {
    background: #0056b3;
    transform: translateY(-1px);
}

.reset-btn {
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
}

.reset-btn:hover {
    background: #545b62;
    transform: translateY(-1px);
}

.card {
    border: 1px solid #e9ecef;
    border-radius: 12px;
    margin-bottom: 25px;
    transition: all 0.3s ease;
    cursor: pointer;
    background: white;
    overflow: hidden;
}

.card:hover {
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transform: translateY(-3px);
    border-color: #007bff;
}

.card-body {
    padding: 25px;
}

.card-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 15px;
    color: #333;
    display: flex;
    align-items: center;
    gap: 10px;
}

.card-title i {
    color: #007bff;
    font-size: 1.2rem;
}

.card-text {
    color: #666;
    margin-bottom: 12px;
    line-height: 1.6;
}

.card-text.keyword {
    font-style: italic;
    color: #888;
    font-size: 0.9rem;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    background: #e9ecef;
    color: #495057;
    border-radius: 20px;
    font-size: 0.8rem;
    margin-right: 8px;
    margin-bottom: 8px;
    font-weight: 500;
}

.badge.discrimination {
    background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
    color: white;
}

.badge.opacity {
    background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
    color: white;
}

.badge.stage {
    background: linear-gradient(135deg, #28a745 0%, #218838 100%);
    color: white;
}

hr.solid {
    border-top: 2px solid #e9ecef;
    margin: 20px 0;
    opacity: 1;
}

#resource-count {
    font-weight: 700;
    color: #007bff;
    font-size: 1.1rem;
}

.results-header {
    text-align: center;
    margin: 40px 0 30px 0;
    padding: 30px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    border-top: 4px solid #007bff;
}

.results-header h2 {
    color: #333;
    font-weight: 400;
    margin-bottom: 10px;
}

.results-header p {
    color: #666;
    margin: 0;
}

.intro-section {
    background: linear-gradient(135deg, #e3f2fd 0%, #f8f9fa 100%);
    padding: 30px;
    border-radius: 12px;
    margin-bottom: 40px;
    border-left: 4px solid #2196f3;
}

.intro-section p {
    margin-bottom: 0;
    color: #333;
    font-size: 1.05rem;
    line-height: 1.7;
}

.loading {
    text-align: center;
    padding: 40px;
    color: #666;
}

/* Responsive design */
@media (max-width: 768px) {
    .search-container {
        flex-direction: column;
    }
    
    .search-container input {
        min-width: 100%;
    }
    
    .button-grid {
        grid-template-columns: 1fr;
    }
    
    .card-body {
        padding: 20px;
    }
    
    .post-title {
        font-size: 2rem;
    }
}
</style>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" integrity="sha256-HtsXJanqjKTc8vVQjO4YMhiqFoXkfBsjBWcX91T1jr8=" crossorigin="anonymous">

<div class="container-custom">
    <header class="post-header">
        <h1 class="post-title">Bias Vocabulary</h1>
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
                Each concept includes definitions, practical questions, and actionable guidance for researchers.
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
            class ConfigBasedBiasVocabulary {
                constructor() {
                    this.state = {
                        type: null,
                        stage: null,
                        searchQuery: ""
                    };
                    this.init();
                }

                init() {
                    // Wait for config to load, then render
                    if (window.biasConfig) {
                        this.renderCards();
                        this.bindEvents();
                        this.filterCards();
                    } else {
                        // Wait a bit for config to load
                        setTimeout(() => this.init(), 100);
                    }
                }

                renderCards() {
                    const cardList = document.getElementById('card-list');
                    
                    if (!window.biasConfig || window.biasConfig.length === 0) {
                        cardList.innerHTML = '<div class="loading">No bias concepts configured. Run generate_bias_config.py to create the configuration.</div>';
                        return;
                    }

                    cardList.innerHTML = window.biasConfig.map(bias => this.createCardHTML(bias)).join('');
                }

                createCardHTML(bias) {
                    const typeBadges = bias.types.map(type => 
                        `<span class="badge ${type}">${this.capitalizeFirst(type)}</span>`
                    ).join('');
                    
                    const stageBadges = bias.stages.map(stage => 
                        `<span class="badge stage">${this.formatStage(stage)}</span>`
                    ).join('');

                    const keywordsText = bias.keywords.join(', ');

                    return `
                        <div class="card-wrapper" onclick="window.open('../types/${bias.slug}/', '_blank');" style="cursor: pointer;">
                            <div class="card" data-type="${bias.types.join(',')}" data-stage="${bias.stages.join(',')}">
                                <div class="card-body">
                                    <h5 class="card-title">
                                        <i class="fa-solid ${bias.icon}"></i>
                                        ${bias.title}
                                    </h5>
                                    <div style="margin-bottom: 15px;">
                                        ${typeBadges}
                                        ${stageBadges}
                                    </div>
                                    <p class="card-text">
                                        ${bias.definition}
                                    </p>
                                    <p class="card-text keyword">
                                        <i class="fa-solid fa-tags"></i>
                                        <strong>Keywords:</strong> ${keywordsText}
                                    </p>
                                    <hr class="solid">
                                    <p class="card-text">
                                        <i class="fa-solid fa-exclamation-triangle" style="color: #ffc107;"></i>
                                        <strong>Stakes:</strong> ${bias.stakes}
                                    </p>
                                </div>
                            </div>
                        </div>
                    `;
                }

                capitalizeFirst(str) {
                    return str.charAt(0).toUpperCase() + str.slice(1);
                }

                formatStage(stage) {
                    const stageMap = {
                        'setup': 'Set Up',
                        'collection': 'Collection',
                        'process': 'Process',
                        'analyse': 'Analyse',
                        'share': 'Share & Preserve'
                    };
                    return stageMap[stage] || this.capitalizeFirst(stage);
                }

                bindEvents() {
                    // Type filter buttons
                    document.querySelectorAll(".type-btn").forEach(btn => {
                        btn.addEventListener("click", () => this.handleFilter("type", btn));
                    });

                    // Stage filter buttons
                    document.querySelectorAll(".stage-btn").forEach(btn => {
                        btn.addEventListener("click", () => this.handleFilter("stage", btn));
                    });

                    // Reset buttons
                    document.querySelectorAll(".reset-btn").forEach(btn => {
                        btn.addEventListener("click", () => {
                            if (btn.dataset.reset === "all") {
                                this.clearAllFilters();
                            } else {
                                this.handleReset(btn.dataset.reset);
                            }
                        });
                    });

                    // Search functionality
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {
                        searchInput.addEventListener("input", () => this.handleSearch());
                        searchInput.addEventListener("keypress", (e) => {
                            if (e.key === "Enter") {
                                e.preventDefault();
                                this.handleSearch();
                            }
                        });
                    }

                    const searchBtn = document.getElementById("search-btn");
                    if (searchBtn) {
                        searchBtn.addEventListener("click", () => this.handleSearch());
                    }

                    const clearBtn = document.getElementById("clear-search-btn");
                    if (clearBtn) {
                        clearBtn.addEventListener("click", () => this.clearSearch());
                    }
                }

                handleFilter(filterType, button) {
                    const value = button.dataset.value;
                    
                    if (this.state[filterType] === value) {
                        this.state[filterType] = null;
                        button.classList.remove("active");
                    } else {
                        document.querySelectorAll(`.${filterType}-btn`).forEach(btn => {
                            btn.classList.remove("active");
                        });
                        this.state[filterType] = value;
                        button.classList.add("active");
                    }
                    
                    this.filterCards();
                }

                filterCards() {
                    const cards = document.querySelectorAll(".card");
                    let visibleCount = 0;

                    cards.forEach(card => {
                        const cardTypes = card.dataset.type ? card.dataset.type.split(",") : [];
                        const cardStages = card.dataset.stage ? card.dataset.stage.split(",") : [];
                        const cardText = card.textContent.toLowerCase();

                        const typeMatch = !this.state.type || cardTypes.includes(this.state.type);
                        const stageMatch = !this.state.stage || cardStages.includes(this.state.stage);
                        const searchMatch = !this.state.searchQuery || cardText.includes(this.state.searchQuery);

                        const shouldShow = typeMatch && stageMatch && searchMatch;
                        
                        card.style.display = shouldShow ? "block" : "none";
                        if (shouldShow) visibleCount++;
                    });

                    document.getElementById("resource-count").textContent = visibleCount;
                }

                handleSearch() {
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {
                        this.state.searchQuery = searchInput.value.toLowerCase();
                        this.filterCards();
                    }
                }

                clearSearch() {
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {
                        searchInput.value = "";
                        this.state.searchQuery = "";
                        this.filterCards();
                    }
                }

                handleReset(filterType) {
                    this.state[filterType] = null;
                    document.querySelectorAll(`.${filterType}-btn`).forEach(btn => {
                        btn.classList.remove("active");
                    });
                    this.filterCards();
                }

                clearAllFilters() {
                    this.state = {
                        type: null,
                        stage: null,
                        searchQuery: ""
                    };
                    
                    document.querySelectorAll(".filter-btn").forEach(btn => {
                        btn.classList.remove("active");
                    });
                    
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {
                        searchInput.value = "";
                    }
                    this.filterCards();
                }
            }

            // Initialize when page loads
            document.addEventListener("DOMContentLoaded", () => {
                new ConfigBasedBiasVocabulary();
            });
        </script>
    </article>
</div>