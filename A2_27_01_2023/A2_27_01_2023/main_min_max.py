n = int(input("Digite n \n"))
A = [0]*n
for i in range(n):
    A[i] = int(input("Digite valor de A["+str(i)+"] \n"))

menor = A[0]
mayor = A[0]
for i in range(1,n):
    print("A[i] es",A[i])
    print("en ",i,"menor es",menor)
    print("en ",i,"mayor es",mayor)
    if(A[i] < menor):
        # encontre un menor que es mas pequeño que el que 
        # tengo almacenado en la variable "menor" 
        menor = A[i]
    else:
        if (A[i] > mayor):
            # encontre un mayor que es mas grande que el que 
            # tengo almacenado en la variable "mayor"
            mayor = A[i]


print("el menor es", menor)
print("el mayor es", mayor)