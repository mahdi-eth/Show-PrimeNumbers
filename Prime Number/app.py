def primer_check(n):
    prime_state = True
    for i in range(2,n+1):
        prime_state = True
        if i == 2:
            print(2)
            continue
        for j in range(2,i):
            if i % j == 0:
                prime_state = False
                break
        if prime_state: print(i)

n = int(input("Enter a number to see the prime numbers up to that number : "))
primer_check(n)

