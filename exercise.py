weight = input('請輸入您的體重')
weight = int(weight)
height = input('請輸入您的身高')
height = int(height)
height = height / 100
BMI = weight / (height * height)
print('您的 BMI 值為:', BMI)
if BMI < 18.5:
	print('體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常範圍')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')

