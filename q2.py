
name = input("Write your full name: ").strip()

nameparts = name.split()

firstname = nameparts[0][0].capitalize()
lastname = nameparts[-1:0].capitalize()

print("Your initials are:", firstname + "." + lastname)
