# String exercises 2
# Using one liners, do:

# 1. Find index of the first ’o’ in ’Anomalocaris’.

print("\n1. Find index of the first ’o’ in ’Anomalocaris’.\n")

print("Anomalocaris".index("o"))

# 2. Find index of the first ’r’ in ’Anomalocaris’.

print("\n2. Find index of the first ’r’ in ’Anomalocaris’.\n")

print("Anomalocaris".index("r"))

# 3. Find index of the last ’on’ in ’Waging on the purple drone’

print("\n3. Find index of the last ’on’ in ’Waging on the purple drone’\n")

print("Waging on the purple drone".rindex("on"))

# 4. Find index of the last ’z’ in ’Superficial’

print("\n4. Find index of the last ’z’ in ’Superficial’\n")

print("Superficial".rfind("z"))

# 5. Find index of first ’a’ in the second half of the sentence
# ’There truly is a dazzling bright world out there, waiting for us to explore.’

print("\n5. Find index of first ’a’ in the second half of the sentence ’There truly is a dazzling bright world out there, waiting for us to explore.’\n")

original = "There truly is a dazzling bright world out there, waiting for us to explore."

print(original.index("a", original.index(",")))

# 6. Find index of the last ’a’ in the first half of the sentence
# ’There truly is a dazzling bright world out there, waiting for us to explore.’

print("\n6. Find index of the last ’a’ in the first half of the sentence ’There truly is a dazzling bright world out there, waiting for us to explore.’\n")

original = "There truly is a dazzling bright world out there, waiting for us to explore."

print(original.rindex("a", 0, original.index(",")))

# 7. Create ’42’ from ’91342391’ (remove trailing and leading characters)

print("\n7. Create ’42’ from ’91342391’ (remove trailing and leading characters)\n")

print("91342391".lstrip("913").rstrip("391"))

# 8. Create ’Warning’ from ’–== Warning! ==–’

print("\n8. Create ’Warning’ from ’–== Warning! ==–’\n")

print("–== Warning! ==–".lstrip("–== ").rstrip(" ==–"))

# 9. Create ’–== Error’ from ’–== Error! ==–’

print("\n9. Create ’–== Error’ from ’–== Error! ==–’\n")

print("–== Error! ==–".rstrip(" ==–"))

# 10. Create ’Success! ==–’ from ’–== Success! ==–’

print("\n10. Create ’Success! ==–’ from ’–== Success! ==–’\n")

print("–== Success! ==–".lstrip("–== "))

# 11. Replace all ’dog’ with ’cat’ in ’Changing your dog for a bird? Some dog-lover you are.’

print("\n11. Replace all ’dog’ with ’cat’ in ’Changing your dog for a bird? Some dog-lover you are.’\n")

print("Changing your dog for a bird? Some dog-lover you are.".replace("dog", "cat"))

# 12. Replace the first ’o’ with ’a’ in ’Being bold has some uses.’

print("\n12. Replace the first ’o’ with ’a’ in ’Being bold has some uses.’\n")

original = "Being bold has some uses."

print(original.replace("o", "a", 1))

# 13. Create ’–== ERROR! ==–’ from ’–== Error! ==–’

print("\n13. Create ’–== ERROR! ==–’ from ’–== Error! ==–’\n")

print("–== Error! ==–".upper())

# 14. Create ’Abraham Lincoln’ from ’abraham lincoln’

print("\n14. Create ’Abraham Lincoln’ from ’abraham lincoln’\n")

print("abraham lincoln".title())

# 15. Create ’readable’ from ’rEaDaBlE’

print("\n15. Create ’readable’ from ’rEaDaBlE’\n")

print("rEaDaBlE".lower())

# 16. Create ’First word is capitalized’ from ’first word is capitalized’

print("\n16. Create ’First word is capitalized’ from ’first word is capitalized’\n")

print("first word is capitalized".capitalize())

# 17. How many ’o’ are there in ’a loooooooooooooooooooong word?’

print("\n17. How many ’o’ are there in ’a loooooooooooooooooooong word?’\n")

print("a loooooooooooooooooooong word?".count("o"))

# 18. How many zeros in godzillion? (Let godzillion be 100000000000000000000000000000000000000000)

print("\n18. How many zeros in godzillion? (Let godzillion be 100000000000000000000000000000000000000000)\n")

print("100000000000000000000000000000000000000000".count("0"))

# 19. How many ’n’ are there in the first half of the string
# ’Something out of nothing? I really doubt we can do it anytime soon..’



# 20. Replace all ’0’ except the first with ’9’ in godzillion (see definition above).
# 21. From ’what,if,we,have,no,choice?....’ create ’What if we have no choice?’
