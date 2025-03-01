def truy_cap_phan_tu(tuple_data):
    phan_tu_dau_tien = tuple_data[0]
    phan_tu_cuoi_cung = tuple_data[-1]
    return phan_tu_dau_tien, phan_tu_cuoi_cung
input_tuple = input("Nhập một danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = tuple(map(int, input_tuple.split(',')))
first, last = truy_cap_phan_tu(numbers)
print("Phần tử đầu tiên là:", first)
print("Phần tử cuối cùng là:", last)
