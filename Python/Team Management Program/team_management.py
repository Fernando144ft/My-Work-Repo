# Fernando Parra
# Team Management Program: Version 2
# 10/26/2024
# Update program that lets the manager of a sport team track the data for each player and output
# the lineup for upcoming games and store data in a csv file

import FileIO
import datetime as dt

def display_menu(): # Display the menu with the required layout
    print(f"\nMENU OPTIONS\n1 - Display lineup\n2 - Add player\n"
          f"3 - Remove Player\n4 - Move player\n5 - Edit player positions\n6 - Edit player stats\n7 - Exit program")
    print(f"\nPOSITIONS\n{", ".join(valid_positions)}\n{"=" * 60}")

def calculate_average(local_object): # Round batting average to three decimal places
    try:
        average = float(local_object["hits"]) / float(local_object["at bats"])
        return average
    except ZeroDivisionError:
        return 0

def integer_exception_handler(prompt):
    while True:
        try:
            variable = int(input(prompt))
            return variable
        except ValueError:
            print("Invalid, please enter a valid number\n")

def player_statistic_handler(at_bats, validate, prompt, hits=None):
    while True:
        match validate:
            case "at_bats":
                if at_bats < 0:
                    print("\nInvalid, negative amount of \"at bats\".")
                    at_bats = integer_exception_handler(prompt)
                else:
                    return at_bats
            case "hits":
                if hits > at_bats or hits < 0:
                    print("\nHits must be lower than \"at bats\", but not negative.")
                    hits = integer_exception_handler(prompt)
                else:
                    return hits

def player_stat_changer(local_object): # Change the statistic values of a player
    for index, value in enumerate(local_object):
        match index:
            case 1:
                position = input("Enter the new Position: ").upper()
                while position.upper() not in valid_positions:
                    print("\nInvalid position, try again.")
                    position = input("Position: ").upper()
                local_object["position"] = position
            case 2:
                at_bats_prompt = "Enter the new \"at bat\" amount: "
                at_bats = integer_exception_handler(prompt=at_bats_prompt)
                at_bats = player_statistic_handler(at_bats= at_bats, validate="at_bats", prompt=at_bats_prompt)
                local_object["at bats"] = at_bats
            case 3:
                hits_prompt = "Enter new hits: "
                hits = integer_exception_handler(hits_prompt)
                hits = player_statistic_handler(at_bats=local_object["at bats"], validate="hits", prompt=hits_prompt,
                                                hits=hits)
                local_object["hits"] = hits
    print(f"{local_object["name"]} was updated.")
    return local_object

def nested_list_iterator(lookup_input, object_list, action): # Iteration for the lineup list

    count = 0
    for local_object in object_list:
        count += 1
        if lookup_input == count:
            match action:
                case "delete":
                    object_list.pop(count - 1)
                    print(f"{local_object["name"]} was deleted.")
                case "change_player":
                    print(f"{local_object["name"]} was selected.")
                    selection_new_lineup = integer_exception_handler("Enter a new lineup number: ")
                    object_list.pop(count - 1)
                    object_list.insert(selection_new_lineup - 1, local_object)
                    print(f"{local_object["name"]} was moved")
                case "change_player_position":
                    print(f"You selected {local_object["name"]}: Position={local_object["position"].upper()}")
                    position = input("Enter the new Position: ").upper()
                    while position not in valid_positions:
                        print("\nInvalid position, try again.")
                        position = input("Position: ").upper()
                    local_object["position"] = position
                    print(f"{local_object["name"]} was updated.")
                case "change_player_stats":
                    print("You selected {}: Position={}, At Bat={}, Hits={}, "
                          "Average={}".format(local_object["name"], local_object["position"],
                                              local_object["at bats"], local_object["hits"],
                                              calculate_average(local_object)))
                    player_stat_changer(local_object)
        else:
            continue

