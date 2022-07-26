import turtle
import pandas
# image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# read file
data = pandas.read_csv("50_states.csv")
list_of_state = data.state.to_list()
# process
state_found = True
guess_count = 0
total_count = 50
guessed_state = []

while state_found:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{total_count} States correct" ,
                                    prompt="What's another state's name? ").title()
    guess_count += 1
    missing_state = [state for state in list_of_state if state not in  guessed_state]
    if answer_state == "Exit":
        missing_state = [state for state in list_of_state if state not in guessed_state]
        # missing_state = []
        # for state in list_of_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        missing_state_data = pandas.DataFrame(missing_state)
        missing_state_data.to_csv("to_learn.csv")

        break

    if answer_state in list_of_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_state = data[data.state == f"{answer_state}"]
        new_state_x = int(new_state.x)
        new_state_y = int(new_state.y)
        t.goto(new_state_x , new_state_y)
        t.write(answer_state)

        if guess_count == total_count:
            state_found = False


