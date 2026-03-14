import hashlib  # 导入 hashlib 模块，用来计算哈希值，比如 MD5

# 打开 OSCP 目录下的 dict.txt 文件
# "a+" 表示：
# a = 追加写入，如果文件不存在会自动创建
# + = 同时支持读和写
file = open("OSCP/dict.txt", "a+")

# range(100) 表示循环 100 次，i 的取值是 0 到 99
for i in range(100):
    # 拼接字符串，生成类似 prs.php0、prs.php1、prs.php2 ... prs.php99
    file_name = "prs.php" + str(i)

    # 对 file_name 字符串做 MD5 哈希计算
    # encode() 是先把字符串转成字节，因为 md5 只能处理字节数据
    hash = hashlib.md5(file_name.encode())

    # hexdigest() 会把 MD5 结果转成 32 位十六进制字符串
    # 然后再拼接上 .php 后缀
    out = hash.hexdigest() + ".php"

    # 把结果写入文件，每写一个结果就换一行
    # \r\n 是 Windows 风格换行
    file.write(out + "\r\n")

# 循环结束后关闭文件
file.close()