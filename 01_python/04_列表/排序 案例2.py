# 这行其实可以删掉，因为下面这段代码没有用到 re（正则表达式）
import re

# 原始端口列表，每个元素都是一个字符串
port_list = [
    'eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7',
    'eth 1/101/2/46', 'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13',
    'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8'
]

sorted_ports = sorted(port_list, key=lambda x: list(map(int,x.replace('eth','').split('/'))))
# x.replace('eth','').split('/') 去掉eth，按照/去拆分，然后变成list
# map(int, ['1', '101', '1', '42'])，把每个元素转成成int，原来是str。另外map就变成了map对象
# list，把map对象转换成列表
# 最后用sorted来排序
print(sorted_ports)