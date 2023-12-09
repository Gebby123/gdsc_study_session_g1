
#for quetion number one 



for i in range(0,100):
    if i<=9:
        print(f"0{i}",end=',')
        
    else:
        print(i, end=',')   
    
   
    #quation number two 
character = input("\n Enter a character: ")

# Check if the entered character is a single character and not a vowel
if len(character) == 1 and character.lower() not in 'aeiou':
    for i in range(1, 10):
        if i % 2 !=0:
              line = character * i      
              print(line)
else:
    print("Invalid input! Please enter a single consonant character.")
 
 
 # quation number 3 palindrom number   examples are Radar
# Level ,Civic,Deified,Rotator,Madam,Noon


word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Check if the original word is equal to its reversed version
if word == reversed_word:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
    
  # quetion number 4
even_sum = 0
count_replaced = 0

for num in range(1, 51):
    if num % 2 == 0:
        even_sum += num
        if num % 3 == 0:
            print("Three")
            count_replaced += 1
        elif num % 5 == 0:
            print("Five")
            count_replaced += 1
        else:
            print(num)
    else:
        print(num)

print("Sum of even numbers:", even_sum)
print("Count of numbers replaced:", count_replaced)

