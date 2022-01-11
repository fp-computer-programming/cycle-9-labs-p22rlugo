# Ryan Lugo: RJL 1/11/22

def add_foods(table):

    # Tables/lists
    sixth_letter = []
    not_foods = []
    short_foods = []
    
    try:
        if type(table) == list:
                for i,v in enumerate(table):
                    if type(v) == str:
                        if len(v) > 5:
                            sixth_letter.append(v[5])
                        else:
                            short_foods.append(v)
                    else:
                        not_foods.append(v)
                print("Sixth_letter:",sixth_letter)
                print("Short_foods:",short_foods)
                print("Not_foods",not_foods)
        else:
            print("This is not an List! This was a:",type(table))
    except:
        print("There was an error.")
    
# add_foods(['potatoes','salsa','cherries','banana','apple'])
# add_foods(['naan','celery','buckwheat',7,'clementine'])
# add_foods(['cheeseburger',True,'chicken','rice','radish'])
