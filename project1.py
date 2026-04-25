#Welcome user
print("Welcome to the Beauty Salon")
print()

#while loop to present menu and ask for user input for hairstyle selection
while True:    
    print("Please select one of our signature styles: ")
    menu=("""
    A. Around the Way Curl($55.99)
    B. Silk Press($65.50)
    C. Two Strand Twists($85.00)
    D. Wash and Go($55.99)
    E. Crochet Faux Locs($199.99)""")
    print(menu)
    print()
    menuinput=(input("Selection:"))
    print()
    #if-elsestatemnts/conditionals for user input of style
    if menuinput== "A":
        print("You've selected Around the Way Curl")
        subtotal= 55.99
        stylena= "Around the Way Curl"
        break
    elif menuinput== "B":
        print("You've selected Silk Press")
        subtotal= 65.60
        stylena= "Silk Press"
        break
    elif menuinput== "C":
        print("You've selected Two Strand Twists")
        subtotal=85.00
        stylena= "Two Strand Twists"
        break
    elif menuinput== "D":
        print("You've selected Wash and Go")
        subtotal=55.99
        stylena= "Wash and Go"
        break
    elif menuinput== "E":
        print("You've selected Crochet Faux Locs")
        subtotal=199.99
        stylena= "Crochet Faux Locs"
        break
    else:
        print("Invalid choice, please try again.")
        
print()
#While loop for to present extras menu and ask for user input
while True:
    #extras menu
    extrasmenu=(""" Feel free to add extra services.
    
    1. Trim (requires Two Strand Twists or Silk Press ($15)
    2. Deep conditioning mask ($20) 
    3. Detangling ($15)
    4. Steam treatment (requires around the way curl or wash and go) ($35)
    5. Take down service (requires Crochet Faux Locs) ($50)
    6. Done""")
    print(extrasmenu)
    #ask for user input for extra services
    print()
    extrasinput=input("Any Extras?")
    print()
    #if-else statements/conditionals for user input of extra services
    if extrasinput== "1":
        if menuinput=="B" or menuinput=="C":
            print("You've added Trim")
        else:
            print("This extra requires Two Strand Twists or Silk Press")
        print()
        extra=15.00
        extraserv= "Trim"
    elif extrasinput=="2":
        print("You've added Deep Conditioning Mask")
        print()
        extra=20.00
        extraserv="Deep Conditioning Mask"
    elif extrasinput=="3":
        print("You've added Detangling")
        print()
        extra=15.00
        extraserv="Detangling"
    elif extrasinput=="4":
        if menuinput=="A" or menuinput=="D":
            print("You've added Steam Treatment")
        else:
            print("This extra requires around the way curl or wash and go")
        print("You've added Steam Treatment")
        print()
        extra=35.00
        extraserv="Steam Treatment"
    elif extrasinput=="5":
        if menuinput=="E":
            print("You've added Take Down Service")
        else:
            print("This extra requires Crochet Faux Locs")
        print()
        extra=50.00
        extraserv="Take Down Service"
    elif extrasinput=="6":
        break
    else:
        print("Invalid input. Please select a number 1-6.")
    
print()
finsub=subtotal+extra             
print("Your subtotal is: $",round(finsub,2))
print()
#while loop for correct tipping amount
while True:
    try:
        tip_input=float(input("Please enter your tip amount:$"))
        if tip_input<0:
            print("Tip cannont be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
print()       
print("*******Your receipt*******")
print()
style=print("Style:",stylena)
print()
Extra=print("Extra:",extraserv,"$",round(extra,2))
print()
Tip=print("Tip:$",tip_input)
print()
total=subtotal+tip_input+extra
print("Your total is:$",round(total,2))


    

    


