def main():
    try:
        length = int(input("Enter the length of the 0-1 triangle: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\n0-1 Triangle:")
            zero_one_triangle(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def zero_one_triangle(length):
    for i in range(1, length+1):
        for j in range(1, i+1):
            if (i + j) % 2 == 0:
                print("0", end ='')
            else:
                print("1", end='')
        print()
        
if __name__ == "__main__":
    main()