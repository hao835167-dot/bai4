S = input("Nhập chuỗi S: ")


print("Các ký tự trong chuỗi (bỏ qua khoảng trắng và tab):")
for ch in S:
    if ch not in [' '. '\t']:   # nỏ qua space và tab
        print(ch)
        
