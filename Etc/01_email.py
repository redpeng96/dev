
names = ["111", "222", "333", "444", "555"]


for name in names:
    with open(f"{name}.txt", "w", encoding="utf8") as email:
        contents = open("contents.txt", "r", encoding="utf8").read()
        email.write(contents)
