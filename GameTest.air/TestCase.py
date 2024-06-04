from airtest.core.api import *
from Events import EventManager
import Config
from GameTrigger import *
import asyncio


lobby = EventManager()
# 關閉登入視窗
def CheakPopup():   # 暫時無使用
    while True:
        if exists(Template(r"tpl1714037407130.png", record_pos=(-0.27, -0.065), resolution=(2400, 1080))):
            lobby.emit('首儲', '首儲')
        elif exists(Template(r"tpl1714037742771.png", record_pos=(0.015, 0.042), resolution=(2400, 1080))):
            lobby.emit('綁定手機', '綁定手機')
        elif exists(Template(r"tpl1714037630865.png", record_pos=(-0.234, -0.152), resolution=(2400, 1080))):
            lobby.emit('最新消息', '最新消息')
        elif exists(Template(r"tpl1714037912623.png", record_pos=(-0.028, -0.182), resolution=(2400, 1080))):
            lobby.emit('任務', '任務')
        elif exists(Template(r"tpl1714037798354.png", record_pos=(-0.001, 0.155), resolution=(2400, 1080))):
            lobby.emit('遊戲彈窗', '遊戲彈窗')
        else:
            break

def ClosePopup(Popup):
    match Popup:
        case "首儲":
            touch(Template(r"tpl1714037420151.png", record_pos=(0.371, -0.195), resolution=(2400, 1080)))
        case "綁定手機":
            touch(Template(r"tpl1714037420151.png", record_pos=(0.371, -0.195), resolution=(2400, 1080)))
        case "最新消息":
            touch(Template(r"tpl1714037654629.png", record_pos=(0.317, -0.18), resolution=(2400, 1080)))
        case "任務":
            touch(Template(r"tpl1714037654629.png", record_pos=(0.317, -0.18), resolution=(2400, 1080)))
        case "遊戲彈窗":
            touch(Template(r"tpl1714037420151.png", record_pos=(0.371, -0.195), resolution=(2400, 1080)))
        case "七日簽到":
            touch(Template(r"tpl1714037654629.png", record_pos=(0.317, -0.18), resolution=(2400, 1080)))

def CheakPopupNew(template, event_name):
    while True:
        if exists(template):
            lobby.emit(event_name)
        else:
            break

