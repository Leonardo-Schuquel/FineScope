# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 637)
        MainWindow.setStyleSheet(u"background: #121212")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMaximumSize(QSize(250, 16777215))
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QFrame(self.menu_frame)
        self.logo.setObjectName(u"logo")
        self.logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_name = QLabel(self.logo)
        self.logo_name.setObjectName(u"logo_name")

        self.horizontalLayout_2.addWidget(self.logo_name)


        self.verticalLayout.addWidget(self.logo)

        self.btns_menu = QFrame(self.menu_frame)
        self.btns_menu.setObjectName(u"btns_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btns_menu.sizePolicy().hasHeightForWidth())
        self.btns_menu.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btns_menu.setFont(font)
        self.btns_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.btns_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.btns_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_home = QPushButton(self.btns_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_release = QPushButton(self.btns_menu)
        self.btn_release.setObjectName(u"btn_release")
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.btn_release.setFont(font1)
        self.btn_release.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_release)

        self.btn_edit = QPushButton(self.btns_menu)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setFont(font1)
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_edit)

        self.btn_history = QPushButton(self.btns_menu)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setFont(font1)
        self.btn_history.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_history)

        self.btn_pdf = QPushButton(self.btns_menu)
        self.btn_pdf.setObjectName(u"btn_pdf")
        self.btn_pdf.setFont(font1)
        self.btn_pdf.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_pdf)

        self.btn_quit = QPushButton(self.btns_menu)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setFont(font1)
        self.btn_quit.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 13px 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2A2A2A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_quit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.btns_menu)


        self.horizontalLayout.addWidget(self.menu_frame)

        self.frame_conteiner = QFrame(self.centralwidget)
        self.frame_conteiner.setObjectName(u"frame_conteiner")
        self.frame_conteiner.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_conteiner.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_conteiner)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.conteiner = QFrame(self.frame_conteiner)
        self.conteiner.setObjectName(u"conteiner")
        self.conteiner.setFrameShape(QFrame.Shape.StyledPanel)
        self.conteiner.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.conteiner)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pages = QStackedWidget(self.conteiner)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_4 = QVBoxLayout(self.page_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.conteiner_balance = QFrame(self.page_home)
        self.conteiner_balance.setObjectName(u"conteiner_balance")
        self.conteiner_balance.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"    border-radius: 16px;\n"
"    padding: 5px, 5px, 5px, 5px;\n"
"}")
        self.conteiner_balance.setFrameShape(QFrame.Shape.StyledPanel)
        self.conteiner_balance.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.conteiner_balance)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_balance = QLabel(self.conteiner_balance)
        self.title_balance.setObjectName(u"title_balance")
        self.title_balance.setStyleSheet(u"QLabel#title_balance {\n"
"    color: #FFFFFF;\n"
"    font-size: 20px;\n"
"    font-weight: 500;\n"
"}")

        self.verticalLayout_5.addWidget(self.title_balance)

        self.value_balance = QLabel(self.conteiner_balance)
        self.value_balance.setObjectName(u"value_balance")
        self.value_balance.setStyleSheet(u"QLabel#value_balance {\n"
"    color: #FFFFFF;\n"
"    font-size: 30px;\n"
"    font-weight: 600;\n"
"}")

        self.verticalLayout_5.addWidget(self.value_balance)


        self.verticalLayout_4.addWidget(self.conteiner_balance)

        self.conteiner_debts = QFrame(self.page_home)
        self.conteiner_debts.setObjectName(u"conteiner_debts")
        self.conteiner_debts.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"    border-radius: 16px;\n"
"    padding: 5px;\n"
"}")
        self.conteiner_debts.setFrameShape(QFrame.Shape.StyledPanel)
        self.conteiner_debts.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.conteiner_debts)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.title_debts = QLabel(self.conteiner_debts)
        self.title_debts.setObjectName(u"title_debts")
        self.title_debts.setStyleSheet(u"QLabel {\n"
"	color: #FFFFFF;\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"}")

        self.verticalLayout_6.addWidget(self.title_debts)

        self.value_debts = QLabel(self.conteiner_debts)
        self.value_debts.setObjectName(u"value_debts")
        self.value_debts.setStyleSheet(u"QLabel#value_debts {\n"
"    color: #FFFFFF;\n"
"    font-size: 30px;\n"
"    font-weight: 600;\n"
"}")

        self.verticalLayout_6.addWidget(self.value_debts)


        self.verticalLayout_4.addWidget(self.conteiner_debts)

        self.total_balance = QFrame(self.page_home)
        self.total_balance.setObjectName(u"total_balance")
        self.total_balance.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"    border-radius: 16px;\n"
