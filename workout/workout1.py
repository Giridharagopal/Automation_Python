class a:
    per_Idly = 20
    per_Dosa = 35
    per_Puri = 50

    def hotel_names(self,Hotel_Name,coupon_code,Dish,B):
        totalamount = 0
        for key in Dish:
            for s in B:
                if key == "Idly":
                     temp= self.per_Idly * s
                     totalamount += temp
                     break
                elif key == "Dosa":
                     temp= self.per_Dosa * s
                     totalamount += temp
                     break
                elif key == "Puri":
                     temp= self.per_Puri * s
                     totalamount+=temp
                     break
        print (totalamount)