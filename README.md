This is my first project on GitHub.

# Rock Paper Scissors 
---
> Description : Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".
>  This Python Program allows user to play this game against computer.
---

## Introduction

Rock paper scissors (also known by other orderings of the three items, with "rock" sometimes being called "stone", roshambo or ro-sham-bo) is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (also indicating "victory" or "peace") except that it is pointed horizontally instead of being held upright in the air.

A simultaneous, zero-sum game, it has only two possible outcomes: a draw, or a win for one player and a loss for the other. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.
[Read More on Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors)

**Possible cases**

* if (player == rock) and (computer == paper); computer wins
* if (player == paper) and (computer == paper); tie
* if (player == scissors) and (computer == paper); player wins

* if (player == rock) and (computer == rock); tie
* if (player == paper) and (computer == rock); player wins
* if (player == scissors) and (computer == rock); computer wins

* if (player == rock) and (computer == scissors); player wins
* if (player == paper) and (computer == scissors); computer wins
* if (player == scissors) and (computer == scissors); tie

## Algorithm

1. The user enters his name.
2. The user enters the action he wants to play - "Paper", "Rock" or "Scissors".
3. The computer will randomly choose between "Paper", "Rock" and "Scissors".
4. The user input will be compared to the computer selection.
5. If the result is tied, a new round is started.
6. The game will continue until there is a winner.

## Dependencies

* Python


A Project by (https://github.com/Dzonix)
