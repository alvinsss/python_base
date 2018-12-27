str1 = "abc"
print(str1[:])
print(str1.__len__())
str2 = 'alvin123'
print(str1 + str2)
print( "#"* 40)
print( 'c' in str1 )
print ('c')
print(max(str2))
print(min(str2))
print(id(str1))
str1= "ab3"
print(id(str1))

userinfo = "alvin 30 male"
print(userinfo[:5])
userinfo = "milo 30 male"
print(userinfo[:5])


t = ("alvin",30,"male")
print(t[0])
t1 = ()
t2 = (2,) #一定有逗号
t[1] = 31 #

namge,age,gender = t
print(t)