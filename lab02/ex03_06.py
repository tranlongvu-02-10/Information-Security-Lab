def xoa_phan_tu_theo_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]  
        print(f"Phần tử với key '{key}' đã được xóa.")
    else:
        print(f"Key '{key}' không tồn tại trong dictionary.")
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
key_to_delete = input("Nhập key muốn xóa: ")
xoa_phan_tu_theo_key(my_dict, key_to_delete)
print("Dictionary sau khi xóa:", my_dict)
