from functools import reduce
# 将一个list中的所有字符串改为首字母大写的格式
def Capitalize(s):
    return str.capitalize(s)
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(Capitalize, L1))
print(L2)

# 计算list的乘积
def prod(L):
    def cheng(a,b):
        return a*b
    return reduce(cheng,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

def s2f(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def s2n(s):
        print(s)
        return digits[s]
    s1,s2=s.split('.')
    return reduce(lambda x,y:x*10+y,map(s2n,s1))+reduce(lambda x,y:x*0.1+y,map(s2n,s2[::-1]))*0.1
print(s2f('111.234'))
