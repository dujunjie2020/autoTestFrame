'''
author:junjie_du
date:2022-03-03
'''
import hashlib
from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from common import getCert
#md5加密算法
class encryption():
    #初始化定义待加密数据,证书文件和密码
    def __init__(self,message,pfxName = None,pfxPass = None):
        self.message = message
        self.pfxName = pfxName
        self.pfxPass = pfxPass.encode()
    #定义md5加密算法
    def md5Crypt(self):
        m = hashlib.md5(self.message.encode('utf-8'))
        value = m.hexdigest()
        return value
    #定义P7签名
    def p7sign(self):
        #获取证书的公钥和私钥
        userCert = getCert.readPfx(self.pfxName,self.pfxPass)
        cert = userCert.getCertInfo()
        key = userCert.getPrivateKey()
        #证书信息加载为X509格式,私钥转化为rsa，cryptography库中p7签名接口要求的格式
        cert_x509 = x509.load_pem_x509_certificate(cert)
        key_rsa = serialization.load_pem_private_key(key,password=self.pfxPass)
        #执行p7签名并返回签名结果
        options = [pkcs7.PKCS7Options.DetachedSignature]
        p7SignData = pkcs7.PKCS7SignatureBuilder().set_data(self.message.encode('utf-8')).add_signer(cert_x509,key_rsa,hashes.SHA256()).sign(serialization.Encoding.SMIME,options)
        return p7SignData
    #基于rsa算法的非对称加密
    def rsaSign(self):
        message = self.message.encode()
        userCert = getCert.readPfx(self.pfxName,self.pfxPass)
        cert = userCert.getPrivateKey()
        certPem =  serialization.load_pem_private_key(cert,self.pfxPass)
        signData = certPem.sign(message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length = padding.PSS.MAX_LENGTH),hashes.SHA256())
        return signData

if __name__ == '__main__':
    pfxName = 'Systemadmin.pfx'
    pfxPass = '1'
    a = '123'
    demo1 = encryption(a,pfxName,pfxPass)
    print(demo1.rsaSign())
