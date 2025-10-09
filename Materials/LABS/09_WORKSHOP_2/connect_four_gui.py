SLOTS_TO_WIN = 4

import tkinter as tk #tk is alias for tkinter
from tkinter import messagebox

class InvalidColumnError(Exception):
    pass

class FullColumnError(Exception):
    pass


def create_matrix(rows,cols):
    return [[0] * cols for _ in range(rows)]



#def validate_column_choice(col_num,max_idx):
#    if not (0 <= int(col_num) <= max_idx):
#        raise InvalidColumnError

def place_player(ma,c,player_n):
    for r in range(len(ma) - 1,-1,-1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r,c 
    return FullColumnError


def is_player_number(ma,r,c,player_n):
    try:
        return ma[r][c] == player_n
    except IndexError:
        return False


def is_vertical_win(ma,r,c,player_n,slots=SLOTS_TO_WIN):
    return all([is_player_number(ma,r + idx ,c,player_n) for idx in range(slots)])

def is_horizontal_win(ma,r,c,player_n,slots=SLOTS_TO_WIN):
    filled = 1

    for idx in range(1,slots):
        if is_player_number(ma,r,c + idx,player_n):
            filled += 1
        else:
            break

    for idx in range(1,slots):
        if is_player_number(ma,r,c - idx,player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_left_diagonal_win(ma,r,c,player_n,slots=SLOTS_TO_WIN):
    filled = 1
    for idx in range(1,slots):
        if is_player_number(ma,r + idx ,c + idx,player_n):
            filled += 1
        else:
            break


    for idx in range(1,slots):
        if is_player_number(ma,r - idx,c - idx,player_n):
            filled += 1
        else:
            break

    return filled >= slots




def is_right_diagonal_win(ma,r,c,player_n,slots=SLOTS_TO_WIN):
    filled = 1
    for idx in range(1,slots):
        if is_player_number(ma,r - idx ,c + idx,player_n):
            filled += 1
        else:
            break
    
       

    for idx in range(1,slots):
        
        if is_player_number(ma,r + idx,c - idx,player_n):
            filled += 1
        else:
            break

    return filled >= slots       


def is_winner(ma,r,c,player_n,slots=SLOTS_TO_WIN): #WE SET THE CONS AS A DEFAULT VALUE FOR THE MATRIX WIN CRITERIA 

    return any ([
        is_vertical_win(ma,r,c,player_n,slots),
        is_horizontal_win(ma,r,c,player_n,slots),
        is_left_diagonal_win(ma,r,c,player_n,slots),
        is_right_diagonal_win(ma,r,c,player_n,slots)
    ])


def update_ui(lables, row,col,player_num):
    colour = 'red' if player_num == 1 else 'blue'
    lables[row][col].config(bg = colour)


def reset(ma,rows,cols, lables):
    for r in range(rows):
        for c in range(cols):
            ma[r][c] = 0
            lables[r][c].config(bg='white')




def handle_click(ma,lables,column_num,player_num,counter,rows,cols,slots):
    try:
        #validate_column_choice(column_num,cols-1)
        row,column_num = place_player(ma,column_num,player_num)
        update_ui(lables,row,column_num,player_num)
        if is_winner(ma,row,column_num,player_num,slots):
            messagebox.showinfo("Game Over",message=f"The winner player {player_num} is the winner!")
            reset(ma,rows,cols,lables)
            return 1,0
        
        counter += 1
        if rows  * cols == counter:
            messagebox.showinfo('Game Over', message= "Draw!")
            reset(ma,rows,cols,lables)
            return 1,0
        
        return 2 if player_num == 1 else 1,counter


    except FullColumnError:
        messagebox.showerror("Invalid move",message='This column is full, please select another')


    return player_num,counter


def create_ui(root,row,col,slots):
    matrix = create_matrix(row,col)
    lables = [[tk.Label(root, text = " ", width=4,height=2,bg = "white",relief="solid") for _ in range(col)] for _ in range(row)] #attaches a lable for every column in every row
    
    for r in range(row):
        for c in range(col):
            lables[r][c].grid(row=r + 1,column = c)   #makes 1 row room for buttons




    game_state = {"player_num" : 1,"counter" : 0}

    def on_click(coulum_num,state):
        state["player_num"],state["counter"] = handle_click(matrix,
                                                            lables,
                                                            coulum_num,
                                                            state["player_num"],
                                                            state["counter"],
                                                            row,
                                                            col,
                                                            slots)                  
        pass            

    buttons = [tk.Button(root,
                         text="A",
                         width=4,
                         height=2,
                         bg='yellow',
                         command =lambda c_idx = c: on_click(c_idx,game_state)) 
                         
                for _ in range(c)]
    for c,button in enumerate(buttons):
        button.grid(row = 0,column = c)

def start_game():
    root = tk.Tk()   #the window for the GUI
    root.title('Connect four') #gives title to the window
    rows,cols,slots_to_win = 6,7,4
    create_ui(root,rows,cols,slots_to_win)

    root.mainloop()  
 
if  __name__ == "__main__":
    start_game()