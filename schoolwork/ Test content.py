#凯撒密码
str = input()
for i in str:
    if'a'<=i<='z':
        print(chr(ord('a')+(ord(i)-ord('a')+3)%26),end='')
    else:
        print(i,end='')