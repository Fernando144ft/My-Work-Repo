"""
Assignment: Project 4C Hockey League BMI
@author: Fernando Parra
Professor Owen Herman
Date: November 27th to 28th 2023
"""

playerCount = 0
bmiSum = 0
largestPlayerBMI = 0
smallestPlayerBMI = 9999
largestTeamBMI = 0
smallestTeamBMI = 9999
teamCount = 0
teamSum = 0
averageTeamBMI = 0
playersDetails = {}  # The player ID and player code
heightsWeights = {}  # The height and weight for every player
categoryAndBMI = {}  # The BMI and the category for every player
avgCatTeam = {}  # Directory for the average team BMI and its category
avgCatLeague = {}  # Average and category for the league


class MaximumBMIValues:
    """Class for Underweight"""

    def __init__(self):
        self.underweightMaxBMI = None
        self.normalMaxBMI = None
        self.OverweightMaxBMI = None

    def Get(self):
        """Get all the maximum BMI values"""
        category = ["Underweight", "Normal", "Overweight"]

        """Iterate through the list to get each category"""
        for index, value in enumerate(category):
            """Exception handler"""
            while True:
                try:
                    self.bmi = float(input(f"Enter the maximum BMI value for the category {value}: "))
                    if self.bmi > 0:
                        print(f"{value} BMI maximum value set to {self.bmi} \n")
                        if index == 0:
                            self.underweightMaxBMI = self.bmi
                        elif index == 1:
                            self.normalMaxBMI = self.bmi
                        else:
                            self.OverweightMaxBMI = self.bmi
                        break
                    else:
                        print("Number has to be greater than 0")
                except ValueError:
                    print("Invalid Input")


class DetailInput:
    """Get and manage all Detail input"""

    def __init__(self):
        self.team = None
        self.playerID = None
        self.playerCode = None
        self.processedBMI = None

    def GetTeam(self):
        """Get the name of the team or terminate the code"""
        self.team = input("Enter team name or 'XXX' to terminate: ").upper()
        if self.team != "XXX":
            print("Once the name of your team is confirmed it can't be changed")
            comfirmation = input("Do you want to keep the name of your team (e.g yes/no): ").lower()
            if comfirmation == "yes":
                self.team = self.team.capitalize()
            else:
                self.GetTeam()

    def GetPlayerID(self):
        """Get the player ID or terminate the input of players"""
        global playerCount

        while True:
            self.playerID = input("\nEnter a player ID (e.g = 101) or -1 to terminate: ")

            if len(self.playerID) == 3 and self.playerID.isdigit():
                playerCount += 1
                break
            elif self.playerID == "-1":
                break
            else:
                print("Invalid Input")

    def GetPlayerCode(self):
        """Get the player code & output the current ID and code"""
        while True:
            try:
                self.playerCode = input("Enter the player code (e.g = 70180): ")
                if len(self.playerCode) == 5 and self.playerCode.isdigit():
                    playersDetails[self.playerID] = self.playerCode
                    for key, value in playersDetails.items():
                        if key == self.playerID:
                            print(f"\nPlayer {key}, set with code {value}")
                    break
            except ValueError:
                print("Invalid Input")

    def ProcessBMI(self):
        """Decode the code, calculate the BMI, and set update working storage"""
        global bmiSum, largestPlayerBMI, smallestPlayerBMI

        """Manage the BMI code first"""
        height = self.playerCode[:2]
        weight = self.playerCode[2:]
        self.processedBMI = (int(weight) / (int(height) ** 2)) * 703
        self.processedBMI = f"{self.processedBMI:.1f}"
        self.processedBMI = float(self.processedBMI)

        """Manage the working storage"""
        bmiSum = bmiSum + self.processedBMI
        if largestPlayerBMI < self.processedBMI:
            largestPlayerBMI = self.processedBMI
        if smallestPlayerBMI > self.processedBMI:
            smallestPlayerBMI = self.processedBMI

    def ProcessHeightWeight(self):
        """Decode and assemble the player height and weight"""
        for key, value in playersDetails.items():
            if key == self.playerID:
                codedHeight = value[:2]
                feet = int(codedHeight) / 12
                inches = int(codedHeight) % 12
                codedWeight = value[2:]
                heightsWeights[f"{str(feet)[0]} Feet {inches} Inches"] = f"{codedWeight} lbs"
                break


