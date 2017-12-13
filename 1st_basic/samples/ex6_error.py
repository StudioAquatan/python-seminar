import sys

if __name__ == '__main__':

    # no error handling
    x = int(input("Please enter a number :"))
    print(x)

    # error handling
    while True:
        try:
            x = int(input("Please enter a number :"))
            print('OK! The number is', x)
            break

        except ValueError:
            sys.stderr.write("Oops!  That was no valid number.\n")
            sys.stderr.write("Try again...\n")