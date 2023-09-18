if __name__ == "__main__":

    animais = [ 
        "Dog", "Cow", "Cat", "Horse",
        "Donkey", "Tiger", "Lion", "Panther",
        "Leopard", "Cheetah", "Bear", "Elephant",
        "Polar", "Bear", "Turtle", "Tortoise", 
        "Crocodile", "Rabbit", "Porcupine", "Hare" 
        ]
    animais.sort()
    print( [x for x in animais] )

    with open("animais.csv", "w") as f:
        for animal in animais:
            f.write(animal + '\n')