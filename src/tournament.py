from time import sleep, time
from draw import start_GUI, draw
from player import Player, RamdomPlayer
from const import HUM, WOLV, VAMP
from board import Board
from game import generate_play

from random import shuffle

class TournamentPlayer():
    def __init__(self, player):
        self.player = player
        self.ELO = 1200
        self.name = "DefaultName"
        self.description = "DefaultDescription"
        self.numberOfGamePlayed = 0
        self.numberOfGameWon = 0

class Tournament:
    def __init__(self):
        self.players = []
        
    def saveTournament(self, path):
        """Prints the state of the tournament to a file to be reused later"""
        raise NotImplementedError()
    
    def importTournament(self, path):
        """Imports the state of a tournament from a file to be continued"""
        raise NotImplementedError()
    
    def addPlayer(self, player):
        self.players = self.players + [player]
        
    def removePlayer(self, numberOfRemainingPlayers):
        self.players.sort(key=lambda x: x.ELO, reverse=True)
        self.players = self.players[0:numberOfRemainingPlayers]
        
    def printBestPlayers(self, topN):
        self.players.sort(key=lambda x: x.ELO, reverse=True)
        print("------ TOURNAMENT TOP"+ str(topN) +" ------")
        for rank in range(0, topN):
            player = self.players[rank]
            print("#"+str(rank+1)+" ELO:"+str(player.ELO) + " " + player.name)
    
    def startTournament(self, totalNumberOfGame):
        for nbGame in range(1, totalNumberOfGame):
            shuffle(self.players)
            #self.players[0].race = VAMP
            #self.players[1].race = WOLV
            self.playOneGame(self.players[0], self.players[1])
    
    def playOneGame(self, player1, player2):
        initial_pop = [{'x': 0, 'y': 0, HUM: 0, VAMP: 40, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]

        board = Board((4, 5), initial_pop)
        # We need to give the actual Player attribute and not a TournamentPlayer
        play = generate_play(player1.player, player2.player, board, False)
        winner = play()
        print(winner + ' won!')
        
        if(winner==VAMP):
            W = 1
        elif(winner==WOLV):
            W = 0.5
        elif(winner==HUM):
            W = 0
        else:
            raise NotImplementedError()
        
        ELO_delta = W - 1/(1+10**((player2.ELO-player1.ELO)/400))
        
        player1.ELO += int(50*ELO_delta)
        player2.ELO -= int(50*ELO_delta)

    
if __name__ == '__main__':
    tournament = Tournament()
    
    player1 = TournamentPlayer(RamdomPlayer(VAMP))
    player1.name = "Dracula"
    tournament.addPlayer(player1)
    
    player2 = TournamentPlayer(RamdomPlayer(WOLV))
    player2.name = "Weird Doggy"
    tournament.addPlayer(player2)
    
    tournament.startTournament(250)
    tournament.printBestPlayers(2)

    
    
    