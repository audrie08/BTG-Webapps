import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BTG Apps Hub",
    page_icon="🚀",
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
    
    /* Main container styling */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Custom styling for the page */
    .main-header {
        text-align: center;
        padding: 60px 20px 40px 20px;
    }
    
    .main-title {
        font-size: 3.5em;
        font-weight: 800;
        letter-spacing: -2px;
        color: #1a1a1a;
        margin-bottom: 15px;
    }
    
    .main-subtitle {
        font-size: 1.3em;
        color: #666666;
        font-weight: 300;
    }
    
    /* Card styling */
    .app-card {
        background: #fafafa;
        border: 1px solid #e5e5e5;
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .app-card:hover {
        transform: translateY(-5px);
        border-color: #FFD700;
        box-shadow: 0 20px 60px rgba(255, 215, 0, 0.2);
        background: #ffffff;
    }
    
    .app-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #FFD700, #FFA500);
    }
    
    .app-icon {
        font-size: 3em;
        margin-bottom: 20px;
    }
    
    .app-title {
        font-size: 2em;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 15px;
        letter-spacing: -1px;
    }
    
    .app-description {
        color: #666666;
        line-height: 1.7;
        font-size: 1.05em;
        margin-bottom: 20px;
    }
    
    .status-badge {
        display: inline-block;
        padding: 6px 14px;
        background: rgba(255, 215, 0, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.3);
        color: #FFA500;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        margin: 10px 0 20px 0;
    }
    
    /* Button styling */
    .stButton > button,
    a[kind="primary"] {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        color: #1a1a1a !important;
        border: none !important;
        padding: 14px 35px !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25) !important;
        width: 100% !important;
        text-decoration: none !important;
        display: inline-block !important;
        text-align: center !important;
    }
    
    .stButton > button:hover,
    a[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(255, 215, 0, 0.35) !important;
    }
    
    /* Style for link buttons specifically */
    div[data-testid="stLinkButton"] > a {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important;
        color: #1a1a1a !important;
        border: none !important;
        padding: 14px 35px !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.05em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25) !important;
        width: 100% !important;
        text-decoration: none !important;
        display: inline-block !important;
        text-align: center !important;
    }
    
    div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(255, 215, 0, 0.35) !important;
    }
    
    /* Footer styling */
    .custom-footer {
        text-align: center;
        color: #999999;
        padding: 50px 0 30px 0;
        font-size: 0.95em;
    }
    
    /* Remove padding from columns */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🚀 BTG Apps Hub</h1>
    <p class="main-subtitle">Your Complete Business Operations Toolkit</p>
</div>
""", unsafe_allow_html=True)

# Create four columns for the app cards
col1, col2, col3, col4 = st.columns(4)

# Commission Calculator Card
with col1:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">💰</div>
        <h2 class="app-title">Commission Calculator</h2>
        <p class="app-description">Calculate commissions accurately and efficiently. Track sales performance and generate detailed commission reports for your team.</p>
        <span class="status-badge">Active</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Launch App →", "https://btg-commi.streamlit.app/", use_container_width=True)

# Subrecipe Guide Card
with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">📋</div>
        <h2 class="app-title">Subrecipe Guide</h2>
        <p class="app-description">Manage recipes, ingredients, and subrecipes with ease. Perfect for food service operations and kitchen management systems.</p>
        <span class="status-badge">Active</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Launch App →", "https://btg-subrecipe-guide.streamlit.app/", use_container_width=True)

# Asset Tagging Card
with col3:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">🏷️</div>
        <h2 class="app-title">Asset Tagging</h2>
        <p class="app-description">Track and manage your business assets efficiently. Tag, categorize, and monitor all your physical and digital assets in one place.</p>
        <span class="status-badge">Active</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Launch App →", "https://btg-asset-tagging.streamlit.app/", use_container_width=True)

# BOM Explosion Card
with col4:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">💥</div>
        <h2 class="app-title">BOM Explosion</h2>
        <p class="app-description">Explode Bill of Materials to view component breakdowns. Analyze product structures and material requirements efficiently.</p>
        <span class="status-badge">Active</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Launch App →", "https://btg-bom-explosion.streamlit.app/", use_container_width=True)
# Footer
st.markdown("""
<div class="custom-footer">
    <p>&copy; 2025 BTG Apps Hub. All rights reserved.</p>
    <p>Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)
