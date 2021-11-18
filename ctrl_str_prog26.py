code='0805'
t=0
for i in range (1,4):
    pin=input("Enter the PIN code:")
    if pin==code:
        print("Correct!")
    else:
        print("Incorrect...")
        t+=1
        if t==3:
            print("Sorry, your payment card has been blocked.")


        
        #if pin!=code:
    #print("Sorry, your payment card has been blocked.")
