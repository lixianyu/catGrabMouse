
magicNum = 21 #起始的步进数,从21开始吧
gn = 1

def eatAMouse(idx, mouses):
    lens = len(mouses)

    m = 1
    global magicNum
    while m < magicNum:
        idx += 1
        if idx >= lens:
            idx = 0
        m += 1
    theTargetMouse = idx

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

print('满足最后一个被吃的耗子是白色的步进数为: ')
curIdx = 0 # 老鼠编号减一
theAllTarget = [] #所有满足要求的步进数都存入此list
for step in range(magicNum, maxStep + 1):
    magicNum = step
    while gn < mouseCount:
        curIdx = eatAMouse(curIdx, mouseList)
        gn += 1
    if mouseList[0] == 1:
        print('步进数： ', step)
        theAllTarget.append(step)
    gn = 1
    curIdx = 0
    mouseList = list(range(1, mouseCount + 1))

print('\ntheAllTarget = ', theAllTarget)
# minusList = []
# for i in range(1, len(theAllTarget)):
#     minusList.append(theAllTarget[i] - theAllTarget[i-1])
# print('minusList = ', minusList)

# 以下为theAllTarget中对应的13~1的余数list
modList13 = [13 if x % 13 == 0 else x % 13 for x in theAllTarget]
modList12 = [12 if x % 12 == 0 else x % 12 for x in theAllTarget]
modList11 = [11 if x % 11 == 0 else x % 11 for x in theAllTarget]
modList10 = [10 if x % 10 == 0 else x % 10 for x in theAllTarget]
modList09 = [9 if x % 9 == 0 else x % 9 for x in theAllTarget]
modList08 = [8 if x % 8 == 0 else x % 8 for x in theAllTarget]
modList07 = [7 if x % 7 == 0 else x % 7 for x in theAllTarget]
modList06 = [6 if x % 6 == 0 else x % 6 for x in theAllTarget]
modList05 = [5 if x % 5 == 0 else x % 5 for x in theAllTarget]
modList04 = [4 if x % 4 == 0 else x % 4 for x in theAllTarget]
modList03 = [3 if x % 3 == 0 else x % 3 for x in theAllTarget]
modList02 = [2 if x % 2 == 0 else x % 2 for x in theAllTarget]
modList01 = [1 if x % 1 == 0 else x % 1 for x in theAllTarget]

# 所有余数相加
add13_01 = []
for a13,a12,a11, a10,a9,a8,a7,a6,a5,a4,a3,a2,a1 in zip(modList13,modList12,modList11,modList10, modList09, modList08, modList07, modList06, modList05, modList04, modList03, modList02, modList01):
    summ = a13 + a12 + a11 + a10 + a9 + a8 + a7 + a6 + a5 + a4 + a3 + a2 + a1
    add13_01.append(summ)
theSET = set(add13_01) # 交集

mod13 = [13 if x % 13 == 0 else x % 13 for x in add13_01] # 对add13_01再取余数观察
print('modList13 = ', modList13)
print('modList12 = ', modList12)
print('modList11 = ', modList11)
print('modList10 = ', modList10)
print('modList09 = ', modList09)
print('modList08 = ', modList08)
print('modList07 = ', modList07)
print('modList06 = ', modList06)
print('modList05 = ', modList05)
print('modList04 = ', modList04)
print('modList03 = ', modList03)
print('modList02 = ', modList02)
print('modList01 = ', modList01)

print('add13_01 = ', add13_01)
print('theSET = ', theSET)
print('mod13 = ', mod13)
print('Done!')
