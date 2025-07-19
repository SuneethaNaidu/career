from career_data import career_data

for role, details in career_data.items():
    print(f"\nRole: {role}")
    print("Skills:", ", ".join(details["skills"]))
    print("Projects:", ", ".join(details["projects"]))
    print("Resources:")
    for link in details["resources"]:
        print(" -", link)
