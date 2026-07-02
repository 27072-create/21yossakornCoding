import random

target_number = random.randint(1, 100)
guess_count = 0

print("=== ยินดีต้อนรับสู่เกมทายเลข (1-100) ===")

while True:
    try:
        user_guess = int(input("ลองทายซิว่าเลขอะไร? (1-100): "))
        guess_count += 1
        
        if user_guess > target_number:
            print(" มากไป! ลองใหม่อีกทีนะ")
        elif user_guess < target_number:
            print(" น้อยไป! ลองใหม่อีกทีนะ")
        else:
            print(f"\n ถูกต้องนะคร้าบบบ! ")
            print(f"คุณทายถูกในเวลาทั้งหมด {guess_count} ครั้ง เก่งมาก!")
            break
            
    except ValueError:
        print(" กรุณาใส่เฉพาะตัวเลขเท่านั้นนะ!")