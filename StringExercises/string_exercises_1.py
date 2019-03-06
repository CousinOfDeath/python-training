#String exercises 1

#1. from ’bark’ create: ’b’,’a’,’r’,’k’ from ’park’ create: ’p’,’a’,’r’,’k’

print("1. from ’bark’ create: ’b’,’a’,’r’,’k’\n")

bark_characters = list("bark")

for char in bark_characters:
    print(char)

print("\nfrom ’park’ create: ’p’,’a’,’r’,’k’\n")

park_characters = list("park")

for char in park_characters:
    print(char)


#2. from ’pin’ create: ’pi’,’in’

print("\n2. from ’pin’ create: ’pi’,’in’\n")

pin = "pin"

print(pin[:2])
print(pin[1:])

#3. from ’abracadabra’ create:’abra’,’cadabra’

print("\n3. from ’abracadabra’ create:’abra’,’cadabra’\n")

abracadabra = "abracadabra"

print(abracadabra[:4])
print(abracadabra[4:])

#4. from ’four’ create: 4

print("\n4. from ’four’ create: 4\n")


print("?")

#5. from ’viisi’ create: 5

print("\n5. from ’viisi’ create: 5\n")


print("?")

#6. from ’breathe’ create: ’breath’

print("\n6. from ’breathe’ create: ’breath’\n")

breathe = "breathe"

print(breathe[:(len(breathe)-1)])

#7. from ’weight’ create: ’weigh’

print("\n7. from ’weight’ create: ’weigh’\n")

weight = "weight"

print(weight[:(len(weight)-1)])


#8. from ’weight’ create: ’eight’

print("\n8. from ’weight’ create: ’eight’\n")

weight = "weight"

print(weight[1:])

#9. from ’hearth’ create: ’earth’

print("\n9. from ’hearth’ create: ’earth’\n")

earth = "hearth"

print(earth[1:])

#10. from ’intermediate’ create: ’media’

print("\n10. from ’intermediate’ create: ’media’\n")

intermediate = "intermediate"

print(intermediate[5:10])

#11. from ’premediates’ create: ’media’

print("\n11. from ’premediates’ create: ’media’\n")

premediates = "premediates"

print(premediates[3:8])

#12. from ’grand’ and ’ma’ create: ’grandma’

print("\n12. from ’grand’ and ’ma’ create: ’grandma’\n")

grand = "grand"
ma = "ma"

print(grand + ma)


#13. from ’grand’ and ’dad’ create: ’grandad’

print("\n13. from ’grand’ and ’dad’ create: ’grandad’\n")

grand = "grand"
dad = "dad"

print(grand + dad[1:])

#14. from ’grand’ and ’ma’ create: ’grandgrandgrandma’

print("\n14. from ’grand’ and ’ma’ create: ’grandgrandgrandma’\n")

grand = "grand"
ma = "ma"

print(grand * 3 + ma)

#15. from ’grand’ and ’dad’ create: ’grandgrandgrandgrandad’

print("\n15. from ’grand’ and ’dad’ create: ’grandgrandgrandgrandad’\n")

grand = "grand"
dad = "dad"

print(grand * 4 + dad[1:])

#16. from 3 create: ’3’

print("\n16. from 3 create: ’3’\n")

num = 3

print(str(num))

#17. from 4 create: ’444’

print("\n17. from 4 create: ’444’\n")

num = 4

print(str(num) * 3)

#18. from ’Another bad example, what a good day’ create: ’Another good example, what a bad day’

print("\n18. from ’Another bad example, what a good day’ create: ’Another good example, what a bad day’\n")

original = "Another bad example, what a good day"

splitted = original.split(" ")


print(f"{splitted[0]} {splitted[5]} {splitted[2]} {splitted[3]} {splitted[4]} {splitted[1]} {splitted[6]}")