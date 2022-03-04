from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization
from common.getPath import *
import os

class readPfx():
    def __init__(self,certFile,certPass):
        #定义证书文件路径和证书密码
        self.certFile = os.path.join(adminCertFilePath,certFile)
        self.certPass = certPass

    def getCertInfo(self):

        cert = pkcs12.load_pkcs12(open(self.certFile,'rb').read(),self.certPass)
        #获取证书公钥
        certInfo = cert.cert.certificate.public_bytes(encoding=serialization.Encoding.PEM)
        #certInfo = cert.cert.certificate.public_key()
        return certInfo
    def getCertPublic(self):

        cert = pkcs12.load_pkcs12(open(self.certFile,'rb').read(),self.certPass)
        #读取证书并以pem格式显示
        certPublic = cert.cert.certificate.public_key().public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.PKCS1)
        #certPublic = cert.cert.certificate.public_key()
        return certPublic
    def getPrivateKey(self):
        cert = pkcs12.load_pkcs12(open(self.certFile,'rb').read(),self.certPass)
        #获取证书私钥并以PEM格式显示
        certPrivate = cert.key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.BestAvailableEncryption(self.certPass))
        #certPrivate = cert.key
        return certPrivate
if __name__ == '__main__':
    sysadmin = readPfx('Systemadmin.pfx',b'1')
    print(sysadmin.getPrivateKey())
    print(sysadmin.getCertPublic())
    print(sysadmin.getCertInfo())
