
class Customer:
    def __init__(self,last_name,customer_ID,phone_number):
        self.last_name=last_name
        self.customer_ID=customer_ID
        self.phone_number=phone_number

    def display(self):
        print("Last Name",self.last_name)
        print("Customer ID:",self.customer_ID)
        print("Phone number:",self.phone_number)
        
class Rental:
    def __init__ (self,rental_id,customer_id,skis=0,snowboards=0,hours=1):
        self.rental_id=rental_id
        self.customer_id=customer_id
        self.skis=skis
        self.snowboards=snowboards
        self.hours=hours

        self.isClosed=False

    def get_total(self):
        ski_cost_per_hour=self.skis*15
        ski_total=ski_cost_per_hour*self.hours

        board_cost_per_hour=self.snowboards*10
        board_total=board_cost_per_hour*self.hours

        total=ski_total+board_total
        return total

    def return_rental(self):
        self.isClosed=True

    def display(self,total):
        print("Rental ID:",self.rental_id)
        print("Customer ID:",self.customer_id)
        print("skis rented:",self.skis)
        print("snowboard rented:",self.snowboards)
        print("Hours rented:",self.hours)
        print("Total cost in dollars:",total)#This is bugging out,come back later to replace with self.
        print("Rental closed status:",self.isClosed)

class Shop:
    def __init__(self,skis_in_inventory,snowboards_in_inventory,customer_list,rental_list,total_income=0):
        self.skis_in_inventory=skis_in_inventory
        self.snowboards_in_inventory=snowboards_in_inventory
        self.customer_list=customer_list
        self.rental_list=rental_list
        self.total_income=total_income

    def find_customer(self,intCustomerIDtoFind):
        for customer in self.customer_list:
            if customer.customer_ID == intCustomerIDtoFind:
                return customer
        return None

