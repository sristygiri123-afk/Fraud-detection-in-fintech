def load_css():
    import streamlit as st
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

    /* ═══════════════════════════════════════
       ROOT VARIABLES
    ═══════════════════════════════════════ */
    :root {
        --neon-blue: #00d4ff;
        --neon-purple: #bf00ff;
        --neon-green: #00ff88;
        --neon-red: #ff003c;
        --neon-gold: #ffd700;
        --bg-deep: #010409;
        --bg-card: rgba(0, 212, 255, 0.03);
        --border-glow: rgba(0, 212, 255, 0.2);
        --text-primary: #e2f4ff;
        --text-dim: #7a9bb5;
    }

    /* ═══════════════════════════════════════
       GLOBAL BACKGROUND — ANIMATED GRID
    ═══════════════════════════════════════ */
    .stApp {
        background-color: var(--bg-deep);
        background-image:
            linear-gradient(rgba(0, 212, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.03) 1px, transparent 1px),
            radial-gradient(ellipse at 20% 20%, rgba(191, 0, 255, 0.08) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 80%, rgba(0, 212, 255, 0.08) 0%, transparent 60%);
        background-size: 40px 40px, 40px 40px, 100% 100%, 100% 100%;
        font-family: 'Rajdhani', sans-serif;
        color: var(--text-primary);
        min-height: 100vh;
    }

    /* Animated scanning line
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--neon-blue), var(--neon-purple), transparent);
        animation: scanline 4s linear infinite;
        z-index: 9999;
        pointer-events: none;
    }

    @keyframes scanline {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0.3; }
    }*/

    /* ═══════════════════════════════════════
       TITLE
    ═══════════════════════════════════════ */
    h1 {
        font-family: 'Orbitron', monospace !important;
        font-weight: 900 !important;
        font-size: 2.4rem !important;
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple), var(--neon-blue));
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 3s linear infinite;
        letter-spacing: 4px !important;
        text-transform: uppercase;
        margin-bottom: 0.5rem !important;
    }

    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    h2, h3 {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-blue) !important;
        letter-spacing: 2px !important;
        font-size: 1rem !important;
    }

    /* ═══════════════════════════════════════
       GLASS CARD — HOLOGRAPHIC
    ═══════════════════════════════════════ */
    .glass {
        background: var(--bg-card);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 24px 28px;
        border: 1px solid var(--border-glow);
        box-shadow:
            0 0 30px rgba(0, 212, 255, 0.05),
            0 8px 32px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }

    .glass::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 60%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.03), transparent);
        animation: glassshine 6s ease-in-out infinite;
    }

    @keyframes glassshine {
        0% { left: -100%; }
        50% { left: 150%; }
        100% { left: 150%; }
    }

    .glass:hover {
        border-color: rgba(0, 212, 255, 0.4);
        box-shadow:
            0 0 50px rgba(0, 212, 255, 0.1),
            0 8px 32px rgba(0, 0, 0, 0.4);
        transform: translateY(-2px);
    }

    /* ═══════════════════════════════════════
       BUTTON — CYBER STYLE
    ═══════════════════════════════════════ */
    .stButton > button {
        font-family: 'Orbitron', monospace !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        background: transparent !important;
        color: var(--neon-blue) !important;
        border: 1px solid var(--neon-blue) !important;
        border-radius: 4px !important;
        padding: 12px 32px !important;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease !important;
        clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
        width: 100%;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: -1;
    }

    .stButton > button:hover {
        color: var(--bg-deep) !important;
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple)) !important;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.5), 0 0 60px rgba(0, 212, 255, 0.2) !important;
        transform: scale(1.02) !important;
        border-color: transparent !important;
    }

    /* ═══════════════════════════════════════
       INPUT FIELDS
    ═══════════════════════════════════════ */
    .stNumberInput input, .stTextInput input {
        background: rgba(0, 212, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        border-radius: 8px !important;
        color: var(--neon-blue) !important;
        font-family: 'Orbitron', monospace !important;
        font-size: 1.1rem !important;
        padding: 10px 16px !important;
        transition: all 0.3s ease;
    }

    .stNumberInput input:focus, .stTextInput input:focus {
        border-color: var(--neon-blue) !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3) !important;
        background: rgba(0, 212, 255, 0.08) !important;
    }

    /* ═══════════════════════════════════════
       SLIDER
    ═══════════════════════════════════════ */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple)) !important;
    }

    .stSlider > div > div > div > div {
        background: var(--neon-blue) !important;
        box-shadow: 0 0 10px var(--neon-blue) !important;
    }

    /* ═══════════════════════════════════════
       METRICS
    ═══════════════════════════════════════ */
    [data-testid="stMetric"] {
        background: rgba(0, 212, 255, 0.04) !important;
        border: 1px solid rgba(0, 212, 255, 0.15) !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }

    [data-testid="stMetricLabel"] {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-dim) !important;
        font-size: 0.8rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
    }

    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-blue) !important;
        font-size: 1.4rem !important;
    }

    /* ═══════════════════════════════════════
       ALERTS — NEON STYLE
    ═══════════════════════════════════════ */
    /* Success */
    [data-testid="stAlert"][data-baseweb="notification"] div,
    .stSuccess > div {
        background: rgba(0, 255, 136, 0.08) !important;
        border: 1px solid rgba(0, 255, 136, 0.4) !important;
        border-radius: 8px !important;
        color: var(--neon-green) !important;
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1rem !important;
        letter-spacing: 1px;
    }

    /* Error */
    .stError > div {
        background: rgba(255, 0, 60, 0.08) !important;
        border: 1px solid rgba(255, 0, 60, 0.4) !important;
        border-radius: 8px !important;
        color: var(--neon-red) !important;
        font-family: 'Rajdhani', sans-serif !important;
        letter-spacing: 1px;
        animation: pulse-red 2s ease-in-out infinite;
    }

    @keyframes pulse-red {
        0%, 100% { box-shadow: 0 0 10px rgba(255, 0, 60, 0.2); }
        50% { box-shadow: 0 0 25px rgba(255, 0, 60, 0.5); }
    }

    /* Warning */
    .stWarning > div {
        background: rgba(255, 215, 0, 0.06) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 8px !important;
        color: var(--neon-gold) !important;
        font-family: 'Rajdhani', sans-serif !important;
        letter-spacing: 1px;
    }

    /* Info */
    .stInfo > div {
        background: rgba(0, 212, 255, 0.06) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 8px !important;
        color: var(--neon-blue) !important;
        font-family: 'Rajdhani', sans-serif !important;
        letter-spacing: 1px;
    }

    /* ═══════════════════════════════════════
       PROGRESS BAR
    ═══════════════════════════════════════ */
    .stProgress > div > div {
        background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple)) !important;
        border-radius: 10px !important;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5) !important;
    }

    .stProgress > div {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 10px !important;
    }

    /* ═══════════════════════════════════════
       SIDEBAR
    ═══════════════════════════════════════ */
    [data-testid="stSidebar"] {
        background: rgba(1, 4, 9, 0.95) !important;
        border-right: 1px solid rgba(0, 212, 255, 0.1) !important;
    }

    [data-testid="stSidebar"]::before {
        content: 'SYSTEM MONITOR';
        display: block;
        font-family: 'Orbitron', monospace;
        font-size: 0.6rem;
        letter-spacing: 4px;
        color: rgba(0, 212, 255, 0.3);
        text-align: center;
        padding: 12px 0 0 0;
    }

    /* ═══════════════════════════════════════
       EXPANDER
    ═══════════════════════════════════════ */
    [data-testid="stExpander"] {
        background: rgba(0, 212, 255, 0.03) !important;
        border: 1px solid rgba(0, 212, 255, 0.15) !important;
        border-radius: 10px !important;
    }

    [data-testid="stExpander"] summary {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--neon-blue) !important;
        letter-spacing: 2px !important;
        font-size: 0.9rem !important;
    }

    /* ═══════════════════════════════════════
       DATAFRAME
    ═══════════════════════════════════════ */
    [data-testid="stDataFrame"] {
        border: 1px solid rgba(0, 212, 255, 0.15) !important;
        border-radius: 10px !important;
        overflow: hidden;
    }

    /* ═══════════════════════════════════════
       CHECKBOX & SELECTBOX
    ═══════════════════════════════════════ */
    .stCheckbox label {
        color: var(--text-dim) !important;
        font-family: 'Rajdhani', sans-serif !important;
        letter-spacing: 1px !important;
    }

    .stSelectbox > div > div {
        background: rgba(0, 212, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }

    /* ═══════════════════════════════════════
       GENERAL TEXT
    ═══════════════════════════════════════ */
    p, label, .stMarkdown {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-primary) !important;
        letter-spacing: 0.5px;
    }

    /* Caption */
    .stCaption {
        color: var(--text-dim) !important;
        font-size: 0.75rem !important;
        letter-spacing: 1px !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--bg-deep); }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(var(--neon-blue), var(--neon-purple));
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)