class Rock_paper_scissors:
    compwin=0
    playerwin=0
    roundcount=0
    def __init__(self,rounds):
        self.dict={"rock":1,"paper":0,"scissor":-1}
        self.rounds=rounds
    def player_choice(self,choice):
        return self.dict.get(choice)
    def comp_choice(self):
        import random
        choice=random.randint(-1,1)
        for key,value in self.dict.items():
            if value==choice:
                print("Computers choice:",key)
        return choice
    def round(self,player,comp):
        sum=player+comp
        self.roundcount+=1
        if sum==1:
            if player==0:
                Rock_paper_scissors.playerwin+=1
                print("Player wins round ",self.roundcount,"!",sep="")
            else:
                Rock_paper_scissors.compwin+=1
                print("Computer wins round ",self.roundcount,"!",sep="")
        elif sum==-1:
            if player<0:
                Rock_paper_scissors.playerwin+=1
                print("Player wins round ",self.roundcount,"!",sep="")
            else:
                Rock_paper_scissors.compwin+=1
                print("Computer wins round ",self.roundcount,"!",sep="")
        elif sum==0:
            if player>0:
                Rock_paper_scissors.playerwin+=1
                print("Player wins round ",self.roundcount,"!",sep="")
            elif comp>0:
                Rock_paper_scissors.compwin+=1
                print("Computer wins round ",self.roundcount,"!",sep="")
            else:
                print("Round",self.roundcount,"is a Tie!")
        else:
            print("Round",self.roundcount,"is a Tie!")
        self.rounds-=1
def main():
    rps=Rock_paper_scissors(int(input("How many rounds do you want to play? ")))
    while rps.rounds>0:
        rps.round(rps.player_choice(input("Players choice: ")),rps.comp_choice())
    if rps.compwin>rps.playerwin:
        print("\nComputer wins this game by ",rps.compwin,"-",rps.playerwin,"!",sep="")
    elif rps.compwin==rps.playerwin:
        print("Game is a Tie by ",rps.playerwin,"-",rps.compwin,"!",sep="")
    else:
        print("Player wins this game by ",rps.playerwin,"-",rps.compwin,"!",sep="")
if __name__=='__main__':
    main()
