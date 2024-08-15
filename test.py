title = "Experience"
content = {
    "Frontend Development": ["HTML", "PHP", "CSS", "SCSS", "TAILWIND", "JavaScript"],
    "Backend Development": ["PYTHON", "MySQL", "GIT", "MyPHPAdmin"],
    "Video Editing": ["PhotoShop", "PremierPro", "AfterEffects", "Davinci Resolve 18", "Illustrator"],
    "Cybersecurity": ["Ethical Hacking", "Blue Hat"]
}

# Print the title
print(title)
print()

# Print the paragraphs with bullet points for each skill set
for category, skills in content.items():
    print(f"{category}:")
    for skill in skills:
        print(f" - {skill}")
    print()
