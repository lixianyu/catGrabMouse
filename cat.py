#输入步进数，得到最后一轮被吃掉的老鼠的编号，以及第三轮被吃掉的老鼠的编号
#一共有13只老鼠围成一个圆圈。

magicNum = 13 #步进数
gn = 1
gtheThirdEatMouse = 0
def eatAMouse(idx, mouses):
    lens = len(mouses)

    m = 1
    while m < magicNum:
        idx += 1
        if idx >= lens:
            idx = 0
        m += 1
    theTargetMouse = idx
    print('Mouse ', mouses[theTargetMouse], "was eatted by my cat!")

    if gn == 3:
        global gtheThirdEatMouse
        gtheThirdEatMouse = mouses[theTargetMouse]

    mouses.pop(theTargetMouse)
    if theTargetMouse >= lens - 1:
        return 0
    return theTargetMouse

curIdx = 0 # 老鼠编号减一
mouseCount = 13 #有13只老鼠，编号为1的老鼠的颜色为白色，其它为黑色
mouseList = list(range(1, mouseCount + 1))
print(mouseList)
print('一共有', mouseCount, '只老鼠\n')

while True:
    magicNum = input('请输入步进数：')
    if not magicNum.isdigit():
        print('请输入数字')
        continue
    magicNum = int(magicNum)
    if magicNum <= 0:
        print('请输入正整数')
    else:
        break

while True:
    curIdx = input('请输入起始老鼠编号：')
    if not curIdx.isdigit():
        print('请输入数字')
        continue
    curIdx = int(curIdx)
    if curIdx > 0 and curIdx <= 13:
        break
    else:
        print('老鼠编号为1至13')

curIdx -= 1
print('\n从编号', curIdx + 1, '的老鼠开始数，每次吃第', magicNum, "个老鼠")

while gn < mouseCount:
    print('Round ', gn, ':')
    curIdx = eatAMouse(curIdx, mouseList)
    gn += 1

print('最后一个被吃的耗子是: ', mouseList[0])
print('第三轮被吃掉的耗子是: ', gtheThirdEatMouse)
