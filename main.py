from PyQt6 import uic

def Perevod_init():


    Form_main, Window_main = uic.loadUiType("Perevod.ui") # в скобках написать название интерфейса


    window_main = Window_main()
    form_main = Form_main()
    form_main.setupUi(window_main)


    def calc_main():
        try:
            V_main = form_main.lineEdit534.text() # Получаем текст из LineEdit
            P_main = form_main.lineEdit_533.text() # Получаем текст из LineEdit
            result_main=float(V_main)*float(P_main)
            form_main.lineEdit_536.setText(str(result_main)) # устанавливаем текст в label
        except:
            form_main.lineEdit_536.setText('Ошибка в данных!')
             

        


    form_main.pushButton538.clicked.connect(calc_main) #привязка функции на кнопку

    return window_main