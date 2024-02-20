print("PUP Enrollment Form")
print("\n")
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
GWA = float(input("Enter your previous general weighted average: "))
isMember = input("Are you a member of AWS Cloud Club? (yes/no): ").lower() == "yes"

print("\n")

print("Your Enrollment Form: ")
print("Name: %s" % (name))
print("Age: %d" % (age))
print("GWA: %.2f" % (GWA))
print("Awstraunot: {}".format(isMember))