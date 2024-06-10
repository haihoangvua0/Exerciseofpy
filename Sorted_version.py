import random
lst = []
add = True
while add:
    a = random.randint(1, 50)
    lst.append(a)
    if len(lst) == 5:
        print(lst)
        b = input("Do you want more? Yes/No: ")
        if b == "yes" or b == "Yes":
            lst.append(a)
        else:
            break
    if len(lst) == 10:
        add = False
        break
        
print("Danh sách ban đầu:", lst)
# Tạo danh sách ngẫu nhiên True hoặc False
def sap_xep_danh_sach_so(danh_sach):
    for i in range(len(danh_sach)):
        for j in range(i + 1, len(danh_sach)):
            if danh_sach[i] > danh_sach[j]:
                danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
    return danh_sach

bieu_trung = sap_xep_danh_sach_so(lst)
print("Danh sách sau khi sắp xếp là:", bieu_trung)
print("Số lớn nhất là: {}".format(bieu_trung[-1]))
print(f"Số lớn thứ hai là: {bieu_trung[-2]}")