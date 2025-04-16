from datetime import datetime

def log_mood():
    mood = input("How are you feeling today? ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("mood_log.txt", "a") as file:
        file.write(f"{now} - {mood}\n")
    
    print("Mood logged. Have a great day!")

def view_log():
    try:
        with open("mood_log.txt", "r") as file:
            print("\nMood Log:\n")
            print(file.read())
    except FileNotFoundError:
        print("No mood log found yet!")

def main():
    print("Mood Logger 😎")
    print("1. Log mood")
    print("2. View mood log")
    choice = input("Choose an option: ")
    
    if choice == "1":
        log_mood()
    elif choice == "2":
        view_log()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
