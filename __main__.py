from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
import os
import mainwindow


class MainCode(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)          # 初始化父类
        mainwindow.Ui_MainWindow.__init__(self)   # 初始化UI界面父类
        self.setupUi(self)                  # 调用界面
        self.btn_open.clicked.connect(self.on_open)     # 链接按钮
        self.btn_convert.clicked.connect(self.on_convert)   # 链接按钮

    def on_open(self):
            FilePath, _ = QFileDialog.getOpenFileName(self, 'Open', r'./')      # 调用文件选择框 并忽略类型赋值
            if FilePath == '':
                pass
            else:
                self.lab_path.setText(FilePath)  # 显示路径

    def on_convert(self):
        pat = self.lab_path.text()      # 获取label显示的内容
        if pat != 'Null':
            try:
                img = Image.open(pat)  # 打开文件
                # new = Image.new('RGB', img.size, (255, 255, 255))
                # new.paste(img, img)
                # new.save('fff' + '.jpg')  # 将图片转码为jpg
            except OSError:
                QMessageBox.critical(self, 'Error', 'This is not a image file !')

            else:
                name, types = os.path.splitext(pat)

                if types != '.bmp':
                    img.save(name + '.bmp')  # 将图片转码为位图
                deal = Image.open(name + '.bmp')
                # 判断取模方式后创建列表
                if self.xs.isChecked():
                    output_size = deal.size[0]
                else:
                    output_size = deal.size[1]
                output = [trans for trans in range(output_size)]  # 创建一个列表
                s_out = ''  # 初始化最终输出的字符串

                if self.xs.isChecked():                 # 判定取模方式
                    for x in range(deal.size[0]):
                        binary = 0      # 初始化输出变量
                        for y in range(deal.size[1]):                  # 上往下 左往右遍历
                            if deal.getpixel((x, y)) != (255, 255, 255):        # 如果像素点不为白色
                                binary = (binary << 1) + 1
                            else:
                                binary = (binary << 1)

                else:
                    for y in range(deal.size[1]):
                        binary = 0      # 初始化输出变量
                        for x in range(deal.size[0]):                  # 右往左 上往下遍历
                            if deal.getpixel((x, y)) != (255, 255, 255):        # 如果像素点不为白色
                                binary = (binary << 1) + 1
                            else:
                                binary = (binary << 1)
                        output[y] = binary  # 所有结果输入值这个列表
                    for i in range(output_size):  # 循环输出列表内容 并且格式化
                        data = str(hex(output[i]))
                        s_out = s_out + data + ', '
                self.tex_out.setText(s_out)
        else:
            QMessageBox.critical(self, 'Error', 'Path is not selected!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainCode()
    mw.show()
    sys.exit(app.exec_())