"    padding: 5px;\n"
"}")
        self.total_balance.setFrameShape(QFrame.Shape.StyledPanel)
        self.total_balance.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.total_balance)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.title_sum = QLabel(self.total_balance)
        self.title_sum.setObjectName(u"title_sum")
        self.title_sum.setStyleSheet(u"QLabel {\n"
"	color: #FFFFFF;\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"}")

        self.verticalLayout_17.addWidget(self.title_sum)

        self.sum_release = QLabel(self.total_balance)
        self.sum_release.setObjectName(u"sum_release")
        self.sum_release.setStyleSheet(u"QLabel{\n"
"    color: #FFFFFF;\n"
"    font-size: 30px;\n"
"    font-weight: 600;\n"
"}")

        self.verticalLayout_17.addWidget(self.sum_release)


        self.verticalLayout_4.addWidget(self.total_balance)

        self.pages.addWidget(self.page_home)
        self.page_release = QWidget()
        self.page_release.setObjectName(u"page_release")
        self.page_release.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.page_release)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.conteiner_release = QFrame(self.page_release)
        self.conteiner_release.setObjectName(u"conteiner_release")
        self.conteiner_release.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    color: #FFFFFF;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"	margin-bottom:12px\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #2A2A2A;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: #FFFFFF;\n"
"	selection-background-color: 2563EB;\n"
"}\n"
"\n"
"QLineEdit::placeholder, QTextEdit::placeholder {\n"
"    color: AAAAAA;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 1px solid #2563EB;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton#save {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"	border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#save:hover {\n"
"    background-color: #1E4FCC;\n"
"}\n"
"\n"
"QPushButton#cance"
                        "l {\n"
