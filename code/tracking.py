import files
import datetime


pointsDictionary = {
	"V0": 1,
	"V1-2": 2,
	"V2-3": 5,
	"V2-4": 10,
	"V3-5": 25,
	"V4-6": 35,
	"V6-8": 50,
	"V8+": 75
	}

climbDictionary = {
    0: "V0",
    1: "V1-2",
    2: "V2-3",
    3: "V2-4",
    4: "V3-5",
    5: "V4-6",
    6: "V6-8",
    7: "V8+",
}

d2 = dict(zip(climbDictionary.values(), climbDictionary.keys()))


#load files
completedClimbs = files.load("completedClimbs")
accountStats = files.load("accountStats")

#function to add a climb to a user
def addClimb(username, difficulty, attempts):
    
    date = str(datetime.date.today())
    

    climbCounts = files.load("climbCounts")
    for user in range(0, len(climbCounts)):

        if climbCounts[user][0] == username:
            climbCounts[user][d2[difficulty] + 1] = climbCounts[user][d2[difficulty] + 1] + 1
            files.save(climbCounts, "climbCounts")



    #if array is empty
    if len(completedClimbs) == 0:
        #add to list
        completedClimbs.append([username, difficulty, attempts, date])
        
    else:
        #search for user
        for user in range(0, len(completedClimbs)):
            if completedClimbs[user][0] == username:
                #add to list
                completedClimbs[user].append(difficulty)
                completedClimbs[user].append(attempts)
                completedClimbs[user].append(date)
            else:
                #add to list
                completedClimbs.append([username, difficulty, attempts, date])

    #save changes to file
    files.save(completedClimbs, "completedClimbs")


#function to count how many points a user has
def countPoints(username):
    for user in range(0, len(completedClimbs)):
        if completedClimbs[user][0] == username:
            total = 0
            for i in range(1, len(completedClimbs[user]), 3):
                points = pointsDictionary[completedClimbs[user][i]]
                total = total + points
            if total == None:
                return 0
            return total
    return 0



def initialliseAccountStats(username):
    array = [username, 0, "", 0, "", 5]
    accountStats.append(array)
    files.save(accountStats, "accountStats")

    climbCounts = files.load("climbCounts")
    climbCounts.append([username, 0, 0, 0, 0, 0, 0, 0, 0])
    files.save(climbCounts, "climbCounts")


def changeGoal(username, goal):
    for user in range(0, len(accountStats)):
        if accountStats[user][0] == username:
            accountStats[user][5] = goal
            files.save(accountStats, "accountStats")

def calcMostComClimb(username):
    climbCounts = files.load("climbCounts")
    largest = 0
    for user in range(0, len(climbCounts)):
        if username == climbCounts[user][0]:
            for i in range(1, len(climbCounts[user])):
                if climbCounts[user][i] >= largest:
                    largest = climbCounts[user][i]
            for i in range(0, len(climbCounts[user])):
                if largest == climbCounts[user][i]:
                    return climbDictionary[i-1], largest
    return "N/A", "N/A"


    


