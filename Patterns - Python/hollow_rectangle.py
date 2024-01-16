def main():
    try:
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        
        if length <= 0 or breadth <= 0:
            print("Please enter positive values for length and breadth.")
        else:
            print("\nHollow Rectangle Pattern:")
            hollow_rectangle(length, breadth)
    
    except ValueError:
        print("Invalid input. Please enter valid integers for length and breadth.")

def hollow_rectangle(length, breadth):
    for i in range(1, breadth+1):
        for j in range(1, length+1):
            if i == 1 or j == 1 or i == breadth or j == length:
                print("*", end ='')
            else:
                print(' ', end='')
        print()
        
if __name__ == "__main__":
    main()