# 找到並點擊遊戲icon
def ClickGame(gamecode):  # 暫時無使用
    if gamecode == "10001":
        while not exists(Template(r"tpl1714698666528.png", record_pos=(0.013, -0.033), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714698666528.png", record_pos=(0.013, -0.033), resolution=(2400, 1080)))
        print("進入遊戲[10001]")
    elif gamecode == "10002":
        while not exists(Template(r"tpl1714645388655.png", record_pos=(0.055, 0.104), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714645388655.png", record_pos=(0.055, 0.104), resolution=(2400, 1080)))
        print("進入遊戲[10002]")
    elif gamecode == "10005":
        while not exists(Template(r"tpl1714698541152.png", record_pos=(0.177, -0.03), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714698541152.png", record_pos=(0.177, -0.03), resolution=(2400, 1080)))
        print("進入遊戲[10005]")
    elif gamecode == "10006":
        while not exists(Template(r"tpl1714698738316.png", record_pos=(0.145, -0.045), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714698738316.png", record_pos=(0.145, -0.045), resolution=(2400, 1080)))
        print("進入遊戲[10006]")
    elif gamecode == "10007":
        while not exists(Template(r"tpl1714711017065.png", record_pos=(0.075, 0.091), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714711017065.png", record_pos=(0.075, 0.091), resolution=(2400, 1080)))
        print("進入遊戲[10007]")
    elif gamecode == "10008":
        while not exists(Template(r"tpl1714698990255.png", record_pos=(0.114, 0.105), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714698990255.png", record_pos=(0.114, 0.105), resolution=(2400, 1080)))
        print("進入遊戲[10008]")
    elif gamecode == "10010":
        while not exists(Template(r"tpl1714699101986.png", record_pos=(-0.097, 0.104), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714699101986.png", record_pos=(-0.097, 0.104), resolution=(2400, 1080)))
        print("進入遊戲[10010]")
    elif gamecode == "10011":
        while not exists(Template(r"tpl1714700634343.png", record_pos=(0.288, -0.035), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714700634343.png", record_pos=(0.288, -0.035), resolution=(2400, 1080)))
        print("進入遊戲[10011]")
    elif gamecode == "10012":
        while not exists(Template(r"tpl1714699055247.png", record_pos=(0.11, -0.046), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714699055247.png", record_pos=(0.11, -0.046), resolution=(2400, 1080)))
        print("進入遊戲[10012]")
    elif gamecode == "10014":
        while not exists(Template(r"tpl1714700769049.png", record_pos=(0.19, 0.101), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714700769049.png", record_pos=(0.19, 0.101), resolution=(2400, 1080)))
        print("進入遊戲[10014]")
    elif gamecode == "10016":
        while not exists(Template(r"tpl1714700892997.png", record_pos=(0.422, -0.046), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714700892997.png", record_pos=(0.422, -0.046), resolution=(2400, 1080)))
        print("進入遊戲[10016]")
    elif gamecode == "10021":
        while not exists(Template(r"tpl1714701153966.png", record_pos=(-0.021, 0.103), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714701153966.png", record_pos=(-0.021, 0.103), resolution=(2400, 1080)))
        print("進入遊戲[10021]")
    elif gamecode == "10022":
        while not exists(Template(r"tpl1714701190630.png", record_pos=(0.26, 0.113), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714701190630.png", record_pos=(0.26, 0.113), resolution=(2400, 1080)))
        print("進入遊戲[10022]")
    elif gamecode == "10023":
        while not exists(Template(r"tpl1714701225000.png", record_pos=(0.059, -0.028), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714701225000.png", record_pos=(0.059, -0.028), resolution=(2400, 1080)))
        print("進入遊戲[10023]")
    elif gamecode == "10038":
        while not exists(Template(r"tpl1714701612737.png", record_pos=(0.237, 0.07), resolution=(2400, 1080))):
            swipe((0.8, 0.30), (0.3, 0.30), 0.6)
        touch(Template(r"tpl1714701612737.png", record_pos=(0.237, 0.07), resolution=(2400, 1080))) 
        print("進入遊戲[10038]")
        while exists(Template(r"tpl1715239401696.png", record_pos=(-0.001, 0.181), resolution=(2400, 1080))):
            touch((1200,960))

def ClickGameNew(gamecode):
    match gamecode:
        case "10001":
            while not exists(Template(r"tpl1714698666528.png", record_pos=(0.013, -0.033), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714698666528.png", record_pos=(0.013, -0.033), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10001]")
        
        case "10002":
            while not exists(Template(r"tpl1714645388655.png", record_pos=(0.055, 0.104), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714645388655.png", record_pos=(0.055, 0.104), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10002]")
            
        case "10005":
            while not exists(Template(r"tpl1714698541152.png", record_pos=(0.177, -0.03), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714698541152.png", record_pos=(0.177, -0.03), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10005]")
        
        case "10006":
            while not exists(Template(r"tpl1714698738316.png", record_pos=(0.145, -0.045), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714698738316.png", record_pos=(0.145, -0.045), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10006]")
        
        case "10007":
            while not exists(Template(r"tpl1714711017065.png", record_pos=(0.075, 0.091), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714711017065.png", record_pos=(0.075, 0.091), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10007]")
        
        case "10008":
            while not exists(Template(r"tpl1714698990255.png", record_pos=(0.114, 0.105), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714698990255.png", record_pos=(0.114, 0.105), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10008]")
        
        case "10010":
            while not exists(Template(r"tpl1714699101986.png", record_pos=(-0.097, 0.104), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714699101986.png", record_pos=(-0.097, 0.104), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10010]")
        
        case "10011":
            while not exists(Template(r"tpl1714700634343.png", record_pos=(0.288, -0.035), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714700634343.png", record_pos=(0.288, -0.035), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10011]")
        
        case "10012":
            while not exists(Template(r"tpl1714699055247.png", record_pos=(0.11, -0.046), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714699055247.png", record_pos=(0.11, -0.046), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10012]")
        
        case "10014":
            while not exists(Template(r"tpl1714700769049.png", record_pos=(0.19, 0.101), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714700769049.png", record_pos=(0.19, 0.101), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10014]")
        
        case "10016":
            while not exists(Template(r"tpl1714700892997.png", record_pos=(0.422, -0.046), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714700892997.png", record_pos=(0.422, -0.046), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10016]")
        
        case "10021":
            while not exists(Template(r"tpl1714701153966.png", record_pos=(-0.021, 0.103), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714701153966.png", record_pos=(-0.021, 0.103), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10021]")
        
        case "10022":
            while not exists(Template(r"tpl1714701190630.png", record_pos=(0.26, 0.113), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714701190630.png", record_pos=(0.26, 0.113), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10022]")
        
        case "10023":
            while not exists(Template(r"tpl1714701225000.png", record_pos=(0.059, -0.028), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714701225000.png", record_pos=(0.059, -0.028), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10023]")
        
        case "10038":
            while not exists(Template(r"tpl1714701612737.png", record_pos=(0.237, 0.07), resolution=(2400, 1080))):
                swipe((0.8, 0.30), (0.3, 0.30), 0.6)
            touch(Template(r"tpl1714701612737.png", record_pos=(0.237, 0.07), resolution=(2400, 1080)))
            wait(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))# 確認進入遊戲
            print("進入遊戲[10038]")
            while exists(Template(r"tpl1715239401696.png", record_pos=(-0.001, 0.181), resolution=(2400, 1080))):# 檢查廣告彈窗
                touch((1200,960))

# Spin
def Spin():
    touch(Template(r"tpl1717407302456.png", record_pos=(0.321, 0.191), resolution=(2400, 1080)))
    sleep(0.2)
    touch((1980, 1000))

def Spin_New(gamecode):
    triggerType = TriggerCheck(gamecode)
    Trigger(gamecode, triggerType)
        
        

# 回到大廳
def Leave():
    while exists(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080))):
        try:
            touch(Template(r"tpl1714638613923.png", record_pos=(-0.357, -0.203), resolution=(2400, 1080)))
        except:
            pass      
    try:
        wait(Template(r"tpl1714037407130.png", record_pos=(-0.27, -0.065), resolution=(2400, 1080)),timeout=5)
        touch(Template(r"tpl1714037420151.png", record_pos=(0.371, -0.195), resolution=(2400, 1080)))
        sleep(1)
    except:
        print('*****找不到[首儲]視窗')

# 遊戲測試(調整spin次數)
def GameTest(times):
    while not exists(Template(r"tpl1714121514055.png", record_pos=(0.32, 0.193), resolution=(2400, 1080))):# 確認進到遊戲
        sleep(2)
    for _ in range(times):
        Spin()
        while not exists(Template(r"tpl1714125010345.png", record_pos=(0.213, 0.201), resolution=(2400, 1080))):# 確認進到FG/BG
            touch((1200, 830))
    Leave()

def AllGameTest(times=Config.SpinTime, GameCode=Config.GameCode):
    for gamecode in GameCode:
        ClickGameNew(gamecode)
        GameTest(times)





