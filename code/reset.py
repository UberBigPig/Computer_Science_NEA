import files as save

array = []

files = ["accountLogin", "accountStats", "dateOfCompletion", "settings", "completedClimbs"]

for file in files:
    save.save(array, file)
