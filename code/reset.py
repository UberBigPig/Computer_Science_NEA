import files as save

array = []

files = ["accountLogin", "accountStats", "dateOfCompletion", "settings"]

for file in files:
    save.save(array, file)
