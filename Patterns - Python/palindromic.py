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
    for i in range(1, length+1):
        for j in range(1, length-i+1):
            print(" ", end ='')
        for j in range(i, 0, -1):
            print(j, end='')
        for j in range(2, i+1):
            print(j, end='')
        print()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    

#     1                         4 spaces                1 to 1              
#    212                        3 spaces                2 to 1              2 to 2
#   32123                       2 spaces                3 to 1              2 to 3
#  4321234                      1 space                 4 to 1              2 to 4
# 543212345                     0 space                 5 to 1              2 to 5