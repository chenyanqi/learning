#输入一个字符串, 返回倒序排列的结果 如: abcdef, 返回 fedcba
text = 'abcdef'
#1、字符串本身的翻转
print(text[::-1])
#2、利用列表的reversed函数，在格式化
print(''.join(reversed(text)))
#3、新建一个列表，从后往前取
def string_reverse3(text='abcdef'):
    new_text = []
    for i in range(1,len(text)+1):
        new_text.append(text[-i])
    return ''.join(new_text)
print(string_reverse3())

#4、利用双向列表deque中的extendleft函数
from collections import deque
def string_reverse4(text='abcdef'):
    d = deque()
    d.extendleft(text)
    return ''.join(d)
print(string_reverse4())
#5、递归：
import sys
sys.setrecursionlimit(10000)
def string_reverse5(text='abcdef'):
    if len(text)<=1:
        return text
    else:
        return string_reverse5(text[1:]+text[0])
print(string_reverse5())
