import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Text & Econometrics Workshop",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #1f3b4d 0%, #2c5f7a 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .subtitle {
        font-size: 1.2rem;
        font-style: italic;
        opacity: 0.95;
    }
    .topic-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 5px solid;
        transition: transform 0.2s;
    }
    .topic-card:hover {
        transform: translateX(5px);
    }
    .level-basic { border-left-color: #1d4ed8; }
    .level-intermediate { border-left-color: #16a34a; }
    .level-advanced { border-left-color: #ea580c; }
    .level-frontier { border-left-color: #b91c1c; }

    .contact-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 2px solid #0284c7;
    }
    .suspense-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin: 2rem 0;
        font-size: 1.1rem;
        text-align: center;
        font-weight: bold;
    }
    .tech-badge {
        display: inline-block;
        background: #1f3b4d;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>📊 Text & Econometrics Workshop</h1>
    <p class="subtitle">Unlocking Economic Insights from Textual Data</p>
    <p style="font-size: 1.1rem; margin-top: 1rem;">
        🎓 Led by Dr. Merwan Roudane
    </p>
</div>
""", unsafe_allow_html=True)

# Suspense Message
st.markdown("""
<div class="suspense-box">
    ⏰ Full schedule and dates coming soon! Stay tuned for the complete program...
</div>
""", unsafe_allow_html=True)

# Introduction Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## 🌟 Why This Workshop Matters

    In today's data-driven economy, **over 80% of economic information exists as unstructured text** — yet traditional 
    econometric training rarely teaches us how to harness this goldmine of insights!

    ### 📰 The Text Data Revolution

    Central banks release policy statements. Companies publish earnings calls. News outlets report economic events in real-time. 
    Social media buzzes with consumer sentiment. Government documents reveal policy shifts. **Every day, billions of words 
    are generated that contain predictive signals for economic outcomes** — but most economists lack the tools to extract them.

    ### 🎯 What You'll Master

    This workshop bridges the gap between traditional econometrics and modern text analysis, teaching you to:
    - **Extract signals** from news, policy documents, and financial reports
    - **Build powerful indices** like Economic Policy Uncertainty (EPU) and sentiment measures
    - **Forecast** economic variables using textual data in real-time
    - **Identify causal relationships** using narrative-based natural experiments
    - **Leverage cutting-edge AI** (LLMs, BERT) for economic research
    """)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
                padding: 1.5rem; border-radius: 10px; border: 2px solid #dc2626; margin-top: 2rem;">
        <h3 style="color: #991b1b; text-align: center;">💡 Did You Know?</h3>
        <ul style="color: #7f1d1d; font-size: 0.95rem;">
            <li>The EPU index predicted the 2008 crisis</li>
            <li>Fed statements move markets by billions</li>
            <li>Job posting text predicts unemployment better than traditional surveys</li>
            <li>Twitter sentiment forecasts stock returns</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Why You Need This
st.markdown("""
## 🚀 Why You Need These Skills NOW

<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); 
            padding: 2rem; border-radius: 15px; border-left: 5px solid #16a34a; margin: 2rem 0;">

### 🔥 The Job Market Reality

**Academic Research:** Top economics journals (AER, QJE, JPE) increasingly publish text-based studies. 
From measuring economic policy uncertainty to analyzing Fed communications, text econometrics is becoming **essential** for publication.

**Central Banks & Policy Institutions:** The ECB, Fed, IMF, and World Bank now employ text analysis teams to monitor 
real-time economic conditions, analyze policy impacts, and forecast macro variables.

**Finance & Consulting:** Bloomberg, Goldman Sachs, McKinsey use NLP to predict market movements, assess corporate 
risk, and advise clients. **Professionals with these skills command premium salaries.**

**Private Sector:** Tech companies, hedge funds, and fintech firms need economists who can extract insights from 
alternative data sources — social media, news feeds, earnings calls, and more.

</div>
""", unsafe_allow_html=True)

# Learning Outcomes
st.markdown("""
## 🎓 What You'll Achieve

By the end of this workshop, you will be able to:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; border-top: 4px solid #1d4ed8;">
        <h4 style="color: #1d4ed8;">📊 Build & Deploy</h4>
        <ul style="font-size: 0.9rem;">
            <li>Create custom economic indices from text</li>
            <li>Build forecasting models with news data</li>
            <li>Design real-time monitoring systems</li>
            <li>Implement reproducible text pipelines</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; border-top: 4px solid #16a34a;">
        <h4 style="color: #16a34a;">🔬 Research & Publish</h4>
        <ul style="font-size: 0.9rem;">
            <li>Design rigorous text-based research</li>
            <li>Address identification challenges</li>
            <li>Validate text-derived measures</li>
            <li>Publish in top-tier journals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; border-top: 4px solid #ea580c;">
        <h4 style="color: #ea580c;">💼 Career Advancement</h4>
        <ul style="font-size: 0.9rem;">
            <li>Stand out in competitive job markets</li>
            <li>Lead innovative research projects</li>
            <li>Consult on data-driven policy</li>
            <li>Transition to industry roles</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Real-World Applications
st.markdown("""
## 🌍 Real-World Impact: Where Text Econometrics Changes Everything
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #3b82f6; margin-bottom: 1rem;">
        <h4>🏛️ Monetary Policy Analysis</h4>
        <p style="font-size: 0.9rem;">Measure hawkish vs. dovish tones in Fed statements. Predict interest rate 
        decisions. Quantify policy uncertainty's impact on investment and growth.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #f59e0b;">
        <h4>🏢 Corporate Analysis</h4>
        <p style="font-size: 0.9rem;">Analyze 10-K filings for risk factors. Measure management tone and its 
        impact on firm performance. Predict bankruptcy using textual risk disclosures.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #22c55e; margin-bottom: 1rem;">
        <h4>📈 Financial Markets</h4>
        <p style="font-size: 0.9rem;">Extract sentiment from earnings calls. Predict stock volatility from news. 
        Build trading strategies using real-time text data from multiple sources.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%); 
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid #ec4899;">
        <h4>👥 Labor Economics</h4>
        <p style="font-size: 0.9rem;">Extract skill requirements from job postings. Forecast unemployment using 
        labor market narratives. Measure automation risk from task descriptions.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Unique Approach
st.markdown("""
## ⭐ What Makes This Workshop Unique
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1f3b4d 0%, #2c5f7a 100%); 
                padding: 2rem; border-radius: 15px; color: white; text-align: center;">
        <div style="font-size: 3rem;">🎯</div>
        <h4 style="color: white;">Economist-First Approach</h4>
        <p style="font-size: 0.9rem;">Not just NLP tutorials — we focus on <strong>identification, 
        causality, and econometric rigor</strong> that matters for research and policy.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1f3b4d 0%, #2c5f7a 100%); 
                padding: 2rem; border-radius: 15px; color: white; text-align: center;">
        <div style="font-size: 3rem;">🔧</div>
        <h4 style="color: white;">Hands-On Practice</h4>
        <p style="font-size: 0.9rem;">Real datasets, real code, real problems. Work with Fed statements, 
        news archives, 10-Ks, and more using <strong>both R and Python</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1f3b4d 0%, #2c5f7a 100%); 
                padding: 2rem; border-radius: 15px; color: white; text-align: center;">
        <div style="font-size: 3rem;">🚀</div>
        <h4 style="color: white;">Cutting-Edge Methods</h4>
        <p style="font-size: 0.9rem;">From classical topic models to modern LLMs. Learn the latest 
        techniques that are <strong>actually being published</strong> in top journals.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Key Workshop Features
st.markdown("""
## 🎯 Workshop Highlights
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 3rem;">💻</div>
        <h4>Dual Programming</h4>
        <p style="font-size: 0.9rem;">Master techniques in <strong>both R and Python</strong>. 
        Choose your preferred language or learn both ecosystems.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 3rem;">📊</div>
        <h4>Real Economic Data</h4>
        <p style="font-size: 0.9rem;">Work with actual datasets from central banks, financial markets, 
        and policy institutions — not toy examples.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 3rem;">🎓</div>
        <h4>Publication-Ready Skills</h4>
        <p style="font-size: 0.9rem;">Learn methods currently used in top-tier journals. 
        Get ready to publish your own text-based research.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Who Should Attend
st.markdown("""
## 👥 Who Should Attend This Workshop?

<div style="background: #f7f7fb; padding: 2rem; border-radius: 10px; margin: 2rem 0;">

This workshop is designed for:

- **📚 PhD Students & Researchers** looking to incorporate text data into their dissertations or publications
- **🏛️ Central Bank & Policy Analysts** needing to monitor economic narratives and sentiment in real-time
- **💼 Finance Professionals** wanting to build text-based trading signals and risk indicators
- **🎓 Academic Economists** seeking to expand their methodological toolkit with modern NLP techniques
- **📊 Data Scientists in Economics** who want to deepen their econometric understanding of text data
- **🔍 Anyone** passionate about extracting economic insights from the growing universe of textual data

### Prerequisites
- Basic econometrics (OLS, panel data)
- Familiarity with either R or Python
- Curiosity and willingness to learn!

</div>
""", unsafe_allow_html=True)

# Technologies
st.markdown("### 💻 Programming Tools")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<span class="tech-badge">🐍 Python</span>', unsafe_allow_html=True)
with col2:
    st.markdown('<span class="tech-badge">📈 R</span>', unsafe_allow_html=True)

st.markdown("---")

# Workshop Modules
st.markdown("## 📚 Workshop Modules")

modules = {
    "Part 0 – Foundations": {
        "level": "basic",
        "icon": "🔤",
        "topics": [
            "Text as Data in Econometrics",
            "Types of text sources for economic analysis",
            "Basics of NLP for Economists",
            "Tokenization, normalization, stopwords",
            "Document-Term Matrix & Sparsity",
            "TF–IDF weighting"
        ]
    },
    "Part 1 – Text Feature Engineering": {
        "level": "intermediate",
        "icon": "⚙️",
        "topics": [
            "Bag-of-Words as regressors in econometric models",
            "TF–IDF features in regression and panel models",
            "N-grams and phrase-based economic signals",
            "Dictionary-based measures (sentiment, tone, policy)",
            "Constructing text indices for econometric analysis"
        ]
    },
    "Part 2 – Unsupervised Methods & Topic Modeling": {
        "level": "advanced",
        "icon": "🔍",
        "topics": [
            "Document clustering (k-means, hierarchical clustering)",
            "Topic Modeling (LDA, NMF) for economic texts",
            "Topic coherence and reliability",
            "Using topic proportions as regressors",
            "Dynamic Topic Models (DTM)",
            "Structural Topic Models (STM)",
            "Embedding-based Topic Models (e.g., BERTopic)"
        ]
    },
    "Part 3 – Econometric Models Using Text": {
        "level": "advanced",
        "icon": "📊",
        "topics": [
            "Text variables in OLS / GLS / IV models",
            "Panel data with text regressors (FE, RE)",
            "VAR / SVAR with text-based variables",
            "Forecasting with text (ARIMAX, MIDAS, VAR-X)",
            "State-space models with text-derived factors"
        ]
    },
    "Part 4 – Identification & Causality": {
        "level": "frontier",
        "icon": "🎯",
        "topics": [
            "Causal inference using text features",
            "Endogeneity of narrative and text-based variables",
            "Instrumental variables for text-derived measures",
            "Natural experiments with narrative data",
            "Difference-in-Differences with text-based treatments"
        ]
    },
    "Part 5 – Text-Based Economic Indices": {
        "level": "advanced",
        "icon": "📈",
        "topics": [
            "Economic Policy Uncertainty (EPU) and related indices",
            "Monetary Policy Uncertainty (MPU) from text",
            "Financial stress & risk indices from news",
            "Topic-based macroeconomic indicators",
            "Narrative policy shocks (Romer & Romer style)",
            "News-based recession indicators"
        ]
    },
    "Part 6 – High-Dimensional Econometrics": {
        "level": "frontier",
        "icon": "🔬",
        "topics": [
            "High-dimensional regressions (LASSO, ElasticNet) with text",
            "Dynamic factor models using news text",
            "Regularization for large text matrices",
            "Latent variable econometrics using embeddings"
        ]
    },
    "Part 7 – Machine Learning & Econometrics": {
        "level": "frontier",
        "icon": "🤖",
        "topics": [
            "Supervised text regressions for macro and finance",
            "Embedding-based regressors (BERT, Doc2Vec, etc.)",
            "Causal Machine Learning with text features",
            "Event-study analysis using textual data",
            "Interpretable ML for economic text models"
        ]
    },
    "Part 8 – Large Language Models (LLMs)": {
        "level": "frontier",
        "icon": "🧠",
        "topics": [
            "LLMs for extracting policy signals from text",
            "LLMs for shock identification (monetary / fiscal)",
            "LLM-based sentiment and uncertainty measures",
            "Fine-tuning LLMs for economic forecasting",
            "Robustness & econometric validation of LLM outputs"
        ]
    },
    "Part 9 – Applications & Case Studies": {
        "level": "advanced",
        "icon": "💼",
        "topics": [
            "Central bank communication analysis",
            "Fiscal policy narrative datasets",
            "Firm-level text analysis (10-Ks, earnings calls)",
            "Labor market indicators from job postings",
            "Inflation expectations derived from news text",
            "Real-time economic monitoring using social media"
        ]
    }
}

# Display modules
for module_name, module_info in modules.items():
    level_class = f"level-{module_info['level']}"

    with st.expander(f"{module_info['icon']} {module_name}", expanded=False):
        st.markdown(f'<div class="topic-card {level_class}">', unsafe_allow_html=True)

        # Level badge
        level_colors = {
            "basic": "🟦 Basic",
            "intermediate": "🟩 Intermediate",
            "advanced": "🟧 Advanced",
            "frontier": "🟥 Frontier"
        }
        st.markdown(f"**Level:** {level_colors[module_info['level']]}")

        # Topics
        st.markdown("**Topics Covered:**")
        for topic in module_info['topics']:
            st.markdown(f"• {topic}")

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Additional Topics Suggestion
st.markdown("""
## 🆕 Bonus Topics (To Be Announced)

This workshop will also cover emerging topics including:
- **Text mining from alternative data sources** (social media, web scraping)
- **Real-time sentiment analysis** for economic forecasting
- **Cross-lingual text analysis** for international economics
- **Ethical considerations** in text-based econometrics
- **Reproducibility and transparency** in text analysis workflows

""")

st.markdown("---")

# Contact Information
st.markdown("## 📞 Contact Information")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="contact-card">
        <h3>📧 Dr. Merwan Roudane</h3>
        <p><strong>Email:</strong> merwanroudane920@gmail.com</p>
        <p><strong>WhatsApp:</strong> +213 797 905 609</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <h3>🌐 Connect on Social Media</h3>
        <p>
            🔗 <a href="https://www.linkedin.com/in/merwan-roudane-b2653114b/" target="_blank">LinkedIn Profile</a>
        </p>
        <p>
            📘 <a href="https://www.facebook.com/profile.php?id=61583239360333" target="_blank">Facebook Page</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f7f7fb; border-radius: 10px;">
    <p style="font-size: 1.2rem; color: #1f3b4d; font-weight: bold;">
        🎓 Don't miss this opportunity to master text econometrics!
    </p>
    <p style="color: #666; margin-top: 1rem;">
        📅 Detailed schedule and registration information will be announced soon
    </p>
</div>
""", unsafe_allow_html=True)