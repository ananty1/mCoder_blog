import random

def print_hello_world():
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Determine whether to print "hello" or "world" based on probabilities
    if random_number < 0.8:
        print("hello")
    else:
        print("world")

# Call the function multiple times to observe the probabilities
for _ in range(10):
    print_hello_world()
