print("Equation should be in a form : ax\u00b2+bx+c=0")
a = eval(input("enter the value of a : "))
b = eval(input("enter the value of b : "))
c = eval(input("enter the value of c : "))
d = b**2 - 4*a*c
x1 = (b*-1 + (d)**(1/2.0))/(2*a)
x2 = (b*-1 - (d)**(1/2.0))/(2*a) 
if d >= 0:
	print("Answer : \n x1 = %.2f \n x2 = %.2f" %(x1,x2))
else:
	print("Answer : \n x1 = %.2f + %.2fj \n x2 = %.2f + %.2fj" %(x1.real, x1.imag, x2.real, x2.imag))