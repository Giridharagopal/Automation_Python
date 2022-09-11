from workout.workout1 import a
class Food_Order(a):
    def Select_Hotel_With_coupon(self,Hotel_Name,coupon_code,Dish,B):
        if Hotel_Name == "A2B" and coupon_code == "zomato123":
            x = obj.hotel_names(Hotel_Name,coupon_code,Dish,B)


obj=Food_Order()
obj.Select_Hotel_With_coupon("A2B","zomato123",("Puri","Idly","Dosa"),(1,2,3))