def filter_prime(list):
    prime_numbers = []
    for i in list:
        x = isprime(i)
        if x == True:
            prime_numbers.append(i)
    print (prime_numbers)

def isprime(num):
    if num < 2:
        return False
    for i in range (2, int(0.5 *num + 1)):
        if num % i == 0:
            return False
    return True



plist = []
while True:
    number = input("Enter the list of numbers(enter 'q' to stop): ")
    if number == 'q': 
        break

    try:
        number = int(number)
        plist.append(number)
        print ("List contains: ", plist)
    except ValueError:
        print ("Enter the list of numbers(enter 'q' to stop): ")
    
filter_prime (plist)