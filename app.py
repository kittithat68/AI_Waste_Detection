
import streamlit as st
import textwrap

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Green AI | Waste Detection",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS - DARK GREEN THEME
# ==========================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #101714;
    color: #FFFFFF;
}

/* Main content */
.block-container {
    padding-top: 2rem;
}

/* Top Header */
header[data-testid="stHeader"] {
    background-color: #101714 !important;
}

header[data-testid="stHeader"] [data-testid="stToolbar"] {
    background-color: transparent !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #17231C;
    border-right: 1px solid #294334;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

/* Sidebar Text */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #7BE0A1 !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #C3D8CA !important;
}

/* Main Titles */
h1, h2, h3 {
    color: #7BE0A1 !important;
}

/* Paragraph */
p {
    color: #C3D8CA;
}

/* General Buttons */
.stButton > button {
    background-color: #16864D;
    color: white !important;
    border: 1px solid #269D60;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button p {
    color: white !important;
}

.stButton > button:hover {
    background-color: #20A65E;
    color: white !important;
    border-color: #20A65E;
    transform: translateY(-2px);
}

/* Image Button */
div.st-key-image_page button,
div.st-key-video_page button,
div.st-key-live_page button {
    background-color: #16864D !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}

div.st-key-image_page button p,
div.st-key-video_page button p,
div.st-key-live_page button p {
    color: #FFFFFF !important;
}

div.st-key-image_page button:hover,
div.st-key-video_page button:hover,
div.st-key-live_page button:hover {
    background-color: #20A65E !important;
    transform: translateY(-2px);
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: #1B2921;
    border: 1px dashed #43865C;
    border-radius: 12px;
    padding: 12px;
}

/* Eco Cards */
.eco-card {
    background-color: #1B2921;
    border: 1px solid #315640;
    border-radius: 16px;
    padding: 24px;
    min-height: 190px;
    box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
}

.eco-card h3 {
    color: #7BE0A1 !important;
    margin-bottom: 12px;
}

.eco-card p {
    color: #C3D8CA;
    line-height: 1.7;
}

/* Hero Banner */
.eco-banner {
    background: linear-gradient(
        120deg,
        #123D29,
        #176B42,
        #218B53
    );
    padding: 42px;
    border-radius: 22px;
    color: white;
    margin-bottom: 30px;
    border: 1px solid #328B58;
}

.eco-banner h1 {
    color: #FFFFFF !important;
    font-size: 34px;
    margin-bottom: 12px;
}

.eco-banner p {
    color: #E0F5E7;
    font-size: 16px;
    line-height: 1.8;
}

/* Sidebar Brand */
.brand-box {
    text-align: center;
    padding: 25px 10px;
    margin-bottom: 30px;
}

.brand-icon {
    font-size: 55px;
    margin-bottom: 12px;
}

.brand-name {
    font-size: 22px;
    font-weight: bold;
    color: #7BE0A1;
}

.brand-caption {
    font-size: 12px;
    color: #A5C8B1;
    letter-spacing: 1px;
    margin-top: 8px;
}

/* Footer */
.eco-footer {
    text-align: center;
    color: #8EAB99;
    font-size: 13px;
    padding: 25px;
    margin-top: 40px;
    border-top: 1px solid #315640;
}

/* Divider */
hr {
    border-color: #315640 !important;
}

/* Streamlit Info / Warning */
[data-testid="stAlert"] {
    background-color: #1B2921;
    border: 1px solid #315640;
    color: #FFFFFF;
}

/* Responsive */
@media (max-width: 768px) {
    .eco-banner {
        padding: 25px;
    }

    .eco-banner h1 {
        font-size: 27px;
    }

    .eco-card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        textwrap.dedent("""
        <div class="brand-box">
            <div class="brand-icon">♻️</div>
            <div class="brand-name">GREEN AI</div>
            <div class="brand-caption">
                WASTE DETECTION SYSTEM
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🌱 เมนูหลัก")

    st.caption("เลือกโหมดการตรวจจับจากเมนูด้านบน")

    st.info(
        "ระบบ AI ตรวจจับและจำแนกประเภทขยะ "
        "ด้วย YOLOv11"
    )


# ==========================================
# HERO SECTION
# ==========================================

st.markdown(
    """
    <div class="eco-banner">
        <div style="font-size:45px;">🌱</div>
        <h1>AI Waste Detection</h1>
        <p>
            ระบบตรวจจับและจำแนกประเภทขยะอัจฉริยะ
            ด้วยเทคโนโลยี YOLOv11
        </p>
        <p>
            ♻️ คัดแยกขยะอย่างถูกต้อง
            เพื่อสิ่งแวดล้อมที่ยั่งยืน
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# ABOUT SECTION
# ==========================================

st.markdown("## 🌎 เกี่ยวกับระบบ")

st.write(
    "เว็บไซต์นี้พัฒนาขึ้นเพื่อช่วยตรวจจับและจำแนกประเภทขยะ "
    "โดยใช้ปัญญาประดิษฐ์ (AI) และโมเดล YOLOv11 "
    "ช่วยให้การคัดแยกขยะสะดวกและรวดเร็วยิ่งขึ้น"
)

st.write("")


# ==========================================
# WASTE CATEGORY SECTION
# ==========================================

st.markdown("## ♻️ ประเภทขยะที่รองรับ")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>♻️ ขยะรีไซเคิล</h3>
            <p>
                ขยะที่สามารถนำกลับมาใช้ใหม่ได้
                เช่น กระดาษ พลาสติก และขวดแก้ว
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>🗑️ ขยะทั่วไป</h3>
            <p>
                ขยะที่ไม่สามารถนำกลับมารีไซเคิลได้ง่าย
                เช่น เศษวัสดุและขยะจากการใช้งานทั่วไป
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>☣️ ขยะอันตราย</h3>
            <p>
                ขยะที่อาจเป็นอันตรายต่อสุขภาพและสิ่งแวดล้อม
                เช่น ถ่านไฟฉายและแบตเตอรี่
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )


# ==========================================
# DETECTION METHOD SECTION
# ==========================================

st.markdown("")
st.markdown("## 🔍 รูปแบบการตรวจจับ")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>🖼️ ตรวจจับจากรูปภาพ</h3>
            <p>
                อัปโหลดรูปภาพเพื่อให้ AI
                ตรวจจับและจำแนกประเภทขยะ
                พร้อมแสดงกรอบวัตถุที่ตรวจพบ
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )

    if st.button("ไปหน้าตรวจจับรูปภาพ", key="image_page"):
        st.switch_page("pages/1_Detect.py")


with col2:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>🎬 ตรวจจับจากวิดีโอ</h3>
            <p>
                อัปโหลดวิดีโอเพื่อประมวลผล
                และแสดงผลการตรวจจับขยะ
                พร้อมกรอบ Bounding Box
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )

    if st.button(
        "ไปหน้าตรวจจับวิดีโอ",
        key="video_page",
        type="primary"
    ):
        st.switch_page("pages/2_Video.py")


with col3:
    st.markdown(
        textwrap.dedent("""
        <div class="eco-card">
            <h3>📷 ตรวจจับเรียลไทม์</h3>
            <p>
                ใช้กล้องเว็บแคมเพื่อตรวจจับขยะ
                แบบเรียลไทม์ผ่านเว็บไซต์
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )

    if st.button("ไปหน้ากล้องเรียลไทม์", key="live_page"):
        st.switch_page("pages/3_Live.py")


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    textwrap.dedent("""
    <div class="eco-footer">
        ♻️ GREEN AI | WASTE DETECTION SYSTEM
        <br>
        Powered by YOLOv11 and Streamlit
    </div>
    """),
    unsafe_allow_html=True
)
