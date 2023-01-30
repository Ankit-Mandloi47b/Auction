class SuperKings:
    amount=50000
    SelectedplayersList={}
    name="SuperKings"
    
class Titans:
    amount=50000
    SelectedplayersList={}
    name="Titans"

    
class Kings:
    amount=50000
    SelectedplayersList={}
    name="Kings"

    

class Auction:
    PlayerList={'Ankit':10000,'Jaishree':10000,'Lovesh':50000,'Atharva':50000}
    
    def __init__(self) -> None:
        self.superKings=SuperKings()
        self.titans=Titans()
        self.kings=Kings()
        self.teamList=[self.superKings,self.titans,self.kings]

    def printSelectedPlayers(self):
        for team in self.teamList:
            print("Team:"+team.name)
            for player in team.SelectedplayersList:         
                print(player)
 
    def bidding(self):      
        for player in Auction.PlayerList:
            print(player+"-> "+str(Auction.PlayerList.get(player)))
            #key as a team name and value is boolean
            Player_selected_by_team={
                'SuperKings':False,
                'Titans':False,
                'Kings':False
                }
            bidding_amount=0
            base_price=Auction.PlayerList[player]
            last_team_bid=""
            passCount=0
            while passCount<2:
                passCount=0
                for team in self.teamList:
                    
                    print(team.name+" "+"reamining balance  "+str(team.amount))
                    inputPrice=(input('Enter your amount: '))
                
                                
                    if inputPrice=="pass":
                        passCount+=1
                        continue                
                    bidding_amount=int(inputPrice)  
                    if bidding_amount>team.amount:
                        print('dont have sufficient amount')  
                        passCount+=1
                        continue
                                
                    else:
                        #team.amount-=bidding_amount
                        base_price+=bidding_amount
                        last_team_bid=team.name
                        #passCount=0
                        print(player+" new Price->"+str(base_price))   
            if passCount==3:
                print(f'{player}not sold')

            for team in self.teamList:
                if team.name==last_team_bid:
                    team.SelectedplayersList.update({player:base_price})
                    print(f'{player} sold')
                    team.amount-=base_price
                
                    
ob=Auction()
ob.bidding()
ob.printSelectedPlayers()
                
                  


            

           
                






