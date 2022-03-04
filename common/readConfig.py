'''
功能：获取配置文件内容
author：junjie_du
date: 2022-02-28
'''
import configparser
import os
from common import getPath

#获取配置文件信息类
class getConfig():
    #初始化
    def __init__(self):
        configFilePath = os.path.join(getPath.configPath, 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(configFilePath)
    #获取服务器信息
    def get_ServerInfo(self,name):
        value = self.config.get('ServerInfo',name)
        return value

if __name__ == '__main__':
    confInfo = getConfig()
    print(confInfo.get_ServerInfo('ServerIP'))