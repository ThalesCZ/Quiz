#Exercício 11

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

lista_numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
primos_encontrados = find_primes(lista_numeros)
print("Números primos na lista:", primos_encontrados)
