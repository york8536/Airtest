from airtest.core.api import *

def TriggerCheck(gamecode):
    print('TriggerCheck')
    match gamecode:
        case '10001':
            if exists(Template(r"tpl1717487932053.png", record_pos=(0.029, -0.167), resolution=(2400, 1080))):
                return 'jp'
            elif exists(Template(r"tpl1717057357556.png", record_pos=(0.0, -0.074), resolution=(2400, 1080))):
                return 'fg'
            else:
                return 'ng'
    
def Trigger(gamecode, triggerType):
    print('Trigger')
    match gamecode:
        case '10001':
            Trigger_10001(triggerType)

def Trigger_10001(triggerType):
    print('Trigger_10001')
    jpPath = [
    (399,626),
    (553,503),
    (585,825),
    (753,648),
    (970,535),
    (1002,834),
    (1207,644),
    (1433,499),
    (1406,794),
    (1624,680),
    (1810,422),
    (1810,807),
    (2001,630)
    ]
    match triggerType:
        case 'jp':
            wait(Template(r"tpl1717057633599.png", record_pos=(-0.015, -0.109), resolution=(2400, 1080)))
            for touchPath in jpPath:
                touch(touchPath)
                sleep(0.7)
            sleep(6)
            wait(Template(r"tpl1717486447305.png", record_pos=(-0.004, 0.138), resolution=(2400, 1080)))
            touch((1211,834))
            sleep(2)
            wait(Template(r"tpl1717486447305.png", record_pos=(-0.004, 0.138), resolution=(2400, 1080)))
            touch((1211,834))
            sleep(2)
            touch((1211,834))
        case 'fg':
            wait(Template(r"tpl1717057357556.png", record_pos=(0.0, -0.074), resolution=(2400, 1080)))
            touch(Template(r"tpl1717488072253.png", record_pos=(-0.007, 0.115), resolution=(2400, 1080)))
            while not exists(Template(r"tpl1717057578915.png", record_pos=(0.214, 0.198), resolution=(2400, 1080))):
                touch((1211,834))
                sleep(0.5)
                touch((1211,834))
        case 'ng':
            touch((1980, 1000))
            sleep(0.2)
            touch((1980, 1000))