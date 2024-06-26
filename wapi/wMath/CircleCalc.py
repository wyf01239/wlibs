﻿from cmath import sqrt
from encodings import utf_8
utf_8

'''
wAPICircleCalc v2 2023.4.24
by wyf9 and Dobastickrn.
出现错误时会被抛出, 注意处理错误 (除原版)
PAI 如不指定, 默认值为 3.14
'''

def r(r, pai = 3.14):
    '''
    圆的半径求其他 (自定义 PAI)
    r: 半径 (int / float)
    pai: 自定的 PAI (int / float)
    返回: tuple (直径, 周长, 面积)
    '''
    try:
        d = 2*float(r)
        C = float(d)*float(pai)
        S = float(r)**2*float(pai)
        wBack = (d, C, S)
        return wBack
    except:
        raise

def d(d, pai = 3.14):
    '''
    圆的直径求其他 (自定 PAI)
    r: 半径 (int / float)
    pai: 自定的 PAI (int / float)
    返回: tuple (半径, 周长, 面积)
    '''
    try:
        r = float(d)/2
        C = float(d)*pai
        S = float(d)**2*pai
        wBack = (r, C, S)
        return wBack
    except:
        raise

def C(C, pai = 3.14):
    '''
    圆的周长求其他 (自定 PAI)
    C: 周长 (int / float)
    pai: 自定的 PAI (int / float)
    返回: tuple (半径, 直径, 面积)
    '''
    assert pai != 0 , "pai Can't be 0"
    try:
        r = float(C) / float(pai) / 2
        d = float(C) / float(pai)
        S = float(r) ** 2 * float(pai)
        wBack = (r, d, S)
        return wBack
    except:
        raise

def S(S, pai = 3.14):
    '''
    圆的面积求其他 (自定 PAI)
    S: 面积 (int / float)
    pai: 自定的 PAI (int / float)
    返回: tuple (半径, 直径, 周长)
    '''
    assert pai != 0, "pai Can't be 0"
    try:
        r = sqrt(float(S) / pai)
        d = float(r) * 2
        C = float(d) * pai
        wBack = (r, d, C)
        return wBack
    except:
        raise

def Original():
    print('Circle Calculator\n©Dobastickrn    Date:2023/4/6\n注意: 本工具中π的取值为3.14\n')

    M = input('输入模式\na: 正向\nb: 反向\n')
    if M == 'a' or M == 'b':
        go = 't'
    else:
        go = 'f'

    if go == 't':
        if M == 'a':
            r = input('输入半径\n')
            d = 2*float(r)
            C = float(d)*3.14
            S = float(r)**2*3.14
            print('当半径为'+r+'时→')
            print('直径为 '+str(d))
            print('周长为 '+str(C))
            print('面积为 '+str(S))
            print('计算完毕\n')

        else:
            M_ = input('面积还是周长？\na: 面积\nb: 周长\n')
            if M_ == 'a' or M == 'b':
                go_ = 't'
            else:
                go_ = 'f'
            if go_ == 't':
                if M_ == 'a':
                    S = input('输入面积\n')
                    r = sqrt(float(S)/3.14)
                    d = 2*float(r)
                    S = float(d)*3.14
                    print('当面积为'+str(S)+'时→')
                    print('直径为 '+str(d))
                    print('周长为 '+str(C))
                    print('计算完毕\n')
                else:
                    C = input('输入周长\n')
                    d = float(C)/3.14
                    r = float(d)/2
                    S = float(r)**2*3.14
                    print('当周长为'+str(C)+'时→')
                    print('半径为 '+str(r))
                    print('直径为 '+str(d))
                    print('面积为 '+str(S))
                    print('计算完毕\n')
    else:
        print('请正常点 :)')
    return 0