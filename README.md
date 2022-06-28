This project aims to implement the MVC (Model, View, Controller) design pattern in the realization of a program to manage chess tournaments

## Clone of the repository

* git clone https://github.com/Herve-2476/OpenClassRoomsProject_4.git

* cd OpenClassRoomsProject_4


## Creation of the virtual environment (Python 3.7)
 
* python -m venv venv

* source venv/bin/activate *#to launch your environment under linux / Mac*

* venv\Scripts\activate.bat *#to launch your environment under windows*

* pip install -r requirements.txt


## Running the program

* python chess.py

## Compliance with PEP 8 guidelines

* flake8 --format=html --htmldir=flake8_rapport --max-line-length 119 views models controllers chess.py

## Use of the program

* Enter at least eight players (Default number of a tournament) through the main menu

* Create a tournament through the tournament menu

* Play all four rounds through the round menu

* Change a player's ranking through the main menu

* Generate reports through the main and tournament menus

* it is possible to create a player, a tournament or modify a player (the ranking for example) at any time

* the last tournament in the database is always select when you choose the tournament menu

