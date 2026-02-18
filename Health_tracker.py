import datetime

# --- 1. Data Storage (Simulated Database) ---
# Store daily records for easy tracking.
health_data = []

# --- 2. Helper Functions for Input ---

def get_integer_input(prompt):
    """Helper to ensure the user enters a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_float_input(prompt):
    """Helper to ensure the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- 3. Core Logic Functions ---

def classify_blood_pressure(systolic, diastolic):
    """
    Classifies BP based on standard guidelines.
    Source: American Heart Association (AHA) simplified categories.
    """
    if systolic < 120 and diastolic < 80:
        return "Normal", "✅ Excellent"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated", "⚠️ Monitor Closely"
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "Hypertension Stage 1", "🛑 Consult Doctor"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2", "🚨 **CRITICAL ALERT**"
    else:
        # Catch-all for very low/unusual values
        return "Atypical Reading", "❓ Check Equipment"

def calculate_sleep_duration(time_to_bed_hrs, sleep_duration_hrs):
    """Simple calculation for total sleep duration and basic advice."""
    
    # We will simulate the duration for simplicity, assuming user enters total hours
    if 7 <= sleep_duration_hrs <= 9:
        advice = "👍 Optimal Range"
    elif sleep_duration_hrs > 9:
        advice = "🥱 Overslept"
    else:
        advice = "😴 Needs More Rest"
    
    return sleep_duration_hrs, advice

def calculate_calories(steps):
    """Estimates calories burned (approx 0.04 kcal per step)."""
    return steps * 0.04

# --- 4. Main Program Functions ---

def record_daily_data():
    """Prompts the user for today's health data and stores it."""
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Check if data for today already exists (optional, but good practice)
    for record in health_data:
        if record["date"] == today:
            print(f"\nData for {today} already exists. Skipping recording.")
            return

    print(f"\n--- Recording Data for {today} ---")
    
    # Fitness Input
    steps = get_integer_input("Enter Steps Taken: ")
    
    # Sleep Input
    sleep_duration = get_float_input("Enter Sleep Duration (hours, e.g., 7.5): ")
    
    # Blood Pressure Input
    print("\n--- Blood Pressure (Chronic Disease Management) ---")
    bp_systolic = get_integer_input("Enter Systolic BP (the top number): ")
    bp_diastolic = get_integer_input("Enter Diastolic BP (the bottom number): ")
    
    # Compile the data
    new_record = {
        "date": today,
        "steps": steps,
        "sleep_duration": sleep_duration,
        "bp_systolic": bp_systolic,
        "bp_diastolic": bp_diastolic
    }
    
    health_data.append(new_record)
    print("\n✅ Data recorded successfully!")

def generate_daily_report():
    """Generates a detailed report for the most recent data entry."""
    
    if not health_data:
        print("\nNo data recorded yet. Please record data first.")
        return

    # Get the latest entry
    latest_record = health_data[-1]
    
    # 1. FITNESS ANALYSIS
    steps = latest_record["steps"]
    calories = calculate_calories(steps)
    fitness_goal = 7000 # Example Goal
    fitness_status = "Goal Achieved!" if steps >= fitness_goal else f"Needs {fitness_goal - steps} more steps."
    
    # 2. SLEEP ANALYSIS
    sleep_hrs, sleep_advice = calculate_sleep_duration(0, latest_record["sleep_duration"])
    
    # 3. BP ANALYSIS (Chronic Disease)
    systolic = latest_record["bp_systolic"]
    diastolic = latest_record["bp_diastolic"]
    bp_classification, bp_alert = classify_blood_pressure(systolic, diastolic)

    # --- Print Report ---
    print("\n" + "="*50)
    print(f"       Health Tracker Pro - Daily Report ({latest_record['date']})")
    print("="*50)
    
    # Fitness Section
    print("\n### 🏃 Daily Fitness ###")
    print(f"Steps Taken: **{steps:,}** | Calories Burned: {calories:.2f} kcal")
    print(f"Goal Status ({fitness_goal:,} steps): **{fitness_status}**")
    
    # Sleep Section
    print("\n### 🌙 Sleep Monitoring ###")
    print(f"Total Sleep Duration: **{sleep_hrs:.1f} hours**")
    print(f"Recommendation: {sleep_advice}")

    # BP Section
    print("\n### 🩸 Chronic Disease Management (Blood Pressure) ###")
    print(f"Last Reading: **{systolic}/{diastolic} mmHg**")
    print(f"Classification: **{bp_classification}**")
    print(f"Alert Status: **{bp_alert}**")
    
    # Final Critical Alert Check
    if "CRITICAL ALERT" in bp_alert:
        print("\n**************************************************")
        print("!!! URGENT MEDICAL ADVISORY !!!")
        print("Your blood pressure is in a critical range. Please seek medical help immediately.")
        print("**************************************************")
        
    print("\n" + "="*50)

# --- 5. Main Menu (The Prototype UI) ---

def main_menu():
    """The main interface for the user."""
    
    print("\n\n--- Health Tracker Pro Prototype ---")
    while True:
        print("\nWhat would you like to do?")
        print("1. Record Today's Health Data")
        print("2. Generate Daily Health Report")
        print("3. Exit Prototype")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            record_daily_data()
        elif choice == '2':
            generate_daily_report()
        elif choice == '3':
            print("\nExiting Health Tracker Pro. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main program
if __name__ == "__main__":
    # Pre-populate some dummy data for demonstration
    health_data.append({
        "date": "2025-11-22", "steps": 5500, "sleep_duration": 6.8, "bp_systolic": 125, "bp_diastolic": 75
    })
    health_data.append({
        "date": "2025-11-21", "steps": 9200, "sleep_duration": 8.0, "bp_systolic": 115, "bp_diastolic": 70
    })
    
    main_menu()