from PyQt6 import uic

def ploshad_init():
    Form_ploshad, Window_ploshad = uic.loadUiType("ploshad.ui")

    window_ploshad = Window_ploshad()
    form_ploshad = Form_ploshad()
    form_ploshad.setupUi(window_ploshad)

    def rectangle():
        try:
            length = form_ploshad.lineEdit_100.text() 
            width = form_ploshad.lineEdit_102.text() 
            result = float(length)*float(width)
            form_ploshad.lineEdit_103.setText(str(result)) 
        except:
            form_ploshad.lineEdit_103.setText('Ошибка!') 


    form_ploshad.pushButton_110.clicked.connect(rectangle)

    def circle():
        try:
            radius = form_ploshad.lineEdit_104.text()
            print(1)
            c_result = float(radius)*float(radius)*3.14
            print(c_result)      
            form_ploshad.lineEdit_105.setText(str(c_result)) 
        except:
            form_ploshad.lineEdit_105.setText('Ошибка!') 


    form_ploshad.pushButton_111.clicked.connect(circle)
    
    def triangle():
        try:
            height = form_ploshad.lineEdit_106.text()
            base = form_ploshad.lineEdit_107.text()
            t_result = 0.5*float(height)*float(base)
            form_ploshad.lineEdit_108.setText(str(t_result))
        except:
            form_ploshad.lineEdit_108.setText('Ошибка!')

    form_ploshad.pushButton_112.clicked.connect(triangle)

    return window_ploshad