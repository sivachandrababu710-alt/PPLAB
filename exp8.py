vowels="aeiouAEIOU"
word=input('Enter a word: ')
a=""
flag=0
for char in word:
    if char in vowels:
        a=char;
        flag=1
        break
if(flag==1):
    print('Given string contains vowel',a)
else:
    print('Given string not contains vowel')

