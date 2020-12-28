#!/usr/local/bin/node
const crypto = require('crypto');
const magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';
const secWebSocketKey = process.argv[2]

if (!secWebSocketKey) {
	console.log('Usage: ./secWebSocketKey_gen.js ${secWebSocketKey}')
	return
}

let secWebSocketAccept = crypto.createHash('sha1')
	.update(secWebSocketKey + magic)
	.digest('base64');

console.log(secWebSocketAccept);
