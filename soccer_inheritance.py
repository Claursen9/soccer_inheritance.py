# AUTHOR: Chad Laursen
# Description: This program simulates a soccer league scenario. 
# It allows the user to input their team name, sponsor information, 
# and the number of games played. It then simulates the games, 
# calculates wins, losses, goals scored, and goals allowed, 
# and displays the season's results. It also allows the user to 
# view the status of individual games played.

# Read ALL OF THE INSTRUCTIONS before starting please!
# everywhere I put "pass", delete pass and then write your own code.


# needed to generate random scores
import random

class SoccerTeam:
    # constructor. Creates the soccerTeam object when called
    def __init__(self, team_name):
        self.team_name = team_name
        self.wins = 0
        self.losses = 0
        self.goals_scored = 0   #SoccerTeam.generateScore
        self.goals_allowed = 0

    # generates the score with the standard chance
    #@staticmethod
    def generateScore(self):
        if not hasattr(self, "_score_count"):
            self._score_count = 1
        else:
            self._score_count += 1
        return self._score_count
        
    def seasonStatus(self):
        # depending on the win rate, display different final messages.
        if self.wins / (self.wins + self.losses) >= .75:
            message = "Qualified for the NCAA Women's Soccer Tournament"
        elif self.wins / (self.wins + self.losses) >= .5:
            message = "You had a good season"
        else:
            message = "Your team needs to practice!"
        return message
    
# here create a class called SponsoredTeam that inherits from SoccerTeam. You need a constructor, and a generateScore method and seasonStatus method
# remember that you can call super().__init__() to get the instance variables from SoccerTeam. in your constructor.
class SponsoredTeam(SoccerTeam):
    def __init__(self, team_name):
        super().__init__(team_name)
    def generateScore(self):
        """Simulates a game and updates wins/losses."""
        if random.random() > 0.5: # simulate win
            self.wins+= 1 
            return "Win!"
        else: 
            self.losses+= 1
            return "Loss!"
        
    def seasonStatus(self):
        """Overrides the seasonStatus method from SoccerTeam."""
        original_status = super().seasonStatus() #get the base status
        if self.wins + self.losses > 10:
            return f"{original_status} (Sponsored by our amazing partners!)" 
        else:
            return original_status



# here create a class called Game. It doesn't inhereit anything, but should have a constructor that stores a home team, 
# and an away team, as well as a method for gameStatus
class Game:
    def __init__(self, home_team, away_team, home_score, away_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    def gameStatus(self):
        return f"{self.home_team.team_name} {self.home_score} - {self.away_team.team_name} {self.away_score}"


# get the inputs
sHomeTeamName = input("Enter the name of your team (the home team): ")
sIsSponsoredTeam = input("If your team is sponsored, enter the name of the sponsor. Otherwise enter N: ")
iNumGamesPlayed = int(input("Enter the number of teams that " + sHomeTeamName + " will play (1-10): "))

# creates a soccerTeam object and stores it in the variable homeTeam
if sIsSponsoredTeam.upper() != "N":
    homeTeam = SponsoredTeam(sHomeTeamName)
else:
    homeTeam = SoccerTeam(sHomeTeamName)

# this is creating an empty list for the away teams and an empty list for the games.
# We need to create the list outside the loop so it doesn't keep getting overwritten. Then in the loop, we just append to the list.
opponentTeamsList = []
gamesList = []

# run the loop for however many times the user entered
for game in range(1, iNumGamesPlayed +1):

    # get away team name
    sAwayTeamName = input(f"Enter the name of the away team for game {game}: " )

    # make the away team object. make sure to randomly make the away team a sponsored or normal team (50% chance)
    #randomly make the team a sponsored team or not:
    if random.random() < 0.5:
        awayTeam = SoccerTeam(sAwayTeamName)
    else:
        awayTeam = SponsoredTeam(sAwayTeamName) 
        opponentTeamsList.append(awayTeam)
    

    # generate scores for both teams by calling generateScore()
    # make sure that if they are a sponsoredTeam, the odds are better for them (see instructions)
    # if you wrote your classes correctly, that means you don't need an if statement here. The SponsoredTeam generateScore() method
    # will just overwrite the original generateScore() method.
        home_score = homeTeam.generateScore()
        away_score = awayTeam.generateScore()


    # keep generating scores if they are the same
    while home_score == away_score:
        home_score = homeTeam.generateScore()
        away_score = awayTeam.generateScore()

    
    # record goals scored & goals allowed
    # into the home team object (e.g. homeTeam.goals_scored += iHomeScore, awayTeam.goals_scored += iAwayScore, etc.)
        homeTeam.goals_scored += home_score
        homeTeam.goals_allowed += away_score

        awayTeam.goals_scored += away_score
        awayTeam.goals_allowed += home_score


    #keep track of wins and losses for the home team and away team (similar to the above code)
    if home_score > away_score: 
        homeTeam.wins += 1
        awayTeam.losses += 1
    
    elif home_score < away_score:
        homeTeam.losses += 1
        awayTeam.wins += 1
        

    # display the score for this game
    # depending on what you call your variables, something like the below:
    #print(f"{homeTeam.team_name}'s score: {iHomeScore} {sAwayTeamName}'s score: {iAwayScore}")
    
    # CRUCIAL: make sure you append your away team to the team list, and create a new game object:
    # it will likely look like the below, but depending on what you call your variables/objects it could lookdifferent.
    #opponentTeamsList.append(opponentTeam)
    #gamesList.append(Game(homeTeam, opponentTeam, iHomeScore, iAwayScore))

# At the end of the loop disply: team name, season record, goals score/allowed, and the season Status.
print(f"\nTeam Name: {homeTeam.team_name}")
print(f"Final season record: {homeTeam.wins} - {homeTeam.losses}")
print(f"Total goals scored: {homeTeam.goals_scored} - Total goals allowed: {homeTeam.goals_allowed}")
print(homeTeam.seasonStatus())

# This is a loop that will keep asking for a game number until you type exit.
# I've written most of it for you. You just need to write one morel line of code in the if statement
# to access the gamesList and call the gameStatus() method for whatever game the user inputs.
# remember that to access the first game, you would do gamesList[0]. So if they enter 1 for example, you'll have to
# translate that to 0, etc.
# once you have access to the game, you can call any method. Like gamesList[0].methodName()
gameSelector = 0
while gameSelector != "exit":
    gameSelector = input(f"\nEnter in a game number between 1 and {iNumGamesPlayed} to see the stats of that game. Otherwise type exit: ")

    if gameSelector.isdigit():
        gameSelector = int(gameSelector)
        if 1 <= gameSelector <= iNumGamesPlayed:
            print(gamesList[gameSelector-1].gameStatus())
        else:
            print("Invalid game number.") # replace pass with your own code to run the gameStatus method on the specified game!