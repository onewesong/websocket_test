# websocket 测试

工具
==

## 服务端
### python版
`websockets_server.py`

## 客户端
### python版

`websockets_client.py ws://localhost:8765`

### js版
```
var ws = new WebSocket('ws://127.1:8765')
ws.onmessage = function(evt) {
  console.log( "< " + evt.data);
}
ws.send('1')
```

### rust版
`websocat ws://127.1:8765`

### curl
```
curl --include \
    --no-buffer \
    --header "Connection: Upgrade" \
    --header "Upgrade: websocket" \
    --header "Host: 127.1:8765" \
    --header "Sec-WebSocket-Key: 9DK5Qa8Nb//lGsRttQVZGw==" \
    --header "Sec-WebSocket-Version: 13" \
    http://127.1:8765/
```
ps. 只能测试到服务端响应101切换协议，无法使用websocket协议继续通信

报文
==
## 抓包
```
tshark -i lo  -w websocket.pcap port 8765
```
追踪tcp流
```
GET / HTTP/1.1
Host: 127.0.0.1:8765
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: 9DK5Qa8Nb//lGsRttQVZGw==

HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: KA+iNH73kJ2gjF1BePnHgJVT0DY=
Date: Mon, 28 Dec 2020 08:18:02 GMT
Server: Python/3.8 websockets/8.1

..........1
```

`Connection: Upgrade`: 表示要升级协议

`Upgrade: websocket`：表示要升级到websocket协议。

`Sec-WebSocket-Version: 13`：表示websocket的版本。如果服务端不支持该版本，需要返回一个Sec-WebSocket-Versionheader，里面包含服务端支持的版本号。

`Sec-WebSocket-Key`：与后面服务端响应首部的Sec-WebSocket-Accept是配套的，提供基本的防护，比如恶意的连接，或者无意的连接。

> Sec-WebSocket-Accept的计算
1. 将Sec-WebSocket-Key跟258EAFA5-E914-47DA-95CA-C5AB0DC85B11拼接。
2. 通过SHA1计算出摘要，并转成base64字符串。
- 验证:
``` bash
❯ ./secWebSocketKey_gen.js 9DK5Qa8Nb//lGsRttQVZGw==
KA+iNH73kJ2gjF1BePnHgJVT0DY=
```

相关资料
==
- https://websockets.readthedocs.io/en/stable/intro.html
- https://www.ruanyifeng.com/blog/2017/05/websocket.html
- https://github.com/vi/websocat
- https://www.cnblogs.com/chyingp/p/websocket-deep-in.html