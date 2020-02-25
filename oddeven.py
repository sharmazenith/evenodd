number = int(input("Enter a number: "))
if number % 2 == 0:
    print("{} is an even number.".format(number))
else:
    if number == 1:
        print("1 is an odd number. -> [NEITHER PRIME NOT COMPOSITE]")
    if number > 1:
        for z in range(2,number):
            if number % z == 0:
                print(f"{number} is an odd number.")
                print(f"But it's is not a prime number.")
                print(f"Because {z} times {number//z} equals {number}")
                break
        else:
            print(f"{number} is a prime number.")




