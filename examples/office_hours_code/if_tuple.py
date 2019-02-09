FEELINGS = ('happy', 'sad', 'indifferent')

current_feeling = input("How do you feel?: ")

if current_feeling in FEELINGS:
    print(f"You're feeling {current_feeling}")
else:
    print("I don't know what you mean")