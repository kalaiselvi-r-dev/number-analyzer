count = 0
total = 0
even_num = 0

while True:
    user_input = input("Enter a number (or type 'stop'): ").strip()

    
    if user_input == "":
        print("Empty input not allowed!")
        continue

    # Stop condition
    if user_input.lower() == "stop":
        break

    try:
        num = float(user_input)

        count += 1
        total += num

        
        if num.is_integer() and int(num) % 2 == 0:
            even_num += 1

    except ValueError:
        print("Invalid input! Enter numbers only.")


if count == 0:
    print("No valid numbers entered!")
else:
    print("Count:", count)
    print("Sum:", total)
    print("Even numbers:", even_num)
