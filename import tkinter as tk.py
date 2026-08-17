import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

def calculate():
    try:
        distance = float(entry_distance.get())
        speed = float(entry_speed.get())
        cost_per_km = float(entry_cost.get())
        extra_minutes = int(entry_extra.get())
        school_time_str = entry_school_time.get()

        if distance <= 0 or speed <= 0 or cost_per_km < 0 or extra_minutes < 0:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกค่าที่ถูกต้อง")
            return

        # แปลงเวลาเข้าเรียน
        school_time = datetime.strptime(school_time_str, "%H:%M")

        # คำนวณเวลาเดินทาง
        travel_hours = distance / speed
        travel_minutes_total = int(travel_hours * 60)

        # คำนวณชั่วโมง/นาที
        hours = travel_minutes_total // 60
        minutes = travel_minutes_total % 60

        # คำนวณค่าใช้จ่าย
        total_cost = distance * cost_per_km

        # เวลาที่ควรออกจากบ้าน
        leave_time = school_time - timedelta(minutes=(travel_minutes_total + extra_minutes))

        # วิธีเดินทาง
        transport = transport_var.get()

        result_text = f"""
สรุปการเดินทางมาโรงเรียน
------------------------------
วิธีเดินทาง: {transport}
ระยะทาง: {distance:.2f} กม.
ความเร็วเฉลี่ย: {speed:.2f} กม./ชม.
เวลาเดินทาง: {hours} ชั่วโมง {minutes} นาที
เวลาเผื่อ: {extra_minutes} นาที
เวลาเข้าเรียน: {school_time_str}
ควรออกจากบ้านเวลา: {leave_time.strftime("%H:%M")}
ค่าใช้จ่ายโดยประมาณ: {total_cost:.2f} บาท
"""
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, result_text)
        result_box.config(state="disabled")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ถูกต้อง\nตัวอย่างเวลาเข้าเรียน: 08:00")

def clear_data():
    entry_distance.delete(0, tk.END)
    entry_speed.delete(0, tk.END)
    entry_cost.delete(0, tk.END)
    entry_extra.delete(0, tk.END)
    entry_school_time.delete(0, tk.END)
    transport_var.set("รถจักรยานยนต์")
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")

def set_speed_by_transport(*args):
    transport = transport_var.get()
    speed_map = {
        "เดิน": 5,
        "จักรยาน": 15,
        "รถจักรยานยนต์": 40,
        "รถยนต์": 35,
        "รถเมล์": 25
    }
    entry_speed.delete(0, tk.END)
    entry_speed.insert(0, str(speed_map.get(transport, 20)))

# สร้างหน้าต่างหลัก
app = tk.Tk()
app.title("School Travel App - แอปคำนวณการเดินทางมาโรงเรียน")
app.state("zoomed")  # เต็มหน้าต่างบน Windows

# ถ้าใช้ระบบอื่นที่ไม่รองรับ zoomed ให้ใช้บรรทัดนี้แทน
# app.attributes("-fullscreen", True)

# สีพื้นหลัง
app.configure(bg="#EAF4FF")

# หัวข้อ
title = tk.Label(
    app,
    text="แอปคำนวณการเดินทางมาโรงเรียน",
    font=("Arial", 24, "bold"),
    bg="#EAF4FF",
    fg="#003366"
)
title.pack(pady=20)

# เฟรมหลัก
main_frame = tk.Frame(app, bg="#EAF4FF")
main_frame.pack(pady=10)

# ฝั่งซ้าย: กรอกข้อมูล
input_frame = tk.LabelFrame(
    main_frame,
    text="กรอกข้อมูลการเดินทาง",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#003366",
    padx=20,
    pady=20
)
input_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")

# วิธีเดินทาง
tk.Label(input_frame, text="วิธีเดินทาง", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky="w", pady=5)
transport_var = tk.StringVar(value="รถจักรยานยนต์")
transport_menu = ttk.Combobox(
    input_frame,
    textvariable=transport_var,
    values=["เดิน", "จักรยาน", "รถจักรยานยนต์", "รถยนต์", "รถเมล์"],
    state="readonly",
    width=27
)
transport_menu.grid(row=0, column=1, pady=5)
transport_var.trace("w", set_speed_by_transport)

# ระยะทาง
tk.Label(input_frame, text="ระยะทาง (กม.)", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_distance = tk.Entry(input_frame, font=("Arial", 12), width=30)
entry_distance.grid(row=1, column=1, pady=5)

# ความเร็ว
tk.Label(input_frame, text="ความเร็วเฉลี่ย (กม./ชม.)", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="w", pady=5)
entry_speed = tk.Entry(input_frame, font=("Arial", 12), width=30)
entry_speed.grid(row=2, column=1, pady=5)

# ค่าใช้จ่ายต่อกิโลเมตร
tk.Label(input_frame, text="ค่าใช้จ่ายต่อกม. (บาท)", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="w", pady=5)
entry_cost = tk.Entry(input_frame, font=("Arial", 12), width=30)
entry_cost.grid(row=3, column=1, pady=5)

# เวลาเผื่อ
tk.Label(input_frame, text="เวลาเผื่อ (นาที)", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="w", pady=5)
entry_extra = tk.Entry(input_frame, font=("Arial", 12), width=30)
entry_extra.grid(row=4, column=1, pady=5)

# เวลาเข้าเรียน
tk.Label(input_frame, text="เวลาเข้าเรียน (HH:MM)", font=("Arial", 12), bg="white").grid(row=5, column=0, sticky="w", pady=5)
entry_school_time = tk.Entry(input_frame, font=("Arial", 12), width=30)
entry_school_time.grid(row=5, column=1, pady=5)

# ปุ่ม
button_frame = tk.Frame(input_frame, bg="white")
button_frame.grid(row=6, column=0, columnspan=2, pady=20)

calc_button = tk.Button(
    button_frame,
    text="คำนวณ",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=calculate
)
calc_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="ล้างข้อมูล",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=15,
    command=clear_data
)
clear_button.grid(row=0, column=1, padx=10)

# ฝั่งขวา: แสดงผล
result_frame = tk.LabelFrame(
    main_frame,
    text="ผลลัพธ์การคำนวณ",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#003366",
    padx=20,
    pady=20
)
result_frame.grid(row=0, column=1, padx=20, pady=10, sticky="n")

result_box = tk.Text(result_frame, width=50, height=20, font=("Consolas", 12), state="disabled")
result_box.pack()

# กำหนดค่าเริ่มต้น
entry_speed.insert(0, "40")
entry_cost.insert(0, "2")
entry_extra.insert(0, "10")
entry_school_time.insert(0, "08:00")

# ปุ่มออกจากโปรแกรม
exit_button = tk.Button(
    app,
    text="ปิดแอป",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    width=20,
    command=app.destroy
)
exit_button.pack(pady=20)

app.mainloop()