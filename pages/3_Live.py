import streamlit as st
import av
import os
from ultralytics import YOLO
from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase,
    WebRtcMode
)

st.set_page_config(
    page_title="Live Detection | Green AI",
    page_icon="📷",
    layout="wide"
)

# ==========================================
# SHARED GREEN AI THEME (MATCHES app.py)
# ==========================================
st.markdown("""
<style>
.stApp {
    background-color: #101714;
    color: #FFFFFF;
}
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
header[data-testid="stHeader"] {
    background-color: #101714 !important;
}
header[data-testid="stHeader"] [data-testid="stToolbar"] {
    background-color: transparent !important;
}
section[data-testid="stSidebar"] {
    background-color: #17231C;
    border-right: 1px solid #294334;
}
section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #7BE0A1 !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    color: #C3D8CA !important;
}
h1, h2, h3 {
    color: #7BE0A1 !important;
}
p, label, span {
    color: #C3D8CA;
}
[data-testid="stMarkdownContainer"] {
    color: #C3D8CA;
}
.stButton > button,
.stDownloadButton > button {
    background-color: #16864D !important;
    color: #FFFFFF !important;
    border: 1px solid #269D60 !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.2rem;
    min-height: 44px;
    font-weight: 600;
    width: 100%;
    transition: 0.2s;
}
.stButton > button p,
.stDownloadButton > button p {
    color: #FFFFFF !important;
}
.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #20A65E !important;
    border-color: #20A65E !important;
    transform: translateY(-2px);
}
[data-testid="stFileUploader"] {
    background-color: #1B2921;
    border: 1px dashed #43865C;
    border-radius: 12px;
    padding: 12px;
}
[data-testid="stAlert"] {
    background-color: #1B2921;
    border: 1px solid #315640;
    color: #FFFFFF;
}
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background-color: #1B2921;
    border: 1px solid #315640;
    border-radius: 10px;
}
[data-testid="stMetric"] {
    background-color: #1B2921;
    border: 1px solid #315640;
    border-radius: 12px;
    padding: 14px;
}
.eco-card {
    background-color: #1B2921;
    border: 1px solid #315640;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 14px;
    box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
}
.eco-card h3 {
    color: #7BE0A1 !important;
}
.eco-card p {
    color: #C3D8CA;
    line-height: 1.7;
}
.eco-banner {
    background: linear-gradient(120deg, #123D29, #176B42, #218B53);
    padding: 32px 38px;
    border-radius: 22px;
    color: #FFFFFF;
    margin-bottom: 26px;
    border: 1px solid #328B58;
}
.eco-banner h1 {
    color: #FFFFFF !important;
    font-size: 32px;
    margin-bottom: 10px;
}
.eco-banner p {
    color: #E0F5E7;
    font-size: 15px;
    line-height: 1.8;
}
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
.card-title {
    background-color: #20372A;
    color: #91E5AE;
    border: 1px solid #315640;
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;
    font-weight: 700;
    margin: 18px 0 12px 0;
}
.summary-box {
    background-color: #1B3325;
    border: 1px solid #39885A;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    color: #E0F5E7;
}
.summary-number {
    color: #7BE0A1;
    font-size: 40px;
    font-weight: 800;
}
.eco-footer {
    text-align: center;
    color: #8EAB99;
    font-size: 13px;
    padding: 25px;
    margin-top: 40px;
    border-top: 1px solid #315640;
}
hr {
    border-color: #315640 !important;
}
@media (max-width: 768px) {
    .eco-banner {
        padding: 24px;
    }
    .eco-banner h1 {
        font-size: 26px;
    }
    .eco-card {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR BRANDING (MATCHES app.py)
# ==========================================
with st.sidebar:
    st.markdown("""
    <div class="brand-box">
        <div class="brand-icon">♻️</div>
        <div class="brand-name">GREEN AI</div>
        <div class="brand-caption">WASTE DETECTION SYSTEM</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🌱 เมนูหลัก")
    st.caption("เลือกโหมดการตรวจจับจากเมนูด้านล่าง")
    st.page_link("app.py", label="🏠 กลับหน้าเมนูหลัก")
    st.info("ระบบ AI ตรวจจับและจำแนกประเภทขยะ ด้วย YOLOv11")

# ==========================================
# PAGE HERO
# ==========================================

st.markdown("""
<div class="eco-banner">
    <div style="font-size:42px;">📷</div>
    <h1>AI Waste Detection – Live</h1>
    <p>ใช้กล้องเว็บแคมเพื่อตรวจจับและจำแนกประเภทขยะแบบเรียลไทม์ด้วย YOLOv11</p>
</div>
""", unsafe_allow_html=True)


MODEL_PATH = os.path.join("model", "best.pt")

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


if not os.path.exists(MODEL_PATH):
    st.error("ไม่พบไฟล์ model/best.pt กรุณาตรวจสอบตำแหน่งไฟล์")
    st.stop()

try:
    model = load_model()
except Exception as e:
    st.error(f"ไม่สามารถโหลดโมเดลได้: {e}")
    st.stop()

confidence = st.slider(
    "ความมั่นใจขั้นต่ำ (Confidence)",
    min_value=0.10,
    max_value=1.00,
    value=0.40,
    step=0.05
)

class WasteDetectionProcessor(VideoProcessorBase):
    def __init__(self, model, conf):
        self.model = model
        self.conf = conf

    def recv(self, frame):
        image = frame.to_ndarray(format="bgr24")
        result = self.model.predict(
            image,
            conf=self.conf,
            imgsz=640,
            verbose=False
        )[0]
        annotated = result.plot()
        return av.VideoFrame.from_ndarray(annotated, format="bgr24")

def processor_factory():
    return WasteDetectionProcessor(model, confidence)

st.markdown('<div class="card-title">🎥 กล้องเว็บแคม</div>',
            unsafe_allow_html=True)
st.info("กด Start เพื่อเริ่มกล้องและตรวจจับ กด Stop เพื่อหยุด")
st.caption("เมื่อเบราว์เซอร์ขอสิทธิ์ใช้งานกล้อง ให้เลือก Allow")

ctx = webrtc_streamer(
    key="waste-live-camera",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=processor_factory,
    media_stream_constraints={"video": True, "audio": False},
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
    async_processing=True
)

st.divider()

if ctx.state.playing:
    st.success("🟢 กล้องกำลังทำงานและตรวจจับขยะแบบเรียลไทม์")
else:
    st.warning("⚪ กล้องยังไม่ได้เริ่มทำงาน")

st.markdown("### ♻️ ประเภทขยะที่โมเดลรองรับ")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("RecycleWaste")
with col2:
    st.info("General Waste")
with col3:
    st.info("HazardousWaste")


st.markdown("""
<div class="eco-footer">
    ♻️ GREEN AI | WASTE DETECTION SYSTEM<br>
    Powered by YOLOv11 and Streamlit
</div>
""", unsafe_allow_html=True)
