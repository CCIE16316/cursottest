# 1.3 替换
result3 = 'aaa---bbb---ccc'.replace('---','===')
print(result3)
# 替换了---位====

# 1.4 sub替换
result4 = re.sub(r'[-=]+','+++','aaa-----bbb=====--cccc')
print(result4)
