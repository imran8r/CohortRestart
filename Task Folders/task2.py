a=float(input('student 1 CGPA:'))
b=float(input('Student 2 CGPA:'))
c=float(input('Student 3 CGPA:'))


if a>4.00 or a<2.00 or b<2.00 or c<2.00 or b>4.00 or c>4.00 :
    print ('Please put valid CGPA')
elif a>b and a>c:
    print('Student 1 has the higest CGPA')
elif b>c and b>a:
    print("Student 2 has the highest CGPA")
else:
    print ('Student 3 has the highest CGPA')

avg= (a+b+c)/3
if a<4.00 or a>2.00 or b<4.00 or b>2.00 or c<4.00 or c>2.00:
    print ('Average CGPA is ',avg)