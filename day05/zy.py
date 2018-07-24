i = eval(input("请输入PM2.5的值:"))
if i>75:
	print("重度污染,提示市民不宜出行")
elif 35<i<=75:
	print("空气良好,适当户外活动")
else:
	print("空气质量优，赶紧出来嗨")
print("空气{}污染".format("是" if i > 75 else "没有"))
