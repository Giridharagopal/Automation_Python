
class Calculations():
    def payment(self, No_of_tickets):
        q = obj.per_ticket_fare * No_of_tickets
        return q

    def discount(self, No_of_tickets):
        w = obj.per_ticket_fare * (50 / 100)
        e = obj.per_ticket_fare - w
        r = No_of_tickets * e
        return r
obj=Calculations()
obj.payment(10)
obj.discount(10)

