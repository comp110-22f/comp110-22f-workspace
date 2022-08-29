""""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730483450"

Word: str= input ("Enter a 5-character word:") 
letter: str= input ("Enter a single character:")
print ("Searching for " + letter + " in " + Word)
str=[0]==1
if Word[0] == letter:
    print(letter + "found at index 0")
str=[1]==1
if Word[1] == letter:
    print(letter + "found at index 1")
str=[2]==2
if Word[2] == letter:
     print(letter + "found at index 2")
str=[3]==3
if Word[3] == letter:
      print(letter + "found at index 3")
str=[4]==4
if Word[4] == letter:
       print(letter + "found at index 4")
else:
    if len(Word) != 5:
        print ("Error: Word must contain 5 characters")
        if len(letter) != 1:
             print ("Error: Character must be a single character")
print("Error: Word must contain 5 characters")

len(letter) != 1
print("Error: Character must be a single character")
