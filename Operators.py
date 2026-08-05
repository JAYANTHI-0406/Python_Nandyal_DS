#1.Arithmetic Operators

a=5
b=3
print(a+b) #1.Addition
print(a-b) #2.Subtraction
print(a/b) #3.Division
print(a*b) #4.Multiplication
print(a%b) #5.Modulus(remainder)
print(a//b) #6.Floor Division(Quotient)
print(a**b) #7.Exponent(power)

#2.Assignment Operators

a=10
print(a) 
#1.Assignment
a=5
b=3
#2.Addition Assignment
a += b    #a=a+b
print(a)
#3.Subtraction Assignment
a -= b     #a=a-b
print(a)
#4.Multiplication Assignment
a *= b    #a=a*b
print(a)
#5.Division Assignment
a /= b    #a=a/b
print(a)
#6.Floor Assignment
a //= b   #a=a//b
print(a)
#7.Modulus Assignment
a %= b   #a=a%b
print(a)

#3.Comparision (Relational)Operators

a=10
b=10
#1.Equal to 
print(a==b) 

a=10
b=20
#2.Not Equal to
print(a!=b)
#3.Grater Than
print(a>b)
#4.less Than
print(a<b)
#5.Greater Than or Equal to
print(a>=b)
#6.Less Than or Equal to
print(a<=b)

#4.Logical Operators

a=10
#and
print(a>5 and a<20)
#or
print(a>15 or a<25)
#not
print(not(a>20))
#Ex.
a=10
b=15
print(a<b and b>a) #Both conditions must be True
print(a>b or b>a) # atleast one condition must be True
print(not(a<b)) #reverse to given condition

#5.Bitwise Operators

a=6
b=4
# 1.&(Bitwise AND)
                      #0110
                      #0100
                      #--------
print(a&b)     #0100=4

#2.|(Bitwise OR)
                       
                     #0110
                     #0100
                     #--------
print(a|b)     #0110 =6

#3.^(Bitwise XOR)
                     #0110
                     #0100
                     #--------
print(a^b)     #0010

#4.~(Bitwisr NOT)
# ~n=-(n+1))
print(~6)
#<<(Left shift)
print(6<<4)
#>>(Right shift)
print(6>>4)

#6.Membership Operator
fruits=["apple","banana","mango"]
#in--->present
print("apple" in (fruits))
#not in----->not present
print("banana" not in (fruits))

#7.Identity Operator
a=[10,20]
b=a
#is 
print(a is b)
#is not
print(a is not b)
a=[10,30]
b=[10,30]
print(a is not b)