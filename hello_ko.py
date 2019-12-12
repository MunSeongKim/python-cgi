#!C:\Python37\python.exe
#-*- coding: utf-8 -*-
# 한글 지원을 위한 모듈 추가
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로, cgitb.enable() 할 경우 런타임 에러를 웹브라우저로 전송한다
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우 웹서버는 클라이언트에게 HTTP 응답코드 500을 전송한다
import cgitb
cgitb.enable()

# 클라이언트 응답 함수 정의
def response(body):
    header = "Content-type: text/html;charset=utf-8"
    print("%s\n\n%s" % (header, body))

# ===================================

body = '''<!DOCTYPE html>
<html>
    <head>
        <title>CGI 테스트</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>안녕하세요.</h1>
        <p>CGI를 이용한 웹 프로그램입니다.</p>
        <p>한글을 출력해 보아요!</p>
    </body>
    </html>'''

response(body)
