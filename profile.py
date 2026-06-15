def get_profile():
    return {
        "name": "ТВОЕ ИМЯ",
        "group": "ТВОЯ ГРУППА",
        "role": "student",
        "skills": ["Git", "VS Code", "Python"]
    }

def print_profile():
    profile = get_profile()
    print(f"Студент: {profile['name']}")
    print(f"Группа: {profile['group']}")
    print("Навыки:", ", ".join(profile["skills"]))
