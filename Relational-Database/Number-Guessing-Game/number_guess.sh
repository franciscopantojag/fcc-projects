#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=number_guess --tuples-only -c"

echo "Enter your username:"
read USERNAME

USER_SELECT_RESULT=$($PSQL "SELECT user_id, username FROM users WHERE username='$USERNAME'")

# if there is no user
if [[ -z $USER_SELECT_RESULT ]]
then
  INSERT_USERNAME_RESULT=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME')")
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  # we get the user_id
  USER_SELECT_RESULT=$($PSQL "SELECT user_id, username FROM users WHERE username='$USERNAME'")
else
  echo "$USER_SELECT_RESULT" | while read USER_ID BAR USERNAME
  do
    # we get the games of that user
    GAMES_SELECT_RESULT=$($PSQL "SELECT COUNT(*), MIN(guesses) FROM games WHERE user_id=$USER_ID")
    echo "$GAMES_SELECT_RESULT" | while read GAMES_PLAYED BAR BEST_GAME
    do
      echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
    done
  done
fi

# create random number
RANDOM_NUMBER=$((1 + $RANDOM % 1000))

# create guesses var
GUESSES=1

# ask for a guess
echo "Guess the secret number between 1 and 1000:"
read GUESS_INPUT
while [[ $GUESS_INPUT != $RANDOM_NUMBER ]]
do
  #increase guesses
  ((GUESSES++))

  # if input is number
  if [[ $GUESS_INPUT =~ ^[0-9]+$ ]]
  then
    if [[ $GUESS_INPUT < $RANDOM_NUMBER ]]
    then
      echo "It's higher than that, guess again:"
    else
      echo "It's lower than that, guess again:"
    fi
  else
    echo "That is not an integer, guess again:"
  fi
  read GUESS_INPUT
done

# insert game
echo "$USER_SELECT_RESULT" | while read USER_ID BAR USERNAME
do
  CREATE_GAME_RESULT=$($PSQL "INSERT INTO games(user_id, guesses) VALUES($USER_ID, $GUESSES)")
done

echo "You guessed it in $GUESSES tries. The secret number was $RANDOM_NUMBER. Nice job!"
