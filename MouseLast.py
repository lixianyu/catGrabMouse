
magicNum = 21 #步进数,从21开始吧
gn = 1

def eatThirteenthMouse1(idx, mouses):
    lens = len(mouses)
    # print('lens = ', lens)
    m = 1
    global magicNum
    while m < magicNum:
        idx += 1
        if idx >= lens:
            idx = 0
        m += 1
    theTargetMouse = idx
    # print('theTargetMouse = ', theTargetMouse)
    # print('Mouse ', mouses[theTargetMouse], "was eatted by my cat!")

    mouses.pop(theTargetMouse)
    if theTargetMouse >= lens - 1:
        return 0
    return theTargetMouse

mouseCount = 13 #有13只老鼠，编号为1的老鼠的颜色为白色，其它为黑色
mouseList = list(range(1, mouseCount + 1))
print(mouseList)
print('一共有', mouseCount, '只老鼠')
print('请输入最大的步进数：')
maxStep = int(input())
print('满足最后一个被吃的耗子是白色的步进数为: ')
curIdx = 0
for step in range(magicNum, maxStep + 1):
    magicNum = step
    while gn < mouseCount:
        curIdx = eatThirteenthMouse1(curIdx, mouseList)
        gn += 1
    if mouseList[0] == 1:
        print('步进数： ', step)
    gn = 1
    curIdx = 0
    mouseList = list(range(1, mouseCount + 1))

print('Done!')
