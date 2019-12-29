
'''
输入一个字符串，统计英文字母，空格，数字和其他字符的个数
'''

s = str(input('str:'))
letter,blank,number,other = 0,0,0,0


for i in s:
    if 'z' >=  i >= 'a' or 'Z' >=  i >= 'A':
        letter+=1
    elif i == ' ':
        blank+=1
    elif '9' >=  i >= '0':
        number+=1
    else:
        other+=1
print(letter,blank,number,other)