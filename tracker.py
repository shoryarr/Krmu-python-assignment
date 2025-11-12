# Name: Shorya
# Date: 4 Nov 2025
# Project: Daily Calorie Tracker

import datetime

print("======================================")
print(" Welcome to Daily Calorie Tracker 🥗 ")
print("======================================")
print("This tool helps you record your meals and track your daily calorie intake.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

# get number of meals with simple validation
while True:
    try:
        num_meals = int(input("How many meals did you have today? (enter 0 if none) "))
        if num_meals < 0:
            print("Please enter 0 or a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number (e.g. 3).")

# collect meals
for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name: ").strip() or f"Meal{i+1}"
    # get calories with simple validation
    while True:
        try:
            cal_value = float(input(f"Enter calories for {meal_name}: "))
            if cal_value < 0:
                print("Calories can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for calories (e.g. 350 or 350.5).")
    meals.append(meal_name)
    calories.append(cal_value)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = 0.0
if len(calories) > 0:
    average_calories = total_calories / len(calories)

# get daily limit (validate)
while True:
    try:
        daily_limit = float(input("\nEnter your daily calorie limit (e.g. 2000): "))
        if daily_limit < 0:
            print("Limit can't be negative. Try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number for the limit.")

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status = "⚠️ You have exceeded your daily calorie limit!"
else:
    status = "✅ You are within your daily calorie limit. Good job!"

# Task 5: Neatly Formatted Output
print("\n=========== Calorie Summary ===========")
print(f"{'Meal Name':<15}\tCalories")
print("----------------------------------------")

if len(meals) == 0:
    print("(No meals recorded)")
else:
    for i in range(len(meals)):
        # calorie displayed without unnecessary decimals when whole
        cal_display = int(calories[i]) if calories[i].is_integer() else round(calories[i], 2)
        print(f"{meals[i]:<15}\t{cal_display}")

print("----------------------------------------")
total_display = int(total_calories) if float(total_calories).is_integer() else round(total_calories, 2)
avg_display = int(average_calories) if float(average_calories).is_integer() else round(average_calories, 2)
print(f"{'Total:':<15}\t{total_display}")
print(f"{'Average:':<15}\t{avg_display}")
print("----------------------------------------")
print(status)

# Task 6 (Bonus): Save Session Log to File
save = input("\nDo you want to save this session? (yes/no): ").strip().lower()
if save in ("yes", "y"):
    filename = "calorie_log.txt"
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Daily Calorie Tracker Log\n")
            f.write(f"Date: {now_str}\n\n")
            f.write(f"{'Meal Name':<15}\tCalories\n")
            f.write("----------------------------------------\n")
            if len(meals) == 0:
                f.write("(No meals recorded)\n")
            else:
                for i in range(len(meals)):
                    f.write(f"{meals[i]:<15}\t{calories[i]}\n")
            f.write("----------------------------------------\n")
            f.write(f"Total:\t\t{total_calories}\n")
            f.write(f"Average:\t{average_calories:.2f}\n")
            f.write("----------------------------------------\n")
            f.write(status + "\n")
        print(f"Session saved successfully as '{filename}'.")
    except Exception as e:
        print("Error saving file:", e)
else:
    print("Session not saved. Goodbye!")

print("\nThanks for using the Daily Calorie Tracker! 🍎")
