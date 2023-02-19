print("####")
print("|  |")
print("|  |")
print("####")

length = int(input("Enter length "))
height = int(input("Enter height "))

top_bot = "+" + "-" * (length-2) + "+"
middle = "|" + " " * (length-2) + "|"

print(top_bot)
for x in range(height-2):
    print(middle)
print(top_bot)

# +-------------+
# | Hello World |
# +-------------+