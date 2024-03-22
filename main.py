board= [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find=find_empty(bo)
    if not find:
        return True
    else:
        row,col=find
    
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True
            bo[row][col]=0
    return False
        


def  print_board(boo):
    for i in range(len(boo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - -")
        
        for j in range(len(boo[0])):
            if j%3==0 and j!=0:
                print(" | ",end="")
            if j==8:
                print(boo[i][j])
            else:
                print(str(boo[i][j]) + " ", end="")



def find_empty(boo):
    for i in range(len(boo)):
        for j in range(len(boo[0])):
            if boo[i][j]==0:
                return (i,j) #row, col
    return None

def valid(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1]!=i:
            return False
    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]]== num and pos[0]!=i:
            return False
        
    #check box
    box_x= pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=i:
                return False
    return True

print_board(board)
solve(board)
print("-----------------------")
print_board(board)