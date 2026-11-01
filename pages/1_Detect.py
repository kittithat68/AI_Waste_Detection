import streamlit as st
import os
import cv2
import numpy as np
import hashlib
from PIL import Image
from collections import Counter
from ultralytics import YOLO

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Image Detection | Green AI",
    page_icon="🖼️",
    layout="wide"
)

# ==========================================
# DARK GREEN THEME
# ==========================================
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
    <div style="font-size:42px;">🖼️</div>
    <h1>AI Waste Detection – Image</h1>
    <p>อัปโหลดรูปภาพเพื่อให้ AI ตรวจจับและจำแนกประเภทขยะด้วย YOLOv11</p>
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

st.markdown('<div class="card-title">📁 เลือกรูปภาพที่ต้องการตรวจจับ</div>',
            unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "รองรับไฟล์ JPG, JPEG และ PNG",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("กรุณาอัปโหลดรูปภาพเพื่อเริ่มใช้งาน")
    st.stop()

try:
    image = Image.open(uploaded_file).convert("RGB")
except Exception as e:
    st.error(f"ไม่สามารถเปิดรูปภาพนี้ได้: {e}")
    st.stop()

image_hash = hashlib.md5(uploaded_file.getvalue()).hexdigest()
if st.session_state.get("image_hash") != image_hash:
    st.session_state.image_hash = image_hash
    st.session_state.detection_result = None

left, right = st.columns(2, gap="large")
with left:
    st.markdown('<div class="card-title">🖼️ รูปภาพต้นฉบับ</div>',
                unsafe_allow_html=True)
    st.image(image, use_container_width=True)

with right:
    st.markdown('<div class="card-title">🎯 ผลการตรวจจับ</div>',
                unsafe_allow_html=True)
    saved = st.session_state.get("detection_result")
    if saved is None:
        st.info("ผลการตรวจจับจะแสดงที่นี่หลังจากกดเริ่มตรวจจับ")
    else:
        st.image(saved["image"], channels="BGR", use_container_width=True)

confidence = st.slider(
    "ความมั่นใจขั้นต่ำ (Confidence)",
    min_value=0.10, max_value=1.00, value=0.40, step=0.05
)

if st.button("🔍 เริ่มตรวจจับขยะ", type="primary", use_container_width=True):
    with st.spinner("AI กำลังวิเคราะห์รูปภาพ..."):
        results = model.predict(
            source=np.array(image),
            conf=confidence,
            imgsz=640,
            verbose=False
        )
        result = results[0]
        annotated = result.plot()
        rows = []
        if result.boxes is not None:
            for box in result.boxes:
                class_id = int(box.cls[0])
                score = float(box.conf[0])
                rows.append({
                    "ประเภทขยะ": model.names[class_id],
                    "ความมั่นใจ": f"{score * 100:.2f}%"
                })
        st.session_state.detection_result = {
            "image": annotated,
            "data": rows
        }
    st.rerun()

saved = st.session_state.get("detection_result")
if saved is not None:
    st.divider()
    st.markdown('<div class="card-title">📊 รายละเอียดวัตถุที่ตรวจพบ</div>',
                unsafe_allow_html=True)

    rows = saved["data"]
    if rows:
        st.dataframe(rows, use_container_width=True, hide_index=True)
        st.markdown(
            f'<div class="summary-box"><div>ตรวจพบวัตถุทั้งหมด</div>'
            f'<div class="summary-number">{len(rows)} ชิ้น</div></div>',
            unsafe_allow_html=True
        )
        st.write("")
        counts = Counter(row["ประเภทขยะ"] for row in rows)
        cols = st.columns(min(3, max(1, len(counts))))
        for index, (name, count) in enumerate(counts.items()):
            with cols[index % len(cols)]:
                st.metric(name, f"{count} ชิ้น")
    else:
        st.warning("ไม่พบวัตถุที่โมเดลตรวจจับได้")

    ok, encoded = cv2.imencode(".jpg", saved["image"])
    if ok:
        st.download_button(
            "⬇️ ดาวน์โหลดรูปภาพผลการตรวจจับ",
            data=encoded.tobytes(),
            file_name="waste_detection_result.jpg",
            mime="image/jpeg",
            use_container_width=True
        )


st.markdown("""
<div class="eco-footer">
    ♻️ GREEN AI | WASTE DETECTION SYSTEM<br>
    Powered by YOLOv11 and Streamlit
</div>
""", unsafe_allow_html=True)
