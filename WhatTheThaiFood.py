import streamlit as st

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="อาหารนี้ชื่ออะไรกันนะ?",
    page_icon="🍲",
    layout="centered"
)

# 2. ข้อมูลโจทย์และคำเฉลย (ตามรูปที่ 1)
questions_data = [
    {
        "hint": "เป็นเส้นเรียว สีเหลือง มีหลายแบบ หลายรสชาติ",
        "answer": "สปาเก็ตตี้"
    },
    {
        "hint": "มีทั้งเส้นและผัก คนต่างจังหวัดต้องมากินที่เชียงใหม่",
        "answer": "สุกี้หมู"
    },
    {
        "hint": "มีทั้งหมู ไข่ ผัก แครอท และข้าวในจานเดียวกัน",
        "answer": "ข้าวผัดหมู"
    },
    {
        "hint": "มีผักสีเขียว และเนื้อหมูที่ทำเป็นหมูกรอบเป็นส่วนใหญ่มีเนื้อไก่",
        "answer": "คะน้าหมูกรอบ"
    },
    {
        "hint": "เป็นอาหารในชาม มีเส้นนุ่มๆ เนื้อตุ๋นๆ เปื่อยๆ น่องก็มี สะโพกก็มี",
        "answer": "ก๋วยเตี๋ยวไก่ตุ๋น"
    },
    {
        "hint": "กินกับข้าวมัน มีแบบต้ม แบบทอด มักกินกับแตงกวา",
        "answer": "ข้าวมันไก่"
    }
]

# 3. ฟังก์ชันคำนวณเกณฑ์ประเมินผู้เล่น (ตามรูปที่ 2)
def get_evaluation(score):
    if score in [0, 1]:
        return "ไม่เคยกิน อาจจะเคย"
    elif score in [1, 2]:
        return "รู้จักพอผ่านๆ"
    elif score in [3, 4]:
        return "กินบ้างไม่กินบ้าง"
    elif score in [5, 6]:
        return "เกือบเป็นเซียนอาหารไทย"
    elif score == 6:
        return "เซียนอาหารไทย"
    return "ไม่เคยกิน อาจจะเคย"

# 4. สไตล์ CSS ตกแต่งให้ตรงกับรูปที่ 3 (กล่องคำใบ้และช่องกรอกสีฟ้า)
st.markdown("""
    <style>
    /* สไตล์ปุ่มคำใบ้รูปทรงมน สีฟ้า */
    .hint-card {
        background-color: #00b4d8;
        color: white;
        padding: 18px 15px;
        border-radius: 20px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
    }
    /* ปรับแต่งช่อง Input ให้โค้งมนสวยงาม */
    div[data-baseweb="input"] > div {
        background-color: #00b4d8 !important;
        border-radius: 15px !important;
        color: white !important;
    }
    div[data-baseweb="input"] input {
        color: white !important;
        font-weight: bold;
    }
    /* ซ่อนเส้นขอบขยะบางส่วน */
    hr {
        margin: 1em 0;
    }
    </style>
""", unsafe_allow_html=True)

# 5. หัวข้อเกม (ตามรูปที่ 3)
st.markdown("<h1 style='text-align: center;'>ชื่อเกม</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>อาหารนี้ชื่ออะไรกันนะ?</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ให้ผู้เล่นเติมคำตอบลงในช่องข้อความให้ถูกต้อง แล้วกดส่งคำตอบข้างคำถาม</p>", unsafe_allow_html=True)
st.write("")

# สร้างตัวแปรเก็บสถานะการตอบคำถามใน Session State
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 6. สร้างรายการคำถาม 6 ข้อ
for i, q in enumerate(questions_data):
    col_left, col_right = st.columns([1.1, 1], gap="medium")
    
    with col_left:
        st.markdown(f"**คำถาม {i+1}: abc**")
        
        # ช่องกรอกคำตอบ และ ปุ่มส่งคำตอบ ในบรรทัดเดียวกัน
        c_input, c_btn = st.columns([3, 1])
        with c_input:
            user_ans = st.text_input(
                label=f"q_{i}", 
                key=f"input_{i}", 
                label_visibility="collapsed",
                placeholder="พิมพ์คำตอบที่นี่..."
            )
        with c_btn:
            submitted = st.button("กด", key=f"btn_{i}")
            if submitted:
                # ตรวจสอบคำตอบ
                if user_ans.strip() == q["answer"]:
                    st.session_state.answers[i] = True
                else:
                    st.session_state.answers[i] = False

        # แสดงสถานะ ถูก/ผิด ด้านล่างช่องกรอก
        if i in st.session_state.answers:
            if st.session_state.answers[i]:
                st.success("✓ ถูกต้อง")
            else:
                st.error("✕ ผิด")

    with col_right:
        # แสดงกล่องคำใบ้
        st.markdown(f"""
            <div class="hint-card">
                คำใบ้: {q['hint']}
            </div>
        """, unsafe_allow_html=True)
    
    st.write("---")

# 7. สรุปคะแนนและเกณฑ์ประเมิน (ด้านล่างสุด)
total_score = sum(1 for is_correct in st.session_state.answers.values() if is_correct)
evaluation_result = get_evaluation(total_score)

st.markdown(f"### คะแนนที่ได้: `{total_score} / 6`")
st.markdown(f"### เกณฑ์: `{evaluation_result}`")
