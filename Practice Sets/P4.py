name = input("Enter Your name: ")

print(f"Good Morning, {name} ")

letter = '''Hey <|Name|>,\t
Is your birthday on <|Day|>'''

print(letter.replace("<|Name|>","Sushree").replace("<|Day|>","Saturday"))