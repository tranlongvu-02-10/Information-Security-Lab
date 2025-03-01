def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
result_dict = dem_so_lan_xuat_hien(numbers)
print("Số lần xuất hiện của mỗi phần tử trong danh sách là:")
for key, value in result_dict.items():
    print(f"Phần tử {key}: {value} lần")
