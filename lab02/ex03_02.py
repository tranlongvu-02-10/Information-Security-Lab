def dao_nguoc_danh_sach(lst):
    return lst[::-1]  
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
dao_nguoc = dao_nguoc_danh_sach(numbers)
print("Danh sách sau khi đảo ngược:", dao_nguoc)
