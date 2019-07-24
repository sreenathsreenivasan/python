class car:
    def __init__(self,regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
        self.is_started=False
    def start(self):
        if self.is_started:
            print("car already started...")
        else:
            print(f"car with regno:{self.regno} started...")
            self.is_started=True
    def stop(self):
        if self.is_started:
            print("car already stoped...")
        else:
            print(f"car with regno:{self.regno} stoped...") 
            self.is_started=False       
    def change_gear(self):
        if self.is_started:
            print("car stoped...")
        else:
            print(f"car with regno:{self.regno} changed gear...")    