print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
# Bài 11: Thêm phần tử vào list
ds = ['abc', '123', 'xyz', 'def']  # Danh sách mẫu

print("Danh sách ban đầu:")
for ch in ds:
    print(ch)

# Thêm phần tử mới
ds.append('new_element')
ds.insert(1, 'inserted_element')  # Chèn vào vị trí index 1

print("\nDanh sách sau khi thêm phần tử:")
for ch in ds:
    print(ch)
