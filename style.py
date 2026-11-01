
import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    /* Main Background */
    .stApp {
        background-color: #F4F8F5 !important;
        color: #244C3B;
    }

    /* Top Header */
    header[data-testid="stHeader"] {
        background-color: #F4F8F5 !important;
    }

    header[data-testid="stHeader"] [data-testid="stToolbar"] {
        background-color: transparent !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #E7F2EA !important;
        border-right: 1px solid #D5E6D9;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #174D37 !important;
    }

    /* Main Text */
    h1, h2, h3 {
        color: #174D37 !important;
    }

    p, label {
        color: #496B5A;
    }

    /* Buttons */
    .stButton > button {
        background-color: #21865B !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #176B46 !important;
    }

    /* File Uploader */
    [data-testid="stFileUploader"] {
        background-color: white !important;
        border: 1px dashed #9CC9AC;
        border-radius: 12px;
        padding: 12px;
    }

    [data-testid="stFileUploader"] section {
        background-color: white !important;
    }

    /* Cards */
    .eco-card {
        background-color: white;
        border: 1px solid #DDEBE0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 3px 12px rgba(31, 91, 60, 0.05);
    }

    .eco-card h3 {
        color: #176B46 !important;
    }

    .eco-card p {
        color: #587564 !important;
        line-height: 1.7;
    }

    /* Banner */
    .eco-banner {
        background: linear-gradient(120deg, #174D37, #2D9560);
        padding: 35px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
    }

    .eco-banner h1 {
        color: white !important;
    }

    .eco-banner p {
        color: #E6F5EB !important;
    }

    /* Input fields */
    [data-baseweb="input"] > div,
    [data-baseweb="textarea"] > div,
    [data-baseweb="select"] > div {
        background-color: white !important;
    }

    /* Footer */
    .eco-footer {
        text-align: center;
        color: #789383;
        padding: 25px;
        margin-top: 40px;
        border-top: 1px solid #DDEBE0;
    }
    .video-card {
    background-color: #21865B !important;
}

.video-card h3,
.video-card p {
    color: white !important;
}

    
    </style>
    """, unsafe_allow_html=True)
    
