def main():
    try:
        length = int(input("Enter the length of the rhombus: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nSolid Rhombus Pattern:")
            solid_rhombus(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def solid_rhombus(length):
    for i in range(1, length+1):
        for j in range(1, (length-i)+1):
            print(" ", end ='')
        for j in range(1, length+1):
            print("*", end='')
        print()
        
if __name__ == "__main__":
    main()
    
    
    

#     *****         4spaces         5stars
#    *****          3spaces         5stars
#   *****           2spaces         5stars
#  *****            1space          5stars 
# *****             0space          5stars