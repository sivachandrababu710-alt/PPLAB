str1=input('Enter first string: ')
str2=input('Enter second string: ')
if len(str1)!=len(str2):
    print('Strings with different lengths')
else:
    for i in range(len(str1)):
        print(str1[i],end="")
        print(str2[i],end="")
