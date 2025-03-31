import time

def main():
    print("Welcome! Please type in '1234'.")
    user_input = input("Input: ")

    if user_input == "1234":
        print("Error: It must be typed in backwards!")
        user_input = input("Try again: ")

        if user_input == "4321":
            print("Yeahhh, try typing in '2341'.")
            user_input = input("One more time: ")

            if user_input == "2341":
                print("You have 15 seconds to shut down the program before the self-destruct feature is utilized.")
                
                # Countdown from 15 to 0
                for i in range(15, -1, -1):
                    print(i)
                    time.sleep(1)  # Wait for 1 second

                print("BOOM!")
            else:
                print("Incorrect input. Program terminated.")
        else:
            print("Incorrect input. Program terminated.")
    else:
        print("Incorrect input. Program terminated.")

if __name__ == "__main__":
    main()
