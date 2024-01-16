def main():
    try:
        length = int(input("Enter the length of the floyd's triangle: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nFloyd's Triangle:")
            floyds_triangle(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def floyds_triangle(length):
    value = 1
    for i in range(1, length+1):
        for j in range(1, i+1):
                print(value, end =' ')
                value += 1
        print()
        
if __name__ == "__main__":
    main()