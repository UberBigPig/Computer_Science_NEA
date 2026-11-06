import files as save

#create blank array
array = []

#create files that will be created/reset
files = ["accountLogin", "accountStats", "dateOfCompletion", "settings", "completedClimbs", "climbCounts"]

#save files
for file in files:
    save.save(array, file)
