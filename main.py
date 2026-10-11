def main_menu():
    print("Welcome to the Lab 1 Application!")
    # Asking name first to greet the user personally
    user_name = input("Please enter your name: ").strip()
    
    while True:
        print(f"\n--- Hello {user_name}, Please Select an Option ---")
        print("1. Body Mass Index (BMI) Calculator")
        print("2. Chinese Zodiac Calculator")
        print("3. Birthday Guessing Game")
        print("4. Exit")
        
        choice = input("Your choice (1-4): ").strip()
        
        if choice == '1':
            run_bmi(user_name) 
        elif choice == '2':
            print(f"\nSorry {user_name}, this tool is still under development.") #still developing these parts
        elif choice == '3':
            print(f"\nSorry {user_name}, this game is still under development.")
        elif choice == '4':
            print(f"\nGoodbye {user_name}! Exiting the app. Code executed successfully!")
            break
        else:
            print("\nError: Invalid choice! Please type 1, 2, 3, or 4.")

# ----------------- TASK 1: BMI CALCULATOR -----------------
def run_bmi(name):
    while True:
        print(f"\n--- BMI Calculator (Active User: {name}) ---")
        try:
            # I used float here because height and weight have decimals
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            
            if weight <= 0 or height <= 0:
                print("Error: Numbers must be greater than 0!")
                continue
        except ValueError:
            # This check stops crashes if the user types letters instead of numbers
            print("Error: Please type numbers only!")
            continue
            
        bmi = weight / (height * height)
        print(f"{name}, your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight [⚠️ Need to gain weight]"
        elif 18.5 <= bmi < 25.0:
            category = "Normal Weight [✅ Great job!]"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight [⚠️ Watch your diet]"
        else:
            category = "Obese [🚨 Please consult a doctor]"
            
        print(f"Your Category: {category}")
        
        repeat = input(f"\n{name}, do you want to check another BMI? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main_menu()
