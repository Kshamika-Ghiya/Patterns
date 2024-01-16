def main():
    try:
        length = int(input("Enter the length of the pyramid: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nInverted and Rotated Half Pyramid Pattern:")
            inverted_rotated_half_pyramid(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def inverted_rotated_half_pyramid(length):
    for i in range(1, length+1):
        for j in range(1, length-i+1):
            print(" ", end ='')
        for j in range(1, i+1):
            print("*", end='')
        print()
        
if __name__ == "__main__":
    main()