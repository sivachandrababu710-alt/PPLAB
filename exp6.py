import random
r=random.randint(1,10)
n=int(input('Enter your number between 1 and 10  '))
print('The random number is ',r)
if(r==n):
   print('Your guess is right') 
else:
    print('Your guess is  wrong')
