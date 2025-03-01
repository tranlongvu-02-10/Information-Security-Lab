so_gio_lam = float(input("Nhap so gio lam viec cua nhan vien trong tuan: "))
muc_luong_hoi = float(input("Nhap muc luong theo gio tieu chuan: "))
gio_tieu_chuan = 44
if so_gio_lam <= gio_tieu_chuan:
    tien_thuc_nhan = so_gio_lam * muc_luong_hoi 
else:
    gio_lam_them = so_gio_lam - gio_tieu_chuan
    tien_thuc_nhan = (gio_tieu_chuan * muc_luong_hoi) + (gio_lam_them * muc_luong_hoi * 1.5)
print("So tien nhan vien thuc nhan trong tuan la: ", tien_thuc_nhan)
