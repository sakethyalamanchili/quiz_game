print('\n"Welcome to My Quiz"')
print('NOTE : The difficulty level increases in each stage, and your score is based on the question complexity.')
print('ALL THE BEST!')

playing = input("Do you wanna start the game? (yes/no): ")

if playing.lower() == 'no':
    print("Window closing...")
    quit()

print("Okay! Let's play ;)\n")
score = 0
count = 0
answer = input(
    'Question 1: What is the national flower of India?\n"Difficulty: Easy"\nRose\nLotus\nJasmine\nSunflower\nAnswer: ')
if answer.lower() == "lotus":
    print("Correct Answer!\n")
    score += 1
    count += 1
else:
    print("Incorrect Answer!\n")

answer = input(
    'Question 2: Who was the first woman Prime Minister of India?\n"Difficulty: Medium"\nIndira Gandhi\nSarojini Naidu\nMother Teresa\nSonia Gandhi\nAnswer: ')
if answer.lower() == "indira gandhi":
    print("Correct Answer!\n")
    score += 2
    count += 1
else:
    print("Incorrect Answer!\n")

answer = input(
    'Question 3: Who is known as the "Missile Man of India"?\n"Difficulty: Difficult"\nAtal Bihari Vajpayee\nDr APJ Abdul Kalam\nLal Bahadur Shastri\nMorarji Desai\nAnswer: ')
if answer.lower() == "dr apj abdul kalam":
    print("Correct Answer!\n")
    score += 3
    count += 1
else:
    print("Incorrect Answer!\n")

answer = input(
    'Question 4: Which Indian mathematician formulated the "Kerala School of Mathematics" and contributed to the study of calculus?\n"Difficulty: Very Difficult"\nSrinivasa Ramanujan\nAryabhata\nBhaskara\nMadhava of Sangamagrama\nAnswer: ')
if answer.lower() == "madhava of sangamagrama":
    print("Correct Answer!\n")
    score += 4
    count += 1
else:
    print("Incorrect Answer!\n")

answer = input(
    'Question 5: In which year did India become a Republic and adopt its Constitution?\n"Difficulty: Extremely Difficult"\n1947\n1950\n1952\n1960\nAnswer: ')
if answer == "1950":
    print("Correct Answer!\n")
    score += 5
    count += 1
else:
    print("Incorrect Answer!\n")

print("You got " + str(count) + " questions correct!")
print("You scored: " + str(score) + "/15")
print("KEY: 1.Lotus  2.Indira Gandhi  3.Dr APJ Abdul Kalam  4.Madhava of Sangamagrama  5.1950")