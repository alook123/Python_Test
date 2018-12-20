
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表

print(list[0:-1])


#!/usr/bin/python3
 
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
 
# print(a)
 
# print(a - b)     # a 和 b 的差集
 
# print(a | b)     # a 和 b 的并集
 
# print(a & b)     # a 和 b 的交集
 
# print(a ^ b)     # a 和 b 中不同时存在的元素


c=set("abc")
d=set("bcd")

print(d-c)
print(c|d)
print(c&d)
print(c^d)


dict1 = {'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
for k,v in dict1.items():
    print(k,":",v)