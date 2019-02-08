#输入步进数，得到最后一轮被吃掉的老鼠的编号，以及第三轮被吃掉的老鼠的编号
#一共有13只老鼠围成一个圆圈。

magicNum = 13#步进数
gn = 1
gtheThirdEatMouse = 0
def eatThirteenthMouse1(idx, mouses):
    lens = len(mouses)
    # print('lens = ', lens)
    m = 1
    while m < magicNum:
        idx += 1
        if idx >= lens:
            idx = 0
        m += 1
    theTargetMouse = idx
    # print('theTargetMouse = ', theTargetMouse)
    print('Mouse ', mouses[theTargetMouse], "was eatted by my cat!")
    # print('gn = ',gn)
    if gn == 3:
        # print('haha')
        global gtheThirdEatMouse
        gtheThirdEatMouse = mouses[theTargetMouse]
        # print('gtheThirdEatMouse =', gtheThirdEatMouse)
    mouses.pop(theTargetMouse)
    if theTargetMouse >= lens - 1:
        return 0
    return theTargetMouse

print('请输入老鼠个数：')
# mouseCount = int(input())
mouseCount = 13 #有13只老鼠，编号为1的老鼠的颜色为白色，其它为黑色
mouseList = list(range(1, mouseCount + 1))
print(mouseList)
print('一共有', mouseCount, '只老鼠')
print('请输入步进数：')
magicNum = int(input())
print('每次吃第', magicNum, "个老鼠")
# print('按任意键继续')
# input()

curIdx = 0
while gn < mouseCount:
    print('Round ', gn, ':')
    curIdx = eatThirteenthMouse1(curIdx, mouseList)

    # print('curIdx = ', curIdx)
    # print(mouseList)
    gn += 1
    # print('\n')

print('最后一个被吃的耗子是: ', mouseList[0])
print('第三轮被吃掉的耗子是: ', gtheThirdEatMouse)
