# GradeBook Analyzer - Super Basic Version
# Name: [Your Name]
# Date: 22 Nov 2025

import csv # Still needed for CSV
# Removing 'statistics' to force manual calculation of median
# Note: This is an easier method than implementing a sorting algorithm

# --- Data Input Function (Simplified) ---
def get_data(choice):
    marks = {}
    if choice == '1':
        print("\n--- Manual Entry ---")
        while True:
            name = input("Enter name (or 'done'): ").strip()
            if name.lower() == 'done':
                break
            try:
                score = int(input(f"Score for {name}: ").strip())
                if 0 <= score <= 100:
                    marks[name] = score
                else:
                    print("Score out of range (0-100).")
            except ValueError:
                print("Bad score.")
    
    elif choice == '2':
        filename = input("Enter CSV file name: ").strip()
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        name = row[0].strip()
                        try:
                            score = int(row[1].strip())
                            if 0 <= score <= 100:
                                marks[name] = score
                        except ValueError:
                            pass # Skip bad data
            print(f"Loaded {len(marks)} records.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            
    return marks

# --- Main Logic / CLI Loop ---

def main():
    print("--- Basic GradeBook Analyzer ---")
    
    while True:
        print("\nMenu: 1. Manual | 2. CSV | 3. Exit")
        choice = input("Select: ").strip()
        
        if choice == '3':
            print("Done.")
            break
        
        marks_data = get_data(choice)
        
        if not marks_data:
            if choice != '3':
                print("No valid data loaded. Try again.")
            continue

        # Convert dictionary values to a list for easier calculations (Task 3)
        scores_list = list(marks_data.values())
        
        print("\n" + "*"*25)
        print("  ANALYSIS SUMMARY")
        print("*"*25)

        # 1. Statistical Analysis (Task 3)
        
        # Average (Mean)
        if scores_list:
            avg = sum(scores_list) / len(scores_list)
        else:
            avg = 0
            
        # Median (Manual-ish calculation - relies on list sorting)
        scores_list.sort()
        n = len(scores_list)
        if n % 2 == 1:
            median = scores_list[n // 2]
        elif n > 0:
            mid1 = scores_list[n // 2 - 1]
            mid2 = scores_list[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = 0
            
        print(f"Total Students: {n}")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score: {median:.2f}")
        print(f"Max Score: {max(scores_list) if n > 0 else 0}")
        print(f"Min Score: {min(scores_list) if n > 0 else 0}")
        
        # 2. Grade Assignment and Distribution (Task 4)
        grades = {}
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

        print("\n--- Grade Distribution ---")
        for name, score in marks_data.items():
            
            # Use if-elif-else directly (no separate function)
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"
            
            grades[name] = grade
            grade_counts[grade] += 1

        print("Grade | Count")
        print("------|------")
        for g, c in grade_counts.items():
            print(f"  {g}   |   {c}")
            
        # 3. Pass/Fail Filter (Task 5)
        PASS_SCORE = 40 
        
        # List comprehensions
        passed_students = [name for name, score in marks_data.items() if score >= PASS_SCORE]
        failed_students = [name for name, score in marks_data.items() if score < PASS_SCORE]
        
        print(f"\n--- Pass/Fail Summary (Pass Mark: {PASS_SCORE}) ---")
        print(f"Passed: {len(passed_students)} ({', '.join(passed_students)})")
        print(f"Failed: {len(failed_students)} ({', '.join(failed_students)})")
        
        print("\nFull Report:")
        print("{:<15} {:<5}".format("Name", "Grade"))
        print("-" * 20)
        # Using sorted marks_data keys for output
        for name in sorted(marks_data.keys()):
             print("{:<15} {:<5}".format(name, grades[name]))
        
        print("*"*25)


if __name__ == "__main__":
    main()













    