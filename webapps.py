import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BTG Commissary Webapps",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Main container styling */
    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #fafafa 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom styling for the page */
    .main-header {
        text-align: center;
        padding: 80px 20px 60px 20px;
        position: relative;
    }
    
    .main-title {
        font-size: 3.8em;
        font-weight: 800;
        letter-spacing: -3px;
        color: #1a1a1a;
        margin-bottom: 20px;
        line-height: 1.1;
    }
    
    .main-subtitle {
        font-size: 1.4em;
        color: #666666;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Accent line under header */
    .accent-line {
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        margin: 30px auto;
        border-radius: 2px;
    }
    
    /* Card styling */
    .app-card {
        background: #ffffff;
        border: 2px solid #f0f0f0;
        border-radius: 24px;
        padding: 45px 35px;
        margin: 20px 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .app-card:hover {
        transform: translateY(-8px);
        border-color: #FFD700;
        box-shadow: 0 25px 70px rgba(255, 215, 0, 0.15);
    }
    
    .app-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .app-card:hover::before {
        opacity: 1;
    }
    
    /* Icon container */
    .app-icon-container {
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(255, 215, 0, 0.25);
        transition: all 0.3s ease;
    }
    
    .app-card:hover .app-icon-container {
        transform: scale(1.05);
        box-shadow: 0 12px 30px rgba(255, 215, 0, 0.35);
    }
    
    .app-icon {
        width: 36px;
        height: 36px;
        stroke: #1a1a1a;
        stroke-width: 2;
        fill: none;
    }
    
    .app-title {
        font-size: 1.5em;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 15px;
        letter-spacing: -0.5px;
        line-height: 1.3;
    }
    
    .app-description {
        color: #666666;
        line-height: 1.8;
        font-size: 0.95em;
        margin-bottom: 25px;
        flex-grow: 1;
        font-weight: 400;
    }
    
    .status-badge {
        display: inline-block;
        padding: 7px 16px;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.2);
        color: #22c55e;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: 600;
        margin: 10px 0 20px 0;
        letter-spacing: 0.5px;
    }
    
    /* Button styling */
    .stButton > button,
    a[kind="primary"] {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        color: #1a1a1a !important;
        border: none !important;
        padding: 16px 35px !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 1em !important;
        letter-spacing: 0.3px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25) !important;
        width: 100% !important;
        text-decoration: none !important;
        display: inline-block !important;
        text-align: center !important;
    }
    
    .stButton > button:hover,
    a[kind="primary"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 14px 40px rgba(255, 215, 0, 0.4) !important;
    }
    
    /* Style for link buttons specifically */
    div[data-testid="stLinkButton"] > a {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        color: #1a1a1a !important;
        border: none !important;
        padding: 16px 35px !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 1em !important;
        letter-spacing: 0.3px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25) !important;
        width: 100% !important;
        text-decoration: none !important;
        display: inline-block !important;
        text-align: center !important;
    }
    
    div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 14px 40px rgba(255, 215, 0, 0.4) !important;
    }
    
    /* Footer styling */
    .custom-footer {
        text-align: center;
        color: #999999;
        padding: 80px 0 40px 0;
        font-size: 0.9em;
        border-top: 1px solid #f0f0f0;
        margin-top: 60px;
    }
    
    .custom-footer p {
        margin: 8px 0;
        font-weight: 400;
    }
    
    /* Remove padding from columns */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5em;
            letter-spacing: -2px;
        }
        
        .main-subtitle {
            font-size: 1.1em;
        }
        
        .app-card {
            padding: 35px 25px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1 class="main-title">BTG Commissary Webapps</h1>
    <div class="accent-line"></div>
    <p class="main-subtitle">Consolidated Website for Commissary Operations</p>
</div>
""", unsafe_allow_html=True)

# Create four columns for the app cards
col1, col2, col3, col4 = st.columns(4, gap="large")

# Dashboard Card
with col1:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon-container">
            <svg class="app-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="3" width="7" height="7" rx="1"/>
                <rect x="14" y="3" width="7" height="7" rx="1"/>
                <rect x="14" y="14" width="7" height="7" rx="1"/>
                <rect x="3" y="14" width="7" height="7" rx="1"/>
            </svg>
        </div>
        <h2 class="app-title">2025 Commissary Dashboard</h2>
        <p class="app-description">Monitor KPI's, production details, machine utilization, and production schedules.</p>
        <span class="status-badge">● ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Open App →", "https://btg-commi.streamlit.app/", use_container_width=True)

# Subrecipe Guide Card
with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon-container">
            <svg class="app-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="9" y1="13" x2="15" y2="13"/>
                <line x1="9" y1="17" x2="15" y2="17"/>
            </svg>
        </div>
        <h2 class="app-title">Subrecipe Guide</h2>
        <p class="app-description">Access subrecipe details, daily/weekly inventory tracking and complete raw materials explosion data.</p>
        <span class="status-badge">● ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Open App →", "https://btg-subrecipe-guide.streamlit.app/", use_container_width=True)

# Asset Tagging Card
with col3:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon-container">
            <svg class="app-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/>
                <line x1="7" y1="7" x2="7.01" y2="7"/>
            </svg>
        </div>
        <h2 class="app-title">Asset Tagging</h2>
        <p class="app-description">Track and manage commissary assets including tools, equipment with comprehensive tagging.</p>
        <span class="status-badge">● ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Open App →", "https://btg-asset-tagging.streamlit.app/", use_container_width=True)

# BOM Explosion Card
with col4:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon-container">
            <svg class="app-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
            </svg>
        </div>
        <h2 class="app-title">BOM Explosion</h2>
        <p class="app-description">Explode Bill of Materials to view component structures and material requirements efficiently.</p>
        <span class="status-badge">● ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Open App →", "https://btg-bom-explosion.streamlit.app/", use_container_width=True)

# Footer
st.markdown("""
<div class="custom-footer">
    <p><strong>BTG Commissary Operations</strong></p>
    <p>© 2025 All rights reserved • Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)
