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
            Player_selected_by_team={
                'SuperKings':False,
                'Titans':False,
                'Kings':False
                }#key as a team name and value is boolean
            bidding_amount=0
            base_price=Auction.PlayerList[player]
            for team in self.teamList:
                print(team.name+" ")
                inputPrice=(input('Enter your amount: '))
               
                            
                if inputPrice=="pass":
                    continue                
                bidding_amount=int(inputPrice)  
                if bidding_amount>team.amount:
                    print('dont have sufficient amount')  
                    continue
                             
                else:
                    team.amount-=bidding_amount
                    base_price+=bidding_amount
                    Player_selected_by_team.update({team:True})  
            check=False
            for soldlist in Player_selected_by_team:
                if Player_selected_by_team.get(soldlist)==True:
                    soldlist.SelectedplayersList.update({player:base_price})
                    print("player sold to"+soldlist.name)
                    check=True
            if check==False:
                print(player+' not sold')
                    
ob=Auction()
ob.bidding()
ob.printSelectedPlayers()
                
                  


            

           
             

    

ob=Auction()
ob.bidding()        






