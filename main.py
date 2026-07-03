# ========================================
# Career Readiness Checker
# Version: 1.0
# Author: Pratyusha
# ========================================

def welcome():
    print("========================================")
    print("      Career Readiness Checker")
    print("========================================")

welcome()

name=input("What is your name?")
print(f"Hello, {name}! Welcome to Career Readiness Checker.")
print()
age=int(input("What is your age?"))
year=input("What school year are you in?")
dream_company=input("What is your dream company?")
language=input("What programming languages are you learning?")
projects=int(input("How many projects have you completed?"))
github=input("Do you have a github account? (yes/no)").lower()


print()
print("========================================")
print("           YOUR PROFILE")
print("========================================")

print(f"👤 Name: {name}")
print(f"🎂 Age: {age}")
print(f"🎓 School Year: {year}")
print(f"🏢 Dream Company: {dream_company}")
print(f"💻 Programming Language: {language}")
print(f"📂 Projects Completed: {projects}")
print(f"🐙 GitHub Account: {github}")

print("========================================")


print()
print(f"Good luck, {name}! Keep working towards {dream_company}!")

print()
print("========== FEEDBACK ==========")

if age<16:
    print("Amazing that you're starting so early!")
elif age>=16 or age<=18:
    print("You're at a perfect age to build a strong portfolio.")
else:
    print("Keep building consistently and gaining experience.")

    

if projects <= 2:
    print("🌱 You're just getting started. Keep building projects!")
elif projects <= 5:
    print("🚀 Great progress! You're building a strong portfolio.")
else:
    print("🌟 Fantastic! Your portfolio is becoming very impressive.")


if github =="yes":
    print("Excellent! Keep uploading your projects.")
else:
    print("Let's create a GitHub account soon!")