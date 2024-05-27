__author__ = "hs059"

from airtest.core.api import *

auto_setup(__file__)
def spin():
    touch(Template(r"tpl1715331022977.png", record_pos=(0.323, 0.195), resolution=(2400, 1080)))
    sleep(3.0)
    touch((1219,525))
    touch(Template(r"tpl1715331105638.png", record_pos=(0.274, 0.035), resolution=(2400, 1080)))
    touch(Template(r"tpl1715328520762.png", record_pos=(-0.001, 0.12), resolution=(2400, 1080)))
    sleep(3.0)
    touch((1219,525))

    

for x in range(100):
    spin()
    print(x)