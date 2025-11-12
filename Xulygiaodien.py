import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidgetItem
from PyQt6 import QtWidgets
from Giaodien_GPA import Ui_MainWindow
from Tinh_GPA import tinh_diem_hoc_phan, xac_dinh_diem_chu,diem_tinh

class MainWindow():
    def __init__(self):
        #Tạo cửa sổ chính
        self.main_win = QMainWindow()
        #Tạo đối tượng UI
        self.uic = Ui_MainWindow()
        #Gán giao diện vào cửa sổ chính
        self.uic.setupUi(self.main_win)
        #liên kết các nút bấm "Nhập" và "Tính GPA"
        self.uic.Nhap.clicked.connect(self.xu_ly)
        self.uic.Tinh_diem.clicked.connect(self.xu_ly_2)
        self.hang= 0
    
    def hien_thi(self):
        self.main_win.show()

    def xu_ly_2(self):
        try:
            # Kiểm tra đã có dữ liệu GPA trước chưa
            if not hasattr(self, "diem_hien_tai") or not hasattr(self, "tin_chi_hien_tai"):
                QMessageBox.warning(self.main_win, "Lỗi", "Vui lòng nhập ít nhất 1 môn học trước khi tính điểm!")
                return

            # Kiểm tra dữ liệu đầu vào
            if not self.uic.so_diem_du_kien.toPlainText() or not self.uic.so_tin_ctdt.toPlainText():
                QMessageBox.warning(self.main_win, "Lỗi nhập liệu",
                                    "Vui lòng nhập đủ 'Số tín chỉ CTĐT' và 'Số điểm bạn muốn'!")
                return

            Diem_aim = float(self.uic.so_diem_du_kien.toPlainText())
            tin_chi_tong = float(self.uic.so_tin_ctdt.toPlainText())
            tin_chi_con_lai = tin_chi_tong - self.tin_chi_hien_tai

            diem_can_dat = diem_tinh(self.diem_hien_tai,self.tin_chi_hien_tai,Diem_aim,tin_chi_tong,tin_chi_con_lai)

            QMessageBox.information(self.main_win, "Kết quả", f"Điểm cần đạt ở các học phần còn lại là: {diem_can_dat:.2f}")

        except Exception as e:
            QMessageBox.warning(self.main_win, "Lỗi", f"Không thể tính toán.\nChi tiết: {e}")

    def xu_ly(self):
        try:
            ten_mon = str(self.uic.Mon_hoc.toPlainText())
            tin_chi = int(self.uic.So_tin.toPlainText())
            trong_so_qua_trinh = float(self.uic.TSQua_trinh.toPlainText())
            trong_so_giua_ki = float(self.uic.TSGiua_ki.toPlainText())
            trong_so_cuoi_ki = float(self.uic.TSCuoi_ki.toPlainText())
            diem_qua_trinh = float(self.uic.DQua_trinh.toPlainText())
            diem_giua_ki = float(self.uic.DGiua_ki.toPlainText())
            diem_cuoi_ki = float(self.uic.DCuoi_ki.toPlainText())


            tong_trong_so = trong_so_qua_trinh + trong_so_giua_ki + trong_so_cuoi_ki
            if abs(tong_trong_so - 1.0) > 0.0001:
                raise ValueError("Tổng trọng số phải bằng 1.0")

            if not (0 <= diem_qua_trinh <= 10 and 0 <= diem_giua_ki <= 10 and 0 <= diem_cuoi_ki <= 10):
                raise ValueError("Điểm phải nằm trong khoảng 0-10")
            if tin_chi <= 0:
                raise ValueError("Số tín chỉ phải là số dương")
            if ten_mon.strip() == "":
                raise ValueError("Tên môn học không được để trống")      
        except ValueError as e:
            QMessageBox.warning(self.main_win, "Lỗi nhập liệu", str(e))

        diem_hoc_phan = tinh_diem_hoc_phan(trong_so_qua_trinh, trong_so_giua_ki, trong_so_cuoi_ki,
                       diem_qua_trinh, diem_giua_ki, diem_cuoi_ki)
        diem_chu = xac_dinh_diem_chu(diem_hoc_phan)

        self.uic.table.insertRow(self.hang)  #Thêm một hàng mới vào bảng
        self.uic.table.setItem(self.hang, 0, QtWidgets.QTableWidgetItem(ten_mon))
        self.uic.table.setItem(self.hang, 1, QtWidgets.QTableWidgetItem(str(tin_chi)))
        self.uic.table.setItem(self.hang, 2, QtWidgets.QTableWidgetItem(f"{trong_so_qua_trinh:.2f}"))
        self.uic.table.setItem(self.hang, 3, QtWidgets.QTableWidgetItem(f"{trong_so_giua_ki:.2f}"))
        self.uic.table.setItem(self.hang, 4, QtWidgets.QTableWidgetItem(f"{trong_so_cuoi_ki:.2f}"))
        self.uic.table.setItem(self.hang, 5, QtWidgets.QTableWidgetItem(f"{diem_qua_trinh:.2f}"))
        self.uic.table.setItem(self.hang, 6, QtWidgets.QTableWidgetItem(f"{diem_giua_ki:.2f}"))
        self.uic.table.setItem(self.hang, 7, QtWidgets.QTableWidgetItem(f"{diem_cuoi_ki:.2f}"))
        self.uic.table.setItem(self.hang, 8, QtWidgets.QTableWidgetItem(f"{diem_hoc_phan:.2f}"))
        self.uic.table.setItem(self.hang, 9, QtWidgets.QTableWidgetItem(f"{diem_chu}"))
        self.hang += 1

        QMessageBox.information(self.main_win, "Thông báo", "Đã thêm môn học thành công!")
        
        #Tính GPA tích lũy sau khi thêm môn học
        tin_hien_tai = 0
        diem_tb = 0

        dem_hang = self.uic.table.rowCount()

        for so_hang in range(dem_hang):
            # Lấy giá trị từ cột tín chỉ và điểm học phần
            tin_chi_item = self.uic.table.item(so_hang, 1)
            diem_hp_item = self.uic.table.item(so_hang, 8)

            # Kiểm tra ô có dữ liệu không
            if tin_chi_item is not None and diem_hp_item is not None:
                try:
                    tin_chi = float(tin_chi_item.text())
                    diem_hp = float(diem_hp_item.text())

                    tin_hien_tai += tin_chi
                    diem_tb += tin_chi * diem_hp
                except ValueError:
                    pass

        # Tính GPA
        if tin_hien_tai > 0:
            gpa = diem_tb / tin_hien_tai
        self.diem_hien_tai=gpa
        self.tin_chi_hien_tai=tin_hien_tai
        
        self.uic.GPA_tichluy.setText(f"{gpa:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.hien_thi()
    app.exec()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.hien_thi()
    app.exec()
