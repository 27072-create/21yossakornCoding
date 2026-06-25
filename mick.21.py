print ("โปรแกรมคำนวณค่าไฟ")
point1=int(input("ค่าไฟ1: "))
point2=int(input("ค่าไฟ2: "))
point3=int(input("ค่าไฟ3: "))

total = point1 + point2 + point3
average = total / 3
print("ค่าไฟรวม", total)
print("ค่าไฟเฉลี่ย ", average )

if average <= 9:
    print("ฟรี")
elif average <= 50:
    print("2 บาท/หน่วย")
elif average <= 100:
    print ("4 บาท/หน่วย")