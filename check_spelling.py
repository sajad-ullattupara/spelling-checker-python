from textblob import TextBlob

# Write a Paragraph here
words = ["Spellink Correctiom vith Python"]
corrected_words = []

for i in words:
    corrected_words.append(TextBlob(i))

print("input words :", words)
print("Corrected Words :")
for i in corrected_words:
    print(i.correct(), end=" ")
