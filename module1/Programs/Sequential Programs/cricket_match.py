# maximum run scored by a player in a cricket match

# get number overs
overs = int(input("Enter the number of overs: "))

max_run = (overs - 1) * 33 + 36

print("Maximum runs scored by a player in {0} overs is {1}".format(overs, max_run))