#look back at slides to remember append 
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
        #include int
    def find_customer(self,intCustomerIDtoFind):
        for customer in self.customer_list:
            if customer.customer_ID == intCustomerIDtoFind:
                return customer
        return None

    def find_rental(self,intRentalID):
        for rental in self.rental_list:
            if rental.rental_id==intRentalID:
                return rental
            return None

    def find_rentals_for_customer(self,intCustomerID):
        rentals=[]
        for rental in self.rental_list:
            if rental.customer_id==intCustomerID:
                rentals.append(rental)
        return rentals
    
    def add_customer(self,last_name,customer_ID,phone_number):#cheek for repeats
        for customer in self.customer_list:
            if customer.customer_ID==customer_ID:
                print("Customer already exist")
                return None
        #the actual customer
        new_customer=Customer(last_name,customer_ID,phone_number)
        self.customer_list.append(new_customer)
        print("New customer ID is:",customer_ID)
        return new_customer
    #-----------
    def new_rental(self,rental_id,customer_id,skis=0,snowboards=0,hours=1):
        for rental in self.rental_list:
            if rental.rental_id==rental_id:
                print("id alread being used")
                return None

        if skis>self.skis_in_inventory or snowboards>self.snowboards_in_inventory:
            print("not enough in inventory")
            return None

        #the actual Rental
        self.skis_in_inventory=self.skis_in_inventory-skis
        self.snowboards_in_inventory=self.snowboards_in_inventory-snowboards
        created_rental=Rental(rental_id,customer_id,skis,snowboards,hours)
        self.rental_list.append(created_rental)
        print("New rental ID is:",rental_id)
        return created_rental
    #----------------
    def complete_rental(self,intRentalIID):#Assignment says to use intRentalIID
        rental=self.find_rental(intRentalIID)


