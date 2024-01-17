def main():
    try:
        length = int(input("Enter the length of the rhombus: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nHollow Rhombus Pattern:")
            hollow_rhombus(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def hollow_rhombus(length):
    for i in range(length):
        for j in range(length-i-1):
            print(" ", end='')
        for j in range(length):
            if(i == 0 or i == length-1 or j == 0 or j == length-1):
                print("*", end='')
            else:
                print(" ", end='')
        print()       
        
if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            
            
#     ******
#    *    *
#   *    *
#  *    *
# *****