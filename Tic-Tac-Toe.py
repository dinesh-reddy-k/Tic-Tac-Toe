from tkinter import *
import random
import os
global count
t1=Tk()
t1.title('Tic-Tac-Toe')
t1.geometry('300x350')
t1.config(bg='orange')

def checkWinner(board,s):
    '''
        Here we will check the winner if the sign s match with three in a same row
        column and cross then it will return the sign else it will return None
    '''
    cross1 = cross2 = True  # for diagonals
    for j in range(3):
        if board[j][0] == s and board[j][1] == s and board[j][2] == s:# check row j
            displayWinner(s,j)
            return True
        if board[0][j] == s and board[1][j] == s and board[2][j] == s: # check column j
            displayWinner(s,j)
            return True
        if board[j][j] != s: # check 1st diagonal
            cross1 = False
        if board[j][2 - j] != s: # check 2nd diagonal
            cross2 = False
    if cross1:
        displayWinner(s,'c1')
        return True
    if cross2:
        displayWinner(s,'c2')
        return True
    if len(e)==0:
        displayWinner('tie','Na')
        return True
    return False

def exitWindow():
    os._exit(0)
    
def createbox(c1,c2,s):
    if s=='x':
        color='yellow'
    elif s=='o':
        color='pink'
    else:
        color='white'
    w.create_rectangle(c1,c2,c1+60,c2+60,fill=color,outline='black',width=5)
    Label(w,text=s,font=50,bg=color).place(x=c1+25,y=c2+15)
    
def displayBoard():
    print(board)
    global w
    w=Canvas(t1,bg='orange',bd=0,height=180,width=180)
    for i in range(3):
        c1=60*i
        for j in range(3):
            c2=60*j
            createbox(c1,c2,board[j][i])
    w.place(x=60,y=20)
    
def displayWinner(result,line):
    global p1,p2,tie,rl1,rl2,rl3,rl4,rl5,b1,b2
    displayBoard()
    if result=='x':
        p1+=1
        a=m1
    elif result=='o':
        p2+=1
        a=m2
    else:
        tie+=1
    t.destroy()
    if result=='tie':
        rl1=Label(t1,text="It's a tie")
        rl1.place(relx=0.5,rely=0.6,anchor=CENTER)
    else:
        rl1=Label(t1,text=a.upper()+' has won the game')
        rl1.place(relx=0.5,rely=0.62,anchor=CENTER)
    rl2=Label(t1,text='Total Number of games = '+str(tie+p1+p2))
    rl2.place(relx=0.2,rely=0.65)
    rl3=Label(t1,text='Games won by '+m1+' = '+str(p1))
    rl3.place(relx=0.2,rely=0.7)
    rl4=Label(t1,text='Games won by '+m2+' = '+str(p2))
    rl4.place(relx=0.2,rely=0.75)
    rl5=Label(t1,text='Match got Tie = '+str(tie))
    rl5.place(relx=0.2,rely=0.8)
    b1=Button(t1,text='play again',command=display)
    b1.place(relx=0.2,rely=0.95,anchor=CENTER)
    b2=Button(t1,text='Start new game',command=main)
    b2.place(relx=0.5,rely=0.95,anchor=CENTER)
    Button(t1,text='quit',command=exitWindow).place(relx=0.8,rely=0.95,anchor=CENTER)

