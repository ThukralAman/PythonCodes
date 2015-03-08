Killer Knights Chess

You have to make Killer Knights chess game . 

Killer Knights is a chess game in which all the rules are normal except the players have only knights and 1 king as pieces. (Knight is Ghoda)

Each player can have any number of knights but only 1 king.

You will be given a string representation of the chess board at a particular point in time.

An example of such string representation is:

String boardString = 
            "|kl|  |  |nl|  |nl|  |nl|=\n" +
            "|  |  |  |  |  |  |  |  |=\n" +
            "|  |nd|nd|  |  |  |  |  |=\n" +
            "|  |  |  |nd|  |  |  |  |=\n" +
            "|  |  |  |  |  |  |  |  |=\n" +
            "|  |  |  |  |  |  |  |  |=\n" +
            "|  |  |  |  |  |  |  |  |=\n" +
            "|  |  |  |  |kd|  |  |  |=\n";


k = king, n = knight(ghoda), l = light(white), d = dark(black)

White pieces are represented as: kl, nl
black pieces are represented as: kd, nd
Empty square is represented by 2 blank spaces "  "

An example image showing possible moves of a Knight:




You have to implement a class called ChessMaster. 

ChessMaster will have the following methods:

public void fromString (String boardString);

set the config of the chessboard based on the boardString.  This replaces the previous configuration, if any.


public boolean isWhiteInCheck();

returns true if white player is in check and false otherwise.

Definition of check:

When the king of a player can be taken by a piece of the opponent, one says that the king is in check. For instance, the black player moves his knight to a position such that it attacks the white king, we say that the black knight gives check.


public boolean isWhiteInCheckMate();
		
returns true is white player is in checkmate and false otherwise.

Definition of checkmate:

When a player is in check, and he cannot make a move such that after the move, the king is not in check, then he is mated. The player that is mated lost the game, and the player that mated him won the game.

If isWhiteInCheck returns false this function will always return false.


public boolean canBlackCheckMateInOneMove();

returns true if black player can make a move that will put white player in checkmate.


public void makeBlackCheckMateMove();

makes the move of black player which will checkmate white player. This function will alter the configuration of the chess board. 

For example if the there is a move available for the black player; the black piece which has to be moved will take the new position by replacing the empty spot by “nd” and original position will be replaced by empty spot string “  “.
If canBlackCheckMateInOneMove returns false this function will make no move.


public String toString();

returns the string representation of the chess board.

This function will return the boradString representation of the chess board in the same format given in the example above.


The program should be runnable from command line and take the board string as input. 

The output of the program should be 

isWhiteInCheck: <answer>
isWhiteInCheckMate: <answer>
canBlackCheckMateInOneMove: <answer>
board string: <answer>

the board string will be the new configuration after calling makeBlackCheckMateMove OR string “no move” if canBlackCheckMateInOneMove is false.

You can create any number of other classes you want. 
