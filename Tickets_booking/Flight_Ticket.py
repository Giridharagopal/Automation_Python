class flight_ticket_booking():
    flight_ticket_fare=3000
    def flight_ticket_data(self,Gender,Age,No_of_tickets):
        if Gender=="Female" and Age>=0:
            print("This cost is totally free for Females:",self.flight_payment(No_of_tickets))
        elif Gender=="Male" and Age<60:
            print("The payment is:",self.flight_payment(No_of_tickets))
        elif Gender=="Male" and Age>=60:
            print("Enjoy flight travelling and You got discount and the payment is:",self.discount(No_of_tickets))

    def flight_payment(self,No_of_tickets):
        q=self.flight_ticket_fare*No_of_tickets
        return q
    def discount(self,No_of_tickets):
        w=self.flight_ticket_fare*(25/100)
        e=self.flight_ticket_fare-w
        r=No_of_tickets*e
        return r
'''obj=flight_ticket_booking()
obj.flight_ticket_data("Male",100,5)'''