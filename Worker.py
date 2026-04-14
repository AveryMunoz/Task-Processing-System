# File pulls text from queue.txt file and validates its composition and prints results

with open("queue.txt", "r") as file:
    for line in file:
        newline = line.strip() 
        parts = line.split()
        
        operation = parts[0]
        num1 = parts[1]
        num2 = parts[2]
        validOperations = ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE"]
        
        if len(parts) != 3:
            Message = f"ERROR: '{line.strip()}' - Invalid task format (Must be 'OPERATION NUMBER NUMBER')"
        elif operation not in validOperations:
            Message = f"ERROR: '{newline}' - Invalid operation (Must be {validOperations})"
        elif not num1.isdigit() or not num2.isdigit():
            Message = f"ERROR: '{newline}' - Invalid numbers (Must be digits)"   
        elif num2 == 0 and operation == "DIVIDE":
            Message = f"ERROR: '{newline}' - Division by zero"
        else:
            Message = f"'{newline}' - Valid task"
        
        with open("results.txt", "a") as file:
            file.write(Message + "\n")