def total_goals(laliga, copa_del_rey, champions):
    return laliga + copa_del_rey + champions


laliga_goals = 30
copa_del_rey_goals = 6
champions_goals = 10


total = total_goals(laliga_goals, copa_del_rey_goals, champions_goals)

print(total)  