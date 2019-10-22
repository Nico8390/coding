# 密碼重試程式

# 設 password = 'a123456'
# 最多輸入3次密碼


password = 'a123456'

i = 1
while i <= 3 :
	pw = input('請輸入密碼：')
	if pw == password :
		print('登入成功')
		break
	else :
		print('密碼錯誤！！！')
		if i < 3 :
			print('你還有', 3 - i  ,'次機會')
		else :
			print('你己使用了3次機會！')
			break
	i = i + 1
