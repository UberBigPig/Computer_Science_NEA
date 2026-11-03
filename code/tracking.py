import files
import datetime

#load files
completedClimbs = files.load("completedClimbs")
accountStats = files.load("accountStats")

#function to add a climb to a user
def addClimb(username, difficulty, attempts):
    

    #if array is empty
    if len(completedClimbs) == 0:
        #add to list
        completedClimbs.append([username, difficulty, attempts, datetime.datetime.now()])
        
    else:
        #search for user
        for user in range(0, len(completedClimbs)):
            if completedClimbs[user][0] == username:
                #add to list
                completedClimbs[user].append(difficulty)
                completedClimbs[user].append(attempts)
            else:
                #add to list
                completedClimbs.append([username, difficulty, attempts])

    #save changes to file
    files.save(completedClimbs, "completedClimbs")


#function to count how many points a user has
def countPoints(username):
    for user in range(0, len(completedClimbs)):
        if completedClimbs[user][0] == username:
            total = 0
            for i in range(2, len(completedClimbs[user]), 3):
                points = int(completedClimbs[user][i])
                total = total + points
            return total


def initialliseAccountStats(username):
    array = [username, 0, "", 0, "", 5]
    accountStats.append(array)


#def changeGoal()