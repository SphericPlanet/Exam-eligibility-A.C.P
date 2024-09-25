x = int(input("Enter the total number of working days (x): "))
y = int(input("Enter the total number of absent days (y): "))

total_attended_days = x - y

if x > 0:
    attendance_percentage = (total_attended_days / x) * 100
else:
    print("Total working days must be greater than zero.")
    exit()

print("Attendance Percentage: {:.2f}%".format(attendance_percentage))

if attendance_percentage < 75:
    print("You are not eligible to sit in the exam.")
else:
    print("You are eligible to sit in the exam.")
