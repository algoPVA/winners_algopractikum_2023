from PyQt6 import uic

def calc_init():
    Form_calc, Window_calc = uic.loadUiType("calculate.ui")

    window_calc = Window_calc()
    form_calc = Form_calc()
    form_calc.setupUi(window_calc)
    
    def get_text():
        line_edit = form_calc.lineEdit501
        return line_edit
    
    def main_calc():
        text = get_text()
        try:
            result = eval(text.text())
            form_calc.lineEdit_502.setText(text.text() + ' = ' + str(result))
        except:
            form_calc.lineEdit_502.setText('Ошибка в данных!')
        finally:
            text.setText('')
    
    def add(char):
        text = get_text()
        text.setText(text.text()+char)




    # Подключаем функции к кнопкам
    form_calc.pushButton_505.clicked.connect(main_calc)
    form_calc.pushButton_512.clicked.connect(lambda: add('1'))
    form_calc.pushButton_514.clicked.connect(lambda: add('2'))
    form_calc.pushButton_504.clicked.connect(lambda: add('3'))
    form_calc.pushButton_503.clicked.connect(lambda: add('4'))
    form_calc.pushButton_506.clicked.connect(lambda: add('5'))
    form_calc.pushButton_507.clicked.connect(lambda: add('6'))
    form_calc.pushButton501.clicked.connect(lambda: add('7'))
    form_calc.pushButton_508.clicked.connect(lambda: add('8'))
    form_calc.pushButton_515.clicked.connect(lambda: add('9'))
    form_calc.pushButton_513.clicked.connect(lambda: add('0'))
    form_calc.pushButton_510.clicked.connect(lambda: add('+'))
    form_calc.pushButton_502.clicked.connect(lambda: add('-'))
    form_calc.pushButton_509.clicked.connect(lambda: add('*'))
    form_calc.pushButton_511.clicked.connect(lambda: add('/'))

    return window_calc


