count = 0
total = 0
even_num = 0

while True:
    user_input = input("Enter a number (or type 'stop'): ")

    if user_input.lower() == "stop":
        break

    if user_input.isdigit():
        num = int(user_input)

        count += 1
        total+= num

        if num % 2 == 0:
            even_num += 1
    else:
        print("Invalid input! Enter numbers only.")

print("Count:", count)
print("Sum:", total)
print("Even numbers:", even_num)