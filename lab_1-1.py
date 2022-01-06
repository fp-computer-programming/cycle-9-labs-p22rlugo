# Ryan Lugo: RJL 1/6/22


def positive_name():
    rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin" "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]


    for lists in rows:
        for names in lists:
            
            if (names.endswith("s")):
                print("{0}\'s".format(names))
            else:
                print("{0}s".format(names))
            

positive_name()