import string

print("STUDY BUDDY")

# Letters used for multiple choice options (A, B, C, etc.)
letters = list(string.ascii_uppercase)

# Stores all flashcards created by the teacher
flashcards = []

# Stores student info so it can be remembered when switching modes
name = ""
section = ""

# Main program loop that keeps running until user exits
while True:

    print("\nCHOOSE MODE")
    print("1 - Teacher")
    print("2 - Student")
    print("3 - Exit")

    choice = input("Enter choice: ").strip()

    # Exit the program
    if choice == "3":
        print("Program ended.")
        break

    # Teacher mode for creating flashcards
    elif choice == "1":

        print("\nTEACHER MODE")

        # Choose type of flashcard system
        mode = input("Select mode (normal, mc, mindmap): ").lower().strip()

        # Validate input
        if mode not in ["normal", "mc", "mindmap"]:
            print("Invalid mode.")
            continue

        print("Type 'switch' to stop adding flashcards")

        # Loop for creating flashcards
        while True:

            question = input("Enter question/topic: ")

            # Stop teacher input
            if question.lower() == "switch":
                break

            # Normal flashcard (question and answer)
            if mode == "normal":

                answer = input("Enter answer: ")

                if answer.lower() == "switch":
                    break

                flashcards.append(["normal", question, answer])
                print("Saved")

            # Multiple choice flashcard
            elif mode == "mc":

                options = []
                option_letters = []

                i = 0

                print("Type 'done' to finish options")

                while True:

                    option = input("Option " + letters[i] + ": ")

                    if option.lower() == "done":
                        break

                    options.append(option)
                    option_letters.append(letters[i])
                    i += 1

                answer = input("Correct letter: ").upper().strip()

                flashcards.append(["mc", question, options, option_letters, answer])

                print("Saved")

            # Mindmap flashcard (branches under a topic)
            elif mode == "mindmap":

                branches = []

                print("Type 'done' to finish branches")

                while True:

                    branch = input("Branch: ")

                    if branch.lower() == "done":
                        break

                    branches.append(branch)

                flashcards.append(["mindmap", question, branches])

                print("Saved")

        print("Teacher session ended.")

    # Student mode for taking quiz
    elif choice == "2":

        print("\nSTUDENT MODE")

        # Store student info once so it is remembered when switching
        if name == "":
            name = input("Enter name: ")

        if section == "":
            section = input("Enter section: ")

        print("Welcome", name)
        print("Section:", section)

        # If no flashcards exist, stop
        if len(flashcards) == 0:
            print("No flashcards available.")
            input("Press Enter to return.")
            continue

        input("Press Enter to start quiz")

        score = 0
        total = 0

        print("\nQUIZ START")

        # Loop through all flashcards
        for i in range(len(flashcards)):

            f = flashcards[i]
            qtype = f[0]

            # Normal question
            if qtype == "normal":

                print("Q", i + 1, ":", f[1])

                ans = input("Answer: ").lower()

                total += 1

                if ans == f[2].lower():
                    print("Correct")
                    score += 1
                else:
                    print("Wrong:", f[2])

            # Multiple choice question
            elif qtype == "mc":

                print("Q", i + 1, ":", f[1])

                for j in range(len(f[2])):
                    print(f[3][j] + ".", f[2][j])

                ans = input("Answer: ").upper()

                total += 1

                if ans == f[4]:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong:", f[4])

            # Mindmap question
            elif qtype == "mindmap":

                print("Topic", i + 1, ":", f[1])

                correct = 0

                for j in range(len(f[2])):

                    ans = input("Branch " + str(j + 1) + ": ").lower()

                    if ans == f[2][j].lower():
                        print("Correct")
                        correct += 1
                    else:
                        print("Wrong:", f[2][j])

                total += len(f[2])
                score += correct

        # Final score display
        print("\nRESULTS")
        print("Score:", score, "/", total)

        input("Press Enter to return to menu")
