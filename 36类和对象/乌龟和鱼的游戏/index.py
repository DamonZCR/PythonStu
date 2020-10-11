'''以一个列表liveAnim来存储存活着的生物，以字典animloca来存储此列表中，生物的信息，
包括以生物的名称为键，生物的当前坐标为值。'''
from fish import Fish
from wgui import Wgui

def index():
    print('游戏开始！')
    fishNum = 5
    guiNum = 1
    num = guiNum#存活的乌龟
    liveAnim = list()#存活的动物
    animloca = dict()#键值为姓名，值为坐标
    #实例化 fishNum 个鱼
    for i in range(fishNum):
        fobj = Fish('&&&'+str(i))
        liveAnim.append(fobj)
        animloca.update({fobj.name: fobj.live()})
    #实例化guiNum 个乌龟
    for i in range(guiNum):
        #这里重复覆盖这个对象，不会影响到已经添加到list 里的已有对象
        gobj = Wgui('@@@'+str(i))
        liveAnim.append(gobj)
        animloca.update({str(gobj.name): gobj.live()})


    while (num > 0) and (len(liveAnim) != 0):
        num = 0
        #输出他们的状态
        #上边界
        for sfir in range(11):
            on = 0
            for oneAnim in animloca.items():
                if (oneAnim[1][1] == 0) and (oneAnim[1][0] == sfir):
                    if '&' in str(oneAnim[0]):
                        print('&&&',end='')
                    else:
                        print('@@@',end='')
                    on = 1#此位置被占
                    
            if on == 0:
                print('+++',end='')
            if sfir == 10:
                print()

        #中间输出1-9行
        for fir in range(9):
            #控制左边边界
            on = 0
            for oneAnim in animloca.items():
                if (oneAnim[1][0] == 0) and (oneAnim[1][1] == fir + 1):
                    if '&' in str(oneAnim[0]):
                        print('&&&', end='')
                    else:
                        print('@@@', end='')
                    on = 1
            if on == 0:
                print(' + ',end='')
            #控制中间空白的活动区域
            for mid in range(9):
                on = 0
                for oneAnim in animloca.items():
                    if (oneAnim[1][0] == mid + 1) and (oneAnim[1][1] == fir + 1):
                        if '&' in str(oneAnim[0]):
                            print('&&&', end='')
                        else:
                            print('@@@', end='')
                        on = 1
                if on == 0:
                    print('   ', end='')
            #输出右边边界
            on = 0
            for oneAnim in animloca.items():
                if (oneAnim[1][0] == 10) and (oneAnim[1][1] == fir + 1):
                    if '&' in str(oneAnim[0]):
                        print('&&&', end='')
                    else:
                        print('@@@', end='')
                    on = 1
            if on == 0:
                print(' + ',end='')
            print('')
        #输出下方边界
        for xfir in range(11):
            on = 0
            for oneAnim in animloca.items():
                if (oneAnim[1][1] == 10) and (oneAnim[1][0] == xfir):
                    if '&' in str(oneAnim[0]):
                        print('&&&', end='')
                    else:
                        print('@@@', end='')
                    on = 1  # 此位置被占

            if on == 0:
                print('+++', end='')
            if xfir == 10:
                print()

        #对活着的动物进行检查
        waitdead = list()
        for eachAn in liveAnim:
            noloca = eachAn.live()
            if noloca == (-1, -1):
                animloca.pop(str(eachAn.name))
                #print(noloca.name+'死亡')
                #标记对象数组里待删除的对象序号
                waitdead.append(liveAnim.index(eachAn))
            else:
                animloca.update({eachAn.name: noloca})
        for adead in waitdead:
            liveAnim.pop(adead)
        #重新记录，待删除的鱼（被吃掉）
        waitdead.clear()
        #对乌龟吃掉的鱼进行删除
        i = 0
        for eachAn1 in animloca.items():
            j = 0
            for aname in animloca.items():
                #如果eachAn1 是鱼，aname是一个龟，并且坐标相等
                if ('@@@'in str(aname[0])) and ('&&&' in str(eachAn1[0])) and (eachAn1[1] == aname[1]):
                    waitdead.append(i)
                    #liveAnim[i].setliveval()
                    liveAnim[j].life +=1
                j +=1
            i +=1
        for adead in waitdead:
            animloca.pop(liveAnim[adead].name)
            liveAnim[adead].setliveval()
            liveAnim.pop(adead)
        for liveWgui in liveAnim:
            if isinstance(liveWgui, Wgui):
                num +=1

index()
            

            
