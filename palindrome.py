a=input("enter a number")
n=a
s=0
while a!=0 :
     m=a%10
     s=(s*10)+m
     a=a/10
if n==s :
  print("palindrome")
else:
  print("not palindrome")
