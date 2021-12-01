from webapp import application
from wsgiref.simple_server import make_server

httpd = make_server('', 8000, application)
print("on 8000...")
# 将持续提供服务，直至进程被结束
httpd.serve_forever()
