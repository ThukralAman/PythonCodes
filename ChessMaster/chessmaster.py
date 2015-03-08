import os
import sys


class ChessMaster(object):
    """ make Killer Knights game. Killer Knights is a chess game in which all the rules are normal except the players have only knights (ghoda) and one king as pieces. Each player can have any number of knights but only one king.

You will be given a string representation of the chess board of a particular point in time.

You have to implement a class called ChessMaster. ChessMaster will have the following methods:"""
    
    def __init__( self ):
        self.boardString = []
        self.kl = None
        self.kd = None
        self.nd_list = []
        self.nl_list = [] 
        
        
        
        
        
    
     
    
    def fromString(self, boardString):
        """set the config of the chessboard based on the boardString.  This replaces the previous configuration, if any. for example:
String chessBoard = 
            "|kl|  |  |nl|  |nl|  |nl|=\n"+
            "|  |  |  |  |  |  |  |  |=\n"+
            "|  |nd|nd|  |  |  |  |  |=\n"+
            "|  |  |  |nd|  |  |  |  |=\n"+
            "|  |  |  |  |  |  |  |  |=\n"+
            "|  |  |  |  |  |  |  |  |=\n"+
            "|  |  |  |  |  |  |  |  |=\n"+
            "|  |  |  |  |kd|  |  |  |";

k = king, n = knight(ghoda), l = light(white), d = dark(black)
so white pieces are represented as: kl, nl
black pieces are represented as: kd, nd"""
        
        for i in range (0,8):
            boardString[i].pop(0)
            boardString[i].pop(8)
            
        self.boardString = boardString
        
        for i in range(0,8):
            for j in range(0,8):
                if self.boardString[i][j] == "kl":
                    self.kl = king(i,j,"l")
                    
                elif self.boardString[i][j] == "kd":
                    self.kd = king(i,j,"d")
                    
                elif self.boardString[i][j] == "nl":
                    white_horse = knight(i,j,"l")
                    self.nl_list.append(white_horse)
                    
                elif self.boardString[i][j] == "nd":
                    black_horse = knight(i,j,"d")
                    self.nd_list.append(black_horse)
                    
                    
                    
    def IsWhiteInCheck(self):
        """returns true if white is in check and false otherwise."""   
        horse_giving_check = self.__get_horse_giving_check(self.kl)
        
        if  horse_giving_check:
            return True
        else :
            return False
        
       
    def IsWhiteInCheckmate(self):
        """returns true is white is in checkmate and false otherwise.""" 
        if not self.IsWhiteInCheck():
            return False
        black_horse = self.__get_horse_giving_check(self.kl)
        for white_horse in self.nl_list:
            for each_move in white_horse.get_valid_move_positions():
                if each_move == black_horse.get_position():
                    return False
                
        king_valid_moves = self.kl.get_valid_move_positions()
        for each_move in king_valid_moves:
            self.kl.make_move(each_move)
            if (self.IsWhiteInCheck()) or self.__isOtherKingBesides() :
                self.kl.undo_move()
                continue
            else:
                self.kl.undo_move()
                return False
            
        return True  
          
              
        
        
        
        
    def canBlackCheckMateInOneMove(self):
        """returns true if black player can make a move that will put white in checkmate""" 
        if self.IsWhiteInCheckmate() or self.IsWhiteInCheck():
            return "White may be checked or checmated, so its white's turn"

        if self.__get_horse_move_to_checkmate(self.nd_list) != None:
            return True
        elif self.__get_king_move_to_checkmate(self.kd)  != None:
            return True
        else :
            return False
        
        
        
        
        
    def makeBlackCheckMateMove(self):
        """makes the move of black player which will checkmate white player"""
        if self.IsWhiteInCheckmate() or self.IsWhiteInCheck():
            return "White may be checked or checmated, so its white's turn "
        
        horse_move = self.__get_horse_move_to_checkmate(self.nd_list)
        # horse_move is a tuple (horse_move, horse_obj)
        if horse_move:
            #print "moving nd from ", "(" , horse_move[1].posx , " , " , horse_move[1].posy , ") to " , horse_move
            print "moving nd from " , horse_move[1].get_position() , "to" , horse_move[0] 
            horse = horse_move[1]
            horse.make_move( horse_move[0] )
            self.__update_boardString(horse)
            return 
            
        king_move = self.__get_king_move_to_checkmate(self.kd)
        if king_move:
            print "moving king to ", king_move
            self.kd.make_move( (king_move) )
            self.__update_boardString(self.kd)
            
            
        
        
        
    def toString(self):
        """returns the string representation of the chess board"""
        for i in range(0,8):
            row = "|"
            for j in range(0,8):
                row = row + self.boardString[i][j] + "|"
            print row
            
            
            
            
    def __get_horse_giving_check(self,king):
        """ Returns the horse giving check to king, None otherwise"""
        if king == self.kl:
            horse_list = self.nd_list
        else:
            horse_list = self.nl_list
        
        check_giving_positions = king.get_check_giving_positions() 
        for each_check_giving_position in check_giving_positions:
            for each_horse in horse_list:
                if each_check_giving_position == each_horse.get_position():
                   return each_horse
        
        return None
    
    
    def __get_horse_move_to_checkmate(self,horse_list):
        """ returns the position of horse, where it can move to give checkmate to opposite king"""
        for each_horse in horse_list:
            for each_move_position in each_horse.get_valid_move_positions():
                if self.boardString[ each_move_position[0] ][ each_move_position[1] ][1] != each_horse.color and self.boardString[ each_move_position[0] ][ each_move_position[1] ] != "kl":
                   each_horse.make_move(each_move_position)
                   
                   if self.IsWhiteInCheckmate() :
                       each_horse.undo_move()
                       return ( (each_move_position, each_horse) )
                   
                   each_horse.undo_move()
        
        return None
    
    def __get_king_move_to_checkmate(self,king):
        """ returns the move of king which checkmates the other king """
        for each_move_position in king.get_valid_move_positions():
            if self.boardString[ each_move_position[0] ][ each_move_position[1] ][1] != king.color:
                king.make_move(each_move_position)
                if self.IsWhiteInCheckmate() :
                    king.undo_move()
                    return ( each_move_position )
                   
                king.undo_move()
        
        return None
    
    
    def __update_boardString(self, piece):
        prev_position = piece.move_history.pop()
        prev_x = prev_position[0]
        prev_y = prev_position[1]
        self.boardString[prev_x][prev_y] = "  "
        if isinstance(piece,knight):
            self.boardString[piece.posx][piece.posy] ="n"+piece.color
        else :
            self.boardString[piece.posx][piece.posy] ="k"+piece.color
             
         
    def __isOtherKingBesides(self):
        if abs(self.kl.posx - self.kd.posx) <= 1 and abs(self.kl.posy - self.kd.posy) <=1:
            return True
        else:
            return False
       
            
        
            
            
