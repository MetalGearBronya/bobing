from websocket_server import WebsocketServer
import random
import json
from bobing import roll, to_symbol
import time

# Called for every client connecting (after handshake)
def new_client(client, server):
	print(client)
	print("New client connected and was given id %d" % client['id'])
	name = client['name']
	server.send_message_to_all(f'{name}已经加入游戏')


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))
	if message == 'roll':
		obj = roll()
		server.send_message_to_all(json.dumps(obj).encode('utf-8'))
		delay = max(obj['timeout']) / 1000
		time.sleep(delay)
		
		name = client['name']
		result, reward = to_symbol(obj['num'])
		server.send_message_to_all(f'{name}掷出了{result}')


PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
