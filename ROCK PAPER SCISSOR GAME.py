#Nothing to do, play Rock Paper Scissor and pass your time!
import random
def rock_paper_scissor(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        else:
            return False
    elif comp=='p':
        if you=='r':
            return False
        else:
            return True
    elif comp=='s':
        if you=='r':
            return True
        else:
            return False
print('Computer\'s Turn : Rock(r) or Paper(p) or Scissor(s)')
game=0
while game==0:
    a=random.randint(1,3)
    if a==1:
        comp='r'
    elif a==2:
        comp='p'
    else:
        comp='s'
    you=input('Your\'s Turn : Rock(r) or Paper(p) or Scissor(s) : ') 
    g=rock_paper_scissor(comp,you)
    print(f'Computer : {comp}')
    print(f'You : {you}')
    if g==True:
        print('You won the game!')
    elif g==None:
        print('Match Drawn!')
    else:
        print('You lose the game!')
    game=int(input('Enter 0 to play the game again or enter 1 to exit from the game: '))
    if game==1:
        break
