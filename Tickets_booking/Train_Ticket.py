class train_ticket_booking():
    per_ticket_fare=500
    def train_ticket_data(self,Gender,Age,No_of_tickets):
        if Gender=="Female" and Age>=0:
            print("This cost is totally free for Females:",self.payment(No_of_tickets))
        elif Gender=="Male" and Age<60:
            print("The payment is:",self.payment(No_of_tickets))
        elif Gender=="Male" and Age>=60:
            print("You got discount and the payment is:",self.discount(No_of_tickets))

    def payment(self,No_of_tickets):
        q=self.per_ticket_fare*No_of_tickets
        return q
    def discount(self,No_of_tickets):
        w=self.per_ticket_fare*(35/100)
        e=self.per_ticket_fare-w
        r=No_of_tickets*e
        return r
'''obj=train_ticket_booking()
obj.train_ticket_data("Female",100,5)'''