import random
import string

# ANSI escape code for green text
GREEN_TEXT = "\033[92m"
RESET_COLOR = "\033[0m"

PASSWORDS_FILE = "passwords.txt"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(password):
    with open(PASSWORDS_FILE, "a") as file:
        file.write(password + "\n")

def about_us():
    about_text = """
    This is a Strong Password Generator tool.
    It generates secure passwords using a combination of letters, numbers, and symbols.
    Created by MR.Joy Mahanty. Youtube Channel - Hacker Joy
    """
    print(about_text)

def main():
    while True:
        print(f"{GREEN_TEXT}=== Strong Password Generator ==={RESET_COLOR}")
        print("1. Generate Password")
        print("2. About Us")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            try:
                length = int(input("Enter password length (default is 12): ") or 12)
                if length <= 0:
                    raise ValueError("Length must be a positive integer.")
                
                password = generate_password(length)
                
                print(f"Generated Password: {GREEN_TEXT}{password}{RESET_COLOR}")
                
                save_option = input("Do you want to save this password? (yes/no): ").lower()
                
                if save_option == "yes":
                    save_to_file(password)
                    print(f"Password saved to '{PASSWORDS_FILE}'")
                else:
                    print("Password not saved.")
            
            except ValueError as ve:
                print(f"{GREEN_TEXT}Error: {ve}{RESET_COLOR}")
            
            except Exception as e:
                print(f"{GREEN_TEXT}An unexpected error occurred: {e}{RESET_COLOR}")

        elif choice == "2":
            about_us()

        elif choice == "3":
            print("Exiting the Strong Password Generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
