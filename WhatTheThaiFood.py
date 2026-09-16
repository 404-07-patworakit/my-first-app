import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="อาหารนี้ชื่ออะไรกันนะ?", page_icon="🍲", layout="centered")

# Custom CSS เพื่อตกแต่ง UI ให้ใกล้เคียงกับรูปที่ 3
st.markdown("""
<style>
    /* พื้นหลังของแอป */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
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
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 12px 15px;
        margin-bottom: 10px;
        min-height: 82px;
        display: flex;
        align-items: center;
        backdrop-filter: blur(5px);
    }

    /* ปรับแต่ง Label ของ Input */
    .stTextInput > label {
        color: #e0f7fa !important;
        font-weight: bold;
        font-size: 1.05rem;
    }
    
    /* กล่องข้อความตอบ */
    .stTextInput > div > div > input {
        border-radius: 8px;
        background-color: #ffffff;
        color: #111111;
        font-weight: bold;
    }

    /* ปุ่มส่งคำตอบ */
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #00b4db, #0083b0);
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 10px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #0083b0, #00b4db);
        transform: translateY(-2px);
    }

    /* สไตล์สรุปผลคะแนน */
    .score-card {
        background: rgba(0, 0, 0, 0.4);
        border: 2px solid #00e676;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 1. ข้อมูลคำถาม คำใบ้ และเฉลย
questions = [
    {
        "id": 1,
        "hint": "เป็นเส้นเรียว สีเหลือง มีหลายแบบ หลายรสชาติ",
        "answer": "สปาเก็ตตี้"
    },
    {
        "id": 2,
        "hint": "มีทั้งเส้นและผัก คนต่างจังหวัดต้องมาในเชียงใหม่",
        "answer": "สุกี้หมู"
    },
    {
        "id": 3,
        "hint": "มีทั้งหมู ไข่ ผัก แครอท และข้าวในจานเดียวกัน",
        "answer": "ข้าวผัดหมู"
    },
    {
        "id": 4,
        "hint": "มีผักสีเขียว และเนื้อหมูที่ทำเป็นหมูกรอบเป็นส่วนใหญ่มีเนื้อไก่",
        "answer": "คะน้าหมูกรอบ"
    },
    {
        "id": 5,
        "hint": "เป็นอาหารในชาม มีเส้นนุ่มๆ เนื้อตุ๋นๆ เปื่อยๆ น่องก็มี สะโพกก็มี",
        "answer": "ก๋วยเตี๋ยวไก่ตุ๋น"
    },
    {
        "id": 6,
        "hint": "กินกับข้าวมัน มีแบบต้ม แบบทอด มักกินกับแตงกวา",
        "answer": "ข้าวมันไก่"
    }
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

# 3. ส่วนหัวของ UI
st.markdown('<div class="main-title">อาหารนี้ชื่ออะไรกันนะ?</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">ให้ผู้เล่นเติมคำตอบลงในช่องข้อความให้ถูกต้อง แล้วกดส่งคำตอบทั้งหมดด้านล่าง</div>', unsafe_allow_html=True)

# สร้าง Form เพื่อเก็บคำตอบไว้ส่งพร้อมกันทีเดียว
with st.form(key="quiz_form"):
    user_answers = {}
    
    # แสดงคำถามตาม Layout แบบ 2 คอลัมน์ (คำถาม/ช่องกรอกอยู่ซ้าย, คำใบ้อยู่อยู่ขวา)
    for q in questions:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            user_answers[q["id"]] = st.text_input(
                f"คำถาม {q['id']}:", 
                placeholder="ใส่คำตอบ...", 
                key=f"q_{q['id']}"
            )
            
        with col2:
            st.markdown(f'''
                <div class="hint-box">
                    <span>💡 <b>คำใบ้:</b> {q["hint"]}</span>
                </div>
            ''', unsafe_allow_html=True)

    st.write("")
    # ปุ่มกดส่งคำตอบทั้งหมด
    submit_button = st.form_submit_button(label="📑 ส่งคำตอบทั้งหมด")

# 4. ส่วนตรวจคำตอบและแสดงผลลัพธ์ (ทำงานหลังกดปุ่มส่งคำตอบ)
if submit_button:
    correct_count = 0
    total_questions = len(questions)
    results_detail = []

    # ตรวจสอบคำตอบแต่ละข้อ
    for q in questions:
        user_ans = user_answers[q["id"]].strip()
        correct_ans = q["answer"].strip()
        
        # เปรียบเทียบคำตอบ (ไม่สนเว้นวรรคส่วนเกิน)
        if user_ans == correct_ans:
            correct_count += 1
            is_correct = True
        else:
            is_correct = False
            
        results_detail.append({
            "id": q["id"],
            "user_ans": user_ans if user_ans else "(ไม่ได้ตอบ)",
            "correct_ans": correct_ans,
            "is_correct": is_correct
        })

    wrong_count = total_questions - correct_count
    evaluation_text = get_evaluation(correct_count)

    # แสดงส่วนสรุปผลคะแนน
    st.markdown("---")
    st.subheader("📊 ผลการแข่งขัน")
    
    # การ์ดแสดงคะแนนและเกณฑ์ประเมิน
    st.markdown(f"""
        <div class="score-card">
            <h2>คะแนนที่ได้: {correct_count} / {total_questions}</h2>
            <p>✅ ตอบถูก: <b>{correct_count}</b> ข้อ | ❌ ตอบผิด: <b>{wrong_count}</b> ข้อ</p>
            <h4 style="color: #ffe082; margin-top: 15px;">🏆 เกณฑ์ประเมิน: {evaluation_text}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.subheader("📝 เฉลยอย่างรายละเอียด:")

    # แสดงเฉลยรายข้อ
    for res in results_detail:
        if res["is_correct"]:
            st.success(f"**ข้อ {res['id']}: ถูกต้อง!** 🎉 (คำตอบของคุณ: {res['user_ans']})")
        else:
            st.error(f"**ข้อ {res['id']}: ผิด!** ❌ (คำตอบของคุณ: {res['user_ans']} | **เฉลยที่ถูกต้อง:** {res['correct_ans']})")
