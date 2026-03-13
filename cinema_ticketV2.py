class Show:
    def __init__(self,name,id,time):
        self.name = name
        self.id = id
        self.time = time
    def __repr__(self):
        return f"{self.name} | {self.time} | Show ID: {self.id}"

class Hall:
    def __init__(self,row,col):
        self.__row = row
        self.__col = col
        self.__shows = {} #dict of shows 
        self.__seat_plan = {} #dict of dict
    
    def add_show(self,id,movie_name,time):
        if self.__shows.get(id) is None:
            show = Show(movie_name,id,time)
            self.__shows[id]=show
            self.__seat_plan[id]=[['O' for j in range(self.__col)] for i in range(self.__row)]
        else:
            print("This ID is already use for a movie. Use another ID. ID used by:")
            print(self.__shows[id])

    def get_show(self): #view all shows for instance hall
        for i,film in enumerate(self.__shows.values(),1):
            print(f"{i}. {film}")

    def get_seat_map(self,id): #prints 2D matrix
        if self.__shows.get(id) is None:
            print("Invalid ID")
        else:
            print(f"Seat Map for {self.__shows[id]}\n")
            grid=self.__seat_plan[id]
            print('   ',end='')

            for j in range(self.__col):
                print(j,end=' ')
            print()

            for i in range(self.__row):
                print(i,end='  ')
                for j in range(self.__col):
                    print(grid[i][j],end=' ')
                print()
            print()

    def get_available_seat_coordinates(self,id): #prints 2D matrix
        if self.__shows.get(id) is None:
            print("Invalid ID")
        else:
            print(f"Available seats for {self.__shows[id]}\n")
            cnt=1
            grid=self.__seat_plan[id]
            for i in range(self.__row):
                for j in range(self.__col):
                    if grid[i][j]=='O':
                        print(f"{cnt}. Seat({i},{j})")
                        cnt+=1
            print("\nAvailable seats: ",cnt-1)
            print("Booked Seats: ", self.__row*self.__col-cnt+1)   
            print() 
    def book_seat(self,id,row,col):
        flag = False
        if id not in self.__shows:
            print("Invalid ID")
        elif row<0 or row>=self.__row:
            print("Invalid Row")
        elif col<0 or col>=self.__col:
            print("Invalid Column")
        elif self.__seat_plan[id][row][col]=='X':
            print("This seat is BOOKED! Please book an available seat")
        else:
            self.__seat_plan[id][row][col]='X'
            flag = True
        return flag
    def find_show(self,id):
        return id in self.__shows  
    def get_show_details(self,id):
        return self.__shows.get(id)
class Cineplex:
    
    def __init__(self,name):
        self.name = name
        self.__hall_list=[]
    
    def add_hall(self,hall):
        self.__hall_list.append(hall)
    
    def get_all_shows(self):
        for i,hall in enumerate(self.__hall_list,1):
            print(f"Shows in Hall {i}:")
            hall.get_show()
    def find_show_hall(self,id):
        for i,hall in enumerate(self.__hall_list):
            if hall.find_show(id):
                return i
        return -1
    def book_ticket(self,id,row,col):
        hall_no=self.find_show_hall(id)
        if hall_no == -1:
            print("Invalid ID")
        else:
            if self.__hall_list[hall_no].book_seat(id,row,col):
                print(f"\nSeat successfully booked!")
                print("For: ",self.__hall_list[hall_no].get_show_details(id))
                print(f"Seat: ({row},{col}) in Hall {hall_no+1}")
                print("Updated Seat Map: ")
                self.__hall_list[hall_no].get_seat_map(id)
                print()
                
    
    def seat_plan(self,id):
        hall_no=self.find_show_hall(id)
        if hall_no == -1:
            print("Invalid ID")
        else:
            self.__hall_list[hall_no].get_available_seat_coordinates(id)
            self.__hall_list[hall_no].get_seat_map(id)

#declaring a cinema theatre
star_cinema=Cineplex('Star Cinema')
#halls of the theatre
hall1=Hall(7,7)
hall2=Hall(10,7)
#hall 1
hall1.add_show(100, "Alice In Wonderlan","14 March 2026, 10:00 AM")
hall1.add_show(101, "Breakfast Club","14 March 2026, 10:00 AM")
hall1.add_show(102, "Casino Royale","14 March 2026, 10:00 AM")
#hall 2
hall2.add_show(200, "Die Hard","14 March 2026, 10:00 AM")
hall2.add_show(201, "E.T","14 March 2026, 10:00 AM")
hall2.add_show(202, "Fight Club","14 March 2026, 10:00 AM")

star_cinema.add_hall(hall1)
star_cinema.add_hall(hall2)

while True:
    print("<----------------------------------------------------->")
    print("""Options:
    1. View all shows
    2. View available seats (show_id)
    3. Book ticket (show_id, row, col)
    4. Exit""")
    op = int(input("Select option: "))
    
    if op==1:
        print("All Shows Today:")
        star_cinema.get_all_shows()
    elif op==2:
        id = int(input("Enter Show ID: "))
        star_cinema.seat_plan(id)
    elif op==3:
        id = int(input("Enter Show ID: "))
        row = int(input("Enter Seat Row: "))
        col = int(input("Enter Seat Col: "))
        star_cinema.book_ticket(id,row,col)
    elif op==4:
        print("Thanks for visiting!")
        break
    else:
        print("Invalid Option")




