# -*- coding: utf-8 -*-
# Created by WIN10 on 2020/9/23
# Copyright (c) 2020 WIN10. All rights reserved.
from robot import *
import socket
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from configparser import ConfigParser


class Robot_Logic(QDialog, Ui_Dialog_Robot):
    # 自定义消息
    dialogSignel = pyqtSignal(str)
    dialogSigne2 = pyqtSignal(str)
    dialogSigne3 = pyqtSignal(str)

    def __init__(self):
        super(Robot_Logic, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.tcp_socket = None
        self.sever_th = None
        self.client_socket_list = list()
        self.link = False  # 用于标记是否开启了连接
        self.connect()
        self.read1()

    # 绑定事件
    def connect(self):
        self.pushButton_robot_close.clicked.connect(self.closeEvent)  # 按钮事件绑定
        self.pushButton_robot_start.clicked.connect(self.tcp_server_start)

    def read1(self):  # 读取
        cp = ConfigParser()
        cp.read("config.ini")
        IP = cp.get("Server", 'IP')
        POST = cp.get("Server", 'POST')
        self.lineEdit_robot_ip.setText(str(IP))
        self.lineEdit_robot_post.setText(str(POST))

    def write(self):  # 写入
        #  实例化configParser对象
        cp = ConfigParser()
        # -read读取ini文件
        cp.read("config.ini")
        cp.remove_option('Server', 'IP')  # 删除type分组的stuno
        cp.remove_option('Server', 'POST')  # 删除type分组的stuno
        cp.set('Server', 'IP', self.lineEdit_robot_ip.text())  # 给type分组设置值
        cp.set('Server', 'POST', self.lineEdit_robot_post.text())  # 给type分组设置值
        o = open('config.ini', 'w')
        cp.write(o)
        o.close()  # 不要忘记关闭

    def closeEvent(self, event):
        self.write()
        self.close()

    def tcp_server_start(self, status):
        """
        功能函数，TCP服务端开启的方法
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        if status == True:
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 取消主动断开连接四次握手后的TIME_WAIT状态
            self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 设定套接字为非阻塞式
            self.tcp_socket.setblocking(False)
            try:
                address = (str(self.lineEdit_robot_ip.text()), int(self.lineEdit_robot_post.text()))
                self.tcp_socket.bind(address)
            except Exception as ret:
                msg = '请检查IP，端口\n'
                self.dialogSignel.emit(msg)
            else:
                self.tcp_socket.listen()
                self.sever_th = threading.Thread(target=self.tcp_server_concurrency)
                self.sever_th.start()
                msg = 'TCP服务端正在监听端口:%s\n' % str(self.lineEdit_robot_post.text())
                self.dialogSignel.emit(msg)
                self.dialogSigne3.emit('0')
                self.pushButton_robot_start.setText(_translate("Dialog", "断开"))
        else:
            try:
                self.tcp_socket.close()
                msg = '已断开网络\n'
                self.dialogSignel.emit(msg)
                self.dialogSigne3.emit('1')
                self.pushButton_robot_start.setText(_translate("Dialog", "连接"))
            except Exception as ret:
                pass

    def tcp_server_concurrency(self):
        """
        功能函数，供创建线程的方法；
        使用子线程用于监听并创建连接，使主线程可以继续运行，以免无响应
        使用非阻塞式并发用于接收客户端消息，减少系统资源浪费，使软件轻量化
        :return:None
        """
        while True:
            try:
                client_socket, client_address = self.tcp_socket.accept()
            except Exception as ret:
                pass
            else:
                client_socket.setblocking(False)
                # 将创建的客户端套接字存入列表,client_address为ip和端口的元组
                self.client_socket_list.append((client_socket, client_address))
                msg = 'TCP服务端已连接IP:%s端口:%s\n' % client_address
                self.dialogSignel.emit(msg)
            # 轮询客户端套接字列表，接收数据
            for client, address in self.client_socket_list:
                try:
                    recv_msg = client.recv(1024)
                except Exception as ret:
                    pass
                else:
                    if recv_msg:
                        msg2 = recv_msg.decode('utf-8')
                        msg = '来自IP:{}端口:{}:{}\n'.format(address[0], address[1], msg2)
                        self.dialogSignel.emit(msg)
                        self.dialogSigne2.emit(msg2)
                    else:
                        client.close()
                        self.client_socket_list.remove((client, address))

    def tcp_send(self,msg):
        try:
            for client, address in self.client_socket_list:
                client.send(msg.encode('utf-8'))
            msg = 'TCP服务端已发送\n'
            self.dialogSignel.emit(msg)
        except Exception as ret:
            msg = '发送失败\n'
            self.dialogSignel.emit(msg)

    def btnClick(self):  # 子窗体自定义事件
        self.close()
