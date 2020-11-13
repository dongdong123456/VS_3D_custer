# -*- coding: utf-8 -*-
# Created by WIN10 on 2020/9/25
# Copyright (c) 2020 WIN10. All rights reserved.
from trans import *
from numpy import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from configparser import ConfigParser


class Trans_Logic(QDialog, Ui_Dialog_Trans):
    # 自定义消息

    dialogSignel = pyqtSignal(str)

    def __init__(self):
        super(Trans_Logic, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connect()

    # 绑定事件
    def connect(self):
        self.pushButton_2.clicked.connect(self.closeEvent)  # 按钮事件绑定关闭
        self.pushButton.clicked.connect(self.write)

    def write(self):  # 写入
        camera_x = self.lineEdit.text()
        camera_y = self.lineEdit_2.text()
        camera_z = self.lineEdit_3.text()
        robot_x = self.lineEdit_4.text()
        robot_y = self.lineEdit_5.text()
        robot_z = self.lineEdit_6.text()
        A1 = array([list(eval(camera_x)), list(eval(camera_y)), list(eval(camera_z))])
        # B1 = R*A1 + tile(t, (1, n))
        B1 = matrix([list(eval(robot_x)), list(eval(robot_y)), list(eval(robot_z))])
        ret_R, ret_t = self.rigid_transform_3D(A1, B1)
        ret_R.dump('ret_R.txt')
        ret_t.dump('ret_t.txt')
        msg = '标定保存完成\n'
        self.dialogSignel.emit(msg)

    def rigid_transform_3D(self,A, B):
        assert len(A) == len(B)

        num_rows, num_cols = A.shape

        if num_rows != 3:
            raise Exception("matrix A is not 3xN, it is {}x{}".format(num_rows, num_cols))

        [num_rows, num_cols] = B.shape
        if num_rows != 3:
            raise Exception("matrix B is not 3xN, it is {}x{}".format(num_rows, num_cols))

        # find mean column wise
        centroid_A = mean(A, axis=1)
        centroid_B = mean(B, axis=1)

        # ensure centroids are 3x1 (necessary when A or B are
        # numpy arrays instead of numpy matrices)
        centroid_A = centroid_A.reshape(-1, 1)
        centroid_B = centroid_B.reshape(-1, 1)

        # subtract mean
        Am = A - tile(centroid_A, (1, num_cols))
        Bm = B - tile(centroid_B, (1, num_cols))

        H = Am * transpose(Bm)

        # sanity check
        # if linalg.matrix_rank(H) < 3:
        #    raise ValueError("rank of H = {}, expecting 3".format(linalg.matrix_rank(H)))

        # find rotation
        U, S, Vt = linalg.svd(H)
        R = Vt.T * U.T

        # special reflection case
        if linalg.det(R) < 0:
            print("det(R) < R, reflection detected!, correcting for it ...\n")
            Vt[2, :] *= -1
            R = Vt.T * U.T

        t = -R * centroid_A + centroid_B

        return R, t
    def closeEvent(self, event):
        self.close()


