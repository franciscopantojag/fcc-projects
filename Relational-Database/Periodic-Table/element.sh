#! /bin/bash

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

# if no input provided
if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."
  exit
fi

# if input is number
if [[ $1 =~ ^[0-9]+$ ]]
then
  FIND_RESULT=$($PSQL "SELECT name, symbol, atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type FROM elements INNER JOIN properties USING (atomic_number) INNER JOIN types USING (type_id) WHERE atomic_number=$1")
else
  # if input is not a number
  FIND_RESULT=$($PSQL "SELECT name, symbol, atomic_number, atomic_mass, melting_point_celsius, boiling_point_celsius, type FROM elements INNER JOIN properties USING (atomic_number) INNER JOIN types USING (type_id) WHERE name='$1' OR symbol='$1'")
fi

# if query result is empty
if [[ -z $FIND_RESULT ]]
then
  echo "I could not find that element in the database."
else
  # if there was a result
  echo "$FIND_RESULT" | while read NAME BAR SYMBOL BAR ATOMIC_NUMBER BAR ATOMIC_MASS BAR MELTING_POINT BAR BOILING_POINT BAR TYPE
  do
    echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING_POINT celsius and a boiling point of $BOILING_POINT celsius."
  done
fi
