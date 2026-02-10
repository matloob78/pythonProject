from colorama import Fore, Style, init
init(autoreset=True)

EngToUrdu = {
    "hell": "Jahannam",
    "paradise": "Jannat",
    "prophet": "Nabi ya Rasool",
    "beliver": "Moomin"
}

while True:
    print(Fore.CYAN + "\n╔════════════════════════════╗")
    print(Fore.CYAN + "║     MINI DICTIONARY APP    ║")
    print(Fore.CYAN + "╠════════════════════════════╣")
    print(Fore.YELLOW + "║ 1. Search word             ║")
    print(Fore.YELLOW + "║ 2. Add new word            ║")
    print(Fore.YELLOW + "║ 3. Show all words          ║")
    print(Fore.YELLOW + "║ 4. Exit                    ║")
    print(Fore.CYAN + "╚════════════════════════════╝")

    choice = input(Fore.GREEN + "Select option (1-4): ")

    # 🔎 Search
    if choice == "1":
        word = input(Fore.WHITE + "Enter word: ").lower().strip()
        print(Fore.MAGENTA + "Meaning:",
              EngToUrdu.get(word, Fore.RED + "Word not found"))

    # ➕ Add
    elif choice == "2":
        word = input("Enter new word: ").lower().strip()
        meaning = input("Enter meaning: ").strip()

        EngToUrdu[word] = meaning
        print(Fore.GREEN + "Word added successfully ✅")

    # 📖 Show all
    elif choice == "3":
        print(Fore.BLUE + "\n--- All Words ---")
        for k, v in EngToUrdu.items():
            print(Fore.WHITE + k, ":", Fore.MAGENTA + v)

    # ❌ Exit
    elif choice == "4":
        print(Fore.RED + "App closed 👋")
        break

    else:
        print(Fore.RED + "Invalid option")
