# CPRG 216
# Final group project 
# Group 9
# Author : PRIYANSHU KUCHHADIYA, RUDRA SOLANKI , GUSTAVO

# Jojo's Hair Salon Appointment Manager
#
# This script is a comprehensive appointment management system designed for Jojo's Hair Salon.
# It includes functionalities for creating a weekly calendar, scheduling, finding, displaying, 
# and canceling appointments. Additionally, it provides features to load appointments from a file 
# and save scheduled appointments to a file. The system operates through a user-friendly menu 
# interface, allowing easy management of salon appointments.
#
# Key Functionalities:
# - Create a weekly calendar with predefined working hours.
# - Schedule new appointments with client details and appointment types.
# - Find appointments by client name or by day.
# - Cancel existing appointments.
# - Load and save appointment data from/to a CSV file.
# - Display appointments for a specific day.
# - User-friendly menu-driven interface for easy navigation and operation.
# Import necessary modules
import csv
import os
from Appointment import Appointment

# Global variable to store appointments
weekly_calendar = []
# Display the main menu
def display_menu():
    # Display the menu options and return the user's choice
    menu_options = """
    Jojo's Hair Salon Appointment Manager
    ======================================
    1) Schedule an appointment
    2) Find appointment by name
    3) Print calendar for a specific day
    4) Cancel an appointment
    9) Exit the system
    """
    print(menu_options)
    return input("Enter your selection: ")

# Create a weekly calendar for appointments
def create_weekly_calendar():
    # Initialize the weekly_calendar with empty appointment slots
    global weekly_calendar
    weekly_calendar = []
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in week_days:
        for hour in range(9, 17):
            # Create an Appointment object and add it to the calendar
            appointment = Appointment()
            weekly_calendar.append(["", "", "available", day, hour, hour + 1])

# Load appointments from a file
def load_appointments_from_file():
    # Load appointments from the specified CSV file
    file_name = input("Enter the appointment file name: ")
    with open(file_name, "r") as file:
        for line in file.readlines():
            # Parse each line and schedule the appointment
            client_name, client_phone, appt_type, day, hour = line.strip().split(',')
            appointment = find_appointment(day, int(hour))
            if appointment:
                # Schedule the appointment
                appointment.schedule(client_name, client_phone, appt_type)

# Find an appointment based on day and time
def find_appointment(day, start_hour):
    # Search for an appointment by day and start hour
    for obj in weekly_calendar:
        if obj[3] == day and obj[4] == start_hour: 
            return obj

# Find appointments by client name
def find_appointment_by_name(name):
    # Display appointments that match the given client name
    print(f"Appointments for {name}")
    print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("=" * 110)

    found = False
    for appointment in weekly_calendar:
        if name.lower() in appointment[0].lower():
            found = True
            # Format and display each matching appointment
            start_time = f"{appointment[4]:02d}:00"
            end_time = f"{appointment[5]:02d}:00"
            appt_type = appointment[2].capitalize() if appointment[2] != "available" else "Available"
            print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format(appointment[0], appointment[1], appointment[3].capitalize(), start_time, end_time, appt_type))

    if not found:
        print(f"No appointments found for {name}.")

# Show appointments for a specific day
def show_appointments_by_day(day):
    # Display all appointments for the specified day
    day = day.lower()  # Normalize the input day for case-insensitive comparison
    print(f"Appointments for {day.capitalize()}")
    print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("=" * 110)

    for appointment in weekly_calendar:
        if appointment[3].lower() == day:
            # Format and display each appointment for the day
            start_time = f"{appointment[4]:02d}:00"
            end_time = f"{appointment[5]:02d}:00"
            appt_type = appointment[2].capitalize() if appointment[2] != "available" else "Available"
            print("{:>12s}{:>20s}{:>20s}{:>10s}{:>10s}{:>12s}".format(appointment[0], appointment[1], appointment[3].capitalize(), start_time, end_time, appt_type))

