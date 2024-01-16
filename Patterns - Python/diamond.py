def main():
    try:
        length = int(input("Enter the length of the diamond: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nDiamond Pattern:")
            diamond(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def diamond(length):
    for i in range(1, length+1):
        for j in range(1, length - i+1):
            print(" ", end ='')
        for j in range(1, 2*i):
            print("*", end='')
        print()
        
    for i in range(length, 0, -1):
        for j in range(1, length - i+1):
            print(" ", end ='')
        for j in range(1, 2*i):
            print("*", end='')
        print()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
# for n = 4
    
#    *                                      3 spaces            1 star
#   ***                                     2 spaces            3 stars
#  *****                                    1 space             5 stars
# *******                                   0 space             7 stars
#                                                               upper half
# --------------------------------------------------------------------
#                                                               lower half
# *******
#  *****
#   ***
#    *