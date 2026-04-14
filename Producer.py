# Task Processing System, incorporating different data structure skills for practice



while True:
    User_Task= input("Enter a task to add to the queue: ")

    if User_Task.strip() == "": # .strip to account for random space inputs
        print("No task entered. Please enter a valid task.")    
    elif User_Task.strip() == "exit" or User_Task.strip() == "Exit":
        print("Exiting the task processing system.")
        break
    else:
        with open("queue.txt", "a") as file:
            file.write(User_Task + "\n")