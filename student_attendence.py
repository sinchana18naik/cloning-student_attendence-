classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
attendance = (classes_attended / classes_held) * 100
print("\nClasses Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance: {:.2f}%".format(attendance))
