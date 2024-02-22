def calculator():
    """
    კალკულატორის ფუნქცია მომხმარებლებს საშუალებას აძლევს შეასრულონ ძირითადი
    არითმეტიკული მოქმედებები (+, -, *, /). მომხმარებლებს შეუძლიათ შეიყვანონ ორი რიცხვი და
    შემდეგ აირჩიონ ოპერაცია შედეგის მისაღებად. კალკულატორი ასევე შეიცავს შეყვანის
    ვალიდაციას არასწორი შეყვანების დასამუშავებლად.
    """

    #  ფუნქცია რიცხვის შეყვანისა და ვალიდაციისთვის
    def validate_input(num):
        while True:
            try:
                value = float(input(num))
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    # პირველი რიცხვის შეყვანა
    num1 = validate_input("Enter the first number: ")

    # მეორე რიცხვის შეყვანა
    num2 = validate_input("Enter the second number: ")

    # ოპერაციის არჩევა
    operation = input("Enter the operation (+, -, *, /): ")
    while operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please enter '+', '-', '*', or '/'")
        operation = input("Enter the operation (+, -, *, /): ")

    # კალკულატორის ლოგიკა
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # რიცხვის შემოწმება 0-ზე გაყოფისთვის
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return 
    else:
        print("Invalid operation")

    print("Result:", result)


# ფუნქციის გამოძახება
calculator()
