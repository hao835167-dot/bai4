ten_day_du = input("Nhập họ và tên (gồm 2 từ): ").strip()
parts = ten_day_du.split()

if len(parts) == 2:
    ho = parts[0]
    ten = parts[1]
    print("Họ:", ho)
    print("Tên:", ten)
else:
    print("Vui lòng nhập đúng định dạng (chỉ gồm họ và tên).")
