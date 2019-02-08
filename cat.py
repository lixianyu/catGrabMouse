
magicNum = 13
def eatThirteenthMouse(idx, mouses):
    lens = len(mouses)
    print('lens = ', lens)
    theTargetMouse = idx + 13 - 1
    if theTargetMouse > lens:
        theTargetMouse = theTargetMouse - lens
    print('theTargetMouse = ', theTargetMouse)
    print('Cat ', mouses[theTargetMouse], "eatted!")
    mouses.pop(theTargetMouse)
    if theTargetMouse >= lens - 1:
        return 0
    return theTargetMouse

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
    print('Cat ', mouses[theTargetMouse], "eatted!")
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
mouseCount = 13
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
