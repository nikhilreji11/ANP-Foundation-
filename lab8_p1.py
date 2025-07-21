#Enter marks for 5 subjects. Raise an exception if any mark is below 0 or above 100.
#Requirement:
#Use raise for invalid mark
#Handle using try-except


def get_marks():
    marks = []
    for i in range(1, 6):
        try:
            mark = int(input(f"Enter marks for subject {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Invalid mark! Marks must be between 0 and 100.")
            marks.append(mark)
        except ValueError as e:
            print("Error:", e)
            return 
    print("\nAll valid marks entered:", marks)
get_marks()
