# Dylan Cheung
# Class for each player


class Player:

    def __init__(self, Name, SkillRating, TopPercentage, Level, MostPlayed):
        self.name = str(Name)
        self.sr = str(SkillRating)
        self.topPercentage = str(TopPercentage)
        self.level = str(Level)
        self.mostPlayed = str(MostPlayed)

    def __str__(self):
        return self.name + "\n\tSkill Rating: " + self.sr + \
               "\n\tTop Percentage: " + self.topPercentage + \
               "\n\tLevel: " +  self.level + \
               "\n\tMost Played Character: " + self.mostPlayed + \
               "\n"
