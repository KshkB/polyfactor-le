# Polyfactor-le

This game is inspired by the popular word guessing game *Wordle*. Instead of letters in a word however, one guesses factors of a polynomial. 

## Gameplay outline

At the outset of the game the player is prompted to choose a difficulty. The difficulty chosen determines the degree $d$ of the polynomial to be presented.

Depending on the difficulty the polynomial will have degree $d = 3, 4, 5$ or $6$. Note, for simplicity, all polynomials here are monic.

The player is then prompted to guess coefficients of a monic polynomial of degree $d -1$ (i.e., the coefficients of terms of order $d - 2, d-3, \ldots, 0$).

There are five stages of guessing. A record is kept of each guess. 

## Files

- The file `polyoperations` contains operations tailored to manipulate one variable polynomials. 
- The file `polygenerator` contains a method for generating polynomials in one variable.
- the file `main` is the main file containing code for the game. 

Run `main` to play the game! 
