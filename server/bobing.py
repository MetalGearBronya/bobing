
def roll():
	spin_duration = [1.5, 2, 2.5, 3, 3.5]
	obj = {"num" : [random.randint(1, 6) for i in range(6)], "timeout" : [int(random.choice(spin_duration) * 1000) for i in range(6)]}
	return obj

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