"    background-color: #3A3A3A;\n"
"    color: #FFFFFF;\n"
"	border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#cancel:hover {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"QPushButton#cancel, QPushButton#save {\n"
"	min-width: 100px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    background-color: #2D2D2D;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"	height: 0;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #2563EB;\n"
"    border: 1px solid #2563EB;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background: transparent;\n"
"    border: 2px solid #2563EB;\n"
"	border-radius: 8px\n"
"}")
        self.conteiner_release.setFrameShape(QFrame.Shape.StyledPanel)
        self.conteiner_release.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.conteiner_release)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Frame_value_release = QFrame(self.conteiner_release)
        self.Frame_value_release.setObjectName(u"Frame_value_release")
        self.Frame_value_release.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_value_release.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Frame_value_release)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.title_generic_3 = QLabel(self.Frame_value_release)
        self.title_generic_3.setObjectName(u"title_generic_3")

        self.verticalLayout_10.addWidget(self.title_generic_3)

        self.value_release = QLineEdit(self.Frame_value_release)
        self.value_release.setObjectName(u"value_release")

        self.verticalLayout_10.addWidget(self.value_release)


        self.gridLayout.addWidget(self.Frame_value_release, 3, 0, 1, 1)

        self.title_description = QFrame(self.conteiner_release)
        self.title_description.setObjectName(u"title_description")
        self.title_description.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_description.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.title_description)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.title_generic_4 = QLabel(self.title_description)
        self.title_generic_4.setObjectName(u"title_generic_4")

        self.verticalLayout_9.addWidget(self.title_generic_4)

        self.description_release = QLineEdit(self.title_description)
        self.description_release.setObjectName(u"description_release")

        self.verticalLayout_9.addWidget(self.description_release)


        self.gridLayout.addWidget(self.title_description, 4, 0, 1, 1)

        self.title_release = QFrame(self.conteiner_release)
        self.title_release.setObjectName(u"title_release")
        self.title_release.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_release.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.title_release)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.title_generic_2 = QLabel(self.title_release)
        self.title_generic_2.setObjectName(u"title_generic_2")

        self.verticalLayout_8.addWidget(self.title_generic_2)

        self.input_title = QLineEdit(self.title_release)
        self.input_title.setObjectName(u"input_title")

        self.verticalLayout_8.addWidget(self.input_title)


        self.gridLayout.addWidget(self.title_release, 2, 0, 1, 1)

        self.title = QLabel(self.conteiner_release)
        self.title.setObjectName(u"title")
        self.title.setFont(font1)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.type_release = QFrame(self.conteiner_release)
        self.type_release.setObjectName(u"type_release")
        self.type_release.setFrameShape(QFrame.Shape.StyledPanel)
        self.type_release.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.type_release)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.title_generic = QLabel(self.type_release)
        self.title_generic.setObjectName(u"title_generic")
        font2 = QFont()
        self.title_generic.setFont(font2)

        self.verticalLayout_7.addWidget(self.title_generic)

        self.options = QFrame(self.type_release)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.Shape.StyledPanel)
        self.options.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.options)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.entrance = QRadioButton(self.options)
        self.entrance.setObjectName(u"entrance")

        self.horizontalLayout_5.addWidget(self.entrance)

        self.departure = QRadioButton(self.options)
        self.departure.setObjectName(u"departure")

        self.horizontalLayout_5.addWidget(self.departure)


        self.verticalLayout_7.addWidget(self.options)


        self.gridLayout.addWidget(self.type_release, 1, 0, 1, 1)

        self.buttons_release = QFrame(self.conteiner_release)
        self.buttons_release.setObjectName(u"buttons_release")
        self.buttons_release.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_release.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.buttons_release)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cancel = QPushButton(self.buttons_release)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_6.addWidget(self.cancel)

        self.save = QPushButton(self.buttons_release)
        self.save.setObjectName(u"save")

        self.horizontalLayout_6.addWidget(self.save)


        self.gridLayout.addWidget(self.buttons_release, 5, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.conteiner_release)

        self.pages.addWidget(self.page_release)
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.verticalLayout_18 = QVBoxLayout(self.edit)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.conteiner_release_2 = QFrame(self.edit)
        self.conteiner_release_2.setObjectName(u"conteiner_release_2")
        self.conteiner_release_2.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    color: #FFFFFF;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"	margin-bottom:12px\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #2A2A2A;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: #FFFFFF;\n"
"	selection-background-color: 2563EB;\n"
"}\n"
"\n"
"QLineEdit::placeholder, QTextEdit::placeholder {\n"
"    color: AAAAAA;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 1px solid #2563EB;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton#edit_save {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"	border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#exclude {\n"
"    background-color: #FF0003;\n"
"    color: #FFFFFF;\n"
""
                        "	border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#exclude, QPushButton#edit_save {\n"
