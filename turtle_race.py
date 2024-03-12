from random import randint
from turtle import Screen, Turtle

def main(money):
    # find out which turtle the user thinks will win the race
    user_choice = screen.textinput(title="Choose a Turtle!",
                                   prompt="red, orange, yellow, green, blue or purple: ")
    race_on = True
    # reset the turtles to their start positions
    for turtle in turtle_list:
        turtle.goto(turtle.x, turtle.y)
    # start the race
    while race_on:
        for turtle in turtle_list: # moves turtles a random distance one at a time
            steps = randint(0, 10)
            turtle.fd(steps)
            if turtle.xcor() > 225: # checks if the turtle has won - if yes this race ends
                race_on = False
                winner = turtle.pencolor()
                if user_choice == winner: # checks to see if the user chose the winning turtle
                    print("\nCongratulations - Your Turtle Won!!!")
                    print(f"\nWinning Turtle: {winner}")
                    new_money = money + 10
                    print(f"\nYou Now Have ${new_money}")
                    return new_money
                else: # takes away some money if the user did not choose the winning turtle
                    print("\nSorry - Your Turtle Is a Lazy Sausage!!!")
                    print(f"\nWinning Turtle: {winner}")
                    new_money = money - 10
                    print(f"\nYou Now Have ${new_money}")
                    return new_money
    screen.exitonclick() # keeps the screen open until the game is over

def populate_turtles():
    y = -125 # first turtle y coordinate
    for i in range(0, len(turtle_colors)): # instantiates turtle objects
        next_turtle = Turtle(shape="turtle")
        next_turtle.penup()
        # each new instance of Turtle class has unique attributes
        next_turtle.color(turtle_colors[i])
        # we give each turtle object an x and y coordinate
        next_turtle.x = -225
        next_turtle.y = y
        # each turtle object is appended to a list of turtle objects
        turtle_list.append(next_turtle)
        # we add to y to move the next turtle up the screen
        y += 50

# entry point
screen = Screen()
screen.setup(width=500, height=400)
turtle_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]
turtle_list = []

populate_turtles() # instantiates objects from Turtle class

money = 50

# enter the main game loop
while money > 0 and money < 100:
    money = main(money)

# let the user know how they did overall
if money <= 0:
    print("\nSorry - you have no more money left to bet with.")
else:
    print("Great job - you have made lots of money at the turtle races!")
