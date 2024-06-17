# -*- encoding=utf8 -*-
# ---------------------------------以下為預設
import sys
sys.path.append('/Users/hs059/GitHub/Airtest_Betrnk/LobbyTest.air')
from airtest.core.api import *
from TestCase import *

# auto_setup(__file__)

lobby = EventManager()
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

# while True:
#     threads = []
#     for template, event_name in event_templates:
#         thread = threading.Thread(target=CheakPopupNew, args=(template, event_name))
#         thread.start()
#         threads.append(thread)

#     # 等待所有線程完成
#     for thread in threads:
#         thread.join()

Config = {
    '溫馨提醒':'vip以外欄位記得+ threshold=1, ',
    'vip':Template(r"tpl1718344862706.png", record_pos=(-0.105, -0.084), resolution=(2400, 1080)),
    'name':Template(r"tpl1718344899282.png",threshold=0.9,  record_pos=(-0.183, 0.061), resolution=(2400, 1080)),
    'playerid':Template(r"tpl1718344932948.png",threshold=0.9,  record_pos=(-0.157, 0.099), resolution=(2400, 1080)),
    'club':Template(r"tpl1718344944144.png",threshold=0.9,  record_pos=(-0.176, 0.138), resolution=(2400, 1080)),
    'summary':Template(r"tpl1718344956453.png",threshold=1,  record_pos=(0.133, 0.035), resolution=(2400, 1080))
}
    



# touch((0.418,0.175)) # 點信箱
# touch((0.567,0.175)) # 點榮譽榜
# touch((0.698,0.175)) # 點好友
# touch((0.272,0.175)) # 點會員檔案


touch((0.429,0.061)) # 點頭像
CheckIMG(Config['vip'], 'VIP')
CheckIMG(Config['name'], '暱稱')
sleep(1)
touch(Template(r"tpl1718267306989.png",record_pos=(-0.057, 0.062), resolution=(2400, 1080)))
CheckIMG(Template(r"tpl1718261072430.png", threshold=0.5, record_pos=(-0.138, 0.063), resolution=(2400, 1080)), '暱稱複製')
CheckIMG(Config['playerid'], '玩家ID')
sleep(1)
touch(Template(r"tpl1718267314833.png", record_pos=(-0.055, 0.1), resolution=(2400, 1080)))
CheckIMG(Template(r"tpl1718261143343.png", threshold=0.5, record_pos=(-0.135, 0.1), resolution=(2400, 1080)), '玩家ID複製')
CheckIMG(Config['club'], '俱樂部')
ChangeSummary()
CheckIMG(Config['summary'], '玩家簡介')
touch(Template(r"tpl1718356811668.png", record_pos=(0.195, 0.127), resolution=(2400, 1080)))
CheckIMG(Template(r"tpl1718356867216.png", record_pos=(0.005, -0.0), resolution=(2400, 1080)), '黑名單')
touch(Template(r"tpl1718357314833.png", record_pos=(0.232, -0.143), resolution=(2400, 1080)))
touch(Template(r"tpl1718357047798.png", record_pos=(0.258, 0.128), resolution=(2400, 1080)))
CheckIMG(Template(r"tpl1718357120459.png", record_pos=(-0.173, -0.024), resolution=(2400, 1080)), '贈禮')
close()
sleep(1)
touch((0.429,0.061)) # 點頭像
touch(Template(r"tpl1718346117440.png", record_pos=(0.257, -0.087), resolution=(2400, 1080)))
CheckIMG(Template(r"tpl1718346175675.png", record_pos=(-0.0, 0.005), resolution=(2400, 1080)), '商店')
close()
close()
print('done')







