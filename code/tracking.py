import files

#function to add a climb to a user
def addClimb(username, difficulty, attempts):
    #load file
    completedClimbs = files.load("completedClimbs")

    #if array is empty
    if len(completedClimbs) == 0:
        #add to list
        completedClimbs.append([username, difficulty, attempts])
        
    else:
        #search for user
        for user in range(0, len(completedClimbs)):
            if completedClimbs[user][0] == username:
                #add to list
                completedClimbs[user].append(difficulty, attempts)
            else:
                #add to list
                completedClimbs.append([username, difficulty, attempts])

    #save changes to file
    files.save(completedClimbs, "completedClimbs")
    print(completedClimbs)
    
