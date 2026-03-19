states_of_china = ['Shanghai','Beijing','Guangzhou','Shenzhen']
states_of_china.extend("Cisco")
# 最后扩展 ['Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen', 'C', 'i', 's', 'c', 'o']
# 所以一定要加[]代表是以列表的形式extend
states_of_china.extend(["CCIE"])
# ['Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen', 'C', 'i', 's', 'c', 'o', 'CCIE']
print(states_of_china)
# 修改0号位内容