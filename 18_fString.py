letter = "Hey my name is {} and I am from {}"
country = "india"
name = "bhupendra"
print(letter.format(name, country))
print(f"my name is {name} and I am from {country}")

# txt = "For only {price:.2f} dollars!"
price=49.0999
txt  = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format(price=49.0999))
print(type(f"{2*30}"))
