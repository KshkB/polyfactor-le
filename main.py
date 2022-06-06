import os
import numpy as np
import polygenerator as plygen

def guessCheck(guess, true):
    guess = np.array(guess)
    true = np.array(true)
    remainder = np.polydiv(true, guess)[1][0]
    if round(remainder, 10) == 0:
        return True
    return False

def guessLog(guess, factor1, factor2):
    log = {}
    m = max(len(factor1), len(factor2))
    if len(guess) == m:
        if len(factor1) == len(factor2):
            for index, coeff in enumerate(guess):
                if coeff == factor1[index] or coeff == factor2[index]:
                    log[index] = f"{coeff} at position {index} is correct!"
                else:
                    log[index] = f"{coeff} at position {index} is incorrect."
            return log

        if len(factor1) < len(factor2):
            for index, coeff in enumerate(guess):
                if index < len(factor1):
                    if coeff == factor1[index] or coeff == factor2[index]:
                        log[index] = f"{coeff} at position {index} is correct!"
                    else:
                        log[index] = f"{coeff} at position {index} is incorrect."
                if index >= len(factor1): 
                    if coeff == factor2[index]:
                        log[index] = f"{coeff} at position {index} is correct!"
                    else:
                        log[index] = f"{coeff} at position {index} is incorrect."
            return log

        if len(factor2) < len(factor1):
            for index, coeff in enumerate(guess):
                if index < len(factor2):
                    if coeff == factor2[index] or coeff == factor1[index]:
                        log[index] = f"{coeff} at position {index} is correct!"
                    else:
                        log[index] = f"{coeff} at position {index} is incorrect."
                if index >= len(factor2): 
                    if coeff == factor1[index]:
                        log[index] = f"{coeff} at position {index} is correct!"
                    else:
                        log[index] = f"{coeff} at position {index} is incorrect."
            return log

    if len(guess) > m:
        guess = guess[:m]
        return guessLog(guess, factor1, factor2)

def guessLog2(guess, factor):
    log = {}
    degree = len(guess)
    for index, coeff in enumerate(guess):
        if guess[index] == factor[index]:
            log[index] = f"the coefficient {coeff} of x^{degree-index-1} is correct!"
        else:
            log[index] = f"the coefficient {coeff} of x^{degree-index-1} is incorrect."

    return log

def polyvisual(polynomial):
    visual = ""
    degree = len(polynomial)
    for i, v in enumerate(polynomial):
        visual += f"{v}x^{degree - i-1} + "

    return visual[:-3]

def main_program(factor1, factor2, polynomial, guess_counter=5, log = {}):
    
    degree = len(polynomial)
    if guess_counter == 5:
        print("\nEnter your guess:")

    if guess_counter < 5 and guess_counter > 0:
        print(f"\nRecall, your polynomial is {polyvisual(polynomial)}.\n\nEnter your guess:")

    guess = [1]
    for i in range(degree-2):
        print(f"coefficient of x**{degree - i-3}")
        ans = int(input().strip())
        guess.append(ans)

    log[f"Round {guess_counter} guess"] = guess
    # curr_log = guessLog(guess, factor1, factor2)
    curr_log = guessLog2(guess, factor1)

    os.system('clear')
    print(f"The polynomial to factor is {polyvisual(polynomial)}.")
    print(f"You have guessed the factor {polyvisual(guess)}.\n\nResults for Round {guess_counter} are:\n")
    for key in curr_log:
        print(f"{curr_log[key]}")

    print("\nYour guess history is:\n")
    for key in log:
        print(f"{key}: {polyvisual(log[key])}")

    if bool(guessCheck(guess, polynomial)):
        print(f"\nCongratulations! You got it!!\nYour guess {polyvisual(guess)} factors {polyvisual(polynomial)}.\n")
        return
    
    guess_counter += -1
    if guess_counter > 0:
        print(f"\nYou did not guess a factor. You MUST try again.\nYou have {guess_counter} attempt(s) remaining.")
        print("\nEnter Y to continue.")
        user_ans = str(input().strip())
        if user_ans == 'Y':
            os.system('clear')
            print("\nYour guess history is:\n")
            for key in log:
                print(f"{key}: {polyvisual(log[key])}")
        
            print("\nYour result in the previous round was:\n")
            for key in curr_log:
                print(f"{curr_log[key]}")

            return main_program(factor1, factor2, polynomial, guess_counter, log)

    if guess_counter == 0:
        os.system('clear')
        print("You have FAILED to guess a factor and there no guesses left.")
        print("\nYour guess history is:\n")
        for key in log:
            print(f"{key}: {polyvisual(log[key])}")

        print(f"\nThe polynomial {polyvisual(polynomial)} is a product of the following factors:\n")
        print(f"first factor: {polyvisual(factor1)}")
        print(f"second factor: {polyvisual(factor2)}")
        print("\nBetter luck next time!")
        return

if __name__ == "__main__":
    os.system('clear')
    print("Choose a difficulty:\nEasy - enter 0;\nMedium - enter 1;\nHard - enter 2;\nSuper hard - enter 3")
    user_ans = int(input().strip())
    degree = 3 + user_ans

    factor1, factor2, polynomial = plygen.generate2(degree)

    factor1 = list(reversed(factor1))
    factor2 = list(reversed(factor2))

    polynomial = list(reversed(polynomial))

    os.system('clear')
    print(f"Your polynomial for today is {polyvisual(polynomial)}.\nGuess a factor, save the world!")
    print("\nEXTREMELY IMPORTANT INFORMATION:\n-all polynomials are MONIC;\n-you need to guess the coefficients of lower order terms;")
    print("-the given polynomial has a linear factor;\n-the coefficients of factors are integers between ZERO and FIVE.")

    main_program(factor1, factor2, polynomial)
    