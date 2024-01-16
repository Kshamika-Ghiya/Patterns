def main():
    try:
        length = int(input("Enter the length of the pyramid: "))
        
        if length <= 0:
            print("Please enter positive value for length.")
        else:
            print("\Full Pyramid Pattern (Numbers):")
            full_pyramid_numbers(length)
    
    except ValueError:
        print("Invalid input. Please enter valid integer for length.")

def full_pyramid_numbers(length):
    for i in range(1, length+1):
        for j in range(1, length-i+1):
            print(" ", end ='')
        for j in range(1, i+1):
            print(j, '', end='')
        print()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5