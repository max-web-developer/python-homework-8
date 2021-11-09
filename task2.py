# figure=input('Enter name of figure: ')
# def Sfigure():
    # if figure == 'circle':
    #     r=int(input('enter radius:'))
    #     S=3.14*r**2
    #     print(S)
    # if figure == 'square':
    #     a=int(input('Enter a: '))
    #     S2=a*4
    #     print (S2)
    # if figure == 'rectangle':
#         a2=int(input('Enter a: '))
#         b2=int(input('Enter b: '))
#         S3=a2*b2
#         print(S3)
#     if figure == 'right triangle':
#         a3=int(input('enter a: '))
#         b3=int(input('enter b: '))
#         c3=int(input('enter c: '))
#         S4=a3*b3/0.5  
#         print(S4)  
# Sfigure()

print('select one of the list: \n1- square \n2- rihgt triangle \n3- cicumference \n4- rectangle')
fig=int(input('enter the  number of listed figures: '))

def caclAreaOfcircumference(radius):
    from math import pi
    return pi * radius *radius
if fig == 3:
    print('You have slected circumference')
    r=int(input('enter radius of circumference: '))
    print(caclAreaOfcircumference(r))

def calcAreaOfsquare(side):
    return side*4
if fig == 1:
    print('You have slected square')
    a=int(input('enter side of square:'))
    print(calcAreaOfsquare(a))

def calcAreofrectangle(side1,side2,side3):
    return side1 * side2 * side3
if fig == 4:
    print('You have selected rectangle')
    s1=int(input('Enter side1:'))
    s2=int(input('Enter side2:'))
    s3=int(input('Enter side2:'))
    print(calcAreofrectangle(s1,s2,s3))

def calcAreaOfright_rectangle(a1,b1):
    return a1 * b1 * 0.5
if fig == 2:
    print('You have selcted right rectangle')
    sd1=int(input('Enter sd1: '))
    sd2=int(input('Enter sd2: '))
    print(calcAreaOfright_rectangle(sd1,sd2))

# sum=0
# for n in range(0,5,1):
#     sum += 3 * n
# print(sum)