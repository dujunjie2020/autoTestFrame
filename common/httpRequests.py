import requests


class httpRequest():
    def __init__(self,method,url,headers=None,data=None,pemName=None,pemKey=None):
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.pemName = pemName
        self.pemKey = pemKey
    #定义http请求
    def httpRequest(self):
        if self.method == 'post' :
            httpPost = requests.post(url=self.url,headers=self.headers,data=self.data)
            return httpPost.content.decode(encoding='utf-8')

        elif self.method == 'get' :
            httpGet = requests.get(url=self.url,headers = self.headers)
            return httpGet.content.decode(encoding='utf-8')
    #定义https单向请求-不需要出示客户端证书
    def httpsOneWayRequest(self):
        if self.method == 'post':
            httpsPostData = requests.post(url = self.url,headers = self.headers,data = self.data,verify = False)
            return httpsPostData.content.decode(encoding='utf-8')
        elif self.method == 'get':
            httpsGetData = requests.get(url = self.url,headers = self.headers,verify = False)
            return httpsGetData.content.decode(encoding='utf-8')
    #定义https双向请求-需要出示客户端证书
    #此处证书格式仅支持pem格式的证书和密钥对
    def httpsMutualRequest(self):
        #获取证书和密钥对，需解密状态
        clientCertPem = self.pemName
        clientCertkey = self.pemKey
        certInfo = (clientCertPem,clientCertkey)

        session = requests.session()
        session.cert = certInfo
        if self.method == 'post':
            httpsMutualPostRequestData = session.post(url = self.url,headers = self.headers,data= self.data,verify = False)
            return httpsMutualPostRequestData.content
        if self.method == 'get':
            httpsMutualGetRequestData = session.get(url = self.url , headers = self.headers,verify = False)
            return httpsMutualGetRequestData.content.decode(encoding='utf-8')

if __name__ == '__main__':
    method = 'get'
    url = 'https://192.168.9.114:8443'
    pem = 'F://09 work//autoTestFrame//inputFile//cert//certPem//systemadmin.pem'
    key = 'F://09 work//autoTestFrame//inputFile//cert//certPem//systemadminkey.key'
    a = httpRequest(method,url,pemName=pem,pemKey=key)
    b = a.httpsMutualRequest()
    print(b)