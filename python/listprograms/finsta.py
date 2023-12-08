all_users=["Mohanlal",
            "Mammootty",
            "Prithviraj Sukumaran",
            "Dulquer Salmaan",
            "Nivin Pauly",
            "Fahadh Faasil",
            "Dileep",
            "Jayasurya",
            "Vineeth Sreenivasan",
            "Tovino Thomas",
            "Kunchacko Boban",
            "Nani",
            "Asif Ali",
            "Unni Mukundan",
            "Sreenivasan",]


Dileep_friends=["Mohanlal","Jayasurya","kunchacko Boban"]

# list suggestions for dileep

for u in all_users:
    if u not in Dileep_friends:
        print(u)
