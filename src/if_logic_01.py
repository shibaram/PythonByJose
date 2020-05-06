friends = ["Dinesh", "Bob", "Sarita"]
family = ["Dunu", "Rita", "Muna"]
user_name = input("Enter your name: ")

for f in friends:
    if f == user_name:
        print(f"{user_name} is my friend")
        break

for fa in family:
    if fa == user_name:
        print(f"{user_name} is my family")
        break
    '''else:
        print(f"{user_name} is a stranger")
        break'''



