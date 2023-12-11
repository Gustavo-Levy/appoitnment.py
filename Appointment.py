# appointment.py
class Appointment:
    # Initializer to create a new Appointment instance with specified day and start time
    def _init_(self, day_of_week, start_time_hour):
        self.client_name = ""  # Name of the client, initialized to an empty string
        self.client_phone = ""  # Phone number of the client, initialized to an empty string
        self.appt_type = 0      # Type of appointment, initialized to 0 (Available)
        self.day_of_week = day_of_week  # Day of the week for the appointment
        self.start_time_hour = start_time_hour  # Start time (hour) for the appointment

    # Getter method for client's name
    def get_client_name(self):
        return self.client_name

    # Getter method for client's phone number
    def get_client_phone(self):
        return self.client_phone

    # Getter method for appointment type
    def get_appt_type(self):
        return self.appt_type

    # Getter method for the day of the week
    def get_day_of_week(self):
        return self.day_of_week

    # Getter method for the start time (hour) of the appointment
    def get_start_time_hour(self):
        return self.start_time_hour

    # Method to calculate and return the end time (hour) of the appointment
    def get_end_time_hour(self):
        return self.start_time_hour + 1  # Assumes all appointments last for 1 hour

    # Method to get a description of the appointment type
    def get_appt_type_desc(self):
        types = {
            0: "Available",
            1: "Mens Cut $50",
            2: "Ladies Cut $80",
            3: "Mens Colouring $50",
            4: "Ladies Colouring $120"
        }
        return types.get(self.appt_type, "Invalid Type")  # Returns the description or 'Invalid Type' if not found

    # Setter method for client's name
    def set_client_name(self, name):
        self.client_name = name

    # Setter method for client's phone number
    def set_client_phone(self, phone):
        self.client_phone = phone

    # Setter method for appointment type
    def set_appt_type(self, appt_type):
        self.appt_type = appt_type

    # Method to schedule an appointment with given client details and appointment type
    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type

    # Method to cancel the appointment, resetting client details and appointment type
    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0

    # Method to format the appointment details into a string record
    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour:02d}"

    # String representation of the appointment details
    def _str_(self):
        return f"{self.client_name.ljust(20)} {self.client_phone.ljust(15)} {self.day_of_week.ljust(9)} {self.start_time_hour:02d}:00 - {self.get_end_time_hour():02d}:00 {self.get_appt_type_desc()}"