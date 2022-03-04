'''
获取文件路径
author：junjie_du
date: 2022-2-25
'''
import os
#获取工作目录
basePath =  os.path.abspath('..')
#print(basePath)
#公共文件夹目录
commonPath = os.path.abspath('.')
#print(commonPath)
#配置文件夹目录
configPath = os.path.join(basePath,'config')
#print(configPath)
#获取输入文件路径
inputFilePath = os.path.join(basePath,'inputFile')
#print(inputFilePath)
#证书文件路径
certFilePath = os.path.join(inputFilePath,'cert')
adminCertFilePath = os.path.join(certFilePath,'adminCert')
userCertFilePath = os.path.join(certFilePath,'userCert')
print(certFilePath)
#测试用例目录
testCaseFile = os.path.join(inputFilePath,'testCase')
#print(testCaseFile)
#输出文件路径
outputFilePath = os.path.join(basePath,'outputFile')
#print(outputFilePath)
#日志文件路径
logsFile = os.path.join(outputFilePath,'logs')
#print(logsFile)
#测试报告路径
testReportFile = os.path.join(outputFilePath,'testReport')
#print(testReportFile)
