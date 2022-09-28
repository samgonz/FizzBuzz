def fizzBuzzPositions():
    startingNumber = int(input('What would you like your starting number to be?\n'))
    endingNumber = int(input('What would you like your ending number to be?\n'))
    return startingNumber,endingNumber

startingNumber, endingNumber = fizzBuzzPositions()
if endingNumber <= startingNumber:
    print('Starting number must be less than ending number.')
    startingNumber, endingNumber = fizzBuzzPositions()
else:
    for i in range(startingNumber, endingNumber + 1):
        if i % 15 == 0:
            print(f'{i}: FizzBuzz')
        elif i % 5 == 0:
            print(f'{i}: Buzz')
        elif i % 3 == 0:
            print(f'{i}: Fizz')
        else:
            print(f'{i}:')