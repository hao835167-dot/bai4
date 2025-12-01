s = input("Nhập chuỗi: ")
chuoi_moi = ''.join(ch for ch in s if not ch.isdigit())
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
