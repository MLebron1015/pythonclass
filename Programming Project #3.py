class seat:
    def __init__(self,type,num,price,fee,note):
        self.type = type
        self.price = price
        self.num = num
        self.fee = fee
        self.note = note
    def __str__(self):
        return f"({self.type}) ({self.price}) ({self.num}) ({self.fee}) ({self.note})"
    def the_type(self):
       return self.type
    def the_num(self):
       return self.num
    def the_price(self):
       return self.price
    def the_fee(self):
       return self.fee
    def the_note(self):
       return self.note
    def select_seat(self, seat_num):
        if seat_num in [1, 2]:
            self.num = seat_num
        else:
            print("Invalid seat number. Please select seat 1 or seat 2.")
    def deselect_seat(self):
        self.num = None


row1= seat("first class",1, 30.00,25.00,"")
row2= seat("first class",1, 30.00,25.00,"")
row3= seat("first class",1, 30.00,25.00,"")
row4= seat("first class",1, 30.00,25.00,"")
row5= seat("normal",1, 30.00,0,"")
row6= seat("normal",1, 30.00,0,"You are prompted to except responsibility for being able to help in-case of an emergency.")
row7= seat("normal",1, 30.00,0,"")
row8= seat("normal",1, 30.00,0,"")
row9= seat("normal",1, 30.00,0,"You are prompted to except responsibility for being able to help in-case of an emergency.")
row10= seat("normal",1, 30.00,0,"")

Seats= [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10]

def choose_row():
    try:
        print("available rows:")
        for i, seat_instance in enumerate(Seats, start=1):
            print(f"row {i}, {seat_instance.type}, ${seat_instance.price} + ${seat_instance.fee}")
        row_num = int(input("Please select a row number: "))
        if 1 <= row_num <= len(Seats):
            selected_row = Seats[row_num - 1]
            choose_seat(selected_row)
            if 1 <= row_num <= 4:
                print("It cost: $55.00")
            else:
                print("It cost $30.00")
                if row_num == 6:
                    print("You are prompted to except responsibility for being able to help in-case of an emergency.")
                elif row_num == 9:
                    print("You are prompted to except responsibility for being able to help in-case of an emergency.")
            return selected_row.price, selected_row.fee
        else:
            print("Invalid row number. Please select a valid row.")
            return 0, 0
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0, 0


def choose_seat(seat_instance):
    try:
        if seat_instance.num == 1:
            seat_num = int(input(f"Please select seat number (2) for {seat_instance.type}: "))
        elif seat_instance.num == 2:
            seat_num = int(input(f"Please select seat number (1) for {seat_instance.type}: "))
        else:
            seat_num = int(input(f"Please select seat number (1 or 2) for {seat_instance.type}: "))
        seat_instance.select_seat(seat_num)
    except ValueError:
        print("Invalid input. Please enter the asked number(s).")

def main():
    total_price = 0
    total_fee = 0
    while True:
        for seat_instance in Seats:
            seat_instance.deselect_seat()
        price,fee = choose_row()
        total_price += price
        total_fee += fee
        priceandfee= total_fee + total_price
        if input("Type '1' to stop or press Enter to continue: ").strip().lower() == '1':
            break
    print(f"Price: ${total_price:.2f}")
    print(f"Price + Fee: ${priceandfee:.2f}")

main()





