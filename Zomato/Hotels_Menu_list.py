class a:
    per_Idly = 20
    per_Dosa = 35
    per_Puri = 50

    def A2B(self,Hotel_Name,coupon_code,Dish_Qty):
        if Hotel_Name=="A2B":
            totalamount = 0
            for key in Dish_Qty:
                s=Dish_Qty[key]
                if key == "Idly":
                     temp= self.per_Idly * s
                elif key == "Dosa":
                     temp= self.per_Dosa * s
                elif key == "Puri":
                     temp= self.per_Puri * s
                totalamount+=temp
            print (totalamount)
class b:
    Tea=15
    samosa=20
    def Chai_kings(self,Hotel_Name,coupon_code,Dish_Qty):
        if Hotel_Name == "Chai_kings":
            totalamount = 0
            for key in Dish_Qty:
                s=Dish_Qty[key]
                if key == "Idly":
                     temp= self.per_Idly * s
                elif key == "Dosa":
                     temp= self.per_Dosa * s
                elif key == "Puri":
                     temp= self.per_Puri * s
                totalamount+=temp
            print (totalamount)


'''obj=a()
obj.hotel_names("A2B","Dosa",3)'''