# Save newly scheduled appointments
def save_scheduled_appointments_list():
    # Prompt the user to schedule a new appointment
    print("**Schedule an appointment**")
    day = input("What day: ").lower()
    startTime = int(input("Enter start hour (24-hour clock): "))

    # Check if the time slot is valid
    if startTime not in range(9, 17) or day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
        print("Sorry, that time slot is not in the weekly calendar!")
        return

    for appointment in weekly_calendar:
        if appointment[3].lower() == day and appointment[4] == startTime:
            # Check if the slot is already booked
            if appointment[2] != "available":
                print("Sorry, that time slot is already booked")
                return

            # Schedule the new appointment
            name = input("Client Name: ")
            phone = input("Client Phone: ")
            print("Appointment types")
            print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
            appt_type = input("Type of Appointment: ")
            if appt_type not in ["1", "2", "3", "4"]:
                print("Sorry, that is not a valid appointment type!")
                return

            appointment[0] = name
            appointment[1] = phone
            appointment[2] = appt_type
            print(f"OK, {name}'s appointment for {day.capitalize()} at {startTime}:00 is scheduled")
            return

    print("No suitable appointment slot found.")

# Save scheduled appointments to a file
def save_scheduled_appointments():
    # Save all scheduled appointments to a CSV file
    count = 0
    while True:
        filename = input("Enter appointment filename: ")

        # Check if the file exists and ask for overwrite confirmation
        if os.path.exists(filename):
            overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ")
            if overwrite.lower() != "y":
                continue  # Ask for a new filename

        with open(filename, "w", newline='') as file:
            filewriter = csv.writer(file)
            for appointment in weekly_calendar:
                if appointment[2] != "available":
                    count += 1
                    # Write each scheduled appointment to the file
                    filewriter.writerow(appointment)

        if count != 0:
            print(f"{count} scheduled appointments have been successfully saved")
            break  # Exit the loop after successful save

# Cancel an appointment
def cancel_appointment(day, start):
    # Cancel an existing appointment based on day and start time
    day = day.lower()
    if day == "sunday" or start not in range(9, 17):
        print("Sorry, that time slot is not in the weekly calendar!")
        return

    for appointment in weekly_calendar:
        if appointment[3].lower() == day and appointment[4] == start:
            if appointment[2] != "available":
                # Clear the appointment details to cancel it
                appointment[0], appointment[1], appointment[2] = "", "", "available"
                print(f"{day.capitalize()} {start}-{start + 1} appointment has been cancelled")
                return
            else:
                print("That time slot isn't booked and doesn't need to be cancelled")
                return

    print("No appointment found for the given time slot")

# Main function to run the application
def main():
    # Start the appointment manager system
    print("Starting the Appointment Manager System")
    create_weekly_calendar()
    print("weekly calendar created")

    # Load previously scheduled appointments
    load_appointment = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
    if load_appointment.lower() == "y":
        while True:
            filename = input("Enter appointment filename: ")
            if os.path.exists(filename):
                # Load appointments from file
                with open(filename, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        newLine = line.rstrip("\n")
                        for i in weekly_calendar:
                            LineList = newLine.split(",")
                            if str(LineList[3]).lower() == str(i[3]).lower() and int(LineList[4]) == int(i[4]) and str(i[2]) == "available":
                                i[0] = LineList[0]
                                i[1] = LineList[1]
                                i[2] = LineList[2]
                print(f"{len(lines)} previously scheduled appointments have been loaded")
                break
            else:
                print("File not found. Please re-enter appointment filename.")

    # [Rest of the main function code...]
    # Main loop to process user menu selections
    while True:
        user_choice = display_menu()
        if user_choice == "1":
            save_scheduled_appointments_list()
        elif user_choice == "2":
            print("** Find appointment by name **")
            client_name = input("Enter client name to search: ")
            find_appointment_by_name(client_name)
        elif user_choice == "3":
            print("** Print calendar for a specific day **")
            day = input("Enter day of week: ")
            show_appointments_by_day(day)
        elif user_choice == "4":
            print("** Cancle an appointment **")
            day = input("What day:")
            start = int(input("Enter start hour (24-hour clock): "))
            cancel_appointment(day, start)
        elif user_choice == "9":
            print("** Exit the system** ")
            if input("Save changes to file? (Y/N): ").lower() == 'y':
                save_scheduled_appointments()
            print("Goodbye!")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
