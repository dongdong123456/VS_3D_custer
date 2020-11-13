# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dl_gui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from trans_logic import  *
from main_logic import *
from robot_logic import *
import sys
class MainWindow(Main_Logic):
    def __init__(self,Robot,Trans):
        super(MainWindow, self).__init__()

        self.Robot = Robot
        self.Trans=Trans
    def connect(self):

        super(MainWindow, self).connect()
        self.pushButton_robot.clicked.connect(Robot.show)
        self.pushButton.clicked.connect(Trans.show)
        # 机器人页
        Robot.dialogSignel.connect(self.slot_emit)
        Robot.dialogSigne2.connect(self.robot_trigle)
        Robot.dialogSigne3.connect(self.change_led)
        Trans.dialogSignel.connect(self.slot_emit)
        # Runthread._signal.connect(Robot.tcp_send)
        self.dialogSignel.connect(Robot.tcp_send)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Robot = Robot_Logic()
    Trans=Trans_Logic()
    ui = MainWindow(Robot,Trans)
    ui.show()
    sys.exit(app.exec_())




