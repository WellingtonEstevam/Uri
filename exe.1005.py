# Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, 
# considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that 
# each grade can go from 0 to 10.0, always with one decimal place.

# Read three values (variables A, B and C),
A = float(input())
B = float(input())
C = float(input())

MEDIA = (A*2.0 + B*3.0 + C*5.0)/(2.0+3.0+5.0)

print("MEDIA = %.1f" %MEDIA)
