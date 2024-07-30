print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n ") # What is your name?
name2 = input("What is their name?\n ") # What is their name?

#Creating counters...
true_counter = 0
love_counter = 0

#Testing first entry for 'True Love' letters
for i in name1.lower():
  if i == 't':
    true_counter +=1
  if i == 'r':
    true_counter +=1
  if i == 'u':
    true_counter +=1
  if i == 'e':
    true_counter +=1
  if i == 'l':
    love_counter +=1
  if i == 'o':
    love_counter +=1
  if i == 'v':
    love_counter +=1
  if i == 'e':
    love_counter += 1

#Testing second entry
for i in name2.lower():
  if i == 't':
    true_counter +=1
  if i == 'r':
    true_counter +=1
  if i == 'u':
    true_counter +=1
  if i == 'e':
    true_counter +=1
  if i == 'l':
    love_counter +=1
  if i == 'o':
    love_counter +=1
  if i == 'v':
    love_counter +=1
  if i == 'e':
    love_counter += 1
#Concatenate and converting back into string...
true_love_score = int(str(true_counter) + str(love_counter))

if true_love_score < 10 or true_love_score > 90:
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score > 40 and true_love_score < 50:
  print(f"Your score is {true_love_score}, you are alright together.")
else: print(f"Your score is {true_love_score}.")


#NOTES FROM LESSON: In the proposed solution, the code is not as clean as it could be.
#For example, I brute forced counting through the names, but i could have used the count()
#method. Also, I could have combined the names from the start and ran through only once.

#Overall, I found this to be a great exercise because i won't always remember that Python
#has shortcuts. Optimization happens after making sure the code is working.
