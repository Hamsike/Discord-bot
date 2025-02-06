# Импорт нужных библиотек
import sys
import time
from random import choice, sample

import datetime as dt
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenuBar, QRadioButton, QComboBox, QTableWidget
from PyQt5.QtWidgets import QLineEdit, QLabel, QAction, QHBoxLayout, QStackedWidget, QVBoxLayout, QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem

# Подключение базы данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Testspeed(QWidget):
    def __init__(self):
        super().__init__()
        self.login = ''  # Логин пользователя
        # Таблица рекордов за всё время
        self.result_alltime = QTableWidget(3, 3, self)
        self.result_alltime.setEnabled(False)
        self.result_alltime.setHorizontalHeaderLabels(['Сложность', 'Точность', 'Скорость'])
        self.result_alltime.setStyleSheet('font-size:30px;'
                                          'color:yellow;')
        self.result_alltime.horizontalHeaderItem(2).setToolTip("Скорость измеряется в количестве символов в секунду")
        self.result_alltime.setItem(0, 0, QTableWidgetItem('Лёгкая'))
        self.result_alltime.setItem(1, 0, QTableWidgetItem('Средняя'))
        self.result_alltime.setItem(2, 0, QTableWidgetItem('Сложная'))
        header_h = self.result_alltime.horizontalHeader()
        header_h.setSectionResizeMode(0, QHeaderView.Stretch)
        header_h.setSectionResizeMode(1, QHeaderView.Stretch)
        header_h.setSectionResizeMode(2, QHeaderView.Stretch)
        header_h.setStyleSheet('QHeaderView::section {background-color: black}')
        header_v = self.result_alltime.verticalHeader()
        header_v.setSectionResizeMode(0, QHeaderView.Stretch)
        header_v.setSectionResizeMode(1, QHeaderView.Stretch)
        header_v.setSectionResizeMode(2, QHeaderView.Stretch)
        header_v.setStyleSheet('QHeaderView::section {background-color: black}')
        self.result_alltime.resizeColumnsToContents()
        # Таблица рекордов за неделю
        self.result_week = QTableWidget(3, 3, self)
        self.result_week.setEnabled(False)
        self.result_week.setHorizontalHeaderLabels(['Сложность', 'Точность', 'Скорость'])
        self.result_week.setStyleSheet('font-size:30px;'
                                       'color:yellow')
        self.result_week.horizontalHeaderItem(2).setToolTip("Скорость измеряется в количестве символов в секунду")
        self.result_week.setItem(0, 0, QTableWidgetItem('Лёгкая'))
        self.result_week.setItem(1, 0, QTableWidgetItem('Средняя'))
        self.result_week.setItem(2, 0, QTableWidgetItem('Сложная'))
        header_h = self.result_week.horizontalHeader()
        header_h.setSectionResizeMode(0, QHeaderView.Stretch)
        header_h.setSectionResizeMode(1, QHeaderView.Stretch)
        header_h.setSectionResizeMode(2, QHeaderView.Stretch)
        header_h.setStyleSheet('QHeaderView::section {background-color: black}')
        header_v = self.result_week.verticalHeader()
        header_v.setSectionResizeMode(0, QHeaderView.Stretch)
        header_v.setSectionResizeMode(1, QHeaderView.Stretch)
        header_v.setSectionResizeMode(2, QHeaderView.Stretch)
        header_v.setStyleSheet('QHeaderView::section {background-color: black}')
        self.result_week.resizeColumnsToContents()
        # Создание нужных виджетов для показа тестов
        self.prv = QLabel(self)
        self.timing = time.time()
        self.text = QLabel(self)
        self.text.setStyleSheet('font-size: 15px')
        self.text1 = QLabel(self)
        self.text1.setStyleSheet('font-size: 15px')
        self.text2 = QLabel(self)
        self.text2.setStyleSheet('font-size: 15px')
        self.text3 = QLabel(self)
        self.text3.setStyleSheet('font-size: 15px')
        self.text4 = QLabel(self)
        self.text4.setStyleSheet('font-size: 15px')
        self.text5 = QLabel(self)
        self.text5.setStyleSheet('font-size: 15px')
        self.text6 = QLabel(self)
        self.text6.setStyleSheet('font-size: 15px')
        self.line = QLineEdit(self)
        self.line.setStyleSheet('font-size: 15px')
        self.line1 = QLineEdit(self)
        self.line1.setStyleSheet('font-size: 15px')
        self.line2 = QLineEdit(self)
        self.line2.setStyleSheet('font-size: 15px')
        self.line3 = QLineEdit(self)
        self.line3.setStyleSheet('font-size: 15px')
        self.line4 = QLineEdit(self)
        self.line4.setStyleSheet('font-size: 15px')
        self.line5 = QLineEdit(self)
        self.line5.setStyleSheet('font-size: 15px')
        self.line6 = QLineEdit(self)
        self.line6.setStyleSheet('font-size: 15px')
        self.check1 = QRadioButton(self)
        self.cb = QComboBox(self)
        self.check = QRadioButton(self)
        # Изменение главного окна
        self.setGeometry(0, 0, 600, 600)
        self.setStyleSheet('background-color:black;'
                           'color: yellow;'
                           'font-style: italic')
        self.setWindowTitle('Тест скорости печати текста')
        self.setWindowIcon(QIcon('images/2.jpg'))
        # Создание стэка и стэковых виджетов
        self.Stack = QStackedWidget(self)
        self.stack1 = QWidget(self)
        self.stack1.setStyleSheet('background-color:black;')
        self.stack2 = QWidget(self)
        self.stack2.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(80, 80, 80))')
        self.stack3 = QWidget(self)
        self.stack3.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(50, 50, 50))')
        self.stack4 = QWidget(self)
        self.stack4.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(50, 50, 50))')
        self.stack5 = QWidget(self)
        self.stack5.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(50, 50, 50))')
        self.stack6 = QWidget(self)
        self.stack6.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(50, 50, 50))')
        self.stack7 = QWidget(self)
        self.stack7.setStyleSheet(
            'background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(0, 0, '
            '0), stop:1 rgb(50, 50, 50))')

        self.mainlt = QVBoxLayout(self)
        # Добавление стэковых виджетов в стэк
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)
        self.Stack.addWidget(self.stack5)
        self.Stack.addWidget(self.stack6)
        self.Stack.addWidget(self.stack7)
        self.mainlt.addWidget(self.Stack)
        # Вызов необходимых виджетов
        self.st7()
        self.Stack.setCurrentIndex(6)
        self.st1()
        # Создание Menubar
        self.menubar = QMenuBar(self)
        self.menubar.setStyleSheet('font-style:normal')
        # Создание Action теста и добавление в меню
        self.act1 = QAction(self)
        self.act1.setText('Тест')
        self.act1.triggered.connect(self.display)
        self.menubar.addAction(self.act1)
        # Создание Action рекордов и добавление в меню
        self.act2 = QAction(self)
        self.act2.setText('Итог')
        self.act2.triggered.connect(self.display1)
        self.menubar.addAction(self.act2)
        # QLabel для показа результата теста
        self.res = QLabel(self)
        self.res.setStyleSheet('font-size: 20px')
        # Виджет показываюзий ошибку при пустых строках
        self.error = QLabel(self)
        self.error.setStyleSheet('color: red;'
                                 'font-size: 18px')
        self.showMaximized()

        # Визуальная часть для виджета, который показывает рекорды
        self.ltresult = QVBoxLayout(self)

        label_all_time = QLabel(self)
        label_all_time.setText('Лучший результат за всё время')
        label_all_time.setStyleSheet('font-size: 20px;'
                                     'background-image: url(images/4.jpg);')
        label_all_time.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.ltresult.addWidget(label_all_time)
        self.ltresult.addWidget(self.result_alltime)

        label_week = QLabel(self)
        label_week.setText('Лучший результат за неделю')
        label_week.setStyleSheet('font-size: 20px;'
                                 'background-image: url(images/4.jpg);')
        label_week.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.ltresult.addWidget(label_week)
        self.ltresult.addWidget(self.result_week)

        self.ltresult.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.stack2.setLayout(self.ltresult)

    # Виджет входа в приложение
    def st7(self):
        lt = QVBoxLayout(self)
        lt1 = QHBoxLayout(self)

        label = QLabel(self)
        label.setText('Вход\n в приложение')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setStyleSheet('font-size: 30px;'
                            'background: url(images/4.jpg)')

        lb = QLabel(self)
        lb.setStyleSheet('font-size:18px;')
        lb.setText('Логин:')
        login = QLineEdit(self)
        login.setStyleSheet('font-size:18px')
        lt1.addWidget(lb)
        lt1.addWidget(login)

        self.prv.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        pb = QPushButton(self)
        pb.setText('Войти')
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 18px')
        pb.clicked.connect(lambda: self.login_input(login.text()))

        lt.addWidget(label)
        lt.addLayout(lt1)
        lt.addWidget(self.prv)
        lt.addWidget(pb)
        self.stack7.setLayout(lt)

    # Получение логина и добавление в баззу данных, если его там нет
    def login_input(self, login):
        self.login = login
        if self.login != '':
            names = cursor.execute('Select Name From AllTime').fetchall()
            s = []
            for el in names:
                s.append(el[0])
            if self.login not in s:
                data = str(dt.date.today())
                # Добавление нулевых рекордов в базу данных, добавляется если пользователя нет в базе данных
                cursor.execute('''INSERT INTO AllTime VALUES (?,?,?,?,?,?,?)''', (self.login, 0, 0, 0, 0,
                                                                                  0, 0))
                cursor.execute('''INSERT INTO Week VALUES (?,?,?,?,?,?,?,?)''', (self.login, data, 0, 0, 0, 0,
                                                                                 0, 0))
                conn.commit()
            else:
                # Добавление нулевых рекордов в базу данных, добавляется если пользователя нет в базе данных
                data_today = dt.date.today()
                value = cursor.execute('''SELECT Data FROM Week
                                          WHERE Name = ?
                                       ''', (self.login,)).fetchall()[0][0].split('-')
                data = dt.date(int(value[0]), int(value[1]), int(value[2]))
                timedelta = (data_today - data).days
                # Сброс рекордов за неделю, если прошла неделя или больше
                if timedelta >= 7:
                    cursor.execute('''UPDATE Week
                                      SET Data = ?,
                                          Easy_acc = 0,
                                          Easy_speed = 0,
                                          Med_acc = 0,
                                          Med_speed = 0,
                                          Hard_acc = 0,
                                          Hard_speed = 0
                                      WHERE Name = ?''', (str(data_today), self.login,))
                    conn.commit()
            self.Stack.setCurrentIndex(0)
        else:
            self.prv.setStyleSheet('font-size: 15px;'
                                   'color: red')
            self.prv.setText('Введите логин')

    # Виджет настройки теста
    def st1(self):
        lt = QVBoxLayout(self)
        lt1 = QHBoxLayout(self)
        lt2 = QHBoxLayout(self)

        text = QLabel()
        text.setText('Тест скорости набора текста')
        text.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        text.setStyleSheet('font-size: 30px;'
                           'background-image: url(images/4.jpg);'
                           'color: yellow;')
        text1 = QLabel()
        text1.setText('Язык')
        text1.setStyleSheet('font-size: 18px;')
        self.check.setText('Русский')
        self.check.setChecked(True)
        self.check.setStyleSheet('font-size: 18px;')

        self.check1.setText('Английский')
        self.check1.setStyleSheet('font-size: 18px;')
        lt1.addWidget(text1)
        lt1.addWidget(self.check)
        lt1.addWidget(self.check1)

        text2 = QLabel()
        text2.setText('Сложность')
        text2.setStyleSheet('font-size: 18px;')
        self.cb.setStyleSheet('color:black;'
                              'background-color:yellow;'
                              'font-size:18px')
        self.cb.addItem('Лёгкая')
        self.cb.addItem('Средняя')
        self.cb.addItem('Сложная')
        lt2.addWidget(text2)
        lt2.addWidget(self.cb)

        pb = QPushButton(self)
        pb.setText('Начать')
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 18px')
        pb.clicked.connect(self.start)

        lt.addWidget(text)
        lt.addLayout(lt1)
        lt.addLayout(lt2)
        lt.addWidget(pb)
        self.stack1.setLayout(lt)

    # Виджет, показывающий рекорды за всё время и за неделю
    def st2(self):
        # Получение рекордов за всё время
        result_all = cursor.execute('''SELECT Easy_acc, Easy_speed, Med_acc, Med_speed,
                                       Hard_acc, Hard_speed FROM AllTime
                                       WHERE Name = ?''', (self.login,)).fetchall()[0]
        rs = [[result_all[0], result_all[2], result_all[4]], [result_all[1], result_all[3], result_all[5]]]
        for i in range(1, 3):
            for j in range(3):
                self.result_alltime.setItem(j, i, QTableWidgetItem(str(rs[i - 1][j])))
        # Получение рекордов за неделю
        result_week = cursor.execute('''SELECT Easy_acc, Easy_speed, Med_acc, Med_speed,
                                               Hard_acc, Hard_speed FROM Week
                                               WHERE Name = ?''', (self.login,)).fetchall()[0]
        rs1 = [[result_week[0], result_week[2], result_week[4]], [result_week[1], result_week[3], result_week[5]]]
        for i in range(1, 3):
            for j in range(3):
                self.result_week.setItem(j, i, QTableWidgetItem(str(rs1[i - 1][j])))

    # Виджет лёгкого теста
    def st3(self):
        lt = QVBoxLayout(self)

        label = QLabel(self)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setText('Легкий тест')
        label.setStyleSheet('font-size: 20px;'
                            'background-image: url(images/4.jpg);')
        tx = []

        if self.check.isChecked():
            f = open('texts/1.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            tx = str(choice(lines)).strip()
        elif self.check1.isChecked():
            f = open('texts/2.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            tx = str(choice(lines)).strip()

        pb = QPushButton(self)
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 15px')
        pb.setText('Результат')
        self.text.setText(f'1. {tx}')
        lt.addWidget(label)
        self.line.setText('')
        lt.addWidget(self.text)
        lt.addWidget(self.line)
        lt.addWidget(self.error)
        lt.addWidget(pb)
        pb.clicked.connect(lambda: self.result(1))
        self.stack3.setLayout(lt)

    # Виджет среднего теста
    def st4(self):
        lt = QVBoxLayout(self)

        label = QLabel(self)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setText('Средний тест')
        label.setStyleSheet('font-size: 20px;'
                            'background-image: url(images/4.jpg);')
        tx = []

        if self.check.isChecked():
            f = open('texts/1.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            while len(set(tx)) != 2:
                tx = sample(lines, 2)
        elif self.check1.isChecked():
            f = open('texts/2.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            while len(set(tx)) != 2:
                tx = sample(lines, 2)

        pb = QPushButton(self)
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 15px')
        pb.setText('Результат')
        s = [str(i).strip() for i in tx]
        self.text1.setText(f'1. {s[0]}')
        self.text2.setText(f'2. {s[1]}')
        lt.addWidget(label)
        self.line1.setText('')
        self.line2.setText('')
        lt.addWidget(self.text1)
        lt.addWidget(self.line1)
        lt.addWidget(self.text2)
        lt.addWidget(self.line2)
        lt.addWidget(self.error)
        lt.addWidget(pb)
        pb.clicked.connect(lambda: self.result(2))
        self.stack4.setLayout(lt)

    # Виджет тяжёлого теста
    def st5(self):
        lt = QVBoxLayout(self)

        label = QLabel(self)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setText('Сложный тест')
        label.setStyleSheet('font-size: 20px;'
                            'background-image: url(images/4.jpg);')
        tx = []

        if self.check.isChecked():
            f = open('texts/1.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            while len(set(tx)) != 4:
                tx = sample(lines, 4)
        elif self.check1.isChecked():
            f = open('texts/2.txt', mode='r', encoding='utf8')
            lines = f.readlines()
            while len(set(tx)) != 4:
                tx = sample(lines, 4)

        pb = QPushButton(self)
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 15px')
        pb.setText('Результат')
        s = [str(i).strip() for i in tx]
        self.text3.setText(f'1. {s[0]}')
        self.text4.setText(f'2. {s[1]}')
        self.text5.setText(f'3. {s[2]}')
        self.text6.setText(f'4. {s[3]}')
        lt.addWidget(label)
        self.line3.setText('')
        self.line4.setText('')
        self.line5.setText('')
        self.line6.setText('')
        lt.addWidget(self.text3)
        lt.addWidget(self.line3)
        lt.addWidget(self.text4)
        lt.addWidget(self.line4)
        lt.addWidget(self.text5)
        lt.addWidget(self.line5)
        lt.addWidget(self.text6)
        lt.addWidget(self.line6)
        lt.addWidget(self.error)
        lt.addWidget(pb)
        pb.clicked.connect(lambda: self.result(4))
        self.stack5.setLayout(lt)

    # Виджет результата теста
    def st6(self, ac, sp, tm):
        lt = QVBoxLayout(self)

        label = QLabel(self)
        label.setStyleSheet('font-size:25px;'
                            'background-image: url(images/4.jpg)')
        label.setText('Ваш результат')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.res.setText(f'Время: {tm} с   Точность: {ac} %   Скорость: {sp} смв/c')
        self.res.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        pb = QPushButton(self)
        pb.setStyleSheet('background-color:yellow;'
                         'color:black;'
                         'font-size: 15px')
        pb.clicked.connect(self.display)
        pb.setText('OK')

        lt.addWidget(label)
        lt.addWidget(self.res)
        lt.addWidget(pb)
        self.stack6.setLayout(lt)

    # Показ виджета настройки теста
    def display(self):
        self.Stack.setCurrentIndex(0)

    # Показ виджета, который выводит рекорды за всё время и за неделю
    def display1(self):
        self.st2()
        self.Stack.setCurrentIndex(1)

    # Показ теста по сложности
    def start(self):
        self.timing = time.time()
        if self.cb.currentText() == 'Лёгкая':
            self.st3()
            self.Stack.setCurrentIndex(2)
        elif self.cb.currentText() == 'Средняя':
            self.st4()
            self.Stack.setCurrentIndex(3)
        elif self.cb.currentText() == 'Сложная':
            self.st5()
            self.Stack.setCurrentIndex(4)

    # Получение результата теста пользователя и обновление базы данных при необоходимости
    def result(self, n):
        time_res = time.time() - self.timing
        if n == 1 and self.line.text():
            # Получение рекордов лёгкой сложности
            result_old = cursor.execute('''SELECT Easy_acc, Easy_speed FROM AllTime
                                           WHERE Name = ?
                                        ''', (self.login,)).fetchall()[0]
            acc_old = result_old[0]
            speed_old = result_old[1]
            self.error.setText('')
            accuracy = self.accuracy(self.text.text()[3:], self.line.text())
            speed = round(len(self.line.text()) / time_res, 1)
            self.st6(accuracy, speed, round(time_res, 1))
            # Обновление если результаты лучше
            if accuracy * speed > acc_old * speed_old:
                cursor.execute('''UPDATE AllTime
                                  SET Easy_acc = ?,
                                      Easy_speed = ?
                                  WHERE Name = ?
                                ''', (accuracy, speed, self.login,))
                conn.commit()
                cursor.execute('''UPDATE Week
                                                SET Easy_acc = ?,
                                                    Easy_speed = ?
                                                WHERE Name = ?
                                                ''', (accuracy, speed, self.login,))
                conn.commit()
            self.Stack.setCurrentIndex(5)
        elif n == 2 and self.line1.text() and self.line2.text():
            # Получение ркордов средней сложности
            result_old = cursor.execute('''SELECT Med_acc, Med_speed FROM AllTime
                                                       WHERE Name = ?
                                                    ''', (self.login,)).fetchall()[0]
            acc_old = result_old[0]
            speed_old = result_old[1]
            self.error.setText('')
            accuracy = self.accuracy(self.text1.text()[3:], self.line1.text())
            speed = round(len(self.line1.text()) / time_res, 1)
            accuracy1 = self.accuracy(self.text2.text()[3:], self.line2.text())
            speed1 = round(len(self.line2.text()) / time_res, 1)
            accuracy_end = round((accuracy + accuracy1) / 2, 1)
            speed_end = round(speed + speed1, 1)
            self.st6(accuracy_end, speed_end, round(time_res, 1))
            # Обновление если результаты лучше
            if accuracy_end * speed_end > acc_old * speed_old:
                cursor.execute('''UPDATE AllTime
                                  SET Med_acc = ?,
                                      Med_speed = ?
                                  WHERE Name = ?
                                ''', (accuracy_end, speed_end, self.login,))
                conn.commit()
                cursor.execute('''UPDATE Week
                                                SET Med_acc = ?,
                                                    Med_speed = ?
                                                WHERE Name = ?
                                                ''', (accuracy_end, speed_end, self.login,))
                conn.commit()
            self.Stack.setCurrentIndex(5)
        elif n == 4 and self.line3.text() and self.line4.text() and self.line5.text() and self.line6.text():
            # Получение результатов сложной сложности
            result_old = cursor.execute('''SELECT Hard_acc, Hard_speed FROM AllTime
                                                                   WHERE Name = ?
                                                                ''', (self.login,)).fetchall()[0]
            acc_old = result_old[0]
            speed_old = result_old[1]
            self.error.setText('')
            accuracy = self.accuracy(self.text3.text()[3:], self.line3.text())
            speed = round(len(self.line3.text()) / time_res, 1)
            accuracy1 = self.accuracy(self.text4.text()[3:], self.line4.text())
            speed1 = round(len(self.line4.text()) / time_res, 1)
            accuracy2 = self.accuracy(self.text5.text()[3:], self.line5.text())
            speed2 = round(len(self.line5.text()) / time_res, 1)
            accuracy3 = self.accuracy(self.text6.text()[3:], self.line6.text())
            speed3 = round(len(self.line6.text()) / time_res, 1)
            accuracy_end = round((accuracy + accuracy1 + accuracy2 + accuracy3) / 4, 1)
            speed_end = round(speed + speed1 + speed2 + speed3, 1)
            self.st6(accuracy_end, speed_end, round(time_res, 1))
            # Обновление если результаты лучше
            if accuracy_end * speed_end > acc_old * speed_old:
                cursor.execute('''UPDATE AllTime
                                  SET Hard_acc = ?,
                                      Hard_speed = ?
                                  WHERE Name = ?
                                ''', (accuracy_end, speed_end, self.login,))
                conn.commit()
                cursor.execute('''UPDATE Week
                                                SET Hard_acc = ?,
                                                    Hard_speed = ?
                                                WHERE Name = ?
                                                ''', (accuracy_end, speed_end, self.login,))
                conn.commit()
            self.Stack.setCurrentIndex(5)
        else:
            if n == 1:
                self.error.setText('Заполните строку')
            else:
                self.error.setText('Заполните все строки')

    # Расчёт точности печати текста
    def accuracy(self, text, text_input):
        count = 0
        try:
            for i, el in enumerate(text):
                if text_input[i] == el:
                    count += 1
        except IndexError:
            pass
        return round((count / len(text)) * 100, 1)


# Показ приложения
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Windows')
    ex = Testspeed()
    ex.show()
    sys.exit(app.exec())
