# coding: utf-8

'''
author: Gcker
解析burp数据包模块
'''

import re

class Parse():
    def __init__(self, fileName):
        self._fileName = fileName
    
    # 检测http方法
    def checkMethod(self, content):
        if re.match(r'POST', content) != None:
            return 'POST'
        if re.match(r'GET', content) != None:
            return 'GET'

    # 读取数据包
    def getPacket(self):
        packet = ''
        with open(self._fileName, 'r') as f:
            packet = [line.strip() for line in f.readlines()]
        return packet
    
    # 解析数据包内容
    def parsePacket(self):
        packet = self.getPacket()

        # 解析header
        head = dict()
        postData = dict()
        for i in range(len(packet)-1):
            if i == 0:
                continue
            # print(i)
            if packet[i] == '':
                tmp = packet[i+1].split('&')
                for t in tmp:
                    datas = t.split('=')
                    postData = {datas[0] : datas[1]}
            else:
                line = packet[i].split(':')
                head[line[0]] = line[1].strip()
        return head, postData



# test = Parse('sql.txt')
# print(test.parsePacket())
