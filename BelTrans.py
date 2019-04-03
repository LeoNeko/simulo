from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
import sqlite3
from functions import *
import sqlalchemy as sa

import os

conn = sqlite3.connect('base.db3')
#conn.create_function("REGEXP", 2, rexexp)
c = conn.cursor()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.words = []

        #Табы
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.translate)
        self.tabs.currentChanged.connect(self.translate)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.translate)

        #self.tabs.addTab()

        #Навигация


        #self.button = QPushButton("Show Greetings")
        #self.revert_btn.setStatusTip("Сменить язык")




        ########################   Остальное
        self.setupUi(self)

        self.firstLang = QPushButton("RU", self)
        self.firstLang.setIconSize(QSize(25, 25))
        self.firstLang.setGeometry(QRect(9, 10, 31, 31))
        self.firstLang.clicked.connect(reverseLang)

        #Reverse button
        self.revButton = QPushButton(self)
        self.revButton.setIcon(QIcon(QPixmap("images/revert.png")))
        self.revButton.setIconSize(QSize(25, 25))
        self.revButton.setGeometry(QRect(50, 10, 31, 31))
        self.revButton.clicked.connect(reverseLang)

        self.secondLang = QPushButton("BY", self)
        self.secondLang.setIconSize(QSize(25, 25))
        self.secondLang.setGeometry(QRect(91, 10, 31, 31))
        #self.secondLang.setStyleSheet()
        self.secondLang.clicked.connect(reverseLang)
        #completer = QtWidgets.QCompleter(words, self)
        #completer.setCaseSensitivity(QtWidgets.Qt.CaseInsensitive)
        #self.lineInputText.setCompleter(completer)


        self.lineInputText.setPlaceholderText("Введите слово...")
        self.lineInputText.returnPressed.connect(self.translate)
        self.lineInputText.textChanged[str].connect(self.onChanged)


        #Сетка

        layout = QVBoxLayout()
        layout.addWidget(self.firstLang)
        layout.addWidget(self.revButton)
        layout.addWidget(self.secondLang)
        layout.addWidget(self.lineInputText)
        self.setLayout(layout)


    def translate(self):
        table = 'RU_BY'
        word = self.lineInputText.text()
        print(word)
        c.execute("SELECT translation FROM ('%s') WHERE word LIKE ('%s')" % (table, word))
        row = c.fetchone()

        try:
            print(row[0])
            self.plainTextEdit.setPlainText(row[0])

        except Exception:
            print('Перевод отсуствует')
            self.plainTextEdit.appendHtml('<font color=red size=40>Перевод отсутсвует</font>')


    def onChanged(self):
        table = 'RU_BY'

        word = self.lineInputText.text()
        c.execute("SELECT * FROM ('%s') WHERE word LIKE ('%s') LIMIT 6" % (table, word + '%'))
        wordList = c.fetchall()

        self.words = objToList(wordList)
        completer = QCompleter(self.words, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineInputText.setCompleter(completer)
        print(self.words)




if __name__ == '__main__':

    app = QApplication([])
    pixmap = QPixmap("images/original.jpg")
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()

    window = MainWindow()
    window.show()
    splash.finish(window)
    app.exec_()