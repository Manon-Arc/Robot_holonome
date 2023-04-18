request_str = "b'POST / HTTP/1.1\r\nHost: 192.168.4.1\r\nConnection: keep-alive\r\nContent-Length: 10\r\nUser-Agent: Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36\r\nContent-type: application/x-www-form-urlencoded\r\nAccept: */*\r\nOrigin: http://192.168.4.1\r\nReferer: http://192.168.4.1/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\njoystick=g'"
if "joystick=g" in request_str:
     print("ok")
else :
     print("no action")