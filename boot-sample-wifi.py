# This file is executed on every boot (including wake-boot from deepsleep)
# Written by Vince Mulhollon for the micropython-freebsd github project

SSID = 'YOUR-WIFI-NAME'
WIFIPASSWORD = 'YOUR-WIFI-PASSWORD'

import esp
esp.osdebug(None)
import gc
import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
if ap_if.active():
     ap_if.active(False)
if not sta_if.isconnected():
     print('Connecting to network')
     sta_if.active(True)
     sta_if.connect(SSID,WIFIPASSWORD)
     while not sta_if.isconnected():
          pass
print('Network configuration:', sta_if.ifconfig())
gc.collect()

