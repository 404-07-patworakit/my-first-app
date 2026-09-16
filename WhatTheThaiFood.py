import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="อาหารนี้ชื่ออะไรกันนะ?", page_icon="🍲", layout="centered")

# Custom CSS เพื่อตกแต่ง UI ทั้งหมด
st.markdown("""
<style>
    /* พื้นหลังของแอป */
    .stApp {
        background-color: #1a2a32;
        color: #ffffff;
    }
    
    /* หัวข้อหลัก */
    .main-title {
        text-align: center;
        color: #e0f7fa;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-align: center;
        color: #80deea;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* กล่องคำใบ้ */
    .hint-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 10px;
        padding: 12px 15px;
        margin-bottom: 10px;
        min-height: 82px;
        display: flex;
        align-items: center;
    }

    /* กล่องข้อความตอบ */
    .stTextInput > div > div > input {
        border-radius: 8px;
        background-color: #ffffff;
        color: #111111;
        font-weight: bold;
    }

    /* ปุ่มส่งคำตอบ (ปรับเป็นสีโทนเดียวและตัวอักษรสีขาว) */
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        background-color: #0284c7 !important; /* สีฟ้าโทนเดียว */
        color: #ffffff !important;             /* ตัวอักษรสีขาว */
        font-weight: bold;
        font-size: 1.2rem;
        padding: 10px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        transition: background-color 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #0369a1 !important; /* สีเมื่อเอาเมาส์ไปชี้ */
        color: #ffffff !important;
    }

    /* สไตล์สรุปผลคะแนน */
    .score-card {
        border: 2px solid #00e676;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        background-color: rgba(0, 0, 0, 0.2);
        margin-bottom: 25px;
    }

    .score-title {
        font-size: 2.2rem;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
    }

    .score-stats {
        font-size: 1rem;
        color: #ffffff;
        margin-bottom: 15px;
    }

    .score-evaluation {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffe082;
    }

    /* สไตล์กล่องเฉลยรายข้อ */
    .result-box-correct {
        background-color: rgba(0, 230, 118, 0.1);
        border: 1px solid rgba(0, 230, 118, 0.2);
        color: #00e676;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 1rem;
    }

    .result-box-wrong {
        background-color: rgba(255, 82, 82, 0.1);
        border: 1px solid rgba(255, 82, 82, 0.2);
        color: #ff5252;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 1. ข้อมูลคำถาม
questions = [
    {"id": 1, "hint": "เป็นเส้นเรียว สีเหลือง มีหลายแบบ หลายรสชาติ", "answer": "สปาเก็ตตี้"},
    {"id": 2, "hint": "มีทั้งเส้นและผัก คนต่างจังหวัดต้องมาในเชียงใหม่", "answer": "สุกี้หมู"},
    {"id": 3, "hint": "มีทั้งหมู ไข่ ผัก แครอท และข้าวในจานเดียวกัน", "answer": "ข้าวผัดหมู"},
    {"id": 4, "hint": "มีผักสีเขียว และเนื้อหมูที่ทำเป็นหมูกรอบเป็นส่วนใหญ่มีเนื้อไก่", "answer": "คะน้าหมูกรอบ"},
    {"id": 5, "hint": "เป็นอาหารในชาม มีเส้นนุ่มๆ เนื้อตุ๋นๆ เปื่อยๆ น่องก็มี สะโพกก็มี", "answer": "ก๋วยเตี๋ยวไก่ตุ๋น"},
    {"id": 6, "hint": "กินกับข้าวมัน มีแบบต้ม แบบทอด มักกินกับแตงกวา", "answer": "ข้าวมันไก่"}
]

# 2. ฟังก์ชันประเมินเกณฑ์
def get_evaluation(score):
    if score <= 1:
        return "0-1 คะแนน : ไม่เคยกิน อาจจะเคย"
    elif score <= 2:
        return "1-2 คะแนน : รู้จักพอผ่านๆ"
    elif score <= 4:
        return "3-4 คะแนน : กินบ้างไม่กินบ้าง"
    else:
        return "5-6 คะแนน : เซียนอาหารไทย"

# จัดการ State การแสดงผล
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# ==================== หน้าที่ 1: หน้าเล่นเกม/ตอบคำถาม ====================
if not st.session_state.submitted:
    st.markdown('<div class="main-title">อาหารนี้ชื่ออะไรกันนะ?</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">ให้ผู้เล่นเติมคำตอบลงในช่องข้อความให้ถูกต้อง แล้วกดส่งคำตอบด้านล่าง</div>', unsafe_allow_html=True)

    with st.form(key="quiz_form"):
        user_answers = {}
        for q in questions:
            col1, col2 = st.columns([1, 1])
            with col1:
                user_answers[q["id"]] = st.text_input(f"คำถาม {q['id']}:", placeholder="ใส่คำตอบ...", key=f"q_{q['id']}")
            with col2:
                st.markdown(f'<div class="hint-box"><span>💡 <b>คำใบ้:</b> {q["hint"]}</span></div>', unsafe_allow_html=True)

        st.write("")
        submit_button = st.form_submit_button(label="ส่งคำตอบทั้งหมด")

        if submit_button:
            # คำนวณคะแนนและบันทึกใส่ session_state
            correct_count = 0
            results_detail = []
            
            for q in questions:
                user_ans = user_answers[q["id"]].strip()
                correct_ans = q["answer"].strip()
                is_correct = (user_ans == correct_ans)
                if is_correct:
                    correct_count += 1
                
                results_detail.append({
                    "id": q["id"],
                    "user_ans": user_ans if user_ans else "(ไม่ได้ตอบ)",
                    "correct_ans": correct_ans,
                    "is_correct": is_correct
                })
            
            st.session_state.correct_count = correct_count
            st.session_state.results_detail = results_detail
            st.session_state.submitted = True
            st.rerun()

# ==================== หน้าที่ 2: หน้าแสดงผลการแข่งขัน ====================
else:
    st.markdown("## 📊 ผลการแข่งขัน")
    
    correct_count = st.session_state.correct_count
    total_questions = len(questions)
    wrong_count = total_questions - correct_count
    evaluation_text = get_evaluation(correct_count)

    # กล่องสรุปคะแนน
    st.markdown(f"""
        <div class="score-card">
            <div class="score-title">คะแนนที่ได้: {correct_count} / {total_questions}</div>
            <div class="score-stats">
                ✅ ตอบถูก: {correct_count} ข้อ &nbsp;|&nbsp; ❌ ตอบผิด: {wrong_count} ข้อ
            </div>
            <div class="score-evaluation">
                🏆 เกณฑ์ประเมิน: {evaluation_text}
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📝 เฉลยอย่างละเอียด:")

    # แสดงรายการเฉลยรายข้อ
    for res in st.session_state.results_detail:
        if res["is_correct"]:
            st.markdown(
                f'<div class="result-box-correct">ข้อ {res["id"]}: ถูกต้อง! 🎉 <span style="color: #a0a0a0;">(คำตอบของคุณ: {res["user_ans"]})</span></div>', 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-box-wrong">ข้อ {res["id"]}: ผิด! ❌ <span style="color: #a0a0a0;">(คำตอบของคุณ: {res["user_ans"]} | </span><b>เฉลย: {res["correct_ans"]}</b>)</div>', 
                unsafe_allow_html=True
            )

    st.write("")
    # ปุ่มเริ่มเล่นใหม่
    if st.button("🔄 เล่นใหม่อีกครั้ง"):
        st.session_state.submitted = False
        st.rerun()
