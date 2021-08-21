'''This program asks a user to insert a number form a specified range and reacts accordingly using exceptions'''

def read_int(prompt, mini, maxi):

    while True:
        print(prompt)
        num = input()

        try:
            num = int(num)
            assert (num <= 10) and (num >= -10)

        except ValueError:
            print("Error: wrong input")
            continue

        except AssertionError:
            print("Error the value is not within the permitted range",mini, maxi)
            continue 

        break
        
    return num 
        

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