"	min-width: 100px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    background-color: #2D2D2D;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 0;\n"
"	height: 0;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #2563EB;\n"
"    border: 1px solid #2563EB;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background: transparent;\n"
"    border: 2px solid #2563EB;\n"
"	border-radius: 8px\n"
"}")
        self.conteiner_release_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.conteiner_release_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.conteiner_release_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.value_release_3 = QFrame(self.conteiner_release_2)
        self.value_release_3.setObjectName(u"value_release_3")
        self.value_release_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.value_release_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.value_release_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.title_generic_5 = QLabel(self.value_release_3)
        self.title_generic_5.setObjectName(u"title_generic_5")

        self.verticalLayout_11.addWidget(self.title_generic_5)

        self.value_release_2 = QLineEdit(self.value_release_3)
        self.value_release_2.setObjectName(u"value_release_2")

        self.verticalLayout_11.addWidget(self.value_release_2)


        self.gridLayout_2.addWidget(self.value_release_3, 3, 0, 1, 1)

        self.title_description_2 = QFrame(self.conteiner_release_2)
        self.title_description_2.setObjectName(u"title_description_2")
        self.title_description_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_description_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.title_description_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.title_generic_6 = QLabel(self.title_description_2)
        self.title_generic_6.setObjectName(u"title_generic_6")

        self.verticalLayout_12.addWidget(self.title_generic_6)

        self.description_release_2 = QLineEdit(self.title_description_2)
        self.description_release_2.setObjectName(u"description_release_2")

        self.verticalLayout_12.addWidget(self.description_release_2)


        self.gridLayout_2.addWidget(self.title_description_2, 4, 0, 1, 1)

        self.title_release_2 = QFrame(self.conteiner_release_2)
        self.title_release_2.setObjectName(u"title_release_2")
        self.title_release_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_release_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.title_release_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.title_generic_7 = QLabel(self.title_release_2)
        self.title_generic_7.setObjectName(u"title_generic_7")

        self.verticalLayout_13.addWidget(self.title_generic_7)

        self.input_title_2 = QLineEdit(self.title_release_2)
        self.input_title_2.setObjectName(u"input_title_2")

        self.verticalLayout_13.addWidget(self.input_title_2)


        self.gridLayout_2.addWidget(self.title_release_2, 2, 0, 1, 1)

        self.title_2 = QLabel(self.conteiner_release_2)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setFont(font1)

        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 1)

        self.type_release_2 = QFrame(self.conteiner_release_2)
        self.type_release_2.setObjectName(u"type_release_2")
        self.type_release_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.type_release_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.type_release_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.title_generic_8 = QLabel(self.type_release_2)
        self.title_generic_8.setObjectName(u"title_generic_8")
        self.title_generic_8.setFont(font2)

        self.verticalLayout_14.addWidget(self.title_generic_8)

        self.options_2 = QFrame(self.type_release_2)
        self.options_2.setObjectName(u"options_2")
        self.options_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.options_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.options_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.entrance_2 = QRadioButton(self.options_2)
        self.entrance_2.setObjectName(u"entrance_2")

        self.horizontalLayout_9.addWidget(self.entrance_2)

        self.departure_2 = QRadioButton(self.options_2)
        self.departure_2.setObjectName(u"departure_2")

        self.horizontalLayout_9.addWidget(self.departure_2)


        self.verticalLayout_14.addWidget(self.options_2)


        self.gridLayout_2.addWidget(self.type_release_2, 1, 0, 1, 1)

        self.buttons_release_2 = QFrame(self.conteiner_release_2)
        self.buttons_release_2.setObjectName(u"buttons_release_2")
        self.buttons_release_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_release_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.buttons_release_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.exclude = QPushButton(self.buttons_release_2)
        self.exclude.setObjectName(u"exclude")

        self.horizontalLayout_10.addWidget(self.exclude)

        self.edit_save = QPushButton(self.buttons_release_2)
        self.edit_save.setObjectName(u"edit_save")

        self.horizontalLayout_10.addWidget(self.edit_save)


        self.gridLayout_2.addWidget(self.buttons_release_2, 5, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.conteiner_release_2)

        self.pages.addWidget(self.edit)
        self.page_historical = QWidget()
        self.page_historical.setObjectName(u"page_historical")
        self.page_historical.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #2A2A2A;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 8px;\n"
"    color: #FFFFFF;\n"
"    gridline-color: #3A3A3A;\n"
"    selection-background-color: #2563EB;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2A2A2A;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#edit {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton#edit:hover {\n"
"    background-color: #1E4FCC;\n"
"}\n"
"\n"
"QPushButton#delete {\n"
"    background-color: #D32F2F;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButto"
                        "n#delete:hover {\n"
