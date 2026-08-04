salary = ["$1000", "$2000", "$3000", "$4000", "$5000"]

amounts = list(map(lambda s: int(s.replace("$","")),salary))
print(amounts)
