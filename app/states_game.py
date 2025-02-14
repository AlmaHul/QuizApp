import turtle
import pandas


def guess_states_play():
    """Använder turtle och pandas för att skapa ett spel där användaren ska gissa
    namnet på alla 50 amerikanska stater"""
    screen = turtle.Screen()
    screen.title("U.S States")
    image = "images/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []


    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another states name?\nWrite 'exit' to exit the game.").title()

        if answer_state == "Exit":
            print("Spelet avslutades av användaren")
            break


        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(state_data.state.item())

    if len(guessed_states) == 50:
        print("Grattis! Du har gissat alla 50 stater!")

    else:
        print(f"Du klarade {len(guessed_states)} stater.")

    # Försök att stänga Turtle fönstret om det inte redan är stängt
    try:
        screen.bye()
    except turtle.Terminator:
        pass  # Om skärmen redan är stängd, ignorera felet

    # Gör en sista säker avslutning för Turtle, bara om den inte redan stängts
    if screen._root is not None:  # Kontrollera om screen root fortfarande existerar
        try:
            turtle.bye()  # Försök att avsluta Turtle
        except turtle.Terminator:
            pass

    turtle.done()