class piece(object):
    def __init__(self,x,y,color):
        self.move_history = []
        self.posx = x
        self.posy = y
        self.color = color
        
    def _is_valid_position(self, x, y):
        if x > -1 and x <8  and y > -1 and y <8 :
            return True
        else :
            return False 
        
    def get_position(self):
        return( (self.posx, self.posy) ) 
    
    def make_move(self, position):
        """NOTE Enhancement required:  instead of accepting position from outside, object should force the client to do king.set_new_position(position) which should update class member variables "new_posx and new_posy"and then call king.move """
        self.move_history.append( (self.posx, self.posy) )
        self.posx = position[0]
        self.posy = position[1] 
        
        
    def undo_move(self, undo_count=1):
        if self.move_history:
            move_history_index = len(self.move_history) - undo_count 
            last_move = self.move_history[move_history_index]
            self.posx = last_move[0]
            self.posy = last_move[1]
            self.move_history.pop(move_history_index)     
        
class king(piece):
    move_displacement_all = [(0,-1),(0,1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]
    checked_by_horse_displacement_all =[(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
    
    
    def get_valid_move_positions(self):
        """ returns list of all positions where king can move"""
        valid_moves = []
        for each_displacement in self.__class__.move_displacement_all :
            move_posx = self.posx + each_displacement[0]
            move_posy = self.posy + each_displacement[1]
            if self._is_valid_position(move_posx, move_posy):
                valid_moves.append( (move_posx, move_posy) )
        return valid_moves
        
    
    def get_check_giving_positions(self):
        """ returns list of all positions where, if horse is present then king is checked"""
        position_giving_check = []
        for each_displacement in self.checked_by_horse_displacement_all :
            check_posx = self.posx + each_displacement[0]
            check_posy = self.posy + each_displacement[1]
            if self._is_valid_position(check_posx, check_posy):
                position_giving_check.append( (check_posx,check_posy) )
                
        return position_giving_check
    
    
        
        
            
    
        #self.move_displacement_list = [(0,-1),(0,1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]
        #self.check_displacement_list = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
        
class knight(piece):
    move_displacement_all = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
    cut_by_horse_displacement_all = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)]
    cut_by_king_displacement_all = [(0,-1),(0,1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]
    
    def get_valid_move_positions(self):
        """ returns all valid position where this horse can move currently"""
        valid_moves = []
        for each_displacement in self.__class__.move_displacement_all :
            move_posx = self.posx + each_displacement[0]
            move_posy = self.posy + each_displacement[1]
            if self._is_valid_position(move_posx, move_posy):
                valid_moves.append( (move_posx, move_posy) )
        return valid_moves
    
    def get_attacked_by_horse_positions(self):
        attacked_by_horse_positions = []
        for each_displacement in self.__class__.cut_by_horse_displacement_all :
            attacked_by_posx = self.posx + each_displacement[0]
            attacked_by_posy = self.posy + each_displacement[1]
            if self._is_valid_position(attacked_by_posx, attacked_by_posy):
                attacked_by_horse_positions.append( (attacked_by_posx,attacked_by_posy) )
                
        return attacked_by_horse_positions
    
    def get_attacked_by_king_positions(self):
        attacked_by_king_positions = []
        for each_displacement in self.__class__.cut_by_king_displacement_all:
            attacked_by_posx = self.posx + each_displacement[0]
            attacked_by_posy = self.posy + each_displacement[1]
            if self._is_valid_position(attacked_by_posx, attacked_by_posy):
                attacked_by_king_positions.append( (attacked_by_posx,attacked_by_posy) )
                
        return attacked_by_king_positions
        
    
    

        
      
def main():
    game = ChessMaster()
#     r1 = sys.stdin.readline().rstrip('=').split("|")
#     r2 = sys.stdin.readline().rstrip('=').split("|")
#     r3 = sys.stdin.readline().rstrip('=').split("|")
#     r4 = sys.stdin.readline().rstrip('=').split("|")
#     r5 = sys.stdin.readline().rstrip('=').split("|")
#     r6 = sys.stdin.readline().rstrip('=').split("|")
#     r7 = sys.stdin.readline().rstrip('=').split("|")
#     r8 = sys.stdin.readline().rstrip('=').split("|")
#     boardString= [r1,r2,r3,r4,r5,r6,r7,r8]
    
    print " ********* Play ChessMaster Game*********** "
    print " *** Menu *** "
    print " Enter new boardString.                                            -> Press 1 "
    print " Print boardString.                                                -> Press 2 "
    print " To check if white king is checked or not.                         -> Press 3 "
    print " To check if white king is checkmated or not.                      -> Press 4 "
    print " To check if black can checkmate white king in next one move.      -> Press 5 "
    print " To make black piece next move such that white king is checkmated. -> Press 6 "
    print " to QUIT                                                           -> Press 7 "
    user_response = sys.stdin.readline().rstrip()
    while(user_response != "7"):
        if user_response == "1":
            print "Please Enter new board string as 8 lines in this format or you can copy this board only"
            print "|kl|  |  |nl|  |  |  |nl|=\n|  |  |  |nd|  |  |  |  |=\n|  |nd|  |  |  |  |  |  |=\n|kd|  |nd|  |  |nl|  |nl|=\n|  |  |nd|nl|  |nl|  |nl|=\n|  |  |  |nl|  |nl|  |nl|=\n|  |  |  |nl|  |nl|  |nl|=\n|  |  |  |nl|  |nl|  |  |=\n"
            print 
            r1 = sys.stdin.readline().rstrip('=').split("|")
            r2 = sys.stdin.readline().rstrip('=').split("|")
            r3 = sys.stdin.readline().rstrip('=').split("|")
            r4 = sys.stdin.readline().rstrip('=').split("|")
            r5 = sys.stdin.readline().rstrip('=').split("|")
            r6 = sys.stdin.readline().rstrip('=').split("|")
            r7 = sys.stdin.readline().rstrip('=').split("|")
            r8 = sys.stdin.readline().rstrip('=').split("|")
            boardString= [r1,r2,r3,r4,r5,r6,r7,r8]
            game.fromString(boardString)
            print "#################################\n"
        
            
            
        elif user_response == "2":
            print "Your boardString \n"
            game.toString()
            print "#################################\n"
            
        elif user_response == "3":
            print "Is White King In Check : ", game.IsWhiteInCheck()
            print "#################################\n" 
            
        elif user_response == "4":
            print "Is White King in Checkmate : " , game.IsWhiteInCheckmate()
            print "#################################\n"
            
        elif user_response == "5":
            print "Can Black CheckMate in one move : " , game.canBlackCheckMateInOneMove()
            print "#################################\n"
            
        elif user_response == "6":
            print "Making Black piece move that checkmates White King"
            temp = game.makeBlackCheckMateMove()
            if temp != None:
                print temp
            print "#################################\n"
        
        user_response = sys.stdin.readline().rstrip()
        
            
#     game.toString()
#     print game.IsWhiteInCheck()
#     print game.IsWhiteInCheckmate()
#     print game.canBlackCheckMateInOneMove()
#     game.makeBlackCheckMateMove()
#     game.toString()
    
    
    
    
if __name__ == "__main__":
    main()