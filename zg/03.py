
i = 1
j = 3
print(i+j) # 运算

a = 123
print (id(a))
a = 789
print (id(a)) #标签重新

h = 123456
b = 123456
print( id(h)  , id(b)) #一条数据包含多个标签


stra = "我的帝！"
print  (stra)

DayPerWeek = 7
HoursPerDay = 24
MinutePerHour = 60
sum = DayPerWeek * HoursPerDay * MinutePerHour
print(sum)
HoursPerDay = 26
sum1 = DayPerWeek * HoursPerDay * MinutePerHour
print( sum1)
print("一个月 %d 小时" %(sum1))

print("{:,}".format(123456))#输出1234,56
print("{a:w^8}".format(a="8"))
