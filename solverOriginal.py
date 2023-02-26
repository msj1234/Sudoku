import pprint
##To run in terminal 
## open terminal cd to folder and run: python3 solverOriginal.py

# the link to the youtube sudoku solver
#declaring the board we want to use for this version of it
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

#algorithm that solves using backtrackunig algorithm and uses all other functions defined
def solve(bo):
    #using recursion
    find = find_empty(bo)
     #base case - board is full 
    if not find:
        return True
    else: 
        row, col = find

    #apply backtracking algorithm here 
    #loop through 1 to 9 and attemt to put them in our solution
    for i in range (1, 10):
        #try this value inside our solution but check if board will be valid with this val
        if valid(bo, i, (row,col)):
            #if its  valid , add it into the board
            bo[row][col] = i

            #try to recursivley solve the board with this new value(1-9) added 
            if solve(bo):
                return True
            bo[row][col] = 0 #else backtrack by reseting the value and repeat this loop of trying 1-9 recursivly

    #if we loop though all nums 1-9 and none of them are valid. return false meaning solve wont be true so we need to backtrack
    return False



#find if current board given is valid 
def valid(bo, num, pos):
    #check row - go through every single column in given row 
    for i in range(len(bo[0])):  #len(bo[0]) will be 9 bc we have 9 rows
        
        #check through each element/ column and check if its equal to whatever num we just added in and if were checking through the board and its the positoon we just added into, ignore it and move on
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check Column vertically (same as row check just switch posiotns)
    for i in range(len(bo)): #loop through every single row 0 to 8
        #check if current value is = numb we just instered and not the exact position we just inserted into 
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check which box we are in within the board of 9 boxes (every 3 rows and 3 columns is a box) - to do this we ca nuse integer divison 
    #think of each box as (0,0) | (0,1) | (0,2)
    #                      --------------------
    #                     (1,0) | (1,1) | (1,2)
    #                      --------------------
    #                     (2,0) | (2,1) | (2,2)
    
    #get column position and integer divide by 3
    box_x = pos[1] // 3
    #get row and interger divide by 3
    box_y = pos[0] // 3

    #now that we know what box we are in, loop through all 9 elements in that box and make sure no duplicates
    #why are we *3? bc we / bthe index by 3 to  get the boxes so to get actual index we must reverse and *3
    for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False #if we found a duplicate then return false

    #at the end of all these checks it means its a valid postion therefore return true
    return True
    

    



#function to print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:  #after every 3 rows, put a divier 
            print(" - - - - - - - - - - -")  
            #len(bo[0]) - gets length of our rows
        #for every position in the row
        for j in range(len(bo[0])): #iterate j through the rows of our board 
        #print horizotal lines 
            if j % 3 == 0 and j != 0:
                #doesnt print /n means we dont go to next line so we can print out rows 
                print(" | ", end="")


            #if were at the last postion in the board
            if j == 8:
                #print the number
                print(bo[i][j])
            else:
                #end="" so that we can stay on the same line when printing things
                print(str(bo[i][j]) + " ", end="")
#this will print out the board declared above
#print_board(board)

#given a board function will find an empty square/place
def find_empty(bo):
    #return posiotn of that square by looping through board and find it as empty (denoted as 0 in this case)
    for i in range(len(bo)):
        for j in range(len(bo[0])): #range is the length of each row
            #check if position is 0
            if bo[i][j] == 0:
                return (i, j) #return row, column
    
    #if there is no blank sqaures = to zero it will trigger the base case in solve func
    return None


            
#to run this solution lets make some calls
print("")
print("unsolved board:") 
print("")
print_board(board) #print bord before 
solve(board) #solve the board
print("")
print("solved board:")
print("")
print_board(board) #print board after
