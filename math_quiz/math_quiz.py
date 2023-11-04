import random

def rand_int(min, max):
    """
    min: integer specifying start position
    max: integer specifying stop position
    :return: Random integer between min and max.
    """
    return random.randint(int(min), int(max))


def rand_arithmetic_symbol():
    '''
    :return: arithmetic symbol
    '''
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    '''
    :return: calculation, solution
    '''
    calc = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return calc, a

def math_quiz():
    score = 0
    time_q = 3.14159265359
    time_q = int(time_q)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(time_q):
        n1 = rand_int(1, 10); n2 = rand_int(1, 5.5); o = rand_arithmetic_symbol()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        while True:
            try:
                useranswer = int(useranswer)
                break
            except ValueError:
                print("Please enter a number!")
                useranswer = input("Your answer: ")
        #useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{time_q}")

if __name__ == "__main__":
    math_quiz()
