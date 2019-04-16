# GetHttpHeaders

通过getId.py来过滤浏览器请求，可以通过getId.py自定义处理逻辑，修改后的脚本实时运行不用重启mitmproxy，浏览器事件流程：https://github.com/mitmproxy/mitmproxy/blob/master/examples/addons/events.py

启动mitmproxy时将浏览器安装代理，关闭时浏览器删除代理，ips.txt中定义不需要经过代理的域名.
