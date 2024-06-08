from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from calc_app import calc_init
from ploshad_app import ploshad_init
from perimetr_app import perimetr_init
from main1 import main1_init
from main import Perevod_init

Form, Window = uic.loadUiType("main_window.kiparh.ui")



app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# создаем окна ребят
window_calc = calc_init()
window_ploshad = ploshad_init()
window_perimetr = perimetr_init()
window_main1 = main1_init()
window_main = Perevod_init()

def show_window(win):
    win.show()


# поключаем функции на кнопки

form.pushButton100.clicked.connect(lambda:show_window(window_calc))
form.pushButton100_3.clicked.connect(lambda:show_window(window_ploshad))
form.pushButton100_2.clicked.connect(lambda:show_window(window_perimetr))
form.pushButton100_5.clicked.connect(lambda:show_window(window_main1))
form.pushButton100_4.clicked.connect(lambda:show_window(window_mainы))


window.show()
app.exec()