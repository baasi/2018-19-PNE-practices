a, b= 0, 1
n = int(input("Type the number you want to sum from the fibonacci series: "))
suma = 0
for i in range(n):
    print(a, end=' ')
    suma += a
    a, b=b, a+b


print(suma)
