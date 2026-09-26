#welcome to Mady Cars
print("========================================")
print("         🚗 MADY CARS 🚗")
print("========================================")
print("#Welcome to Mady Cars")

#car list

Cars = ["Bmw","Mercedes", "Toyota", "Honda", "Nissan"]
price = [5000000, 4000000, 3000000, 2000000, 1000000]
discount = [10, 20, 30, 40, 50]

# Show Available Cars
print(f"Available Cars: \n {'\n'.join(Cars)}")

#search for a car
search_Car = input("Enter the Car You Want: ").strip().capitalize()

print("=" * 50)

if search_Car in Cars:
 
 print(f"Yes, {search_Car} is available.")
 print("=" * 50)
  # Get Car Index
 car_index = Cars.index(search_Car)

  # Get Car Price
 Car_Price = price[car_index]

 print(f"The Price of {search_Car} is: {Car_Price :,d} EGP")

  # Get Discount
 Car_Discount = discount[car_index]

 print(f"You Have A Discount Equal To {Car_Discount}%")

# Calculate Discount Value
 discount_value = int(Car_Price *  Car_Discount / 100)

 print(f"The Discount Value is: {discount_value:,d} EGP")
 
  # Calculate Final Price
 final_price = int(Car_Price - discount_value)

 print(f"The Final Price  is: {final_price:,d} EGP")
 print("=" * 50)
 buy_car = input("Do You Want To Buy This Car? Y / N: ").strip().capitalize()
 if buy_car == "Yes" or buy_car == "Y":
    
    customer_name = input("Enter Your Name: ").strip().capitalize()
    customer_age = int(input("Enter Your Age: ").strip())
    customer_phone = input("Enter Your Phone Number: ").strip()
    print("=" * 50)

    customer_budget = int(input("Enter Your Budget: ").strip())
    print("=" * 50)

    if customer_age >= 18:
       if customer_budget >= final_price:
           
           print(f"Your Budget Is Enough To Buy {search_Car}.")
           print(f"Customer Name: {customer_name}")
           print(f"Customer Age: {customer_age}")
           print(f"Customer Phone: {customer_phone}")
           print(f"Car Bought: {search_Car}")
           print(f"Final Price: {final_price:,d} EGP")

           print("=" * 50)

           payment_method = input("Choose Payment Method: Cash / Visa: ").strip().capitalize()

           print("=" * 50)

           if payment_method == "Cash" or payment_method == "C":
            print(f"You Have Paid {final_price:,d} EGP In Cash.")
            print(f"Congratulations, You Have Bought {search_Car}.")

           elif payment_method == "Visa" or payment_method == "V":
             print(f"You Have Paid {final_price:,d} EGP Using Visa.")
             print(f"Congratulations, You Have Bought {search_Car}.")
             
           else:
             print("Invalid Payment Method.")  

       else:
           print(f"Sorry, Your Budget Is Not Enough To Buy {search_Car}.") 
           
    else:
     print("Sorry, You Are Not Eligible To Buy A Car.")

 elif buy_car == "No" or buy_car == "N":
   print(f"Thank You For Visiting Mady Cars.")
   

else:
 print(f"Sorry, {search_Car} is not available.")

   # Add the car to the list if not available
 status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

 if status == "Yes" or status == "Y":
         
         print("You Have Been Added")
    
         Cars.append(search_Car) 

         print(f"Available Cars: \n {'\n'.join(Cars)}")

