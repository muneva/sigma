#PRIME NUMBER DETECTOR

def prime(number):

    if (number > 1):
        for i in range (2, number, 1):
            if (number % i == 0):
                return 1

        else:
            return 0

    elif (number == 1):
        return 0


while (1):
    
    num = int(input("Please enter an integer => "))

    while (1):

        if (prime(num) == 0):
            
            print(num, "is a prime number.")
            break

        num+=1




