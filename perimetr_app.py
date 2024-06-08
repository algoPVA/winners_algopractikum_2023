from PyQt6 import uic

def perimetr_init():
    Form_perimetr, Window_perimetr = uic.loadUiType("perimetr.ui")

    window_perimetr = Window_perimetr()
    form_perimetr = Form_perimetr()
    form_perimetr.setupUi(window_perimetr)

    def rectangle_perim():
        try:
            length_perim = form_perimetr.lineEdit_110.text() 
            width_perim = form_perimetr.lineEdit_111.text() 
            result_perim = (float(length_perim)+float(width_perim))*2
            form_perimetr.lineEdit_112.setText(str(result_perim)) 
        except:
            form_perimetr.lineEdit_112.setText('Ошибка!') 

    form_perimetr.pushButton_113.clicked.connect(rectangle_perim)

    def circle_perim():
        try:
            radius_perim = form_perimetr.lineEdit_113.text()
            c_result_perim = float(radius_perim)*3.14*2
            form_perimetr.lineEdit_114.setText(str(c_result_perim))
        except:
            form_perimetr.lineEdit_114.setText('Ошибка!')

    form_perimetr.pushButton_114.clicked.connect(circle_perim)

    def triangle_perim():
        try:
            side1 = form_perimetr.lineEdit_115.text()
            side2 = form_perimetr.lineEdit_116.text()
            side3 = form_perimetr.lineEdit_117.text()
            t_result_perim = float(side1)+float(side2)+float(side2)
            form_perimetr.lineEdit_118.setText(str(t_result_perim))
        except:
            form_perimetr.lineEdit_118.setText('Ошибка!')

    form_perimetr.pushButton_115.clicked.connect(triangle_perim)

    return window_perimetr