def nextMove(i):
    '''
        Here we will get the button value as i which are in board
        Then we will update the board and disable the button such that
        the players won't press the button again and display the sign value.
        And check with this move we will get any winner or not.
        And pick random number from the left of items if playing with computer.
    '''
    global result
    e.remove(i)
    board[(i-1)//3][(i-1)%3]='x' if b[0] else 'o'
    b[i]['state']=DISABLED
    b[i].config(bg='yellow' if b[0] else 'pink')
    b[i]['text']='x' if b[0] else 'o'
    if len(e)<5:
        r=checkWinner(board,'x' if b[0] else 'o')
        if r:
            return
    if m2!='Computer':
        b[10]['text']=m2+' turn' if b[0] else m1+' turn'
        b[0]=not b[0]
    else:
        if b[0]:
            b[0]=not b[0]
            nextMove(random.choice(e))
        else:
            b[0]=not b[0]

def display(i=0):
    '''
        Here we will display the button which are the main key of the game
        when we press the button it will redirect to 
    '''
    global m1,m2,t,b,board,e
    if i==0:
        t=Frame(t1)
        t.pack(side='top',expand=True,fill='both')
        t.config(bg='orange')
        e=[1,2,3,4,5,6,7,8,9]
        board=[['','',''],['','',''],['','','']] #to save the board
        b=['']*11 #for the buttons and label in tkinter
        b[0]=True
    if i==1:
        m1=fe.get()
        m2='Computer'
        fe.destroy()
    if i==2:
        m1=fe1.get()
        m2=fe2.get()
        fe2.destroy()
        fe1.destroy()
        fl1.destroy()
        fl2.destroy()
    fl.destroy()
    fb.destroy()
    b[1]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(1))
    b[1].place(x=10,y=10)
    b[2]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(2))
    b[2].place(x=105,y=10)
    b[3]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(3))
    b[3].place(x=200,y=10)
    b[4]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(4))
    b[4].place(x=10,y=105)
    b[5]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(5))
    b[5].place(x=105,y=105)
    b[6]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(6))
    b[6].place(x=200,y=105)
    b[7]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(7))
    b[7].place(x=10,y=200)
    b[8]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(8))
    b[8].place(x=105,y=200)
    b[9]=Button(t,font=(50),height=3,width=7,command=lambda:nextMove(9))
    b[9].place(x=200,y=200)
    b[10]=Label(t,text=m1+' turn',font=50)
    b[10].place(relx=0.5,rely=0.9,anchor=CENTER)

def VsComputer():
    global fe,fl,fb
    l1.destroy()
    bc.destroy()
    bp.destroy()
    fl=Label(t,text='please enter the player Name',font=50)
    fl.place(relx=0.5,rely=0.4,anchor=CENTER)
    fe=Entry(t,font=50,justify=CENTER)
    fe.place(relx=0.5,rely=0.5,anchor=CENTER)
    fb=Button(t,text='submit',command=lambda:display(1))
    fb.place(relx=0.5,rely=0.6,anchor=CENTER)
    
def VsOpponent():
    global fe1,fe2,fl1,fl2,fl,fb
    l1.destroy()
    bc.destroy()
    bp.destroy()
    fl=Label(t,text='please enter the players Names',font=50)
    fl.place(relx=0.5,rely=0.4,anchor=CENTER)
    fl1=Label(t,text='player-1 Name',font=50)
    fl1.place(relx=0.25,rely=0.5,anchor=CENTER)
    fl2=Label(t,text='player-2 Name',font=50)
    fl2.place(relx=0.75,rely=0.5,anchor=CENTER)
    fe1=Entry(t,font=50,justify=CENTER,width=10)
    fe1.place(relx=0.25,rely=0.6,anchor=CENTER)
    fe2=Entry(t,font=50,justify=CENTER,width=10)
    fe2.place(relx=0.75,rely=0.6,anchor=CENTER)
    fb=Button(t,text='submit',command=lambda:display(2))
    fb.place(relx=0.5,rely=0.8,anchor=CENTER)
    
def previous():
    global rl1,rl2,rl3,rl4,rl5,b1,b2
    rl1.destroy()
    rl2.destroy()
    rl3.destroy()
    rl4.destroy()
    rl5.destroy()
    b1.destroy()
    b2.destroy()
 
def main():
    global l1,bc,bp,t,b,board,e,tie,p1,p2,count
    if count!=0:
        previous()
    count+=1
    p1=0
    p2=0
    tie=0
    t=Frame(t1)
    t.pack(side='top',expand=True,fill='both')
    t.config(bg='orange')
    e=[1,2,3,4,5,6,7,8,9]
    board=[['','',''],['','',''],['','','']] #to save the board
    b=['']*11 #for the buttons and label in tkinter
    b[0]=True #for the turn if player 1 turn means True player2 turn means False
    l1=Label(t,text='How would you like to play',font=(500))
    l1.config(bg='red',fg='yellow')
    l1.place(relx=0.5,rely=0.4,anchor=CENTER)
    bc=Button(t,text='vs computer',font=(50),command=VsComputer)
    bc.place(relx=0.2,rely=0.6,anchor=CENTER)
    bc.config(bg='gray',fg='orange')
    bp=Button(t,text='vs opponent',font=(50),command=VsOpponent)
    bp.place(relx=0.8,rely=0.6,anchor=CENTER)
    bp.config(bg='gray',fg='blue')
count=0
main()
t1.mainloop()
