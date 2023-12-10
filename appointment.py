class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self._client_name = ""                     #Assign empty
        self._client_phone = ""                    #Assign empty          
        self._appt_type = ""                       #Assign empty
        self._day_of_week = day_of_week
        self._start_time_hour = start_time_hour

    # Getters for...
    # Client Name
    def client_name(self):
        return self._client_name
    
    # Client Phone
    def client_phone(self):
        return self._client_name
    
    # Appointment Type
    def appt_type(self):
        return self._appt_type
    
    # Day of the Week
    def day_of_week(self):
        return self._day_of_week
    
    # Start Time
    def start_time_hour(self):
        return self._start_time_hour
    
    

    # Setters for...
    # Client Name
    def client_name(self, value):
        self._client_name = value 

    # Client Phone
    def client_phone(self, value):
        self._client_phone = value 

    # Appointment Type
    def appt_type(self, value):
        self._appt_type = value 

    # Day of the Week
    def day_of_week(self, value):
        self._day_of_week = value 

    # Start Time
    def start_time_hour(self, value):
        self._start_time_hour = value 



    # Getter that returns start_time_hour + 1
    def get_end_time_hour(self):
        return self._start_time_hour + 1

    # Getter to translate and returns appt_type as a text
    def get_appt_type_desc(self):
        get_appt_type_desc = {
            0 : "Available",
            1 : "Mens Cut",
            2 : "Ladies Cut",
            3 : "Mens Colouring",
            4 : "Ladies Colouring"
        }
        return get_appt_type_desc.get(self._appt_type)
    
    
