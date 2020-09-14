import re

def print_match(m):
    if m:
        print("GROUP : ", m.group())
        print("STRING : ", m.string)
        print("START index : ", m.start())
        print("END index : ", m.end())
        print("SPAN : ", m.span())
    else:
        print("NO MATCH")

p = re.compile("ca.e")

# . : one letter (ca.e) = case, cafe, cave
# ^ : start of word (^ca) = casecade, cake, cale
# $ : end of word (ca$) = osca, nasca

#m = p.match("casse")
#m = re.compile("ca.e").search("meaningle cases ensive")
#print_match(m)

lst = p.findall("good care giver cares more")
print(lst[1], lst[0])