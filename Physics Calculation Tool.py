

#functions----------------------------------------------------------

def speed():
    try:
        distance = float(input("Enter the distance (in meters): "))
        time = float(input("Enter the time (in seconds): "))
        if time == 0:
            print("Time cannot be zero.")
            return
        speed_value = distance / time
        print(f"The speed is {speed_value} meters per second.")
    except ValueError:
        print("Invalid input. Please enter numeric values for distance and time.")

def avg_velocity():
    try:
        displacement = float(input("enter displacement in meters: "))
        elapsed_time = float(input("enter elapsed time in seconds:"))
        if elapsed_time == 0:
            print("Elapsed time cannot be zero.")
        velocity_value = displacement / elapsed_time
        print(f"The velocity is {velocity_value} meters per second.")
    except ValueError:
        print("Invalid input. Please enter numeric values for displacement and elapsed time.")

def acceleration():
    try:
        initial_velocity = float(input("Enter the initial velocity in meters per second: "))
        final_velocity = float(input("Enter the final velocity in meters per second: "))
        elapsed_time = float(input("Enter elapsed time in seconds:"))
        if elapsed_time == 0:
            return "Elapsed time cannot be zero."
        acceleration_value = (final_velocity - initial_velocity) / elapsed_time
        print(f"The acceleration is {acceleration_value} meters per second squared.")
    except ValueError:
        print("Invalid input. Please enter numeric values for velocities and elapsed time.")

    
#---------main code----------------------------------------------------------


print("1. speed")
print("2. velocity")
print("3. acceleration")
print("4. exit")

while True:

    user_input = input("Enter your desired calculation: ").strip().lower()

    if user_input == "speed":
        speed()
    elif user_input == "velocity":
        avg_velocity()
    elif user_input == "acceleration":
        acceleration()
    elif user_input == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'speed', 'velocity', or 'acceleration'.")
    

