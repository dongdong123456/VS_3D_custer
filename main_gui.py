# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QColor
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_msg = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit_msg.sizePolicy().hasHeightForWidth())
        self.textEdit_msg.setSizePolicy(sizePolicy)
        self.textEdit_msg.setObjectName("textEdit_msg")
        self.gridLayout.addWidget(self.textEdit_msg, 1, 1, 1, 1)
        self.graphicsView_camera = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.graphicsView_camera.sizePolicy().hasHeightForWidth())
        self.graphicsView_camera.setSizePolicy(sizePolicy)
        self.graphicsView_camera.setObjectName("graphicsView_camera")
        self.gridLayout.addWidget(self.graphicsView_camera, 0, 0, 1, 1)
        self.graphicsView_robot = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.graphicsView_robot.sizePolicy().hasHeightForWidth())
        self.graphicsView_robot.setSizePolicy(sizePolicy)
        self.graphicsView_robot.setObjectName("graphicsView_robot")
        self.gridLayout.addWidget(self.graphicsView_robot, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_camera.sizePolicy().hasHeightForWidth())
        self.pushButton_camera.setSizePolicy(sizePolicy)
        self.pushButton_camera.setCheckable(True)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.verticalLayout.addWidget(self.pushButton_camera)
        self.pushButton_robot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_robot.sizePolicy().hasHeightForWidth())
        self.pushButton_robot.setSizePolicy(sizePolicy)
        self.pushButton_robot.setCheckable(True)
        self.pushButton_robot.setObjectName("pushButton_robot")
        self.verticalLayout.addWidget(self.pushButton_robot)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)

        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_model = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_model.sizePolicy().hasHeightForWidth())
        self.pushButton_model.setSizePolicy(sizePolicy)
        self.pushButton_model.setCheckable(True)
        self.pushButton_model.setObjectName("pushButton_model")
        self.verticalLayout.addWidget(self.pushButton_model)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textEdit_robot = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit_robot.sizePolicy().hasHeightForWidth())
        self.textEdit_robot.setSizePolicy(sizePolicy)
        self.textEdit_robot.setObjectName("textEdit_robot")
        self.horizontalLayout.addWidget(self.textEdit_robot)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(722, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        m_red_SheetStyle = "min-width: 16px; min-height: 16px;max-width:16px; max-height: 16px;border-radius: 8px;  border:1px solid black;background:red"
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SICK"))
        MainWindow.setWindowIcon(QIcon('SICK-logo.png'))
        palette1 = QtGui.QPalette()
        palette1.setColor(MainWindow.backgroundRole(), QColor(135,206,250))  # 背景颜色
        MainWindow.setPalette(palette1)
        MainWindow.setAutoFillBackground(True)
        self.pushButton_camera.setText(_translate("MainWindow", "连接相机"))
        self.pushButton_model.setText(_translate("MainWindow", "模型加载"))
        self.pushButton.setText(_translate("MainWindow", "坐标转换"))
        self.pushButton_robot.setText(_translate("MainWindow", "服务端"))
        self.label.setText(_translate("MainWindow", "相机"))
        self.label_2.setStyleSheet(m_red_SheetStyle)
        self.label_3.setText(_translate("MainWindow", "服务端"))
        self.label_4.setStyleSheet(m_red_SheetStyle)
        self.label_5.setText(_translate("MainWindow", "版本号：V1.0"))


    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.textEdit_msg.insertPlainText(msg)
        # 滚动条移动到结尾
        self.textEdit_msg.moveCursor(QtGui.QTextCursor.End)

    def send_robot(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.textEdit_robot.insertPlainText(msg)
        # 滚动条移动到结尾
        self.textEdit_robot.moveCursor(QtGui.QTextCursor.End)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        self.close_all()

    def close_all(self):
        pass

