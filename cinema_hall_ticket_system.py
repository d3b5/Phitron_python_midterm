class Hall:        
    def __init__(self,row,col,hall_no):
        #5 instance attributes
        self.__seat={} #dictionary
        self._show_list=[] #list of tuple
        self.__row=row
        self.__col=col
        self.__hall_no=hall_no        

    def entry_show(self,id,movie_name,time):        
        show = (id,movie_name,time) #tuple
        self._show_list.append(show)
        self.__seat[id]=[[0 for j in range(self.__col)] for i in range(self.__row)]

    def view_available_seats(self,id):
        if self.__seat.get(id) is None:
            print("Invalid Movie ID")
        else:
            grid = self.__seat[id]
            cnt=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        cnt+=1
                    print (grid[i][j],end=' ')
                print()
            print("Booked Seat: ",cnt)
            print("Available seat: ",self.__row*self.__col - cnt)

    def view_show_list(self):
        print(f"Shows in Hall {self.__hall_no}:")
        for i,film in enumerate(self._show_list,1):
            print(f"{i}. MOVIE NAME: {film[1]}, SHOW ID: {film[0]}, TIME: {film[2]} ")

    def book_seat(self,id,row,col):
        if row <0 or self.__row<row :
            print("Invalid Seat Row")
        elif col <0 or self.__col<col:
            print("Invalid Seat Column")
        elif self.__seat.get(id) is None:
            print("Invalid Movie ID")
        elif self.__seat[id][row][col]==1:
            print("This is seat is booked. Choose another one.")
        else:
            self.__seat[id][row][col]=1
            print("Purchase successful!")

class Star_Cinema:
    __hall_list = []
    def __init__(self,name):
        self.name=name
    def entry_hall(self,hall):
        self.__hall_list.append(hall)

cineplex = Star_Cinema('Star Cinema')
hall1=Hall(10,10,1)
hall1.entry_show(100,'Alice In Wonderland',"12 March 2026, 10:00 AM")
hall1.entry_show(101,'Batman Begins',"12 March 2026, 01:00 PM")
hall1.entry_show(102,'Captain America',"12 March 2026, 04:30 AM")
hall1.entry_show(103,'Don',"12 March 2026, 07:30 AM")
cineplex.entry_hall(hall1)
while True:
    print("""<--------------------------------------------------------->
    1. View All Show Today
    2. View Available Seats
    3. Book Ticket
    4. Exit""")
    op = int(input("Select Option:"))

    if op==1:
        hall1.view_show_list()
    elif op==2:
        id = int(input("Movie ID: "))
        hall1.view_available_seats(id)
    elif op==3:
        id = int(input("Movie ID: "))
        row = int(input("Row: "))
        col = int(input("Col: "))
        hall1.book_seat(id,row,col)
    elif op==4:        
        print("Goodye")
        print("<--------------------------------------------------------->")
        break
    else:
        print("Invalid Option")
    print("<--------------------------------------------------------->")
