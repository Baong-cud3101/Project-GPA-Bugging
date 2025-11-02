import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import QtWidgets
from Giaodien_GPA import Ui_MainWindow
from Tinh_GPA import *

class MainWindow():
    def __init__(self):
        #Tạo cửa sổ chính
        self.main_win = QMainWindow()
        #Tạo đối tượng UI
        self.uic = Ui_MainWindow()
        #Gán giao diện vào cửa sổ chính
        self.uic.setupUi(self.main_win)
        self.linkbuttons()
    def linkbuttons(self):
        #liên kết các nút bấm "Nhập" và "Tính GPA"
        self.uic.Nhap.clicked.connect(self.add_subject)

        """self.uic.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.uic.table.customContextMenuRequested.connect(self.show_context_menu)"""
        self.current_row = 0
    
    def show(self):
        self.main_win.show()

    def add_subject(self):
        try:
            ten_mon = str(self.uic.Mon_hoc.toPlainText())
            tin_chi = int(self.uic.So_tin.toPlainText())
            trong_so_qua_trinh = float(self.uic.TSQua_trinh.toPlainText())
            trong_so_giua_ki = float(self.uic.TSGiua_ki.toPlainText())
            trong_so_cuoi_ki = float(self.uic.TSCuoi_ki.toPlainText())
            diem_qua_trinh = float(self.uic.DQua_trinh.toPlainText())
            diem_giua_ki = float(self.uic.DGiua_ki.toPlainText())
            diem_cuoi_ki = float(self.uic.DCuoi_ki.toPlainText())
            
            # Kiểm tra trọng số tổng = 100%
            tong_trong_so = trong_so_qua_trinh + trong_so_giua_ki + trong_so_cuoi_ki
            if abs(tong_trong_so - 1.0) > 1e-6:
                raise ValueError("Tổng trọng số phải bằng 1.0")
             # Kiểm tra điểm hợp lệ
            if not (0 <= diem_qua_trinh <= 10 and 0 <= diem_giua_ki <= 10 and 0 <= diem_cuoi_ki <= 10):
                raise ValueError("Điểm phải nằm trong khoảng 0-10")
            if tin_chi <= 0:
                raise ValueError("Số tín chỉ phải là số dương")
            if ten_mon.strip() == "":
                raise ValueError("Tên môn học không được để trống")      
        except ValueError as e:
            QMessageBox.warning(self.main_win, "Lỗi nhập liệu", str(e))
        # Nếu không có lỗi, tính điểm tổng và thêm vào bảng
        trong_so = (trong_so_qua_trinh, trong_so_giua_ki, trong_so_cuoi_ki)
        diem = (diem_qua_trinh, diem_giua_ki, diem_cuoi_ki)
        diem_hoc_phan = tinh_diem_hoc_phan(trong_so, diem)
        diem_chu = xac_dinh_diem_chu(diem_hoc_phan)

        self.uic.table.insertRow(self.current_row)  #Thêm một hàng mới vào bảng
        self.uic.table.setItem(self.current_row, 0, QtWidgets.QTableWidgetItem(ten_mon))
        self.uic.table.setItem(self.current_row, 1, QtWidgets.QTableWidgetItem(str(tin_chi)))
        self.uic.table.setItem(self.current_row, 2, QtWidgets.QTableWidgetItem(f"{trong_so_qua_trinh:.2f}"))
        self.uic.table.setItem(self.current_row, 3, QtWidgets.QTableWidgetItem(f"{trong_so_giua_ki:.2f}"))
        self.uic.table.setItem(self.current_row, 4, QtWidgets.QTableWidgetItem(f"{trong_so_cuoi_ki:.2f}"))
        self.uic.table.setItem(self.current_row, 5, QtWidgets.QTableWidgetItem(f"{diem_qua_trinh:.2f}"))
        self.uic.table.setItem(self.current_row, 6, QtWidgets.QTableWidgetItem(f"{diem_giua_ki:.2f}"))
        self.uic.table.setItem(self.current_row, 7, QtWidgets.QTableWidgetItem(f"{diem_cuoi_ki:.2f}"))
        self.uic.table.setItem(self.current_row, 8, QtWidgets.QTableWidgetItem(f"{diem_hoc_phan:.2f}"))
        self.uic.table.setItem(self.current_row, 9, QtWidgets.QTableWidgetItem(f"{diem_chu}"))
        self.current_row += 1

        QMessageBox.information(self.main_win, "Thông báo", "Đã thêm môn học thành công!")
        
        #Tính GPA tích lũy sau khi thêm môn học
        total_credits = 0
        weighted_sum = 0

        row_count = self.uic.table.rowCount()

        for row in range(row_count):
            # Lấy giá trị từ cột tín chỉ và điểm học phần
            tin_chi_item = self.uic.table.item(row, 1)
            diem_hp_item = self.uic.table.item(row, 8)

            # Kiểm tra ô có dữ liệu không
            if tin_chi_item is not None and diem_hp_item is not None:
                try:
                    tin_chi = float(tin_chi_item.text())
                    diem_hp = float(diem_hp_item.text())

                    total_credits += tin_chi
                    weighted_sum += tin_chi * diem_hp
                except ValueError:
                    pass  # Bỏ qua nếu dữ liệu không hợp lệ (ví dụ text)

        # Tính GPA
        if total_credits > 0:
            gpa = weighted_sum / total_credits
        
        self.uic.GPA_tichluy.setText(f"{gpa:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()