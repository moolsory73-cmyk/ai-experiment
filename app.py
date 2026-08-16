import streamlit as st
import requests

st.set_page_config(page_title="AI 선동 수사학 통합 실험실", layout="centered")
st.title("🧪 뉴미디어 선동 수사학 통합 실험실")

API_KEY = "sk_52d36a79b1212c59494df34287265e45d61e8110f7b9d0f0"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Rachel 목소리

tab1, tab2 = st.tabs(["[실험 1] 음성 파라미터 조작", "[실험 2] 미디어 연출 조작"])
DEFAULT_TEXT = "우리가 매일 접하는 정보 뒤에는 교묘하게 가공된 사실들이 숨겨져 있습니다. 이제는 침묵하지 말고 숨겨진 진실에 주목해야 합니다."

# --- [실험 1] ---
with tab1:
    st.header("🔊 [실험 1] AI 음성 내재적 요인 조작")
    st.text_area("고정 대본", DEFAULT_TEXT, height=100, disabled=True, key="t1")
    
    c1, c2 = st.columns(2)
    with c1:
        speed = st.slider("말하기 속도 (Speed)", 0.7, 1.5, 1.0, 0.05, key="s1")
        stability = st.slider("음성 안정성 (Stability - 낮을수록 격앙)", 0.0, 1.0, 0.5, 0.05, key="st1")
    with c2:
        style = st.slider("감정 과장도 (Style Exaggeration)", 0.0, 1.0, 0.0, 0.05, key="sy1")
    
    if st.button("🔊 음성 생성 및 청취", key="btn1"):
        with st.spinner("AI 음성 생성 중..."):
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": API_KEY
            }
            data = {
                "text": DEFAULT_TEXT,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": stability,
                    "similarity_boost": 0.75,
                    "style": style,
                    "use_speaker_boost": True,
                    "speed": speed
                }
            }
            
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                st.audio(response.content, format="audio/mp3")
            else:
                st.error(f"음성 생성 실패 (오류 코드: {response.status_code}). API 키를 재발급받아야 할 수 있습니다.")
            
    if st.button("✅ [실험 1] 이 설정값을 임계점으로 제출", key="sub1"):
        st.success(f"제출 완료! (속도: {speed} / 안정성: {stability} / 과장도: {style})")

# --- [실험 2] ---
with tab2:
    st.header("🎬 [실험 2] 미디어 연출(외재적 요인) 조작")
    caption = st.radio("자막 스타일", ["표준 자막 (흰색/기본)", "자극적 자막 (빨간색/강조/동적)"], key="c2_cap")
    bg_img = st.radio("배경 이미지", ["중립 이미지 (기본 그래픽)", "위기 자극 이미지 (공포/위기)"], key="c2_img")
    
    st.info(f"선택 조건: [{caption}] + [{bg_img}]")
    
    if st.button("✅ [실험 2] 연출 조건 제출", key="sub2"):
        st.success("제출 완료! 선택한 시각 연출 데이터가 기록되었습니다.")
