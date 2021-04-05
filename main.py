import random

mm_count = 5  # random.randint(1,100)

attempt_limit = 5
attempts = 0

print("davaj")

while attempts < attempt_limit:
    guess_text = input("kolko?")
    guess = int(guess_text)
    if mm_count == guess:
        print(f"ano! bolo to {guess}")
        break
    elif guess < mm_count:
        print("malo")
    else:
        print("privela")
    attempts += 1

print("bye")
print(f"bolo to {mm_count}")
