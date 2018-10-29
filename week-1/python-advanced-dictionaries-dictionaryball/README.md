
# Dictionaryball

## Instructions

Great news! You're going to an NBA game. The only catch is that you've been volunteered to keep stats at the game.
Fork and clone this lab and run the test suite to get started. You'll be coding your solution in `dictionaryball.py`.

## Objectives
1. Practice building nested dictionaries
2. Practice iterating over nested dictionaries and lists

### Part 1: Building the Dictionary

The first step is to build the dictionary itself! We will need to assign the dictionary to a variable, let's call it `game_dictionary`. This nested dictionary should be constructed in the following manner:

* The top level of the dictionary has two keys: `home`, for the home team, and `away`, for the away team.
* The values of the `home` and `away` keys are dictionaries. These dictionaries have the following keys:
  * `team_name`
  * `colors`
  * `players`
  

* The `team_name` key points to a string of the team name.
* The `colors` key points to a list of strings that are that team's colors.
* The `players` key points to a dictionary of players whose names (as strings) are the keys to a dictionary containing their stats. The values for each player's names and their stats can be found in the table below. The stats keys should be formatted like this:
    * `number`
    * `shoe`
    * `points`
    * `rebounds`
    * `assists`
    * `steals`
    * `blocks`
    * `slam_dunks`

Use the following data to populate your `game_dictionary` as outlined above.

Home Team:

* team name: Brooklyn Nets
* colors: Black, White
* players:


|          Stat          | Info | Info |  Info | Info | Info   |
|:------------------:|:-------------:|:------------:|:------------:|:-------------:|:-------------:|
| **Player Name**    |  Alan Anderson| Reggie Evans | Brook Lopez  | Mason Plumlee | Jason Terry   |
| **Number**         | 0             | 30           | 11           | 1             | 31            |
| **Shoe**           | 16            | 14           | 17           | 19            | 15            |
| **Points**         | 22            | 12           | 17           | 26            | 19            |
| **Rebounds**       | 12            | 12           | 19           | 12            | 2             |
| **Assists**        | 12            | 12           | 10           | 6             | 2             |
| **Steals**         | 3             | 12           | 3            | 3             | 4             |
| **Blocks**         | 1             | 12           | 1            | 8             | 11            |
| **Slam Dunks**     | 1             | 7            | 15           | 5             | 1             |


Away Team:

* team name: Charlotte Hornets
* colors: Turquoise, Purple
* players:

|        Stat       |     Info          |         Info     |              Info |         Info     |         Info      |               
|:------------------:|:-----------------:|:-----------------:|:-----------------:|:---------------:|:-----------------:|
| **Player Name**  | Jeff Adrien     | Bismak Biyombo    | DeSagna Diop      | Ben Gordon      | Brendan Haywood   |
| **Number**         | 4                 | 0                 | 2                 | 8               | 33                |
| **Shoe**           | 18                | 16                | 14                | 15              | 15                |
| **Points**         | 10                | 12                | 24                | 33              | 6                 |
| **Rebounds**       | 1                 | 4                 | 12                | 3               | 12                |
| **Assists**        | 1                 | 7                 | 12                | 2               | 12                |
| **Steals**         | 2                 | 7                 | 4                 | 1               | 22                |
| **Blocks**         | 7                 | 15                | 5                 | 1               | 5                 |
| **Slam Dunks**     | 2                 | 10                | 5                 | 0               | 12                |

### Step 2: Building Functions

### Calling Functions within Functions

You'll be building a series of functions that operate on the above game dictionary to return certain information about the teams and players. Each function will operate on the game dictionary by referencing the `game_dict` function. 

For example, let's say we want to build a function, `home_team_name`, that returns the name of the home team, `"Brooklyn Nets"`. We can call the function `game_dict` inside of our `home_team_name` function and operate on the game_dict:

```python
def home_team_name():
  return game_dict()['home']['team_name']

print(home_team_name()) # "Brooklyn Nets"
```

Now that we understand how we are going to operate on the `game_dict` inside of the functions we're building, let's build those functions:

### Iterating through Nested Levels:

This lab requires us to iterate through the many levels of our nested dictionary. **Don't take your understanding of your dictionary for granted.** Every time you iterate into a new level of the dictionary, immediately place a `import pdb; pdb.set_trace()` there. Then, run your function to see what the key/value pairs of that dictionary are.

> **hint:** to run the function, call it at the bottom of your file and run the file from your terminal with the following command: `python dictionaryball.py`

Let's take a look at an example:

```python
def good_practices():
  for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
      for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)
```

Open up the `dictionaryball.py` and copy and paste the above function. Then, at the bottom of the file, call the function (`good_practices()`) and, in your terminal, run the file with `python dictionaryball.py`. Play around with the values at each level of the function until you get comfortable with the iteration. To continue to the next pdb trace, you can enter `c` in your terminal. This practice should give you a stronger sense of how we iterate through so many levels of a nested dictionary and what happens on each level. If you find yourself getting stuck in building out other functions, try using this method of adding in pdb traces to check the values of your for loop variables.

Okay, ***now*** we're ready to build out functions:

### Function Building

* Build a function, `num_points_scored` that takes in an argument of a player's name and returns the number of points scored for that player.
  * Think about where in the dictionary you will find a player's `points`. How can you iterate down into that level? Think about the return value of your function.

* Build a function, `shoe_size`, that takes in an argument of a player's name and returns the shoe size for that player.
  * Think about how you will find the shoe size of the correct player. How can you check and see if a player's name matches the name that has been passed into the function as an argument?
  
* Build a function, `team_colors`, that takes in an argument of the team name and returns a list of that teams colors.

* Build a function, `team_names`, that operates on the game dictionary to return a list of the team names.

* Build a function, `player_numbers`, that takes in an argument of a team name and returns a list of the jersey number's for that team.

* Build a function, `player_stats`, that takes in an argument of a player's name and returns a dictionary of that player's stats.
  * Check out the following example of the expected return value of the `player_stats` function:

```python
player_stats("Alan Anderson")
# {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1}
```

* Build a function, `big_shoe_rebounds`, that will return the number of rebounds associated with the player that has the largest shoe size. Break this one down into steps:
  * First, find the player with the largest shoe size
  * Then, return that player's number of rebounds
  * Remember to think about return values here. Use pdb traces to drop into your function and understand what it is returning and why.

> **hint:** If you find yourself repeating code from one function to the next, that is a good time to create a `helper function` that does just that one job for you. Then you can call that helper function in another function instead of re-writing the code you need.

## Bonus

Define functions to return the answer to the following questions:

1. Which player has the most points? Call the function `most_points_scored`.

2. Which team has the most points? Call the function `winning_team`.

3. Which player has the longest name? Call the function `player_with_longest_name`.

**Super Bonus:**

1. Write a function that returns true if the player with the longest name had the most steals. Call the function `long_name_steals_a_ton?`.
