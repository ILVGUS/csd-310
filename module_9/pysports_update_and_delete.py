# Jennifer Adams
# CYBR410-T301
# July 31, 2022
#
# Objective: Connect to mysql database, insert entry into team gandalf and perform an INNER JOIN to connect player
# table and team table using team_id. Update entry to team 2 and perform an INNER JOIN to connect player
# table and team table using team_id. Delete entry and perform an INNER JOIN to connect player
# table and team table using team_id

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
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1);")

    # Use cursor to process result data row by row
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")

    # Assign cursor method fetchall to return rows 
    players = cursor.fetchall()

    # Mark the display of player records
    print("\n-- DISPLAYING PLAYERS AFTER INSERT --")

    # Iterate through rows in the player table
    for player in players:

        # Display row information
        print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(player[0], player[1], player[2], player[3]))
    
    # Use cursor to process result data row by row
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    # Use cursor to process result data row by row
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")

    # Assign cursor method fetchall to return rows 
    players = cursor.fetchall()

    # Mark the display of player records
    print("\n\n-- DISPLAYING PLAYERS AFTER UPDATE --")

    # Iterate through rows in the player table
    for player in players:

        # Display row information
        print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(player[0], player[1], player[2], player[3]))
    
    
    # Use cursor to process result data row by row
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

    # Use cursor to process result data row by row
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id")

    # Assign cursor method fetchall to return rows 
    players = cursor.fetchall()

    # Mark the display of player records
    print("\n\n-- DISPLAYING PLAYERS AFTER DELETE --")

    # Iterate through rows in the player table
    for player in players:

        # Display row information
        print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(player[0], player[1], player[2], player[3]))
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
