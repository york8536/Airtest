from airtest.core.api import *
from Events import EventManager

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

def close():
    try:
        touch(Template(r"tpl1718346290731.png", record_pos=(0.36, -0.154), resolution=(2400, 1080)))
        touch(Template(r"tpl1718346353916.png", record_pos=(0.371, -0.198), resolution=(2400, 1080)))
    except:
        pass

def ChangeHead():
    touch(Template(r"tpl1718269809498.png", record_pos=(-0.13, 0.014), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269879679.png", record_pos=(0.07, -0.07), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269891222.png", record_pos=(-0.175, 0.135), resolution=(2400, 1080)))
    exists(Template(r"tpl1718269879679.png", record_pos=(0.07, -0.07), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269809498.png", record_pos=(-0.13, 0.014), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269985541.png", record_pos=(0.133, -0.07), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269891222.png", record_pos=(-0.175, 0.135), resolution=(2400, 1080)))
    exists(Template(r"tpl1718269985541.png", record_pos=(0.133, -0.07), resolution=(2400, 1080)))

def CheckIMG(img, title):
    if exists(img):
        print(title+ '-ok')
    else:
        print(title+ '-error')

def ChangeHead():
    touch(Template(r"tpl1718269809498.png", record_pos=(-0.13, 0.014), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269879679.png", record_pos=(0.07, -0.07), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269891222.png", record_pos=(-0.175, 0.135), resolution=(2400, 1080)))
    CheckIMG(Template(r"tpl1718269879679.png", record_pos=(0.07, -0.07), resolution=(2400, 1080)), '頭貼更換')
    touch(Template(r"tpl1718269809498.png", record_pos=(-0.13, 0.014), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269985541.png", record_pos=(0.133, -0.07), resolution=(2400, 1080)))
    touch(Template(r"tpl1718269891222.png", record_pos=(-0.175, 0.135), resolution=(2400, 1080)))
    CheckIMG(Template(r"tpl1718269985541.png", record_pos=(0.133, -0.07), resolution=(2400, 1080)), '換回預設')

def ChangeSummary():
    touch(Template(r"tpl1718272143476.png", record_pos=(0.27, 0.084), resolution=(2400, 1080)))
    touch(Template(r"tpl1718346843904.png", record_pos=(0.11, 0.065), resolution=(2400, 1080)))
    touch(Template(r"tpl1718347277335.png", record_pos=(0.128, 0.195), resolution=(2400, 1080)), duration=1.8)
    touch(Template(r"tpl1718347301267.png", record_pos=(0.139, 0.133), resolution=(2400, 1080)))
    touch(Template(r"tpl1718352592813.png", record_pos=(-0.18, 0.128), resolution=(2400, 1080)))
    touch(Template(r"tpl1718347277335.png", record_pos=(0.128, 0.195), resolution=(2400, 1080)), duration=1.8)
    touch(Template(r"tpl1718347301267.png", record_pos=(0.139, 0.133), resolution=(2400, 1080)))
    touch(Template(r"tpl1718347320966.png", record_pos=(0.411, 0.033), resolution=(2400, 1080)))
    text("Hello")
    touch(Template(r"tpl1718352444278.png", record_pos=(0.418, 0.17), resolution=(2400, 1080)))
    touch(Template(r"tpl1718352460463.png", record_pos=(-0.172, 0.133), resolution=(2400, 1080)))
    CheckIMG(Template(r"tpl1718353166556.png", record_pos=(0.133, 0.035), resolution=(2400, 1080)), '編輯簡介')
    touch(Template(r"tpl1718272143476.png", record_pos=(0.27, 0.084), resolution=(2400, 1080)))
    touch(Template(r"tpl1718353489163.png", record_pos=(0.009, 0.068), resolution=(2400, 1080)))
    touch(Template(r"tpl1718353514356.png", record_pos=(-0.404, 0.193), resolution=(2400, 1080)), duration=1.8)
    touch(Template(r"tpl1718347320966.png", record_pos=(0.411, 0.033), resolution=(2400, 1080)))
    touch(Template(r"tpl1718353567989.png", record_pos=(-0.356, 0.193), resolution=(2400, 1080)), duration=1.8)
    touch(Template(r"tpl1718352623374.png", record_pos=(-0.388, 0.123), resolution=(2400, 1080)))
    touch(Template(r"tpl1718347320966.png", record_pos=(0.411, 0.033), resolution=(2400, 1080)))
    touch(Template(r"tpl1718352444278.png", record_pos=(0.418, 0.17), resolution=(2400, 1080)))
    touch(Template(r"tpl1718352460463.png", record_pos=(-0.172, 0.133), resolution=(2400, 1080)))
    

        





