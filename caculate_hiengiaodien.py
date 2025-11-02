"""import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from caculate_giaodien import Ui_MainWindow  
from Caculate_xuly import *
class MainWindow():                         #Tạo một cửa sổ
    def __init__(self):                     #Hàm khởi tạo
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)      #Tạo giao diện chính       
    
    def show(self):                         #Hàm hiện cửa sổ    
        self.main_win.show()                #Nếu dùng này thì không cần dùng window.show() 

    def lienketnutlenh(self):              #Hàm liên kết nút với lệnh
        self.uic.tinh.clicked.connect(self.xulynoibo)     #Khi nút tính được nhấn thì sẽ gọi hàm xử lý nội bộ
    
    def xulynoibo(self):
        a = float(self.uic.nhap_a.toPlainText())   #Lấy giá trị a từ ô nhập liệu và chuyển thành số thực
        b = float(self.uic.nhap_b.toPlainText())   #Lấy giá trị b từ ô nhập liệu và chuyển thành số thực
        try:    
            if self.uic.Tong.isChecked():               #Kiểm tra nếu nút cộng được chọn
                result = tong(a, b)                          #Thực hiện phép cộng
            elif self.uic.Hieu.isChecked():             #Kiểm tra nếu nút trừ được chọn
                result = hieu(a, b)                          #Thực hiện phép trừ
            elif self.uic.Tich.isChecked():             #Kiểm tra nếu nút nhân được chọn
                result = tich(a, b)                          #Thực hiện phép nhân
            elif self.uic.Thuong.isChecked():           #Kiểm tra nếu nút chia được chọn
                result = thuong(a, b)                        #Thực hiện phép chia
            else:
                result = "Please select an operation"   #Thông báo nếu không có phép toán nào được chọn 
            self.uic.ket_qua.setPlainText(str(result))  #Hiển thị kết quả trong ô kết quả
        except ValueError:
            self.uic.ket_qua.setPlainText("Error: Invalid input")  #Thông báo lỗi nếu nhập liệu không hợp lệ
if __name__ == "__main__":                  #Kiểm tra nếu file được chạy trực tiếp
    app = QApplication(sys.argv)            #Hiện giao diện chính
    window = MainWindow()                   #Tạo một cửa sổ chính
    window.lienketnutlenh()                 #Liên kết nút với lệnh
    window.show()                           #Hiện cửa sổ
    app.exec()                              #Dùng để thực thi

"""

