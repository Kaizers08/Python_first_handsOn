grades = int(input("Please input a grade: "))

if grades > 100 or grades < 0:  # ✅ Stops if invalid
    print("Invalid grade! Program stopped.")
else:
    if 98 <= grades <= 100:
        print("With Highest Honors")
    elif 95 <= grades <= 97:
        print("With High Honors")
    elif 90 <= grades <= 94:
        print("With Honors")
    elif 75 <= grades <= 89:
        print("Passed")
    else:
        print("Failed")
