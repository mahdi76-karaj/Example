walk_week = {"sat": 3000, "Sun": 4000, "Mon": 4000, "Tue": 5000, "Wed": 6000, "Thu": 3000, "Fri": 1000}
walk_week_backup = walk_week.copy()
walk_week["holiday"] = 0
print("walk_week: ", walk_week)
print("walk_week_backup: ", walk_week_backup)
walk_week.update({"h": 2})
print("walk week new: ", walk_week)


# dict.fromkeys
a = ["x", "y", "w", "z"]
# a = ("x", "y", "w", "z")
b = 10

dic = dict.fromkeys(a,b)
print(dic)
#--------------------------------------