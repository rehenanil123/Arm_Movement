class AssistiveDevice:
    def __init__(self):
        self.mode = None

    def get_input(self, prompt, min_val, max_val):
        while True:
            try:
                value = float(input(prompt))
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"Please enter a value between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def acceleration_profile(self, total_duration, acceleration):
        # Create an acceleration profile (20% at the beginning and end)
        initial_acceleration = 0.2 * acceleration
        middle_duration = total_duration - 60  # 30 seconds at each end
        middle_acceleration = acceleration

        return [initial_acceleration] + [middle_acceleration] * middle_duration + [initial_acceleration]

    def passive_mode(self):
        print("1.1 PASSIVE MODE: THERAPY PROGRAMMING")
        print("1. Flexion / Extension")
        print("2. Pronation / Supination")
        print("3. Combination")

        sub_mode = int(input("Enter sub-mode (1/2/3): "))

        if sub_mode == 1:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            speed = self.get_input("Enter speed (0-3000): ", 0, 3000)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 2:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            speed = self.get_input("Enter speed (0-3000): ", 0, 3000)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 3:
            flexion_angle = self.get_input("Set flexion/extension angle (0-180°): ", 0, 180)
            pronation_angle = self.get_input("Set pronation/supination angle (0-180°): ", 0, 180)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        else:
            print("Invalid sub-mode selection. Please choose 1, 2, or 3.")
            return

        print("Movement completed!")
        
    def active_assisted_mode(self):
        print("ACTIVE ASSISTED")
        print("1.1 Flexion / Extension")
        print("1.2 Pronation / Supination")
        print("1.3 Combination")

        sub_mode = int(input("Enter sub-mode (1/2/3): "))

        if sub_mode == 1:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            assistance = self.get_input("Enter assistance level (0-100%): ", 0, 100)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 2:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            assistance = self.get_input("Enter assistance level (0-100%): ", 0, 100)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 3:
            flexion_angle = self.get_input("Set flexion/extension angle (0-180°): ", 0, 180)
            pronation_angle = self.get_input("Set pronation/supination angle (0-180°): ", 0, 180)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            assistance = self.get_input("Enter assistance level (0-100%): ", 0, 100)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        else:
            print("Invalid sub-mode selection. Please choose 1, 2, or 3.")
            return

        print("Movement completed!")

    def active_resisted_mode(self):
        print("ACTIVE RESISTED")
        print("1.1 Flexion / Extension")
        print("1.2 Pronation / Supination")
        print("1.3 Combination")

        sub_mode = int(input("Enter sub-mode (1/2/3): "))

        if sub_mode == 1:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            resistance = self.get_input("Enter resistance level (0-100%): ", 0, 100)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 2:
            angle = self.get_input("Enter angle (0-180°): ", 0, 180)
            resistance = self.get_input("Enter resistance level (0-100%): ", 0, 100)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        elif sub_mode == 3:
            flexion_angle = self.get_input("Set flexion/extension angle (0-180°): ", 0, 180)
            acceleration = self.get_input("Enter acceleration (0-1000): ", 0, 1000)
            pronation_angle = self.get_input("Set pronation/supination angle (0-180°): ", 0, 180)
            resistance = self.get_input("Enter resistance level (0-100%): ", 0, 100)
            duration = self.get_input("Enter duration (seconds): ", 0, float("inf"))
        else:
            print("Invalid sub-mode selection. Please choose 1, 2, or 3.")
            return

        print("Movement completed!")

    def main(self):
        print("MODE SELECTION")
        print("1. Passive Mode")
        print("2. Active assisted")
        print("3. Active resisted")

        self.mode = int(input("Enter mode (1/2): "))

        if self.mode == 1:
            self.active_passive_mode()
        elif self.mode == 2:
            self.active_assisted_mode_mode()
        elif self.mode == 3:
            self.active_resisted_mode()
        else:
             print("Invalid mode selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    device = AssistiveDevice()
    device.main()

