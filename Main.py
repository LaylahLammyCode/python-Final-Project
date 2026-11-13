
import Classes
from Classes import Customer
from Classes import Rental
from Classes import Shop

#-----------
person_One=Customer("Smith",1001,"513-550-1234")
order=Rental(1,person_One.customer_ID,5,2,4)
#---------
All_customers=[person_One]
All_rentals=[order]
#--------
total=order.get_total()
my_shop=Shop(20,15,All_customers,All_rentals,total)
#-----------------
person_One.display()
print("-------------")
order.display(total)
#-----------
found_customer=my_shop.find_customer(1001)
print("--------------")
print("Customer found:",found_customer.last_name)

