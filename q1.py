def inFibonacci(num):
    if num < 0:
        return False
    
    if num == 0 or num == 1:
        return True
    
    fib1, fib2 = 0, 1

    while num > fib2:
        fib1, fib2 = fib2, fib1 + fib2

    return num == fib2

try:
    num = int(input("Informe um numero inteiro\n"))

    if inFibonacci(num):
        print("Este numero PERTENCE a sequencia de fibonacci")
    else:
        print("Este numero NAO pertence a sequencia de fibonacci")

except:
    print("Insira um numero valido")