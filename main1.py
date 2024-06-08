from PyQt6 import uic

def main1_init():

    Form_main1, Window_main1 = uic.loadUiType("obem.ui") # в скобках написать название интерфейса


    window_main1 = Window_main1()
    form_main1 = Form_main1()
    form_main1.setupUi(window_main1)


    def calc_main1():
        try:
            a = form_main1.lineEdit_900.text() # Получаем текст из LineEdit
            b = form_main1.lineEdit_902.text() # Получаем текст из LineEdit
            c = form_main1.lineEdit_903.text()

            result_main1=float(a)*float(b)*float(c)

            form_main1.lineEdit_904.setText(str(result_main1)) # устанавливаем текст в label
        except:
            form_main1.lineEdit_904.setText('Ошибка!')      
                    

    form_main1.pushButton_900.clicked.connect(calc_main1) #привязка функции на кнопку

    return window_main1
