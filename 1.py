'''
Create a program in your favourite programming language
Perform any task you'd like to do
'''

numbers = []
while True:
    try:
        number = eval(input('enter a number or -1 to quit: '))
    except ValueError:
        print(f"please enter a number")
        continue
    if number == -1:
        break
    numbers.append(number)
print(f"mean of numbers is {sum(numbers)/len(numbers)}")


