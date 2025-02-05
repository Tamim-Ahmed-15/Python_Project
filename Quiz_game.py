questions = (
    "1.Which data structure uses the principle of LIFO?: ",
    "2.Time complexity Binary Search: ",
    "3.Which of the following is NOT a type of linked list?: ",
    "4.Which sorting algorithm has the best average-case time complexity?: ",
    "5.A graph with no cycles is called a: ",
    "6.Which data structure is used to implement a priority queue efficiently?: ",
    "7.Which of these is NOT a linear data structure?: ",
    "8.Most efficient for large datasets: ",
    "9.Which of the following is a linear data structure?: ",
    "10.Which of the following data structures finds its use in recursion?: ")


options = (
    ("A. Queue", "B. Stack", "C. Linked List", "D. Tree"),
    ("A. O(n)", "B. O(n^2)", "C. O(log n)", "D. O(1)"),
    ("A. Singly Linked List", "B. Doubly Linked List", "C. Circular Linked List", "D.  Binary Tree"),
    ("A. Bubble Sort", "B. Insertion Sort", "C. Merge Sort", "D. Selection Sort"),
    ("A. Complete Graph", "B. Directed Graph", "C. Tree", "D. Weighted Graph"),
    ("A.  Array", "B. Linked List", "C. Heap", "D. Stack"),
    ("A. Array", "B. Linked List", "C. Queue", "D. Tree"),
    ("A. Bubble Sort", "B. Insertion Sort", "C. Quick Sort", "D. Selection Sort"),
    ("A. Array", "B. AVL Tree", "C. Binary Tree", "D. Graph"),
    ("A. Stack", "B. Array", "C. Linked List", "D. Queue"),)


Answers = ("B", "C", "D", "C", "C","C","D","C","A","A")
Guesses = []
score = 0
question_num = 0
r8_count=0

play=input("Do you want to play? (yes/no) : ")
if play !='yes':
    print("Maybe next time! Goodbye!")
else :
    print("-"*30)
    print("Correct answer =Score+5")
    print("Wrong answer =Score-2")
    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        Guesses.append(guess)
        if guess == Answers[question_num]:
            score += 5
            r8_count+=1
            print("\n✅ Correct!")
        else:
            score-=2
            print("\n❌ INCORRECT!")
            print(f"{Answers[question_num]} is the correct answer")

        print(f"\n⭐ Current Score: {score}/50 ⭐\n")
        # print("-" * 30)
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("Answers: ", end="")
    for answer in Answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in Guesses:
        print(guess, end=" ")
    print()
    print("-"*32)
    print(f"Total correct answer : {r8_count}")
    print(f"Total wrong answer : {10-r8_count}")
    print("-"*32)
    score = int(score / len(questions) * 10)
    print(f"Your score is: {score}/50")
    if score >= 30:
        print("🎉 Congratulations! You passed 🎉")
        print("---------------------------------")
    else:
        print("Better luck next time!")
        print("----------------------")
