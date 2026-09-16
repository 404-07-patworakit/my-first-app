import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# 1. ข้อมูลโจทย์และคำเฉลย
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# 2. ฟังก์ชันคำนวณเกณฑ์ประเมิน
# ---------------------------------------------------------
def get_evaluation(score):
    if score == 0:
        return "ไม่เคยกิน อาจจะเคย"
    elif score in [1, 2]:
        return "รู้จักพอผ่านๆ"
    elif score in [3, 4]:
        return "กินบ้างไม่กินบ้าง"
    elif score == 5:
        return "เกือบเป็นเซียนอาหารไทย"
    elif score == 6:
        return "เซียนอาหารไทย"
    return ""

# ---------------------------------------------------------
# 3. การสร้างหน้าต่าง GUI
# ---------------------------------------------------------
root = tk.Tk()
root.title("อาหารนี้ชื่ออะไรกันนะ?")
root.geometry("650x700")
root.configure(bg="#ffffff")

# ตัวแปรสำหรับเก็บสภาวะคำตอบและคะแนน
entry_widgets = []
status_labels = []
user_answers = [""] * len(questions_data)
scores = [0] * len(questions_data)

# หัวข้อเกม
title_label = tk.Label(root, text="อาหารนี้ชื่ออะไรกันนะ?", font=("Tahoma", 20, "bold"), bg="#ffffff", fg="#000000")
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(root, text="ให้ผู้เล่นเติมคำตอบลงในช่องข้อความให้ถูกต้อง แล้วกดส่งคำตอบข้างคำถาม", font=("Tahoma", 11), bg="#ffffff", fg="#333333")
subtitle_label.pack(pady=(0, 20))

# ส่วนแสดงคำถามแต่ละข้อ
frame_questions = tk.Frame(root, bg="#ffffff")
frame_questions.pack(padx=20, fill="both", expand=True)

def submit_answer(index):
    ans = entry_widgets[index].get().strip()
    if not ans:
        messagebox.showwarning("เตือน", "กรุณากรอกคำตอบก่อนกดส่ง")
        return
    
    correct_ans = questions_data[index]["answer"]
    if ans == correct_ans:
        scores[index] = 1
        status_labels[index].config(text="✓ ถูกต้อง", fg="green")
    else:
        scores[index] = 0
        status_labels[index].config(text="✕ ผิด", fg="red")
    
    update_score_and_eval()

def update_score_and_eval():
    total_score = sum(scores)
    evaluation = get_evaluation(total_score)
    
    score_val_label.config(text=f"{total_score} / 6")
    eval_val_label.config(text=f"{evaluation}")

for i, q in enumerate(questions_data):
    # แถวของแต่ละข้อ
    row_frame = tk.Frame(frame_questions, bg="#ffffff")
    row_frame.pack(fill="x", pady=6)

    # ด้านซ้าย (คำถาม, ช่องกรอก, ปุ่มกดส่ง, แสดงผลถูก/ผิด)
    left_frame = tk.Frame(row_frame, bg="#ffffff")
    left_frame.pack(side="left", anchor="w")

    q_label = tk.Label(left_frame, text=f"คำถาม {i+1}:", font=("Tahoma", 11, "bold"), bg="#ffffff")
    q_label.grid(row=0, column=0, sticky="w", columnspan=2)

    entry = tk.Entry(left_frame, font=("Tahoma", 11), width=18, bg="#00b4d8", fg="white", insertbackground="white")
    entry.grid(row=1, column=0, pady=2, padx=(0, 5))
    entry_widgets.append(entry)

    btn_submit = tk.Button(left_frame, text="ส่ง", font=("Tahoma", 9), bg="#00b4d8", fg="white", activebackground="#0077b6", activeforeground="white", command=lambda idx=i: submit_answer(idx))
    btn_submit.grid(row=1, column=1)

    status_lbl = tk.Label(left_frame, text="", font=("Tahoma", 10, "bold"), bg="#ffffff")
    status_lbl.grid(row=1, column=2, padx=5)
    status_labels.append(status_lbl)

    # ด้านขวา (กล่องคำใบ้)
    right_frame = tk.Frame(row_frame, bg="#ffffff")
    right_frame.pack(side="right", fill="x", expand=True, padx=(20, 0))

    hint_box = tk.Label(right_frame, text=f"คำใบ้: {q['hint']}", font=("Tahoma", 10), bg="#00b4d8", fg="white", wraplength=280, justify="left", padding=8)
    hint_box.pack(fill="x")

# ---------------------------------------------------------
# 4. ส่วนสรุปคะแนนและเกณฑ์ประเมิน
# ---------------------------------------------------------
frame_result = tk.Frame(root, bg="#ffffff")
frame_result.pack(fill="x", padx=30, pady=20)

score_title_label = tk.Label(frame_result, text="คะแนนที่ได้:", font=("Tahoma", 12, "bold"), bg="#ffffff")
score_title_label.grid(row=0, column=0, sticky="w")

score_val_label = tk.Label(frame_result, text="0 / 6", font=("Tahoma", 12), bg="#ffffff", fg="#00b4d8")
score_val_label.grid(row=0, column=1, sticky="w", padx=10)

eval_title_label = tk.Label(frame_result, text="เกณฑ์:", font=("Tahoma", 12, "bold"), bg="#ffffff")
eval_title_label.grid(row=1, column=0, sticky="w", pady=(5, 0))

eval_val_label = tk.Label(frame_result, text="ไม่เคยกิน อาจจะเคย", font=("Tahoma", 12), bg="#ffffff", fg="#00b4d8")
eval_val_label.grid(row=1, column=1, sticky="w", padx=10, pady=(5, 0))

# เริ่มการทำงานของโปรแกรม
root.mainloop()
