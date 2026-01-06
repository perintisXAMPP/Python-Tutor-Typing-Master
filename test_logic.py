def calculate_stats(target, user, duration):
    correct_chars = 0
    for i in range(min(len(target), len(user))):
        if target[i] == user[i]:
            correct_chars += 1
            
    accuracy = (correct_chars / len(target)) * 100 if len(target) > 0 else 0
    wpm = (len(user) / 5) / (duration / 60)
    return accuracy, wpm

# Test case
target = "print('Hello World')"
user = "print('Hello World')"
duration = 5 # seconds

acc, wpm = calculate_stats(target, user, duration)
print(f"Test 1 - Accuracy: {acc}%, WPM: {wpm}")

user_fail = "print('Hello')"
acc, wpm = calculate_stats(target, user_fail, duration)
print(f"Test 2 - Accuracy: {acc}%, WPM: {wpm}")
