def main():
    print("MODE SELECTION")
    print("\n1. Passive")
    print("2. Active assisted")
    print("3. Active resisted")

    mode = int(input("Enter the mode (1/2/3): "))

    if mode == 1:
        passive_mode()
    elif mode == 2:
        active_assisted_mode()
    elif mode == 3:
        active_resisted_mode()
    else:
        print("Invalid mode selection. Please choose 1, 2, or 3.")

def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Value must be between {min_value} and {max_value}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def gradual_change(current_value, target_value, rate_of_change):
    # Gradually change the current value towards the target value
    while abs(current_value - target_value) > 0.01:
        current_value += rate_of_change * (target_value - current_value)
        yield current_value

def flexion_extension_mode():
    angle = validate_input("Angle (0-180°): ", 0, 180)
    speed = validate_input("Speed (0-3000): ", 0, 3000)
    acceleration = validate_input("Acceleration (0-1000): ", 0, 1000)
    duration = validate_input("Duration: ", 0, float("inf"))

    # Gradual acceleration
    for gradual_speed in gradual_change(0, speed, acceleration):
        # Perform flexion/extension movement logic here
        print(f"Current speed: {gradual_speed:.2f}")

    # Gradual deceleration
    for gradual_speed in gradual_change(speed, 0, acceleration):
        # Perform flexion/extension movement logic here
        print(f"Current speed: {gradual_speed:.2f}")

        
def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Value must be between {min_value} and {max_value}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def passive_mode():
    print("\nPASSIVE MODE: THERAPY PROGRAMMING")
    print("\n1. Flexion / Extension")
    print("2. Pronation / Supination")
    print("3. Combination")

    submode = int(input("Enter the submode (1/2/3): "))

    if submode == 1:
        flexion_extension_mode()
    elif submode == 2:
        pronation_supination_mode()
    elif submode == 3:
        combination_mode()
    else:
        print("Invalid submode selection. Please choose 1, 2, or 3.")

def flexion_extension_mode():
    angle = validate_input("Angle (0-180°): ", 0, 180)
    speed = validate_input("Speed (0-3000): ", 0, 3000)
    acceleration = validate_input("Acceleration (0-1000): ", 0, 1000)
    duration = validate_input("Duration: ", 0, float("inf"))
    print("Stop")
    print("Back")

    # Perform flexion/extension movement logic here

def pronation_supination_mode():
    angle = validate_input("Angle (0-180°): ", 0, 180)
    speed = validate_input("Speed (0-3000): ", 0, 3000)
    acceleration = validate_input("Acceleration (0-1000): ", 0, 1000)
    duration = validate_input("Duration: ", 0, float("inf"))
    print("Stop")
    print("Back")

    # Perform pronation/supination movement logic here

def combination_mode():
    flexion_angle = validate_input("Set flexion/extension angle (0-180°): ", 0, 180)
    pronation_angle = validate_input("Set pronation/supination angle (0-180°): ", 0, 180)
    acceleration = validate_input("Acceleration (0-1000): ", 0, 1000)
    duration = validate_input("Duration: ", 0, float("inf"))
    print("Stop")
    print("Back")
def active_assisted_mode():
    print("\nACTIVE ASSISTED")
    print("\n1. Flexion / Extension")
    print("2. Pronation / Supination")
    print("3. Combination")

    submode = int(input("Enter the submode (1/2/3): "))

    if submode == 1:
        flexion_extension_mode()
    elif submode == 2:
        pronation_supination_mode()
    elif submode == 3:
        combination_mode()
    else:
        print("Invalid submode selection. Please choose 1, 2, or 3.")

def active_resisted_mode():
    print("\nACTIVE RESISTED")
    print("\n1. Flexion / Extension")
    print("2. Pronation / Supination")
    print("3. Combination")

    submode = int(input("Enter the submode (1/2/3): "))

    if submode == 1:
        flexion_extension_mode()
    elif submode == 2:
        pronation_supination_mode()
    elif submode == 3:
        combination_mode()
    else:
        print("Invalid submode selection. Please choose 1, 2, or 3.")

    # Perform combination movement logic here

if __name__ == "__main__":
    main()
