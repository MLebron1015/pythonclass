class price:
    def __init__(self,bevarage, cost):
        self.bevarage = bevarage
        self.cost = cost
    def __str__(self):
        return f"{self.bevarage} ({self.cost})"

    def the_cost(self):
       return self.cost
    def the_bevarage(self):
       return self.bevarage


d1 = price("1Coke", 1.25)
d2 = price("2water", .50)
d3 = price("3Fanta", 1.00)
d4 = price("4MD", 1.25)
d5 = price("7up", 2.00)
d6 = price("Redbull", 3.00)
selection = [d1,d2,d3,d4,d5,d6]


while True:
 print(selection[0],selection[1],selection[2],selection[3],selection[4],selection[5])
 for x in selection:
    try:
        x = int(input("\nSelect an option (1<->6): ")) - 1
        if x < 0 or x >= len(selection):
            print(selection[x])
        print(f"The cost of your selection is: ${selection[x].the_cost()}")

        M = selection[x].the_cost()
        y = float(input("\nMoney: "))

        pay = y - M
        if pay>=0:
            print(f"change: ${pay:.2f}")
            print(f"you get: {selection[x].the_bevarage()}")

        if pay < 0:
            remaining = pay * -1
            button = input(f"Press 1 pay the remaining: ${remaining:.2f} or press 2 to cancel: ")
            if button == '2':
                print("Transaction canceled. Restarting...")
                restart = True

            if button == '1':
               pay=float(input("\nMoney: "))-remaining
               print(f"change: ${pay:.2f}")
               print(f"you get: {selection[x].the_bevarage()}")

        else:
            restart = False
    except ValueError as e:
        print(f": {e}")









