from websocket_server import WebsocketServer
import random
import json


symbol = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

def to_symbol(num_list):
	# num_dict = {}
	# for num in num_list:
	# 	if num not in num_dict:
	# 		num_dict[num] = 1
	# 	else:
	# 		num_dict[num] += 1

	# if num_dict[4] == 4 and num_dict[1] == 2:
	# 	return symbol[4] * 4 + symbol[1] * 2, '状元插金花'
	#
	# for num in [2, 3, 5, 6]:
	# 	if num_dict[num] == 6:
	# 		return symbol[num] * 6, '六勃黑'

	string = ''
	for num in sorted(num_list):
		string += symbol[num] + ' '
	return string, '无'


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
		spin_duration = [1.5, 2, 2.5, 3, 3.5]
		obj = {"num" : [random.randint(1, 6) for i in range(6)], "timeout" : [int(random.choice(spin_duration) * 1000) for i in range(6)]}
		server.send_message_to_all(json.dumps(obj).encode('utf-8'))
		delay = max(obj['timeout']) / 1000
		import time
		time.sleep(delay)
		name = client['name']
		result, reward = to_symbol(obj['num'])
		server.send_message_to_all(f'{name}掷出了{result}')
		# for client in server.clients:
		# 	if client.name = name:
        #     	self._unicast(client, msg)


PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
