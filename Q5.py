x= int(input("Enter a number of repetitions: "))

# Write your decorator here
def decorator(f):
    def loop():
        for i in range(x):
            f()
    return loop

@decorator
def hello():
       print ('Hello')

hello()
