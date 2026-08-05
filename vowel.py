text= input("Enter a paragraph: ").lower()

character =len(text)

space =text.count("")

word =len(text.split())

vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

#display results

print("=========text analysis======:")
print("character :",character)
print("Total words:", word)
print("Total spaces:", space)
print("Total vowels:", vowel_count)

#demonstraiting indexing
if len(text)>0:
    print("/n first character(indexing):",text[0])
    print("/n last character (indexing):",text[-1])

print("/n first 10 character(slicing):",text[:10])
print("/n last 10 character(slicing):",text[-10:])