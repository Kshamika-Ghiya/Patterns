def main():
    try:
        length = int(input("Enter the length of the butterfly: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nHollow Butterfly Pattern:")
            hollow_butterfly(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def hollow_butterfly(length):
    for i in range(1, length+1):
        space_before = 2 * (length - i)
        space_between = 2 * (i - 1)
        
        for j in range(1, i+1):
            if j == 1 or j == i:
                print("*", end='')
            else:
                print(" ", end='')
                
        for j in range(1, space_before + 1):
            print(" ", end='')

        for j in range(1, i+1):
            if j == 1 or j == i:
                print("*", end='')
            else:
                print(" ", end='')
            
        print()
        
    for i in range(length, 0, -1):
        space_before = 2 * (length - i)
        space_between = 2 * (i - 1)
        
        for j in range(1, i+1):
            if j == 1 or j == i:
                print("*", end='')
            else:
                print(" ", end='')
                
        for j in range(1, space_before + 1):
            print(" ", end='')

        for j in range(1, i+1):
            if j == 1 or j == i:
                print("*", end='')
            else:
                print(" ", end='')
            
        print()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
# *        *
# **      **
# * *    * *
# *  *  *  *
# *   **   *
