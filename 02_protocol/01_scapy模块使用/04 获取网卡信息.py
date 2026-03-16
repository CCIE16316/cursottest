import netifaces

result = netifaces.ifaddresses('ens160')
print(result)
# Linux比较简单，如果是Windows需要用唯一ID，需要把网卡名字给他，转换成唯一ID。


# Windows获取的原理
# 其实就是通过工具或者注册表信息，里面有network connection就可以通过网卡名找到唯一ID。