def date_prompt():
    current_date = dt.datetime.now().date()
    print("{}{:>14}".format("CURRENT DATE:", current_date.strftime("%Y-%m-%d")))

    while True:
        try:
            game_date = input(f"{"GAME DATE:":<17}")
            if game_date != "":
                game_date = dt.datetime.strptime(game_date, "%Y-%m-%d").date()
                days_until_game = game_date - current_date
                return print(f"DAYS UNTIL GAME: {days_until_game.days}")
            else:
                return
        except ValueError:
            print("\nInvalid, try again or leave empty, use the proper formatting: YYYY-MM-DD.")


def display_lineup(object_list):
    print(f"{"Player":>9}{"POS":>31}{"AB":>6}{"H":>6}{"AVG":>8}" + f"\n{"-" * 60}")
    count = 0
    for item in object_list:
        count += 1
        print("{:<3}{:<35}{:<5}{:<6}{:<6}{:<8.3f}".format(count, item["name"], item["position"], item["at bats"],
                                                       item["hits"], calculate_average(item)))

def add_player(local_object): # Add a single player to the lineup list
    name = input("Name: ").capitalize()
    local_object["name"] = name
    position = input("Position: ").upper()
    while True:
        if position not in valid_positions:
            print("\nInvalid position, try again.")
            position = input("Position: ").upper()
        else:
            local_object["position"]= position
            break

    # Data Validation
    at_bats = integer_exception_handler("At bats: ")
    at_bats = player_statistic_handler(at_bats=at_bats, validate="at_bats", prompt="At bats: ")
    local_object["at bats"] = at_bats
    hits = integer_exception_handler("Hits: ")
    hits = player_statistic_handler(at_bats=at_bats, validate="hits", prompt="Hits: ", hits=hits)
    local_object["hits"] = hits

    # Data Submission
    objects_list.append(local_object)
    FileIO.save_csv(objects_list)
    print(f"{name} was added.")

def remove_player(object_list): # Remove a single player to the lineup list
    player_number = integer_exception_handler("Enter a lineup number to remove: ")

    while player_number < 1 or player_number > len(object_list):
        print("Invalid: Lineup number out of range, try again.\n")
        player_number = integer_exception_handler("Enter a lineup number to remove: ")

    nested_list_iterator(lookup_input=player_number, object_list=object_list, action="delete")
    FileIO.save_csv(object_list)

def move_player(object_list):
    selection_to_move = integer_exception_handler("Enter a current lineup number to move: " )
    nested_list_iterator(lookup_input=selection_to_move, object_list=object_list, action="change_player")
    FileIO.save_csv(object_list)

def edit_player_position(object_list):
    player_number = integer_exception_handler("Enter a lineup number to edit: ")
    nested_list_iterator(lookup_input=player_number, object_list=object_list, action="change_player_position")
    FileIO.save_csv(object_list)

def edit_player_stats(object_list):
    player_number = integer_exception_handler("Enter a lineup number to edit stats: ")

    while player_number < 1 or player_number > len(object_list):
        print("Invalid: Lineup number out of range, try again.\n")
        player_number = integer_exception_handler("Enter a lineup number to edit stats: ")

    nested_list_iterator(lookup_input=player_number, object_list=object_list, action="change_player_stats")

def main(): # Display the menu, manage nested list, and validate data
    try:
        global player_object, objects_list, valid_positions
        valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
        player_object = {} # Same as aPlayerVariable
        objects_list = FileIO.open_csv() # Same as aLineupVariable

        print(f"{"=" * 64}\n{"":^19}Baseball Team Manager")

        date_prompt()
        display_menu()

        while True:
            user_selection = input("\nMenu Option: ")
            match user_selection:
                case "1": # DISPLAY
                    display_lineup(objects_list)
                case "2": # ADD
                    add_player(player_object)
                case "3": # REMOVE
                    remove_player(objects_list)
                case "4": # MOVE PLAYER
                    move_player(objects_list)
                case "5": # CHANGE POSITION
                    edit_player_position(objects_list)
                case "6": # CHANGE STATS
                    edit_player_stats(objects_list)
                case "7": # EXIT
                    print("Bye!")
                    break
                case Exception:
                    print("Invalid option, try again.")
                    display_menu()
    except FileNotFoundError:
        print("ERROR: CSV File Not Found...")
if __name__ == '__main__':
    main()
