str1 = 'jinkin'
str2 = "jinkin"
str3 = """jinkin"""
# 多行的情况下用三引号
print(type(str1))
print(type(str2))
print(type(str3))
# 字符串


##################################转义################################## 
str4 = 'jinkin"CIsco"'
print(str4)
str5 = "jinkin\'"
print(str5)
# 转义符，比如上面的'用\转义
folder1 = "C:\\nexus\\abc"
print(folder1)
# 方法1：比如windows路径就需要转义
folder2 = r"C:\nexus\abc"
print(folder2)
# 方法2：通过r=raw来解决问题，告诉他是原始字符串，不要过多解析。


##################################转字节字符串################################## 

print(b'\x73\x70\x01')
# b=bytes字节字符串，# \x73其实就是0x73,是16进制，一个16是8bit，8bit就是一个Byte，所以叫字节。
# 方法1：转换成十进制是01110011，等于115。
# 方法2: 7就是7个16，那么10x7=70 6x7=42 总计就是112，然后3就是3，那么112+3
# 115对应ASCII码就是s
# 所有文本文档可以识别成字符串
# 但是WORD、PDF、图片文档等都是二进制，都是字节字符串。


##################################字符串太长、换行################################## 

str10 = "asdasdasdasd \
    asdasdasdasdsa \
        asdasdasd"
print(str10)
# \代码特别长的时候可以用，主动换行


##################################\n和\r的问题################################# 
# linux换行是\n，如果windows普通notepad就是\r\n
file1 = open('04_Resource/FileLinux', 'rb').read()
print(file1)
# 这里的路径一定要注意使用/（正斜杠），如果是/（反斜杠）就是转义了。
# 可以看到读出的内容是b'123asdas\n'，其中有一个\n，说明是linux。
file2 = open('04_Resource/FileWin.txt', 'rb').read()
print(file2)
# Windows就是\r\n  b'asdasdasda\r\ndasasdasdas\r\nasd'
# 微软是基于经典打字机来解释的，比如\n就是老的打字机滚轮往左移到最左边（换行），\r就是打印针拨到前面，其实就是（enter）。

file3 = open('04_Resource/FileWinTranslated.txt', 'rb').read()
print(file3)
# 这个是Dos2Unix转换后的 b'asdasdasda\ndasasdasdas\nasd'




