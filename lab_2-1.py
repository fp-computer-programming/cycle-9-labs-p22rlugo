# Ryan Lugo: RJL 1/10/22

def double_stuff(table):

    if type(table) == list:
        for i,v in enumerate(lst):
            lst[i] = v * 2
    else:
        print("This is not a list of items, make a list of items to send for it to work.")
    return lst

lst = [6,50,5.4,"6.9"]

print(double_stuff(lst) == [12,100,10.8,"6.96.9"])