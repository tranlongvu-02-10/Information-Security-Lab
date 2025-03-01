def tao_tuple_tu_list(lst):
    result_tuple = () 
    for item in lst:
        result_tuple += (item,) 
    return result_tuple
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

result_tuple = tao_tuple_tu_list(numbers)

print("Tuple được tạo từ danh sách là:", result_tuple)
