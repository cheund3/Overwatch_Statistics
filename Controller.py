# Dylan Cheung
# Overwatch Stats for Zoo Brothers
from Stats import Stats


# Input is an array of usernames
def update(info, input):
    for i in input:
        info.add(i[0], i[1])


if __name__ == "__main__":
    gameInfo = Stats()
    players = []

    # To add player, parameters are (<username> , <xbox/ps4/pc>)
    # The information for each player is added to the array "players"
    #      in the form of a tuple
    # Examples are below for users important to me
    players.append(("henhen52", "xbox"))
    players.append(("Incentives", "xbox"))
    players.append(("Pand3mic2all", "xbox"))
    players.append(("Fang121212", "xbox"))
    players.append(("iradiov", "xbox"))

    # Program currently only works for xbox users. Will update later
    #players.append(("cheunga-1388", "pc"))
    update(gameInfo, players)
    gameInfo.printInfo()
    gameInfo.add()

