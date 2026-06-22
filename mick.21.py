print("โปรแกรมคำนวณคะแนน")

score_Math = int(input("คะแนนคณิตคุณได้เท่าไหร่: "))
score_Thai = int(input("คะแนนภาษาไทยคุณได้เท่าไหร่: "))
score_Eng = int(input("คะแนนอังกฤษคุณได้เท่าไหร่: "))

total_score = (score_Math + score_Thai + score_Eng)
average = (total_score/3)
print("คะแนนรวมทั้ง 3 วิชา", total_score, "คะแนน")
print("คะแนนเฉลี่ยรวมทั้ง 3 วิชา", average, "คะแนน")

if average <60:
    print("ควรปรับปรุง")
elif average <80:
    print("ผ่าน")
else:
    print("ดีเยี่ยม")

print("/n นายยศกร ศรีวาจา ม.4/4 เลขที่ 21 ")
