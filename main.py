from calculator import My_calc


while True:
    print("what do you want to do :")
    print("1. Add values")
    print("2. Subtract values")
    print("3. Multiply values")
    print("4. Divide values")
    print("5. Exit")
    print()

    CHOICE = input("Enter your choice: ")
    
    try:
        pick = int(CHOICE)
    except Exception:
        print("please enter a choice")
        print()
        CHOICE = input("Enter your choice: ")
        try:
            pick = int(CHOICE)
        except Exception:
            print("try again")
            break

    if pick == 5:
        print("Exiting...")
        quit()
        
    if pick == 1:
        x = input("enter the values you want to ADD (separate them with ','):\n")
        
        try:
            values = [int(i.strip()) for i in x.split(",")]
            result = My_calc.add(*values)
        except Exception :
            print("ValueError: some of your values are not a numbers")
            print("Please enter numbers!!")
            break
        print("ANSWER :", result)
        print()
    
    elif pick == 2:
        x = input("enter the values you want to SUBTRACT (separate thenm with ):\n")
        
        try:
            values = [int(i.strip()) for i in x.split(",")]
            result = My_calc.subtraction(*values)
        except Exception :
            print("ValueError: some of your values are not a numbers")
            print("Please enter numbers!!")
            break
        print("ANSWER :", result)
        print()

    elif pick == 3:
        x = input("enter the values you want to MULTIPLY (separate thenm with ):\n")
        
        try:
            values = [int(i.strip()) for i in x.split(",")]
            result = My_calc.multiply(*values)
        except Exception :
            print("ValueError: some of your values are not a numbers")
            print("Please enter numbers!!")
            break
        print("ANSWER :", result)
        print()
    
    elif pick == 4:
        x = input("enter the values you want to MULTIPLY (separate thenm with ):\n")
        
        try:
            values = [int(i.strip()) for i in x.split(",")]
            result = My_calc.division(*values)
        except ZeroDivisionError:
            print("Cannot divide by 0")
            break
        except Exception :
            print("ValueError: some of your values are not a numbers")
            print("Please enter numbers!!")
            break
        print("ANSWER :", result)
        print()
    

    