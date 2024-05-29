# ---------------------------------以下為預設
# -*- encoding=utf8 -*-
import sys
sys.path.append('/Users/hs059/GitHub/Airtest_Betrnk/GameTest.air')
from airtest.core.api import *
from TestCase import *
import Config
import threading


event_templates = [ # 登入彈窗
    (Template(r"tpl1714037407130.png", record_pos=(-0.27, -0.065), resolution=(2400, 1080)), '首儲'),
    (Template(r"tpl1714037742771.png", record_pos=(0.015, 0.042), resolution=(2400, 1080)), '綁定手機'),
    (Template(r"tpl1714037630865.png", record_pos=(-0.234, -0.152), resolution=(2400, 1080)), '最新消息'),
    (Template(r"tpl1714037912623.png", record_pos=(-0.028, -0.182), resolution=(2400, 1080)), '任務'),
    (Template(r"tpl1714037798354.png", record_pos=(-0.001, 0.155), resolution=(2400, 1080)), '遊戲彈窗'),
    (Template(r"tpl1716516876076.png", record_pos=(-0.025, 0.185), resolution=(2400, 1080)), '七日簽到'),
    (Template(r"tpl1716444686691.png", record_pos=(-0.033, 0.014), resolution=(2400, 1080)), '回到大廳')
]
# 打開監聽事件
lobby.on('首儲',ClosePopup)
lobby.on('綁定手機',ClosePopup)
lobby.on('最新消息',ClosePopup)
lobby.on('任務',ClosePopup)
lobby.on('遊戲彈窗',ClosePopup)
lobby.on('七日簽到',ClosePopup)
lobby.on('回到大廳',AllGameTest)

# 檢查彈窗

CheakPopupNew(Template(r"tpl1716444686691.png", record_pos=(-0.033, 0.014), resolution=(2400, 1080)), '回到大廳')
# while True:
#     threads = []
#     for template, event_name in event_templates:
#         thread = threading.Thread(target=CheakPopupNew, args=(template, event_name))
#         thread.start()
#         threads.append(thread)

#     # 等待所有線程完成
#     for thread in threads:
#         thread.join()































