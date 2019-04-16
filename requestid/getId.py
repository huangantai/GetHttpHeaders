from mitmproxy import ctx
from mitmproxy import http
from mitmproxy.proxy.protocol import Layer
import winreg
import os
from mitmproxy.connections import ServerConnection

class RequestId:
    def running(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",access=winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key,"ProxyEnable", 0,winreg.REG_DWORD,1)
        winreg.SetValueEx(key, "ProxyServer", 0,winreg.REG_SZ,"127.0.0.1:8080")
        a=os.path.dirname(sys.argv[0])
        b=os.path.join(a,"ips.txt")
        with open(b) as ips:
            iplist=ips.readlines()
            ipstring=';'.join(iplist)
            winreg.SetValueEx(key, "ProxyOverride", 0,winreg.REG_SZ,ipstring)

    def serverdisconnect(self, conn:ServerConnection):
        ctx.log.info("--"*30)

    def response(self,flow: http.HTTPFlow) -> None:
      #  for a in flow.request.headers:
      #      print("{}:{}".format(a,flow.request.headers[a]))
        if "requestId" in flow.response.headers:
            ctx.log.info("url:{}{}".format(flow.request.host,flow.request.path))
            ctx.log.warn("requestId:{}".format(flow.response.headers["requestId"]))

#    def done(self):
#        donekey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
#                                 r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
#                                 access=winreg.KEY_ALL_ACCESS)
#        winreg.SetValueEx(donekey, "ProxyEnable", 0, winreg.REG_DWORD, 0)

addons = [
    RequestId()
]

import signal
import sys
import win32api
def on_close(sig):
    donekey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                             access=winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(donekey, "ProxyEnable", 0, winreg.REG_DWORD, 0)
win32api.SetConsoleCtrlHandler(on_close, True)
