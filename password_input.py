password = 'a123456'
x = 3 #剩餘輸入次數

while x > 0:
	x = x - 1
	keyin = input('請輸入密碼: ')
	if keyin == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('帳號被鎖了')
		