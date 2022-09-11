from Tickets_booking.Bus_Ticket import bus_ticket_booking
from Tickets_booking.Flight_Ticket import flight_ticket_booking
from Tickets_booking.Train_Ticket import train_ticket_booking
class tickets_booking(train_ticket_booking,bus_ticket_booking,flight_ticket_booking):
    def select_transport(self,mode_of_transport):
        if mode_of_transport=="bus":
            print("u opted for bus",obj.bus_ticket_data("Male",30,5))
        elif mode_of_transport == "train":
            print("u opted for train",obj.train_ticket_data("Male",20,5))
        elif mode_of_transport == "flight":
            print(obj.flight_ticket_data("Male",70,5))
obj=tickets_booking()
obj.select_transport("train")









