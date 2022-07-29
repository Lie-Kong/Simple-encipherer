from statistics import mode


print("\vpy版加密工具\n\t制作by猎空\v ")

Mode = input("需要启用的功能：\nA:加密\nB:解密\nC:全都要\nE:退出(A B C or E)\n ")

#  ↓  加密部分  ↓  

# import numpy as np
i=0
list = []
list1 = []
list2 = []
list3 = []


# ↑ 配置文件

if Mode == 'A' or Mode == 'C':


    temp = input("请输入明文：")
    while temp == '':
        print('明文不可为空')
        temp = input('请重新输入明文')
    m = temp

# ↑ 输入待加密内容

    temp = input('请输入加密符 1/4 ：')

    while temp == '':
        temp = input('请输入加密符 1/4 ：')
    j1 = temp

    temp = input('请输入加密符 2/4 ：')

    while temp == '':
        temp = input('请输入加密符 2/4 ：')
    j2 = temp

    while j2 == j1 :
            print('加密符不可相同')
            temp = input('请重新输入加密符 2/4 ：')
            while temp == '':
                temp = input('请输入加密符 2/4 ：')
                j2 = temp

    temp = input('请输入加密符 3/4 ：')

    while temp == '':
        temp = input('请输入加密符 3/4 ：')
    j3 = temp

    while j3 == j1 or j3 == j2:
        print('加密符不可相同')
        temp = input('请重新输入加密符 3/4 ：')
        while temp == '':
            temp = input('请输入加密符 3/4 ：')
        j3 = temp

    temp = input('请输入加密符 4/4 ：')

    while temp == '':
        temp = input('请输入加密符 4/4 ：')
    j4 = temp

    while j4 == j3 or j4==j2 or j4==j1 :
        print('加密符不可相同')
        temp = input('请重新输入加密符 4/4 ：')
        while temp == '':
            temp = input('请输入加密符 4/4 ：')
        j4 = temp

# ↑ 输入加密符,并检测是否合法

    temp = input('请输入分割符：')
    fen = temp
    while fen == '':
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
        # uni = np.base_repr(un, base=4)
        while un!=0:
            ul = un%4
            un = (un - un%4)/4
            ul = int(ul)
            list2.append(ul)
        c = len(list2) - 1
        while c > -1:
            a=(list2[c])
            a=str(a)
            list3.append(a)
            c=c - 1
        uni = ''.join(list3)
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

if Mode == 'B' or Mode == 'C':
    temp = input("请输入密文：")
    m = temp

# ↑ 输入待加密内容

    temp = input('请输入加密符 1/4 ：')

    while temp == '':
        temp = input('请输入加密符 1/4 ：')
    j1 = temp

    temp = input('请输入加密符 2/4 ：')

    while temp == '':
        temp = input('请输入加密符 2/4 ：')
    j2 = temp

    while j2 == j1 :
            print('加密符不应相同')
            temp = input('请重新输入加密符 2/4 ：')
            while temp == '':
                temp = input('请输入加密符 2/4 ：')
                j2 = temp

    temp = input('请输入加密符 3/4 ：')

    while temp == '':
        temp = input('请输入加密符 3/4 ：')
    j3 = temp

    while j3 == j1 or j3 == j2:
            print('加密符不应相同')
            temp = input('请重新输入加密符 3/4 ：')
            while temp == '':
                temp = input('请输入加密符 3/4 ：')
            j3 = temp

    temp = input('请输入加密符 4/4 ：')

    while temp == '':
        temp = input('请输入加密符 4/4 ：')
    j4 = temp

    while j4 == j3 or j4==j2 or j4==j1 :
            print('加密符不应相同')
            temp = input('请重新输入加密符 4/4 ：')
            while temp == '':
                temp = input('请输入加密符 4/4 ：')
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

input("按下enter退出")
