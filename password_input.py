x = 3
while True:
	keyin = input('請輸入密碼: ')
	if keyin == 'a123456':
		print('登入成功')
		break
	else:
		x = x - 1
		print('密碼錯誤! 還有', x, '次機會')
		if x == 0:
			break
