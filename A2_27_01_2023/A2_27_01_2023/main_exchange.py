n = int(input("Digite n \n"))
A = [0]*n
for i in range(n):
    A[i] = int(input("Digite valor de A["+str(i)+"] \n"))

print("Antes de intercambio")
for i in range(n):
    print(A[i], end = " ")
print("")
### parte importante
j = n-1
for i in range(n//2):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    j = j - 1

print("despues de intercambio")
for i in range(n):
    print(A[i], end = " ")
print("")