ds_tu = input("Nhập dãy các từ: ").split()


max_len = max(len(tu) for tu in ds_tu)
cac_tu_dai_nhat = [tu for tu in ds_tu if len(tu) == max_len]

print("Các từ dài nhất là:", cac_tu_dai_nhat)
