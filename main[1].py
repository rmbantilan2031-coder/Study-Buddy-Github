import string

print("==================================================")
print("                  STUDY BUDDY")
print("==================================================")

letters = list(string.ascii_uppercase)
flashcards = []


# MAIN MENU LOOP


while True:

    print("\n==================================================")
    print("CHOOSE MODE")
    print("1 - Teacher")
    print("2 - Student")
    print("3 - Exit")
    print("==================================================")

    choice = input("Enter choice: ").strip()

    # ---------------- EXIT ----------------
    if choice == "3":
        print("\nGoodbye! 👋")
        break

    # ==================================================
    #                    TEACHER MODE
    # ==================================================
    elif choice == "1":

        print("\n================ TEACHER MODE ================")

        print("Type 'switch' anytime to finish setup.\n")

        mode = input("Select mode (normal, mc, mindmap): ").lower()

        if mode not in ["normal", "mc", "mindmap"]:
            print("Invalid mode. Returning to menu.")
            continue

        while True:

            question = input("Enter question/topic: ")

            if question.lower() == "switch":
                break

            # NORMAL
            if mode == "normal":

                answer = input("Enter answer: ")

                if answer.lower() == "switch":
                    break

                flashcards.append(["normal", question, answer])
                print("Saved!\n")

            # MC
            elif mode == "mc":

                options = []
                option_letters = []

                print("Type 'done' to finish options")

                i = 0
                while True:

                    option = input("Option " + letters[i] + ": ")

                    if option.lower() == "done":
                        break

                    options.append(option)
                    option_letters.append(letters[i])
                    i += 1

                answer = input("Correct letter: ").upper()

                flashcards.append(["mc", question, options, option_letters, answer])
                print("Saved!\n")

            # MINDMAP
            elif mode == "mindmap":

                branches = []

                print("Type 'done' to finish branches")

                while True:

                    branch = input("Branch: ")

                    if branch.lower() == "done":
                        break

                    branches.append(branch)

                flashcards.append(["mindmap", question, branches])
                print("Saved!\n")

        print("\nTeacher session ended. Returning to menu...")

    # ==================================================
    #                    STUDENT MODE
    # ==================================================
    elif choice == "2":

        print("\n================ STUDENT MODE ================")

        name = input("Enter your name: ")
        section = input("Enter your section: ")

        print("\nWelcome,", name)
        print("Section:", section)

        # ---------------- NO FLASHCARDS ----------------
        if len(flashcards) == 0:
            print("\n No flashcards available yet.")
            print(" Ask teacher to create flashcards.")
            print("Type 'switch' in menu and choose Teacher Mode.\n")

            input("Press Enter to return to menu...")
            continue

        input("\nPress Enter to start quiz...")

        score = 0
        total = 0

        print("\n================ QUIZ START ================\n")

        # ---------------- QUIZ ----------------
        for i in range(len(flashcards)):

            f = flashcards[i]
            qtype = f[0]

            # NORMAL
            if qtype == "normal":

                print("Q", i + 1, ":", f[1])
                ans = input("Answer: ").lower()

                total += 1

                if ans == f[2].lower():
                    print("Correct!\n")
                    score += 1
                else:
                    print("Wrong! Answer:", f[2], "\n")

            # MC
            elif qtype == "mc":

                print("Q", i + 1, ":", f[1])

                for j in range(len(f[2])):
                    print(f[3][j] + ".", f[2][j])

                ans = input("Answer: ").upper()

                total += 1

                if ans == f[4]:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Wrong! Answer:", f[4], "\n")

            # MINDMAP
            elif qtype == "mindmap":

                print("Topic", i + 1, ":", f[1])

                correct = 0

                for j in range(len(f[2])):

                    ans = input("Branch " + str(j + 1) + ": ").lower()

                    if ans == f[2][j].lower():
                        print("Correct!\n")
                        correct += 1
                    else:
                        print("Wrong! Correct:", f[2][j], "\n")

                total += len(f[2])
                score += correct

        # ---------------- FINAL SCORE ----------------
        print("==================================================")
        print("QUIZ COMPLETED")
        print("SCORE:", score, "/", total)
        print("==================================================")

        input("\nPress Enter to return to menu...")