"    background-color: #B71C1C;\n"
"}\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.page_historical)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.historical_conteiner = QFrame(self.page_historical)
        self.historical_conteiner.setObjectName(u"historical_conteiner")
        self.historical_conteiner.setStyleSheet(u"")
        self.historical_conteiner.setFrameShape(QFrame.Shape.StyledPanel)
        self.historical_conteiner.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.historical_conteiner)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.options_historical = QFrame(self.historical_conteiner)
        self.options_historical.setObjectName(u"options_historical")
        self.options_historical.setFrameShape(QFrame.Shape.StyledPanel)
        self.options_historical.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.options_historical)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.entrance_historical = QPushButton(self.options_historical)
        self.entrance_historical.setObjectName(u"entrance_historical")

        self.horizontalLayout_12.addWidget(self.entrance_historical)

        self.departure_historical = QPushButton(self.options_historical)
        self.departure_historical.setObjectName(u"departure_historical")

        self.horizontalLayout_12.addWidget(self.departure_historical)

        self.last_month = QPushButton(self.options_historical)
        self.last_month.setObjectName(u"last_month")

        self.horizontalLayout_12.addWidget(self.last_month)


        self.verticalLayout_16.addWidget(self.options_historical)

        self.historical = QTableWidget(self.historical_conteiner)
        if (self.historical.columnCount() < 5):
            self.historical.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.historical.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.historical.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.historical.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.historical.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.historical.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.historical.setObjectName(u"historical")

        self.verticalLayout_16.addWidget(self.historical)


        self.verticalLayout_15.addWidget(self.historical_conteiner)

        self.pages.addWidget(self.page_historical)
        self.list_edit = QWidget()
        self.list_edit.setObjectName(u"list_edit")
        self.list_edit.setStyleSheet(u"QFrame {\n"
"    background-color: #1E1E1E;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #2A2A2A;\n"
"    border: 1px solid #3A3A3A;\n"
"    border-radius: 8px;\n"
"    color: #FFFFFF;\n"
"    gridline-color: #3A3A3A;\n"
"    selection-background-color: #2563EB;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2A2A2A;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#edit {\n"
"    background-color: #2563EB;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton#edit:hover {\n"
"    background-color: #1E4FCC;\n"
"}\n"
"\n"
"QPushButton#delete {\n"
"    background-color: #D32F2F;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButto"
                        "n#delete:hover {\n"
"    background-color: #B71C1C;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.list_edit)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_2 = QFrame(self.list_edit)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_edit_2 = QPushButton(self.frame)
        self.btn_edit_2.setObjectName(u"btn_edit_2")

        self.horizontalLayout_8.addWidget(self.btn_edit_2)

        self.btn_exclude = QPushButton(self.frame)
        self.btn_exclude.setObjectName(u"btn_exclude")

        self.horizontalLayout_8.addWidget(self.btn_exclude)


        self.verticalLayout_20.addWidget(self.frame)

        self.list_edit_2 = QTableWidget(self.frame_2)
        if (self.list_edit_2.columnCount() < 5):
            self.list_edit_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_edit_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list_edit_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list_edit_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_edit_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list_edit_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.list_edit_2.setObjectName(u"list_edit_2")

        self.verticalLayout_20.addWidget(self.list_edit_2)


        self.verticalLayout_19.addWidget(self.frame_2)

        self.pages.addWidget(self.list_edit)

        self.horizontalLayout_3.addWidget(self.pages)


        self.verticalLayout_3.addWidget(self.conteiner)


        self.horizontalLayout.addWidget(self.frame_conteiner)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">FineScope</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_release.setText(QCoreApplication.translate("MainWindow", u"Lan\u00e7amentos", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Editar Lan\u00e7amento", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.btn_pdf.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.title_balance.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Entradas</span></p></body></html>", None))
        self.value_balance.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.title_debts.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt; font-weight:700;\">Saidas</span></p></body></html>", None))
        self.value_debts.setText(QCoreApplication.translate("MainWindow", u"R$0,00", None))
        self.title_sum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt; font-weight:700;\">Saldo Total</span></p></body></html>", None))
        self.sum_release.setText(QCoreApplication.translate("MainWindow", u"R$0,00", None))
        self.title_generic_3.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.value_release.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.title_generic_4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.title_generic_2.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.input_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Conta de ...", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Novo Lan\u00e7amento", None))
        self.title_generic.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.entrance.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.departure.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.title_generic_5.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.value_release_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.title_generic_6.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.title_generic_7.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.input_title_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Conta de ...", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Editar Lan\u00e7amento", None))
        self.title_generic_8.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.entrance_2.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.departure_2.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.exclude.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.edit_save.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.entrance_historical.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.departure_historical.setText(QCoreApplication.translate("MainWindow", u"Saidas", None))
        self.last_month.setText(QCoreApplication.translate("MainWindow", u"Ultimo M\u00eas", None))
        ___qtablewidgetitem = self.historical.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.historical.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem2 = self.historical.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem3 = self.historical.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem4 = self.historical.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.btn_edit_2.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_exclude.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem5 = self.list_edit_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.list_edit_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem7 = self.list_edit_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem8 = self.list_edit_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem9 = self.list_edit_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
    # retranslateUi

