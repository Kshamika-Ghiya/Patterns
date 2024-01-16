def main():
    try:
        length = int(input("Enter the length of the pyramid: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\nPyramid Pattern (Numbers):")
            numbers_pyramid(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def numbers_pyramid(length):
    for i in range(1, length+1):
        for j in range(1, (length-i)+1):
            print(" ", end ='')
        for j in range(1, i+1):
            print(i, "", end='')
        print()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    

#    1                                  4 spaces                1(x1)
#   2_2                                 3 spaces                2(x2)
#  3_3_3                                2 spaces                3(x3)
# 4_4_4_4                               1 space                 4(x4)
#5_5_5_5_5                              0 space                 5(x5)