"""Process"""


def AssignCategories(bmi, dict):
    """Assign the BMI with the correct category"""
    if bmi > userBMIValues.OverweightMaxBMI:
        dict[bmi] = "Obese"
    elif bmi > userBMIValues.normalMaxBMI:
        dict[bmi] = "Overweight"
    elif bmi > userBMIValues.underweightMaxBMI:
        dict[bmi] = "Normal"
    else:
        dict[bmi] = "Underweight"


def ProcessTeam():
    """Manage Team level average BMI"""
    global teamSum, largestTeamBMI, smallestTeamBMI

    averageTeamBMI = bmiSum / playerCount
    teamSum = teamSum + averageTeamBMI
    AssignCategories(averageTeamBMI, avgCatTeam)

    """Update League largest and smallest variables"""
    if largestTeamBMI < averageTeamBMI:
        largestTeamBMI = averageTeamBMI
    if smallestTeamBMI > averageTeamBMI:
        smallestTeamBMI = averageTeamBMI


def ProcessLeague():
    """Manage League level average BMI"""
    averageBMILeague = teamSum / teamCount
    averageBMILeague = f"{averageBMILeague:.1f}"
    averageBMILeague = float(averageBMILeague)
    AssignCategories(averageBMILeague, avgCatLeague)


"""Outputs"""


def OutputDetail():
    """Output player level detail"""
    for (key, value), (key1, value1), (key2, value2) in zip(playersDetails.items(), heightsWeights.items(),
                                                            categoryAndBMI.items()):
        print(f"{key}: {key1}, {value1}, {key2}, {value2}")


def OutputTeamLevelSum(team, bmiDict):
    """Output team level summary"""
    for avg, cat in bmiDict.items():
        print(f"\nTeam Level: {team}, Average = {avg:.1f}, {cat}, Largest = {largestPlayerBMI}, Smallest = {smallestPlayerBMI}\n")


def OutputLeagueLevelSum():
    """Output league level summary"""
    last = ""
    for avg, cat in avgCatLeague.items():
        last = (f"\nLeague Level: Average = {avg}, {cat}, Largest = {largestTeamBMI}, Smallest = {smallestTeamBMI}")
    print(last)


"""Reset for players"""


def ResetPlayerVariables():
    """Set player variables back to default"""
    global playerCount, bmiSum, largestPlayerBMI, smallestPlayerBMI, playersDetails, heightsWeights, categoryAndBMI

    playerCount = 0
    bmiSum = 0
    largestPlayerBMI = 0
    smallestPlayerBMI = 9999
    playersDetails.clear()
    heightsWeights.clear()
    categoryAndBMI.clear()
    avgCatTeam.clear()


if __name__ == '__main__':
    print("Fernando Parra\nHockey League BMI\nWritten from November 27th to 28th\n")
    userBMIValues = MaximumBMIValues()
    userBMIValues.Get()
    user = DetailInput()

    while True:
        """Iterate or terminate the program"""
        user.GetTeam()
        if user.team == "XXX":
            """Print League Level Sum Output"""
            ProcessLeague()
            OutputLeagueLevelSum()
            break
        else:
            teamCount += 1

        while True:
            user.GetPlayerID()
            if user.playerID == "-1":
                """Print Team Level Sum Output"""
                ProcessTeam()
                OutputTeamLevelSum(user.team, avgCatTeam)
                ResetPlayerVariables()
                break
            else:
                user.GetPlayerCode()
                user.ProcessHeightWeight()
                user.ProcessBMI()
                AssignCategories(user.processedBMI, categoryAndBMI)
                OutputDetail()
