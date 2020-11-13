# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Robot(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 223, 177))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_robot_ip = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_robot_ip.sizePolicy().hasHeightForWidth())
        self.lineEdit_robot_ip.setSizePolicy(sizePolicy)
        self.lineEdit_robot_ip.setMinimumSize(QtCore.QSize(150, 20))
        self.lineEdit_robot_ip.setMaximumSize(QtCore.QSize(150, 20))
        self.lineEdit_robot_ip.setObjectName("lineEdit_robot_ip")
        self.horizontalLayout.addWidget(self.lineEdit_robot_ip)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEdit_robot_post = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_robot_post.sizePolicy().hasHeightForWidth())
        self.lineEdit_robot_post.setSizePolicy(sizePolicy)
        self.lineEdit_robot_post.setMinimumSize(QtCore.QSize(150, 20))
        self.lineEdit_robot_post.setMaximumSize(QtCore.QSize(150, 20))
        self.lineEdit_robot_post.setObjectName("lineEdit_robot_post")
        self.horizontalLayout_2.addWidget(self.lineEdit_robot_post)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_robot_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_robot_start.setObjectName("pushButton_robot_start")
        self.pushButton_robot_start.setCheckable(True)
        self.horizontalLayout_3.addWidget(self.pushButton_robot_start)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_robot_close = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_robot_close.setObjectName("pushButton_robot_close")
        self.horizontalLayout_3.addWidget(self.pushButton_robot_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.lineEdit_robot_ip)
        self.label_2.setBuddy(self.lineEdit_robot_post)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "机器人"))
        self.label.setText(_translate("Dialog", "IP:"))
        self.label_2.setText(_translate("Dialog", "POST:"))

        self.pushButton_robot_start.setText(_translate("Dialog", "连接"))
        self.pushButton_robot_close.setText(_translate("Dialog", "返回"))
