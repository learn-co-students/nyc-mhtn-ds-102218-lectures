import unittest2 as unittest
from dictionaryball import game_dict, num_points_scored, shoe_size, team_colors, team_names, player_numbers, player_stats

class TestDictionaryBall(unittest.TestCase):

    def test_game_dict(self):
        self.assertEqual(type(game_dict()), type({}), "Return value must be a dictionary")
        self.assertEqual(type(game_dict()['home']), type({}), "Return value must be a dictionary")
        self.assertEqual(type(game_dict()['away']), type({}), "Return value must be a dictionary")
        self.assertEqual(type(game_dict()['home']['team_name']), type(""), "Return value must be a string")
        self.assertEqual(type(game_dict()['home']['colors']), type([]), "Return value must be a list")
        self.assertEqual(type(game_dict()['home']['players']), type({}), "Return value must be a dictionary")

    def test_num_points_scored(self):
        self.assertEqual(type(num_points_scored('Mason Plumlee', 'aslkjsakljklj')), type(26), "Return value must be an integer")
        self.assertEqual(num_points_scored('Mason Plumlee'), 26)

    def test_shoe_size(self):
        self.assertEqual(type(shoe_size('Mason Plumlee')), type(19), "Return value must be an integer")
        self.assertEqual(shoe_size('Mason Plumlee'), 19)

    def test_team_colors(self):
        self.assertEqual(type(team_colors('Brooklyn Nets')), type([]), "Return value must be a list")
        self.assertItemsEqual(team_colors('Brooklyn Nets'), ["Black", "White"], "Return value must be a list containing the strings 'Black' and 'White'")

    def test_team_names(self):
        self.assertEqual(type(team_names()), type([]), "Return value must be a list")
        self.assertItemsEqual(team_names(), ['Brooklyn Nets', 'Charlotte Hornets'], "Return value must be a list containing the strings 'Brooklyn Nets' and 'Charlotte Hornets'")

    def test_player_numbers(self):
        self.assertEqual(type(player_numbers("Charlotte Hornets")), type([]), "Return value must be a list")
        self.assertItemsEqual(player_numbers("Charlotte Hornets"), [4, 0, 2, 8, 33], "Return value must be a list containing the itegers [4, 0, 2, 8, 33]")

    def test_player_stats(self):
        self.assertEqual(type(player_stats('Mason Plumlee')), type({}), "Return value must be a dictionary")
        self.assertEqual(player_stats('Mason Plumlee'), {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5})
