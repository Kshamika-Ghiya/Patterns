def main():
    try:
        length = int(input("Enter half of the length of the butterfly: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nButterfly Pattern:")
            butterfly(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def butterfly(length):
    for i in range(1, length+1):
        spaces = 2 * (length - i)
        for j in range(1, i+1):
            print("*", end ='')
        for j in range(1, spaces+1):
            print(" ", end='')
        for j in range(1, i+1):
            print("*", end='')
        print()
        
    for i in range(length, 1, -1):
        spaces = 2 * (length - i)
        for j in range(1, i+1):
            print("*", end ='')
        for j in range(1, spaces+1):
            print(" ", end='')
        for j in range(1, i+1):
            print("*", end='')  
        print()
        
if __name__ == "__main__":
    main()
    
    
    
   
   
   
   
# for n = 5 
# *        *    i = 1       1star           8 spaces            1star 
# **      **    i = 2       2star           6 spaces            2star
# ***    ***    i = 3       3star           4 spaces            3star
# ****  ****    i = 4
# **********    i = 5
#                                                                         upper half
#-------------------------------------------------------------------------------    
#                                                                         lower half
# **********
# ****  ****
# ***    ***
# **      **
# *        *



#spaces = 2(n-i)