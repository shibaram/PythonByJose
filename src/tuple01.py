my_contacts = [
    {"name": "Rabi", "phone": 8598808560, "company": "AGL Corp"},
    {"name": "Sagar", "phone": 9852365895, "company": "Infosys Corp"},
    {"name": "Dina", "phone": 7548565461, "company": "Exfo Inc"},
]
my_contacts[1]["name1"] = "Diana"
print(my_contacts[1])
my_contacts[1]["name"] = "Harish"
print(my_contacts[1])
print(my_contacts[1]["name"] + "'s phone number is :", str(my_contacts[1]["phone"]))