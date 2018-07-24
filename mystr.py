'''
week="星期一星期二星期三星期四星期五星期六星期日"
i =int( input("请输入一个1～7之间的数字"))
s=(i-1)*3
if 0<i<8:
	
	s1=week[s:s+3]
	print(s1)
else:
	print("输入的数字有误")

print(week[s:s+3])
'''


s = input("请输入一个字符串")
s1= ""
l = len(s)
i = 0
while i < l:
	m = ord(s[i])
	if 65<=  m <=90:
		m += 32
		s1+=chr(m)
	elif 97 <= m <= 122:
		m -= 32
		s1 += chr(m)
	else:
		s1+= s[i]
	i += 1 
print(s1)







