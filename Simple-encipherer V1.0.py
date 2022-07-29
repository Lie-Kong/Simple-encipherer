print("\vpy版加密工具\n\t制作by猎空\v ")

#  ↓  加密部分  ↓  


import numpy as np
i=0
list = []

# ↑ 配置文件

temp = input("请输入明文：")
m = temp

# ↑ 输入待加密内容

temp = input('请输入加密符 1/4 ：')
j1 = temp
if j1 == '':
    temp = input('请输入加密符 1/4 ：')
    j1 = temp

temp = input('请输入加密符 2/4 ：')
j2 = temp
if j2 == '':
    temp = input('请输入加密符 2/4 ：')
    j2 = temp
else:
    if j2 == j1 :
        print('加密符不可相同')
        temp = input('请重新输入加密符 2/4 ：')
        j2 = temp

temp = input('请输入加密符 3/4 ：')
j3 = temp
if j3 == '':
    temp = input('请输入加密符 3/4 ：')
    j3 = temp
else:
    if j3 == j1 or j3 == j2:
        print('加密符不可相同')
        temp = input('请重新输入加密符 3/4 ：')
        j3 = temp

temp = input('请输入加密符 4/4 ：')
j4 = temp
if j4 == '':
    temp = input('请输入加密符 4/4 ：')
    j4 = temp
else:
    if j4 == j3 or j4==j2 or j4==j1 :
        print('加密符不可相同')
        temp = input('请重新输入加密符 4/4 ：')
        j4 = temp

# ↑ 输入加密符,并检测是否合法

temp = input('请输入分割符：')
fen = temp
if fen == '':
    print('分隔符不可为空')
    temp = input('请重新输入分隔符：')
    fen = temp

# ↑ 输入加密符

m = [one for one in m]
list1 = m
m = list1[0]

# ↑ 明文拆解

while i<len(list1):
    tp = (list1[i])
    un = ord(tp)
    uni = np.base_repr(un, base=4)
    uni = uni.replace('0',j1)
    uni = uni.replace('1',j2)
    uni = uni.replace('2',j3)
    uni = uni.replace('3',j4)
    list.append(uni)
    i+=1

# ↑ 明文加密，输出密文

x = fen.join(list)

# ↑ 密文重新排列

print (x)

# ↑ 输出密文

print(r'以下是您的加密符,请小心保存："', j1 , j2 , j3 , j4 , "'" )

# ↑ 输出加密符

print(r'以下是您的分隔符,请小心保存："', fen , '"')

# ↑ 输出分隔符



# ↓  解密部分

temp = input("是否启用解密：(Y or N)")

if temp == 'Y':
    temp = input("请输入密文：")
    m = temp

# ↑ 输入待加密内容

    temp = input('请输入加密符 1/4 ：')
    j1 = temp
    if j1 == '':
        temp = input('请输入加密符 1/4 ：')
        j1 = temp


    temp = input('请输入加密符 2/4 ：')
    j2 = temp
    if j2 == '':
        temp = input('请输入加密符 2/4 ：')
        j2 = temp
    else:
        if j2 == j1:
            print('加密符不应相同')
            temp = input('请输入正确的加密符 2/4 ：')
            j2 = temp

    temp = input('请输入加密符 3/4 ：')
    j3 = temp
    if j3 == '':
        temp = input('请输入加密符 3/4 ：')
        j3 = temp
    else:
        if j3 == j1 or j3 == j2:
            print('加密符不应相同')
            temp = input('请输入正确的加密符 3/4 ：')
            j3 = temp

    temp = input('请输入加密符 4/4 ：')
    j4 = temp
    if j4 == '':
        temp = input('请输入加密符 4/4 ：')
        j4 = temp
    else:
        if j4 == j3 or j4==j2 or j4==j1 :
            print('加密符不应相同')
            temp = input('请输入正确的加密符 4/4 ：')
            j4 = temp

# ↑ 输入加密符,并检测是否合法

    temp = input('请输入分割符：')
    fen = temp
    if fen == '':
        print('分隔符不应为空')
        temp = input('请输入正确的分隔符：')
        fen = temp

# ↑ 输入加密符

    m=m.replace(j1,'0')
    m=m.replace(j2,'1')
    m=m.replace(j3,'2')
    m=m.replace(j4,'3')
    m=m.replace(fen,' ')
    list = m.split();

# ↑ 将密文转换为四进制

    for i in list:
        i = int(i,4)
        i = chr(i)
        list1.append(i)

# ↑ 将四进制转为明文

    x = ''.join(list1)

# ↑ 明文重新排列

    print (x)

# ↑ 输出明文

input("请输入任意按键退出")
