musicians = ["Frank ocean", "Daniel ceaser", "Tyler the craetor"]

long_lat = ("26.2056", "28.0337")

Dict_ME = {"Height":
           "173",
           "Mass":
           "65",
           "Favourite Colour":
           "Green"}

Ask = input("Ask: ")
if "Height".upper() in Ask.upper():
    print(f"My height is {Dict_ME["Height"]}cm")

elif "Mass".upper() in Ask.upper():
    print(f"My mass is {Dict_ME["Mass"]}kg")

elif "Favourite Colour".upper() in Ask.upper():
    print(f"My fav colour is {Dict_ME["Favourite Colour"]}")

else:
    print("Invalid entry!!!")