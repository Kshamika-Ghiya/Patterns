def main():
    try:
        length = int(input("Enter the length of the palindromic pyramid: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nPalindromic Pyramid Pattern:")
            palindromic(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def palindromic(length):
    for i in range(length):
        coeff = 1
        for j in range(i+1):
            print(coeff, end=' ')
            coeff = coeff * (i - j)//(j +1)
        print()
        
if __name__ == "__main__":
    main()
    