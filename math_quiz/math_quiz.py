import random

def rand_int(min, max):
    """
    :input:
        min (int): specifying start position
        max (int): specifying stop position
    If min > max, arguments are switched:
    :return: Random integer between min and max.
    """
    if min > max:
        t = min
        min = max
        max = t
    return random.randint(min, max)


def rand_arithmetic_symbol():
    '''
    :return: arithmetic symbol
    '''
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    '''
    :input:
        n1 (int): first number
        n2 (int): second number
        o: arithmetic symbol
    Function checks wether the arithmetic symbol is '+', '-' or '*' and calculates solution
    :return: calculation, solution
    '''
    calc = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return calc, a

def math_quiz():
    '''
    A math quiz is started with a score counting the right answers:
    User is asked to solve to problem displayed on screen time_q times.
    For correct answers the score is increased by one.
    In the end the result is displayed on screen.
    '''
    score = 0
    time_q = 3.14159265359
    time_q = int(time_q)
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for _ in range(time_q):
        #variable selection and calcuation
        n1 = rand_int(1, 10); n2 = rand_int(1, int(5.5)); o = rand_arithmetic_symbol()
        PROBLEM, ANSWER = calculation(n1, n2, o)
        #user input
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        #wrong input handling
        while True:
            try:
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Please enter a number!")
                useranswer = input("Your answer: ")

        #user answer checking
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    # score message
    print(f"\nGame over! Your score is: {score}/{time_q}")

if __name__ == "__main__":
    math_quiz()
