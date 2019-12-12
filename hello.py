#!C:\Python37\python.exe
#-*- coding: utf-8 -*-

import cgi
# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로, cgitb.enable() 할 경우 런타임 에러를 웹브라우저로 전송한다
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우 웹서버는 클라이언트에게 HTTP 응답코드 500을 전송한다
import cgitb
cgitb.enable()

# ===================================

print("Content-type: text/html;charset=utf-8", end="\n\n")

print("""<!DOCTYPE html>
<html>
    <head>
        <title>Python CGI Test</title>
    </head>
    <body>
        <h1>Hello, Python CGI!</h1>
        <p>First CGI program</P>
    </body>
</html>""")