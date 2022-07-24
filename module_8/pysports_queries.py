# Jennifer Adams
# CYBR410-T301
# July 23, 2022
# Objective: Use Python to query MySQL database tables

# Import statements
import mysql.connector
from mysql.connector import errorcode

# Configuration information
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Try/catch block for errors 
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
   
    # Create a value for MySQL cursor function
    cursor = db.cursor()

    # Use cursor to process result data row by row
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Assign cursor method fetchall to return rows 
    teams = cursor.fetchall()

    # Mark the display of team records
    print("\n-- DISPLAYING TEAM RECORDS --")

    # Iterate through rows in the teams table
    for team in teams:

        # Display row information
        print("Team ID: {} \nTeam Name: {} \nMascot: {}\n".format(team[0], team[1], team[2]))
    
    # Use cursor to process result data row by row
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    
    # Assign cursor method fetchall to return rows
    players = cursor.fetchall()

    # Mark the display of player records
    print("\n-- DISPLAYING PLAYER RECORDS --")

    # Iterate through rows in the players table
    for player in players:
        
        # Display row information
        print("Player ID: {}\nFirst Name: {} \nLast Name: {} \nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))
    
    # Gather input from user to continue
    input("\n\nPress any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print (" The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()

