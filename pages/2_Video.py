import streamlit as st
import os
import cv2
import tempfile
import subprocess
from pathlib import Path
from ultralytics import YOLO

st.set_page_config(
    page_title="Video Detection | Green AI",
    page_icon="🎬",
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
    <div style="font-size:42px;">🎬</div>
    <h1>AI Waste Detection – Video</h1>
    <p>อัปโหลดวิดีโอ ดูตัวอย่างต้นฉบับ แล้วเริ่มตรวจจับด้วย YOLOv11</p>
</div>
""", unsafe_allow_html=True)


MODEL_PATH = os.path.join("model", "best.pt")

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

def get_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return None

def convert_to_browser_mp4(source_path, output_path):
    ffmpeg = get_ffmpeg()
    if not ffmpeg:
        raise RuntimeError(
            "ยังไม่มี imageio-ffmpeg กรุณาติดตั้งด้วยคำสั่ง: "
            "python -m pip install imageio-ffmpeg"
        )
    command = [
        ffmpeg, "-y", "-i", source_path,
        "-map", "0:v:0", "-map", "0:a?",
        "-c:v", "libx264", "-preset", "fast",
        "-crf", "23", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart", output_path
    ]
    completed = subprocess.run(
        command, capture_output=True, text=True
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr[-2500:])


if not os.path.exists(MODEL_PATH):
    st.error("ไม่พบไฟล์ model/best.pt")
    st.stop()

try:
    model = load_model()
except Exception as e:
    st.error(f"โหลดโมเดลไม่สำเร็จ: {e}")
    st.stop()

uploaded = st.file_uploader(
    "เลือกวิดีโอ (MP4, MOV, AVI)",
    type=["mp4", "mov", "avi"]
)

if uploaded is None:
    st.info("กรุณาอัปโหลดวิดีโอเพื่อเริ่มต้น")
    st.stop()

suffix = Path(uploaded.name).suffix or ".mp4"
temp_paths = []

def make_temp(suffix):
    handle = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    path = handle.name
    handle.close()
    temp_paths.append(path)
    return path

try:
    original_path = make_temp(suffix)
    with open(original_path, "wb") as f:
        f.write(uploaded.getvalue())

    # Convert only for browser playback; this does NOT run object detection.
    preview_path = make_temp(".mp4")
    try:
        convert_to_browser_mp4(original_path, preview_path)
        preview_bytes = Path(preview_path).read_bytes()
        st.markdown('<div class="card-title">🎞️ วิดีโอต้นฉบับ (ยังไม่ตรวจจับ)</div>',
                    unsafe_allow_html=True)
        st.video(preview_bytes)
    except Exception as e:
        st.warning(
            "แปลงวิดีโอเพื่อแสดงตัวอย่างไม่ได้ จึงลองแสดงไฟล์ต้นฉบับแทน "
            f"รายละเอียด: {e}"
        )
        st.video(uploaded.getvalue())

    confidence = st.slider(
        "ความมั่นใจขั้นต่ำ (Confidence)",
        min_value=0.10, max_value=1.00, value=0.40, step=0.05
    )

    if st.button("🔍 เริ่มตรวจจับวิดีโอ", type="primary", use_container_width=True):
        output_avi = make_temp(".avi")
        output_mp4 = make_temp(".mp4")

        cap = cv2.VideoCapture(original_path)
        if not cap.isOpened():
            st.error("OpenCV เปิดวิดีโอนี้ไม่ได้ กรุณาลองไฟล์ MP4 อีกไฟล์")
            st.stop()

        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if width <= 0 or height <= 0:
            cap.release()
            st.error("อ่านขนาดวิดีโอไม่ได้")
            st.stop()

        if not (1 <= fps <= 120):
            fps = 25.0

        out_width = width - (width % 2)
        out_height = height - (height % 2)

        writer = cv2.VideoWriter(
            output_avi,
            cv2.VideoWriter_fourcc(*"MJPG"),
            fps,
            (out_width, out_height)
        )

        if not writer.isOpened():
            cap.release()
            st.error("สร้างไฟล์วิดีโอผลลัพธ์ไม่ได้")
            st.stop()

        progress = st.progress(0)
        status = st.empty()
        frame_index = 0
        total_detections = 0

        try:
            while True:
                ok, frame = cap.read()
                if not ok:
                    break

                prediction = model.predict(
                    frame, conf=confidence, imgsz=640, verbose=False
                )[0]
                annotated = prediction.plot()
                if prediction.boxes is not None:
                    total_detections += len(prediction.boxes)

                if annotated.shape[1] != out_width or annotated.shape[0] != out_height:
                    annotated = cv2.resize(annotated, (out_width, out_height))

                writer.write(annotated)
                frame_index += 1

                if total_frames > 0:
                    progress.progress(min(frame_index / total_frames, 1.0))
                status.write(f"กำลังประมวลผลเฟรม {frame_index}/{total_frames or '?'}")

        finally:
            cap.release()
            writer.release()

        if frame_index == 0:
            st.error("ไม่พบเฟรมในวิดีโอ")
            st.stop()

        with st.spinner("กำลังแปลงวิดีโอผลลัพธ์ให้เล่นบนเว็บได้..."):
            convert_to_browser_mp4(output_avi, output_mp4)

        result_bytes = Path(output_mp4).read_bytes()
        st.success(f"ตรวจจับเสร็จแล้ว ประมวลผล {frame_index} เฟรม")
        st.metric("จำนวนกรอบตรวจจับรวมทุกเฟรม", total_detections)
        st.markdown('<div class="card-title">🎯 วิดีโอผลการตรวจจับ</div>',
                    unsafe_allow_html=True)
        st.video(result_bytes)
        st.download_button(
            "⬇️ ดาวน์โหลดวิดีโอผลการตรวจจับ",
            data=result_bytes,
            file_name="waste_detection_result.mp4",
            mime="video/mp4",
            use_container_width=True
        )

finally:
    # Temporary files are removed when the page script finishes.
    # The displayed videos are held in memory by Streamlit.
    for path in temp_paths:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            pass


st.markdown("""
<div class="eco-footer">
    ♻️ GREEN AI | WASTE DETECTION SYSTEM<br>
    Powered by YOLOv11 and Streamlit
</div>
""", unsafe_allow_html=True)
