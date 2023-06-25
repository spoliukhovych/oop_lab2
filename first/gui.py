import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from insertion_sort import SortingAlgorithmFactory, SortingClient
from min_element import MinElementDirector, MinElementBuilder
from max_element import MaxElementFinder, MaxElementObserver
import re


def is_all_digits(string):
    return re.fullmatch(r"^[\d,]+$", string) is not None

class ClssDialog1(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog1, self).__init__(parent)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

    def btnClosed(self):
        self.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 301)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 65, 600, 196))
        self.plainTextEdit.setObjectName("plainTextEdit")
        # self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        # self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 20, 600, 25))
        # self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(235, 0, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 45, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 260, 601, 42))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc_button)
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(300, 260, 300, 42))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2 = QtWidgets.QPushButton("Обрати", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 20, 600, 25))
        self.pushButton_2.clicked.connect(self.choose_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Оберіть алгоритм"))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow", "Введіть набір даних(через кому без пробілів)"))
        self.label_2.adjustSize()
        self.pushButton.setText(_translate("MainWindow", "Розрахувати"))
        # self.pushButton_2.setText(_translate("MainWindow", "Мої нотатки"))

    def choose_btn(self):
        self.choose_dialog = ClssDialog1()
        self.choose_dialog.setWindowTitle("Оберіть алгоритм")
        self.choose_dialog.resize(200, 200)

        self.choose_dialog.pushButton1 = QtWidgets.QPushButton(self.choose_dialog)
        self.choose_dialog.pushButton1.setText("Сортування вставкою")
        self.choose_dialog.pushButton1.setGeometry(0, 30, 200, 30)
        self.choose_dialog.pushButton1.clicked.connect(self.handle_button1_clicked)

        self.choose_dialog.pushButton2 = QtWidgets.QPushButton(self.choose_dialog)
        self.choose_dialog.pushButton2.setText("Пошук мінімального елементу")
        self.choose_dialog.pushButton2.setGeometry(0, 80, 200, 30)
        self.choose_dialog.pushButton2.clicked.connect(self.handle_button2_clicked)

        self.choose_dialog.pushButton3 = QtWidgets.QPushButton(self.choose_dialog)
        self.choose_dialog.pushButton3.setText("Пошук максимального елементу")
        self.choose_dialog.pushButton3.setGeometry(0, 130, 200, 30)
        self.choose_dialog.pushButton3.clicked.connect(self.handle_button3_clicked)

        self.choose_dialog.exec()

    def handle_button1_clicked(self):
        self.choose_dialog.close()
        self.pushButton_2.setText("Сортування вставкою")
        self.plainTextEdit.setPlainText("")

    def handle_button2_clicked(self):
        self.choose_dialog.close()
        self.pushButton_2.setText("Пошук мінімального елементу")
        self.plainTextEdit.setPlainText("")

    def handle_button3_clicked(self):
        self.choose_dialog.close()
        self.pushButton_2.setText("Пошук максимального елементу")
        self.plainTextEdit.setPlainText("")


    def calc_button(self):
        calc_dialog = ClssDialog1()
        # print(self.plainTextEdit.toPlainText())
        data = self.plainTextEdit.toPlainText()
        if is_all_digits(data):
            data = data.split(",")
            data = [int(x) for x in data]
            if self.pushButton_2.text() == "Сортування вставкою":
                algorithm_factory = SortingAlgorithmFactory()
                algorithm = algorithm_factory.create_algorithm('insertion')
                client = SortingClient(algorithm)
                client.sort_data(data)
                data = ','.join(map(str, data))
                self.plainTextEdit.setPlainText(data)
            elif self.pushButton_2.text() == "Пошук мінімального елементу":
                builder = MinElementBuilder()
                director = MinElementDirector(builder)
                data = director.construct(data)
                data = str(data)
                self.plainTextEdit.setPlainText(f"Мінімальний елемент: {data}")
            elif self.pushButton_2.text() == "Пошук максимального елементу":
                finder = MaxElementFinder()
                observer1 = MaxElementObserver()
                observer2 = MaxElementObserver()
                finder.attach(observer1)
                finder.attach(observer2)
                data = finder.find_max_element(data)
                data = str(data)
                self.plainTextEdit.setPlainText(f"Максимальний елемент: {data}")
            else:
                self.plainTextEdit.setPlainText("Оберіть алгоритм!")
        else:
            self.plainTextEdit.setPlainText("Введіть правильно числа!")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)