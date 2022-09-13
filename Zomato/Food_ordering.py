from Zomato.Hotels_Menu_list import a, b
class Food_Order(a,b):
    def Select_Hotel_With_coupon(self,Hotel_Name,coupon_code,Dish_Qty):
        if Hotel_Name == "A2B" and coupon_code == "zomato123":
            x = obj.A2B(Hotel_Name,coupon_code,Dish_Qty)
        elif Hotel_Name == "Chai_kings" and coupon_code == "zomato123":
            x = obj.Chai_kings(Hotel_Name, coupon_code, Dish_Qty)

obj=Food_Order()
obj.Select_Hotel_With_coupon("A2B","zomato123",{"Puri":1,"Idly":1,"Dosa":0})
obj.Select_Hotel_With_coupon("Chai_kings","zomato123",{"Tea":1,"Samosa":2})
