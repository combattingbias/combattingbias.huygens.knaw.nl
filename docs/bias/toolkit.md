---
title: Bias Toolkit
hide:
  - toc
---

<style>
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1;
}

.container-custom {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.post-title {
    color: #333;
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 10px;
    text-align: center;
}

.post-description {
    text-align: center;
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 20px;
}

.filter-section {
    margin-bottom: 30px;
    padding: 25px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    border: 2px solid #1d4066ff;
}

.filter-section h3 {
    color: #333;
    font-weight: 500;
    margin-bottom: 20px;
    margin-top: 10px;
    font-size: 1rem;
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
    border: 1px solid rgba(0,123,255,0.15);
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
    font-size: 0.8rem;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    background: #e9ecef;
    color: #495057;
    border-radius: 20px;
    font-size: 0.7rem;
    margin-right: 8px;
    margin-bottom: 8px;
    font-weight: 500;
}

.badge.discrimination {
    background: linear-gradient(135deg, #ca6a73ff 0%, #c82333 100%);
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
    font-size: 0.9rem;
}

.results-header {
    text-align: center;
    margin: 0px 0 10px 0;
    padding: 30px;
    background: #fffffdff;
    border-radius: 12px;
    border: 2px solid #e7ec54ff;
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
    background: #f1f5f8ff;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 40px;
    border: 1px solid #d8dbcbff;
}

.intro-section p {
    margin: 0;
    color: #333;
    font-size: 0.85rem;
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
            const BIAS_DATA = [
        {
                "title": "FAIR",
                "slug": "FAIR",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "setup",
                        "collection",
                        "share"
                ],
                "keywords": [
                        "findable",
                        "reusable",
                        "interoperable",
                        "accessible",
                        "reuse",
                        "legacy data",
                        "provenance",
                        "robustness",
                        "sustainability",
                        "license"
                ],
                "definition": "Principles to improve \"the Findability, Accessibility, Interoperability, and Reuse of digital assets.",
                "stakes": "Adhering to the FAIR Principles ensures your data is technically responsible, as it benefits the reusability and interoperability of the data. This also supports sustainability and better research practices, and consequently, better knowledge production.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Accessibility",
                "slug": "accessibility",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "collection",
                        "share"
                ],
                "keywords": [
                        "available",
                        "findable",
                        "inclusivity"
                ],
                "definition": "“Accessibility ensures that all people—regardless of ability—can interact with the information or services you provide.",
                "stakes": "Ensuring equal accessibility to your research (data) is a core part of creating responsible research, because it allows for knowledge to be fairly shared.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Accuracy",
                "slug": "accuracy",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "collection",
                        "process"
                ],
                "keywords": [
                        "factual",
                        "correct",
                        "errors"
                ],
                "definition": "Being exact or correct.",
                "stakes": "It is important to be as accurate as you can be - describing precisely your process or avoiding factual mistakes in descriptions or annotations for example. Inaccurate information left in your data, will be transposed onto subsequent research using your data.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Availability",
                "slug": "availability",
                "types": [
                        "discrimination"
                ],
                "stages": [
                        "collection"
                ],
                "keywords": [
                        "accessible",
                        "findable",
                        "inclusivity"
                ],
                "definition": "Denotes whether a source of data is in existence, reachable and operational.",
                "stakes": "Availability of sources impacts what type of research you can conduct and conclusions you can draw. Acknowledging a lack of availability signals to the audience that narratives are likely missing from the output. Availability also creates accountability.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Collaboration",
                "slug": "collaboration",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "setup",
                        "collection",
                        "share"
                ],
                "keywords": [
                        "stakeholder engagement",
                        "community involvement",
                        "plurivocality",
                        "multivocality",
                        "participatory research",
                        "co-creation",
                        "partnership"
                ],
                "definition": "Working together respectfully with others who bring in different perspectives.",
                "stakes": "Collaboration in any form is crucial in creating ethically responsible datasets. Not allowing for other perspectives on your work produces tunnel-visioned, and often incorrect work.",
                "icon": "fa-handshake"
        },
        {
                "title": "Documentation",
                "slug": "documentation",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "set up",
                        "collect",
                        "process",
                        "analyse",
                        "share"
                ],
                "keywords": [
                        "transparency",
                        "context",
                        "reuse",
                        "robust"
                ],
                "definition": "The descriptive account of the process of creating or curating information.",
                "stakes": "Creating extensive documentation is crucial to ensure adequate contextualisation of your research and transparency around research practices. This creates accountability as well.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Durability",
                "slug": "durability",
                "types": [
                        "opacity",
                        "discrimination"
                ],
                "stages": [
                        "setup"
                ],
                "keywords": [
                        "robustness",
                        "future",
                        "sustainability",
                        "FAIR",
                        "data management"
                ],
                "definition": "Maintenance of data's integrity and availability for the future.",
                "stakes": "Enabling accessibility and availability of your research output after the end of your project, is very valuable, because it allows other researchers to build off of your work.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Expertise",
                "slug": "expertise",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "collection",
                        "process"
                ],
                "keywords": [
                        "knowledge",
                        "power",
                        "multivocality",
                        "collaboration",
                        "team"
                ],
                "definition": "“A high level of knowledge or skill”\n\n_Definition source: Cambridge Dictionary (n.",
                "stakes": "Your expertise impacts what type of research you conduct and conclusions you draw.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Harmful Language",
                "slug": "harmful-language",
                "types": [
                        "discrimination"
                ],
                "stages": [
                        "setup",
                        "collection",
                        "process",
                        "share"
                ],
                "keywords": [
                        "harm",
                        "racism",
                        "categories"
                ],
                "definition": "Language that causes uncomfort, pain, feelings of unsafety to an individual or group of people.",
                "stakes": "Harmful language can cause hurt to people and make the spaces they access your data in feel unsafe.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Historicity",
                "slug": "historicity",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "collection"
                ],
                "keywords": [
                        "original",
                        "primary source",
                        "significance",
                        "context"
                ],
                "definition": "Philosophical term denoting an authenticity of an event in the past.",
                "stakes": "Historicity is important because we do not want to erase past wrongs. A dataset or narrative for historical research must include flaws, but must also be contextualised and not reiterated responsibly.",
                "icon": "fa-circle-question"
        },
        {
                "title": "impact",
                "slug": "impact",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "setup"
                ],
                "keywords": [
                        "topic",
                        "audience",
                        "community",
                        "benefit",
                        "harm"
                ],
                "definition": "an effect on, change or benefit to the economy, society, culture, public policy or services, health, the environment or quality of life (beyond academia)\"\n\n_Definition source: UKRI (n.",
                "stakes": "If impact goes unconsidered, and therefore not discussed in research’s output, there can be (unintended) harm done. In order to work as responsibly as possible, while aiming for just knowledge production, impact should be accounted for during conceptualisation of the project already.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Methodology",
                "slug": "methodology",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "analyse"
                ],
                "keywords": [
                        "algorithm",
                        "methods",
                        "evaluate",
                        "approach"
                ],
                "definition": "a systematic deviation in the outcomes of an evaluation process, stemming directly from the specific methods or approaches employed.",
                "stakes": "",
                "icon": "fa-microscope"
        },
        {
                "title": "Multivocality",
                "slug": "multivocality",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "collection",
                        "process"
                ],
                "keywords": [
                        "perspectives",
                        "narratives",
                        "silences",
                        "plurivocality",
                        "polyvocality",
                        "polyphony"
                ],
                "definition": "“An approach to archaeology, but also for historical reasoning, explanation and understanding that accepts a high degree of relativism and thus encourages the contemporaneous articulation of numerous ...",
                "stakes": "If multivocality is neither considered, nor represented in the publication of research (documentation), it gives an unfair representation of the past and/or present, as there are always parallel discourses present.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Ownership",
                "slug": "ownership",
                "types": [
                        "discrimination"
                ],
                "stages": [
                        "setup",
                        "share"
                ],
                "keywords": [
                        "possession",
                        "responsibility",
                        "power",
                        "accessible",
                        "privilege",
                        "oppression"
                ],
                "definition": "Data ownership refers to both the possession of and responsibility for information.",
                "stakes": "Ownership should be considered in order to confront unbalanced power structures. Concrete actions can then be taken to provide more fairness in these structures (such as shifting ownership).",
                "icon": "fa-circle-question"
        },
        {
                "title": "Positionality",
                "slug": "positionality",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "setup"
                ],
                "keywords": [
                        "social position",
                        "power structures",
                        "identity",
                        "reflexivity",
                        "privilege",
                        "oppression",
                        "situatedness"
                ],
                "definition": "“One’s social position or place in a given society in relation to race, ethnicity, and other statuses (e.",
                "stakes": "When positionality goes unconsidered or unacknowledged, the research is impacted and lacks connection to the current situation (tone-deaf). Also hinders transparency, reuse and reproducibility.",
                "icon": "fa-user-circle"
        },
        {
                "title": "Privacy",
                "slug": "privacy",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "collection"
                ],
                "keywords": [
                        "legal",
                        "difficult to share"
                ],
                "definition": "Privacy is concerned with the protection of personal data: “any information that relates to an identified or identifiable living individual (data subject).",
                "stakes": "Privacy has many (legal) regulations around it, and is therefore important to consider.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Provenance",
                "slug": "provenance",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "collection"
                ],
                "keywords": [
                        "context",
                        "agency",
                        "chronology",
                        "origin",
                        "metadata"
                ],
                "definition": "“The chronology of the origin, development, ownership, location, and changes to a system or system component and associated data [and objects and documentation].",
                "stakes": "To understand the journey your data has been through, as well as understanding the context of its creation and changes, is integral to understanding the data itself and how it can serve your research.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Recruitment",
                "slug": "recruitment",
                "types": [
                        "opacity",
                        "discrimination"
                ],
                "stages": [
                        "setup"
                ],
                "keywords": [
                        "diversity",
                        "representation",
                        "expertise",
                        "team",
                        "inclusivity",
                        "management"
                ],
                "definition": "The process of finding and hiring people to work in the same project as you.",
                "stakes": "If recruitment practices are not done thoughtfully, it will make it so that your team may lack expertise and/or diversity. Both of those are crucial in creating conscientious research.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Representation",
                "slug": "representation",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "collection",
                        "analyse",
                        "share"
                ],
                "keywords": [
                        "inclusion",
                        "diversity",
                        "voice",
                        "visibility",
                        "marginalization",
                        "marginalisation",
                        "demographics",
                        "sampling"
                ],
                "definition": "How (in what ways) something is depicted.",
                "stakes": "When groups, cultures, and histories are mis- or underrepresented, it skews narratives, lacking multiple perspectives.",
                "icon": "fa-users"
        },
        {
                "title": "Reproducibility",
                "slug": "reproducibility",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "analyse",
                        "share"
                ],
                "keywords": [
                        "documentation",
                        "reuse",
                        "evaluate"
                ],
                "definition": "A central tenet of science: To produce a reliable scientific body of knowledge, researchers must be able to trace the steps of each other’s work and verify that they yield the claimed results, or to e...",
                "stakes": "_related to: documentation; FAIR; accessibility; provenance  If research is not reproducible, it means the process has been untransparent. The research, as a result, is not trustworthy and lacks accountability.",
                "icon": "fa-circle-question"
        },
        {
                "title": "Silences",
                "slug": "silences",
                "types": [
                        "opacity",
                        "discrimination"
                ],
                "stages": [
                        "setup",
                        "analyse"
                ],
                "keywords": [
                        "archival gaps",
                        "missing data",
                        "representation",
                        "absences",
                        "documentation",
                        "historical record"
                ],
                "definition": "“A gap in the (historical) record resulting from the unintentional or purposeful absence or distortion of documentation.",
                "stakes": "Silences cause a skewed narrative of history, in which certain narratives are not acknowledged and/or included.",
                "icon": "fa-volume-xmark"
        },
        {
                "title": "Transparency",
                "slug": "transparency",
                "types": [
                        "opacity"
                ],
                "stages": [
                        "setup",
                        "collection",
                        "process",
                        "share"
                ],
                "keywords": [
                        "reuse",
                        "documentation",
                        "contextualisation",
                        "audit"
                ],
                "definition": "make data, analysis, methods, and interpretive choices underlying their claims visible in a way that allows others to evaluate them\"\n\n_Definition source: Princeton (n.",
                "stakes": "Transparency is crucial in research: in documentation, communication, publications. Research that lacks transparency causes wrongful reiterations and conclusions to be drawn - it also does not encourage responsible reuse of knowledge.",
                "icon": "fa-eye"
        },
        {
                "title": "Unintented Use",
                "slug": "unintended-use",
                "types": [
                        "discrimination",
                        "opacity"
                ],
                "stages": [
                        "analyse",
                        "share"
                ],
                "keywords": [
                        "impact",
                        "harm",
                        "accountability",
                        "risk assessment",
                        "misinterpretation",
                        "function creep",
                        "misleading"
                ],
                "definition": "Uses of produced data that are not as intended by the researcher.",
                "stakes": "Similar to risk assessments: by considering unintended uses during research, some of these uses could already be mitigated. Noting unintended uses also flags responsibility and accountability to other researchers.",
                "icon": "fa-circle-question"
        }
];

            class BiasToolkit {
                constructor() {
                    this.biasData = BIAS_DATA;
                    this.state = {
                        type: null,
                        stage: null,
                        searchQuery: ""
                    };
                    this.init();
                }

                init() {
                    this.renderCards();
                    this.bindEvents();
                    this.filterCards();
                    
                    // Handle URL parameters for SPA navigation
                    this.loadFromURL();
                    window.addEventListener('popstate', () => this.loadFromURL());
                }

                renderCards() {
                    const cardList = document.getElementById('card-list');
                    cardList.innerHTML = this.biasData.map(bias => this.createCardHTML(bias)).join('');
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
                        <div class="card-wrapper" onclick="this.navigateToPage('${bias.slug}');" style="cursor: pointer;">
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

                navigateToPage(slug) {
                    // SPA navigation - can be customized for your routing
                    window.open(`../types/${slug}/`, '_blank');
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
                    this.updateURL();
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
                        this.updateURL();
                    }
                }

                clearSearch() {
                    const searchInput = document.getElementById("search-input");
                    if (searchInput) {
                        searchInput.value = "";
                        this.state.searchQuery = "";
                        this.filterCards();
                        this.updateURL();
                    }
                }

                handleReset(filterType) {
                    this.state[filterType] = null;
                    document.querySelectorAll(`.${filterType}-btn`).forEach(btn => {
                        btn.classList.remove("active");
                    });
                    this.filterCards();
                    this.updateURL();
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
                    this.updateURL();
                }

                // SPA Navigation with URL state
                updateURL() {
                    const params = new URLSearchParams();
                    
                    if (this.state.type) params.set('type', this.state.type);
                    if (this.state.stage) params.set('stage', this.state.stage);
                    if (this.state.searchQuery) params.set('search', this.state.searchQuery);
                    
                    const newURL = window.location.pathname + (params.toString() ? '?' + params.toString() : '');
                    history.replaceState(null, '', newURL);
                }

                loadFromURL() {
                    const params = new URLSearchParams(window.location.search);
                    
                    this.state.type = params.get('type');
                    this.state.stage = params.get('stage');
                    this.state.searchQuery = params.get('search') || '';
                    
                    // Update UI to match URL
                    document.getElementById('search-input').value = this.state.searchQuery;
                    
                    // Update filter buttons
                    document.querySelectorAll('.filter-btn').forEach(btn => {
                        btn.classList.remove('active');
                        if ((btn.dataset.filter === 'type' && btn.dataset.value === this.state.type) ||
                            (btn.dataset.filter === 'stage' && btn.dataset.value === this.state.stage)) {
                            btn.classList.add('active');
                        }
                    });
                    
                    this.filterCards();
                }
            }
            // Initialize BiasToolkit function
            function initBiasToolkit() {
                // Always re-initialize to handle MkDocs page navigation
                window.biasToolkitInstance = new BiasToolkit();
            }
            
            // Initialize on DOM ready and MkDocs navigation events
            document.addEventListener('DOMContentLoaded', initBiasToolkit);
            document.addEventListener('navigation.loaded', initBiasToolkit);

        </script>
    </article>
</div>