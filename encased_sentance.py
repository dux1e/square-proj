sentance = input("Enter sentance to be encased: ")


top_bot = "+" + "-" * (len(sentance)+2) + "+"
middle = "| " + sentance + " |"

print(top_bot)
print(middle)
print(top_bot)

# +-------------+
# | Hello World |
# +-------------+