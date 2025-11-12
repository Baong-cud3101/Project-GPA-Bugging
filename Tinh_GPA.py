def tinh_diem_hoc_phan(trong_so_qua_trinh, trong_so_giua_ki, trong_so_cuoi_ki,
                       diem_qua_trinh, diem_giua_ki, diem_cuoi_ki):
    diem_tong = ((diem_qua_trinh * trong_so_qua_trinh) + (diem_giua_ki * trong_so_giua_ki) +(diem_cuoi_ki * trong_so_cuoi_ki))
    return round(diem_tong, 1)  # Làm tròn đến 1 chữ số thập phân

def xac_dinh_diem_chu(diem_hoc_phan):
    """Xác định điểm chữ từ điểm học phần."""
    if diem_hoc_phan >= 9.0:
        return "A+"
    elif diem_hoc_phan >= 8.0:
        return "A"
    elif diem_hoc_phan >= 7.0:
        return "B+"
    elif diem_hoc_phan >= 6.0:
        return "B"
    elif diem_hoc_phan >= 5.0:
        return "C"
    else:
        return "F"
def diem_tinh(gpa,tinchi_hientai,gpa_aim,tin_chi_tong,tin_chi_con_lai):
    Diem_can_dat = ((gpa_aim *tin_chi_tong) - (gpa * tinchi_hientai))/(tin_chi_con_lai)
    return Diem_can_dat
# Chạy chương trình
if __name__ == "__main__":
    pass
