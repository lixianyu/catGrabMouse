
gDiJiGe = 3 # 第几个被吃掉
magicNum = 1 # 步进数,从1开始吧
gn = 1
gtheThirdEatMouse = 0 # 第gDiJiGe个被吃掉的老鼠编号

def eatAMouse(idx, mouses):
    lens = len(mouses)

    m = 1
    global gn
    global magicNum
    global gtheThirdEatMouse
    while m < magicNum:
        idx += 1
        if idx >= lens:
            idx = 0
        m += 1
    theTargetMouse = idx
    if gn == gDiJiGe:
        global gtheThirdEatMouse
        gtheThirdEatMouse = mouses[theTargetMouse]

    mouses.pop(theTargetMouse)
    if theTargetMouse >= lens - 1:
        return 0
    return theTargetMouse

mouseCount = 13 #有13只老鼠，编号为1的老鼠的颜色为白色，其它为黑色
mouseList = list(range(1, mouseCount + 1))
print(mouseList)
print('一共有', mouseCount, '只老鼠\n')

while True:
    maxStep = input('请输入最大的步进数：')
    if not maxStep.isdigit():
        print('请输入数字')
        continue
    maxStep = int(maxStep)
    if maxStep <= 0:
        print('请输入正整数')
    else:
        break

print('满足第', gDiJiGe, '个被吃的耗子是白色的步进数为: ')
curIdx = 0 # 老鼠编号减一
theAllTarget = [] #所有满足要求的步进数都存入此list
for step in range(magicNum, maxStep + 1):
    magicNum = step
    while gn < mouseCount:
        curIdx = eatAMouse(curIdx, mouseList)
        if gn == gDiJiGe:
            break
        gn += 1
    if gtheThirdEatMouse == 1:
        print('步进数： ', step)
        theAllTarget.append(step)
    gn = 1
    curIdx = 0
    mouseList = list(range(1, mouseCount + 1))

print('theAllTarget = ', theAllTarget, '  长度为：', len(theAllTarget))
# minusList = []
# for i in range(1, len(theAllTarget)):
#     minusList.append(theAllTarget[i] - theAllTarget[i-1])
# print('minusList = ', minusList)

modList13 = [13 if x % 13 == 0 else x % 13 for x in theAllTarget]
modList12 = [12 if x % 12 == 0 else x % 12 for x in theAllTarget]
modList11 = [11 if x % 11 == 0 else x % 11 for x in theAllTarget]
modList10 = [10 if x % 10 == 0 else x % 10 for x in theAllTarget]

# 余数相加
add131211 = [x + y + z for x,y,z in zip(modList13, modList12, modList11)]
# for i, j, k, m in zip(modList13,modList12,modList11,modList10):
#     summ = i + j + k + m
#     add131211.append(summ)
# for i, j, k in zip(modList13, modList12, modList11):
#     summ = i + j + k
#     add131211.append(summ)

# modIsFifteenOrOne = list(filter(lambda x : x == 15 or x == 1, add131211))
# modIsFifteenOrOne = []
# for i in range(len(add131211)):
#     if add131211[i] == 15 or add131211[i] == 1:
#         modIsFifteenOrOne.append(theAllTarget[i])
print('\nmodList13 = ', modList13)
print('modList12 = ', modList12)
print('modList11 = ', modList11)
print('modList10 = ', modList10)
print('\nadd131211 = ', add131211)
# print('modIsFifteenOrOne = ' , modIsFifteenOrOne)
print('Done!')
