import pandas as pd
import pdb
# mv test/index_test.py .
# pwd
# open .
# What's the data structure i want
    # How would I do this in the real world
    # give me a list of players
    # find the player from the list
    # find his shoe size

game_dictionary = {
    'home': {
        'team_name': "Brooklyn Nets",
        'colors': ["Black", "White"],
        'players': {
            "Alan Anderson": {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1 },
            "Reggie Evans": {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7 },
            "Brook Lopez": {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15 },
            "Mason Plumlee": {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5 },
            "Jason Terry": {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1 }
        }
    },
    'away': {
        'team_name': "Charlotte Hornets",
        'colors': ["Turquoise", "Purple"],
        'players': {
            "Jeff Adrien": {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2 },
            "Bismak Biyombo": {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10 },
            "DeSagna Diop": {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5 },
            "Ben Gordon": {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0 },
            "Brendan Haywood": {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12 }
        }
    }
}

def game_dict():
    pass

def find_player(name):
    players = all_players()
    return players[name]


def num_points_scored(name):
    # 1. relate this to the real world
        # STOP talking code to me
        # write out comments of the steps
        # a. give me all the player
        # b. find the correct player
        # 3. the number of points scored
    # 2. Think of the data structure you want
        # And use reject and coerce to get there.

    # Reject
    # Coerce
    # Act
    # Return

    # reject

    player = find_player(name)
    return player['points']

    #



     # and returns the number of points scored for that player.

def all_players():
    # pdb.set_trace()
    # {'alksjlsa': }
    home_players = game_dictionary['home']['players']
    away_players = game_dictionary['away']['players']
    all_players = home_players.copy()
    all_players.update(away_players)
    return all_players

def shoe_size(name):
    players = all_players()
    return players[name]['shoe']

def team_colors():
    pass

def team_names():
    pass

def player_numbers(team_name):
    pass

def player_stats():
    pass


# all_players()
