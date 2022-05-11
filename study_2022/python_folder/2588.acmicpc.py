a = input()
b = input()
a = int(a)
b = int(b)
result = a * b
while int(b/10) != 0 or int(b%10) != 0 :
    print(a*(b%10))
    b = int(b/10)

print(result)