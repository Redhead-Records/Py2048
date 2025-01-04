# Modified on 1/2/2024 to be contained in a single .py file

# Garett Dahlen and Emanuel Bogdanovic
# 2048 - base algorithms


# algorithm .py file


#____________________________________________________________________________________________________________________
# BE SURE TO IMPORT RANDOM AND COPY!!
import random
import copy


# Class setup
                # converted everything into a class in order to execute code in a simpler way


# Name the class
class Game_Algorithm:
    """class for running the base 2048 alorithm and keeping track of total score."""

    # Define methods in the class just as you would in a function, except add self
    # as a parameter
    
    # __init__ is a class method called by the constructor to initilize the 
    # new object of the class
    def __init__(self, grid, total_score, game_state,last_grid):
        """Initialize an Account object."""

        # if initial score is not equal to 0, raise an exception
        if total_score != 0.00:
            raise ValueError('Initial score must be >= to 0.00.')
            
        if game_state != "":
            raise TypeError('Initial state must be ""')
        
        
        #self. assigns the parameters from the constructor to this instance
        self.grid = grid
        self.total_score = total_score
        self.game_state = game_state
        self.last_grid = last_grid
        
#___________________________________________________________________________________________________________________________
    # Import Section
        # most imported code is used in checking movement and in adding spots
    import random
    import copy

    # GAME GRID
    # test obtaining individual spots
    #   print(game_grid[0])
    #   print(game_grid[1])
    #   print(game_grid[2])  <- gets horizontal row <->
    #   print((game_grid[2])[3])  <- gets individual spot 
    #   print(game_grid[:: -1]) <-  makes list backwards 

#________________________________________________________________________________________________________________________________________________
#  ALGORITHM 4.0

#____________________________________________________________
#  Change Log

        # changes in 2.0
            # - new method of being called
            # - added the (input) and (grid_inp) modifiers
            # created user input section
        
        # Changes in 3.0
            # - Added "YOU WIN" conditions
            # - Added "Reset" input (to restart game)
            
        # Changes in 4.0
            # - Converted into a class
            # - Added a system to track score

        # Changes in 5.0
            # - Added testing area at bottom
            # - Added "GAME_STATE" into class
        
        # Changes in 6.0
            # - Added "previous grid" in order to make the "random_add" function like the real game
#____________________________________________________________


    def algorithm(self,inp):
    
        # get user input
       # user = input("move what way? \n>")
        """completes the calculations for 2048 tile movements"""

   
    
#________________________________________________________________________________________________________________________________________________________
# RESET* <- added in 3.0
    
        # if input is RESET ... Set all spots to 0 and run "random_add(self.grid)" once (in order to make it easier later)
        if inp.lower() == "reset":
            # set grid to all zeros
            self.grid[:] = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
            #random_add(self.grid) # <- removed this "random_add" because the "godsend" function (the FINAL movement function) adds a random spot every time
                                # Becasue of "godsend" adding a random spot every time it's executed, this makes it easier than adding a separate condition within "godsend"
            # add a 2 or a 4 randomly to the grid
            self.random_add()
            # change game state to plauing
            self.game_state = "playing"
            # return the grid
            self.total_score = 0
            #self.last_grid = []
            return self.grid
        
            
    
    
#________________________________________________________________________________________________________________________________________________________
# RIGHT
    
        # if input is RIGHT, start from right end and calculate
        if inp.lower() == "right":

        
            # create a loop that goes through all of the rows and moves tiles one by one        
            for row in self.grid:
            
            
                    # repeat 3 times per row (in order to calculate fully... this is needed in order to move tiles 2 or 3 spots in one move)
                    for number in range(3):
                    
                        # create a counter set at 3 ... this is to be able to combine later
                        counter = 3
                    
                        #  range is on a reversed list... this is becasue it needs to calculate from the right to prevent issues with combining tiles
                        for tile in reversed(row[:3]):
                    
                        
                            # first test for a blank space... if the tile to the right is a zero, move the current tile to the right one spot
                            # this is done by changing counter tile to the current tile's number... and then changing current to zero
                            if row[counter] == 0:
                                row[counter] = tile
                                # counter-1 becasue using "tile" didn't work
                                row[counter-1] = 0
                                counter -= 1
                            
                            
                            # does not combine numbers if tile is a string
                            elif tile == row[counter] and type(tile) == str:
                                counter -= 1
#                                ^- BUG FIX becasue sometimes it would combine wrong due to the 3 repetitions
#                                   this condition will prevent tiles that were previously merged from merging again
#                                     EXAMPLES:   
#                                              [2,2,2,2]  -> [0,0,0,8] <- before fix     AFTER -> [0,0,4,4]
#                                              [4,4,8,16] -> [0,0,0,32] <- before fix     AFTER -> [0,8,8,16]
        

                        
                            # if the tile in the horizontal list matches the tile to the right of it and both = 1024, the numbers combine and game is won
                            # this is done by taking the counter tile += current tile... and then changing current tile to zero
                            elif tile == row[counter] and type(tile) == int and tile == 1024:
                                row[counter] += tile
                                row[counter] = str(row[counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                                # counter-1 becasue using "tile" didn't work
                                row[counter-1] = 0
                                # ADD 2048 TO TOTAL SCORE - 4.0 CHANGE
                                self.total_score += 2048
                                return "YOU WIN"
                                counter -= 1

                        
                            # if the tile in the horizontal list matches the tile to the right of it, the numbers combine
                            # this is done by taking the counter tile += current tile... and then changing current tile to zero
                            elif tile == row[counter] and type(tile) == int:
                                row[counter] += tile
                                row[counter] = str(row[counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                                # counter-1 becasue using "tile" didn't work
                                row[counter-1] = 0
                                # ADD NEW TILE AMOUNT TO TOTAL SCORE - 4.0 CHANGE
                                self.total_score += int(row[counter])
                                counter -= 1   
                            else:      
                                counter -= 1
                            
                        # create counter for int change
                    int_count = 0
                        # create loop that sets every item back to being a number
                    for tile in row:
                        row[int_count] = int(tile)
                        int_count += 1
                        
                        
#________________________________________________________________________________________________________________________________________________________
# LEFT
    
        # if input is LEFT, start from left end and calculate
        if inp.lower() == "left":
        
        
            # create a loop that goes through all of the rows and moves tiles one by one        
            for row in self.grid:
            
            
                    # repeat 3 times per row (in order to calculate fully... this is needed in order to move tiles 2 or 3 spots in one move)
                    for number in range(3):
                    
                        # create a counter set at 1 ... this is to be able to combine later
                        counter = 0
                    
                        #  for loop that uses all but the left-most tile... this prevents errors and none of the left end tiles have any reson to go left
                        for tile in row[1:]:
                    
                        
                            # first test for a blank space... if the tile to the left is a zero, move the current tile to the left one spot
                            # this is done by changing counter tile to the current tile's number... and then changing current to zero
                            if row[counter] == 0:
                                row[counter] = tile
                                # counter-1 becasue using "tile" didn't work
                                row[counter+1] = 0
                                counter += 1
                            
                            
                            # does not combine numbers if tile is a string
                            elif tile == row[counter] and type(tile) == str:
                                counter += 1
#                                     ^- BUG FIX becasue sometimes it would combine wrong due to the 3 repetitions
#                                         this condition will prevent tiles that were previously merged from merging again
#                                           EXAMPLES:   
#                                                    [2,2,2,2]  -> [0,0,0,8] <- before fix     AFTER -> [0,0,4,4]
#                                                    [4,4,8,16] -> [0,0,0,32] <- before fix     AFTER -> [0,8,8,16]
        
                            
                        
                            # if the tile in the horizontal list matches the tile to the left of it, the numbers combine
                            # this is done by taking the counter tile += current tile... and then changing current tile to zero
                            elif tile == row[counter] and tile == 1024:
                                row[counter] += tile
                                row[counter] = str(item[counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                                # counter-1 becasue using "tile" didn't work
                                row[counter+1] = 0
                                # ADD 2048 TO TOTAL SCORE - 4.0 CHANGE
                                self.total_score += 2048
                                return "YOU WIN"
                                counter += 1   
                                                
                            # if the tile in the horizontal list matches the tile to the left of it and both = 1024, the numbers combine and return "YOU WIN"
                            # this is done by taking the counter tile += current tile... and then changing current tile to zero
                            elif tile == row[counter]:
                                row[counter] += tile
                                row[counter] = str(row[counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                                # counter-1 becasue using "tile" didn't work
                                row[counter+1] = 0
                                # ADD NEW AMOUNT TO TOTAL SCORE - 4.0 CHANGE
                                self.total_score += int(row[counter])
                                counter += 1
       
                            
                            # if nothing is done... add one to the counter
                            else:      
                                counter += 1
                            
                        # Create counter for int change
                    int_count = 0
                        # Create loop that sets every item back to being a number
                        # For every tile in a row
                    for tile in row:
                        # Change each tile from a string to a number
                        row[int_count] = int(tile)
                        # Add 1 to the counter
                        int_count += 1
                        
                        
#________________________________________________________________________________________________________________________________________________________

# UP
    
        # if input is UP, start from top end and calculate
        if inp.lower() == "up":

        
        
            # create a loop takes a single number from each list to make a vertical line 
            # do this with counters - for each item in a list (not using the "item" part other than having it repeat for the amt of items)
            for row in self.grid:
                # make counter for the current x pos (this will stay the same until end of iteration)
                x_pos_counter = 0
            
            
                    # repeat 4 times to cover all vert lines
                for number in range(4):
                
                     # make a y pos counter starting at 1 - this is so the very top line is ignored... if top was included, it would cause errors
                    y_pos_counter = 1                                                
                    
                    #  range is the length of the list (grid size)
                    # make a loop that will calculate movement for each vertical line
                    for num in range(len(self.grid)-1):
                    
                        
                        # first test for a blank space... if the tile above is a zero, move the current tile to the one above
                        # this is done by changing higher tile to the current tile's number... and then changing current to zero
                        # VERTICAL DETAILS - instead of using lists in the same way as left and right, up and down have to be usnig the same spot in different lists.
                        if (self.grid[y_pos_counter-1])[x_pos_counter] == 0:
                            (self.grid[y_pos_counter-1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter]
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            y_pos_counter += 1
                            
                            
                        # does not combine numbers if tile is a string
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter-1])[x_pos_counter] and type((self.grid[y_pos_counter])[x_pos_counter]) == str:
                            y_pos_counter += 1
#                           ^- BUG FIX becasue sometimes it would combine wrong due to the 3 repetitions
#                              this condition will prevent tiles that were previously merged from merging again
#                                EXAMPLES:   
#                                         [2,2,2,2]  -> [0,0,0,8] <- before fix     AFTER -> [0,0,4,4]
#                                         [4,4,8,16] -> [0,0,0,32] <- before fix     AFTER -> [0,8,8,16]
        
                            
                            # if the current tile matches the tile above it and both = 1024, the numbers combine and return "YOU WIN"
                            # this is done by taking the tile above  += current tile... and then changing current tile to zero
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter-1])[x_pos_counter] and (self.grid[y_pos_counter])[x_pos_counter] == 1024:
                            (self.grid[y_pos_counter-1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter] + (self.grid[y_pos_counter-1])[x_pos_counter]
                            (self.grid[y_pos_counter-1])[x_pos_counter] = str((self.grid[y_pos_counter-1])[x_pos_counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                            # counter-1 becasue using "tile" didn't work
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            self.total_score += 2048

                            return "YOU WIN"
                            self.total_score += 2048
                            y_pos_counter += 1   
                        
                        
                            # if the current tile matches the tile above it, the numbers combine
                            # this is done by taking the tile above  += current tile... and then changing current tile to zero
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter-1])[x_pos_counter]:
                            (self.grid[y_pos_counter-1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter] + (self.grid[y_pos_counter-1])[x_pos_counter]
                            (self.grid[y_pos_counter-1])[x_pos_counter] = str((self.grid[y_pos_counter-1])[x_pos_counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                            # counter-1 becasue using "tile" didn't work
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            self.total_score += int((self.grid[y_pos_counter-1])[x_pos_counter])
                            y_pos_counter += 1   
                        
                        
                        
                        else:      
                            y_pos_counter += 1
                        
                        # add 1 to the x_pos counter
                    x_pos_counter += 1
          
        
                    # create loop that sets every item back to being a number
            for row in self.grid:
                # create counter for int change
                int_count = 0
                for tile in row:
                    row[int_count] = int(tile)
                    int_count += 1

                
                
#________________________________________________________________________________________________________________________________________________________

# DOWN
    
        # if input is UP, start from top end and calculate
        if inp.lower() == "down":

        
        
            # create a loop takes a single number from each list to make a vertical line 
            # do this with counters - for each item in a list (not using the "item" part other than having it repeat for the amt of items)
            for row in self.grid:
                # make counter for the current x pos (this will stay the same until end of iteration)
                x_pos_counter = 0
            
            
                    # repeat 4 times to cover all vert lines
                for number in range(4):
                
                     # make a y pos counter starting at 2 - this is so the very bottom line is ignored... if bottom was included, it would cause errors
                    y_pos_counter = 2                                                
                    
                    #  range is the length of the list (grid size)
                    # make a loop that will calculate movement for each vertical line
                    for num in range(len(self.grid)-1):
                    
                        
                        # first test for a blank space... if the tile below is a zero, move the current tile to the one below
                        # this is done by changing lower tile to the current tile's number... and then changing current to zero
                        # VERTICAL DETAILS - instead of using lists in the same way as left and right, up and down have to be usnig the same spot in different lists.
                        if (self.grid[y_pos_counter+1])[x_pos_counter] == 0:
                            (self.grid[y_pos_counter+1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter]
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            y_pos_counter -= 1
                            
                            
                        # does not combine numbers if tile is a string
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter+1])[x_pos_counter] and type((self.grid[y_pos_counter])[x_pos_counter]) == str:
                            y_pos_counter -= 1
#                           ^- BUG FIX becasue sometimes it would combine wrong due to the 3 repetitions
#                              this condition will prevent tiles that were previously merged from merging again
#                                EXAMPLES:   
#                                         [2,2,2,2]  -> [0,0,0,8] <- before fix     AFTER -> [0,0,4,4]
#                                         [4,4,8,16] -> [0,0,0,32] <- before fix     AFTER -> [0,8,8,16]
        
                            
                            # if the current tile matches the tile below it and both = 1024, the numbers combine and return "YOU WIN"
                            # this is done by taking the tile below  += current tile... and then changing current tile to zero
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter+1])[x_pos_counter] and (self.grid[y_pos_counter])[x_pos_counter] == 1024:
                            (self.grid[y_pos_counter+1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter] + (self.grid[y_pos_counter+1])[x_pos_counter]
                            (self.grid[y_pos_counter+1])[x_pos_counter] = str((self.grid[y_pos_counter+1])[x_pos_counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                            # counter-1 becasue using "tile" didn't work
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            self.total_score += 2048

                            return "YOU WIN"
                            y_pos_counter -= 1   
                        
                        
                            # if the current tile matches the tile below it, the numbers combine
                            # this is done by taking the tile below  += current tile... and then changing current tile to zero
                        elif (self.grid[y_pos_counter])[x_pos_counter] == (self.grid[y_pos_counter+1])[x_pos_counter]:
                            (self.grid[y_pos_counter+1])[x_pos_counter] = (self.grid[y_pos_counter])[x_pos_counter] + (self.grid[y_pos_counter+1])[x_pos_counter]
                            (self.grid[y_pos_counter+1])[x_pos_counter] = str((self.grid[y_pos_counter+1])[x_pos_counter]) # <- BUGFIX - changes to string to prevent numbers from merging twice in the same move
                            # counter-1 becasue using "tile" didn't work
                            (self.grid[y_pos_counter])[x_pos_counter] = 0
                            self.total_score += int((self.grid[y_pos_counter+1])[x_pos_counter])
                            y_pos_counter -= 1   
                        
                        
                        
                        else:      
                            y_pos_counter -= 1
                        
                        # add 1 to the x_pos counter
                    x_pos_counter += 1
          
        
                    # create loop that sets every item back to being a number
            for row in self.grid:
                # create counter for int change
                int_count = 0
                for tile in row:
                    row[int_count] = int(tile)
                    int_count += 1
        
        return self.grid

                
                

#_______________________________________________________________________________________________________________________________________________________________________________
#                                                                          ADDING SECTION   
#_______________________________________________________________________________________________________________________________________________________________________________

#  Sections: rand_value_finder, rand_row_find, rand_spot_find, and random_add

#  These functions form the system for adding a 2 or 4 to any spot where there is no number in the game. The number adding functions execute after every move in the game

#__________________________________
#  TESTING LIST
# create a list for testing value adding
    test_lst = [[8, 8, 8, 8], [4, 2, 0, 8], [8, 5, 9, 8], [32, 8, 8, 8]]

#________________________________________________________________________________________________________________________________________________________________________________

# RAND_VALUE_FINDER



    # create a function that picks either a 2 or a 4 (2 happens 9/10 times...4 happens 1/10 times)
    def rand_value_finder(self):
        """either returns a 2 or a 4 at a 1:9 ratio"""
        # randomly generate a number between 0 and 9 (10 possible digits)
        # if the number generated is a 9, return a 4... if not a 9, return a 2
        if random.randint(0,9) == 9:
            return 4
        else:
             return 2
        
        
        
#_________________________________________________________________________________________________________________________________________________________________________________

#  RAND_ROW_FIND 2.0

    # create a function that picks a random row that can have a value added to it
    #   ^- 2.0 CHANGE - Also CAUSES THE GAME TO END IF NO SPOT CAN BE ADDED - this is becuase without an end command, the loop would never end
    def rand_row_find(self):
        """Finds and randomly selects a horizontal row to add a value to"""
        # 2.0 CHANGE - Create a blank list that will tell what rows have been used
        used_number_lst = []
        # create a variable "random_row" that uses a random number between 0-3 to represent rows
        random_row = random.randint(0,3)
        # while loop - while (given row) does not have a zero in it, keep trying to find rows with a zero
        while 0 not in self.grid[random_row]:
            # 2.0 CHANGE - If the generated number is not in the "used number" list, add it and [testing reasons] print "failed"... after that, randomly generate another number
            if random_row not in used_number_lst:
                # 2.0 CHANGE - Add number to "used number" list
                used_number_lst += [random_row]
                # TESTING - Print "failed"
                #print("failed")
                # Change the "random_row" value in order to loop
                random_row = random.randint(0,3)
             # If the generated number is in the list and the list is less than 4 long... generate a new number  
            elif len(used_number_lst) < 4:
                # change the "random_row" value in order to loop
                random_row = random.randint(0,3)
            # if the list is 4 or more long... break the loop
            else:
                # break the loop
                break
        # if the list has a length of 4, return "Game Over"
        if len(used_number_lst) == 4:
            # return "Game Over"
            return "Game Over"
        # else, return the row value
        else:
            # return "random_row"
            return random_row

    # rand_row_find(test_lst) # <- TESTING

#_________________________________________________________________________________________________________________________________________________________________________________

# RAND_SPOT_FIND 2.0

    # create a function that picks a random spot that can have a value added to it
    #   ^- 2.0 CHANGE - Also CAUSES THE GAME TO END IF NO SPOT CAN BE ADDED - this is becuase without an end command, the loop would never end
    def rand_spot_find(self,row):
        """Finds and randomly selects a spot to add a value to"""
        # if "rand_row_find" returns "Game Over" ... return "Game Over" and end function
        if self.rand_row_find() == "Game Over":
            return "Game Over"
        # Otherwise, operate like normal and find a random spot to add a value to
        else:
        
            # 2.0 CHANGE - Create a blank list that will tell what spots have been used
            used_spot_lst = []
            # create a variable "random_spot" that uses a random number between 0-3 to represent spots
            random_spot = random.randint(0,3)
            # while loop - while (given spot) does not have a zero in it, keep trying to find spots with a zero
            while (self.grid[row])[random_spot] != 0:
                # 2.0 CHANGE - If the generated number is not in the "used spot" list, add it and [testing reasons] print "failed"... after that, randomly generate another number
                if random_spot not in used_spot_lst:
                    # 2.0 CHANGE - Add number to "used spot" list
                    used_spot_lst += [random_spot]
                    # TESTING - Print "failed"
                    #print("failed")
                    # Change the "random_spot" value in order to loop
                    random_spot = random.randint(0,3)
                 #if the generated number is in the list and the list is less than 4 long... generate a new number  
                elif len(used_spot_lst) < 4:
                    # change the "random_spot" value in order to loop
                    random_spot = random.randint(0,3)
                # if the list is 4 or more long... break the loop
                else:
                    # break the loop
                    break
            # if the list has a length of 4, return "Game Over"
            if len(used_spot_lst) >= 4:
                # return "Game Over"
                return "Game Over"
            # else, return the row value
            else:
                # return "random_spot"
                return random_spot
        
#_________________________________________________________________________________________________________________________________________________________________________________

#  RANDOM_ADD 2.0

    # create a function that adds a 2 or a 4 to the game grid
    #  ^- 2.0 CHANGE - Also tells if game is over (not the function to end game) 
    #    ("Game End" requires there to be no way to move at all along with no space to add)
    def random_add(self):
        """Adds a 2 or a 4 to a random spot within the game grid"""
        # if either the row finder returns "Game Over", return "Game Over"
        if self.rand_row_find()  == "Game Over" or self.rand_spot_find == "Game Over":
            # Return "Game Over"
            return "Game Over"
        # if the last grid is the same as the current ... do not add a spot
        elif self.grid == self.last_grid:
            return self.grid
        
        # Otherwise, operate like normal and add a value to a blank spot
        else:
            # create a variable "rand_row" that tells the row that the value will be added to
            rand_row = self.rand_row_find()
            # create a variable "rand_spot" that tells the spot within the given row where the value will be added
            rand_spot = self.rand_spot_find(rand_row)
            # create a variable "rand_value" that tells weather to add a 2 or a 4 to the given spot
            rand_value = self.rand_value_finder()
            # set the given spot to the given value
            (self.grid[rand_row])[rand_spot] = rand_value
            # return the new grid
            return self.grid
    
    # random_add(test_lst) #  <- TESTING


#_________________________________________________________________________________________________________________________________________________________________________________
#                                                   MOVEMENT CHECK
#_________________________________________________________________________________________________________________________________________________________________________________


#  This section is for checking if the tiles can move in any given direction... if the tiles can not move at all, this section will be responsible for ending the game.


#__________________________________________________________________________________
    #  testing
    Motion_test_lst = [[1, 2, 2, 4], [5, 2, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#_________________________________________________________________________________________________________________________________________________________________________________
#            calling info (ver3.0):
#                          to run, use "test_moves(grid)"    < grid is the list that represents the layout of the game
#_________________________________________________________________________________________________________________________________________________________________________________
# TEST_MOVES

    # TESTING FUNCTION
    # create function called test_moves
    def test_moves(self):
        # create a blank list for output
        test_results = []
        # create a clone of the grid - so that testing does not affect the real one - 5.0 change - create new class to perform this task
        self.secondary_grid = copy.deepcopy(self.grid)
        self.total_score_clone = copy.deepcopy(self.total_score) #<- copies score because it was using the score after testing moves
        # going to need 4 if statements

    # TEST LEFT
        # if the list is the same before and after being tested, add a "false" to the list
        if self.algorithm("left") == self.secondary_grid:
            test_results += ["false"]
            # if not... add a "true" to the list
        else:
            test_results += ["true"]
        
        # create a clone of the grid - so that testing does not affect the real one and so all movements are tested individually
        self.grid = copy.deepcopy(self.secondary_grid)
        self.total_score = copy.deepcopy(self.total_score_clone)

        
    # TEST RIGHT
        # if the list is the same before and after being tested, add a "false" to the list
        if self.algorithm("right") == self.secondary_grid:
            test_results += ["false"]
            # if not... add a "true" to the list
        else:
            test_results += ["true"]
        
        # create a clone of the grid - so that testing does not affect the real one and so all movements are tested individually
        self.grid = copy.deepcopy(self.secondary_grid)
        self.total_score = copy.deepcopy(self.total_score_clone)

        
    # TEST UP
        # if the list is the same before and after being tested, add a "false" to the list
        if self.algorithm("up") == self.secondary_grid:
            test_results += ["false"]
            # if not... add a "true" to the list
        else:
            test_results += ["true"]

        # create a clone of the grid - so that testing does not affect the real one and so all movements are tested individually
        self.grid = copy.deepcopy(self.secondary_grid)
        self.total_score = copy.deepcopy(self.total_score_clone)

    
    # TEST DOWN
        # if the list is the same before and after being tested, add a "false" to the list
        if self.algorithm("down") == self.secondary_grid:
            test_results += ["false"]
            # if not... add a "true" to the list
            self.grid = copy.deepcopy(self.secondary_grid)
            self.total_score = copy.deepcopy(self.total_score_clone)

        else:
            test_results += ["true"]
        self.grid = copy.deepcopy(self.secondary_grid)
        self.total_score = copy.deepcopy(self.total_score_clone)



        return test_results
    
#______________________________________________________________________________________________________________________________________________________________________________        
#                                         GODSEND!!!!!!!!!!!!!!!! (the main algorithm)
#______________________________________________________________________________________________________________________________________________________________________________
# The "godsend" algorithm contains everything listed above and is responsible for calculating things like game ends


#______________________________________________________________________________________________________________________________________________________________________________
# main function - GODSEND

    # create a function that performes a single move
    def godsend(self,inp):
        """performes a single move"""
        # if algorithm returns "YOU WIN" ... return "YOU WIN"
        if self.algorithm(inp) == "YOU WIN":
            # return "GAME WIN" STATE
            self.game_state = "GAME WIN"
            return self.grid
        # Else... execute "test_moves(grid)"
        else:
            # If "test_moves(grid)" == all false... return "GAME OVER"
            if self.test_moves() == ["false", "false", "false", "false"]:
                # Return "GAME OVER" STATE
                self.game_state = "GAME OVER"
                return self.grid
            #  Else... Execute "random_add(grid)" to add either a 2 or a 4 to the grid
            else:
                # Create a copy of the grid so that if "GAME OVER" is given it will not be returned
                grid_temp_clone = self.grid[:]
                # If the adding function is unable to add a number... return the original grid
                if self.random_add() == "GAME OVER":
                    # return the original grid
                    #print(self.grid[0])
                    #print(self.grid[1])
                    #print(self.grid[2])
                    #print(self.grid[3])   
                    # create a clone of the grid in order to make the "random_add" function work properly ... this makes it so if the grid does not change, a random spot is not added
                    self.last_grid = copy.deepcopy(self.grid)
                    return self.grid
                # If the adding function succeeds in adding a number... return the new grid
                else:
                    # Return the new grid
                    self.grid = copy.deepcopy(grid_temp_clone)
                    
                    # create a clone of the grid in order to make the "random_add" function work properly ... this makes it so if the grid does not change, a random spot is not added
                    self.last_grid = copy.deepcopy(self.grid)
                    #print(self.grid[0] , " added")
                    #print(self.grid[1] , " added")
                    #print(self.grid[2] , " added")
                    #print(self.grid[3] , " added")
                    return self.grid                
                
                
                
                
                
#_____________________________________________________________________________________________________________________________________________________________________________
# GAME START- 4.0 Change
#_____________________________________________________________________________________________________________________________________________________________________________
# Create a function that starts the game and will create a blamk list... This function will make it simpler later in the process to code a game start
#                                                                        becasue all you'd need is something like "game_1 = Game_Algorithm([],0)
#                                                                                                                     and then "game_1.newgame"




#_______________________________________________________________________________________________________________________________________________________________________________


    def newgame(self):
        """Starts a new game and sets a blank list"""
        # this function just acts as a shortcut for the godsend "reset" function
        return self.godsend("reset")

#________________________________________________________________________________________________________________________________________
# test function
            # this function will run a basic text only version of the game
    
    def game_test_ver1(self):
        """runs a test version of 2048"""
        # start new game
        self.newgame()

        # while game is not won or lost... run moves and get typed inputs
        while self.game_state != "GAME OVER" and self.game_state != "GAME WIN":
            # get user input
            user_inp = input("what now? \n>")
            
            # if user types up or w ... move up
            if user_inp.lower() == "up" or user_inp.lower() == "w":
                self.godsend("up")
                # print grid line by line
                print(self.grid[0])
                print(self.grid[1])
                print(self.grid[2])
                print(self.grid[3])

                
             # if user types down or s ... move down
            elif user_inp.lower() == "down" or user_inp.lower() == "s":
                self.godsend("down")
                # print grid line by line
                print(self.grid[0])
                print(self.grid[1])
                print(self.grid[2])
                print(self.grid[3])
                
         # if user types left or a ... move left
            elif user_inp.lower() == "left" or user_inp.lower() == "a":
                self.godsend("left")
                # print grid line by line
                print(self.grid[0])
                print(self.grid[1])
                print(self.grid[2])
                print(self.grid[3])
                
         # if user types right or d ... move right
            elif user_inp.lower() == "right" or user_inp.lower() == "d":
                self.godsend("right")
                # print grid line by line
                print(self.grid[0])
                print(self.grid[1])
                print(self.grid[2])
                print(self.grid[3])
        
        # if user types reset ... the game resets
            elif user_inp.lower() == "reset" or user_inp.lower() == "r":
                self.godsend("reset")
                 # print grid line by line
                print(self.grid[0])
                print(self.grid[1])
                print(self.grid[2])
                print(self.grid[3])

        # if user types help ... print out a control screen
            elif user_inp.lower() == "help" or user_inp.lower() == "h":
                print("WELCOME TO 2048")
                print("\n")
                print("Type in 'up' or 'w' to move up")
                print("\n")
                print("Type in 'down' or 's' to move down")
                print("\n")
                print("Type in 'left' or 'a' to move left")
                print("\n")
                print("Type in 'right' or 'd' to move right")
            
            # if user types end ... break the loop
            elif user_inp.lower() == "end":
                break
        # if user types anything not listed ... this tells user to type help for controlls
            else:
                print("Type 'help' for controls")
                
            

        if self.game_state == "GAME WIN":
            print("YOU WIN!!!!!!")
            print("TOTAL SCORE: " + str(self.total_score))
        elif self.game_state == "GAME OVER":
            print("GAME OVER!")
            print("Total score: " + str(self.total_score))



# set up a new game

# classes are setup like this -> game_1 = game_algorithm.Game_Algorithm({list/grid},{total_score}, {game_state})
            # when setting up... leave the values as follows: [] = grid, 0 = score,"" = state, and [0] = last_grid
game_1 = Game_Algorithm([],0,"",[0])


            
# import everything

# import tkinter
from tkinter import *


# set up a new game

# classes are setup like this -> game_1 = Game_Algorithm({list/grid},{total_score}, {game_state})
            # when setting up... leave the values as follows: [] = grid, 0 = score, and "" = state
game_1 = Game_Algorithm([],0,"",[0])

# start new game
game_1.newgame()


# import tkinter
from tkinter import *

# create dictionaries for colors

# create game color dict - this dictionary contains the colors for the background of the game
game_colors = {"window_bg" : "#fbf8f1", "grid_bg" : "#bbada0", "dark_text_color" : "#776e65" , "light_text_color" : "#ffffff"}

# create tile color dict - This dictionary contains the colors for the tiles in the game
tile_colors = {0 : "#ccc0b3", 2 : "#eee4da", 4 : "#ece0ca", 8 : "#f2b179", 16 : "#ec8d53", 32 : "#f57c5f", 64 : "#e95839", 128 : "#f4d86d", 256 : "#f1d04b", 512 : "#e4c02a", 1024 : "#e5b910", 2048 : "#ecc400" }

# create a text color dict - this grid contains the colors for the grid text 
number_colors_and_text = {0 : ["", "#ffffff"], 2 : [2, "#776e65"], 4 : [4, "#776e65"], 8 : [8, "#ffffff"], 16 : [16, "#ffffff"], 32 : [32, "#ffffff"], 64 : [64, "#ffffff"], 128 : [128, "#ffffff"], 256 : [256, "#ffffff"],
                          512 : [512, "#ffffff"], 1024 : [1024, "#ffffff"], 2048 : [2048, "#ffffff"]}




#______________________________________________________________________________________________________________________________________________________________________________
#  game grid drawer

def grid_update(g):
    """draws a grid based on the grid_list"""
    # for every row ... place rectangles and text for every spot
    

    
def up_press(event):
    """this executes when a button for 'up' is pressed"""
    game_1.godsend("w")
    grid_update(g)


def down_press(event):
    """this executes when a button for 'down' is pressed"""
    print(event.char)
    

def left_press(event):
    """this executes when a button for 'left' is pressed"""
    print(event.char)
    

def right_press(event):
    """this executes when a button for 'right' is pressed"""
    print(event.char)
                
def reset_press(event):
    """this executes when a button for 'reset' is pressed"""
    print(event.char)
                
                               
                               
                               
def game_play():
    # create window
    window = Tk()
    # name window
    window.title("Py2048")
    # change window bg color to match 2048 colors
    window.configure(bg=game_colors["window_bg"])

    # set dimensions - 9:16 ratio (normal phone ratio)
    canvas_width = 450
    canvas_height = 800
    w = Canvas(window, 
               width=canvas_width,
               height=canvas_height)
    
    # change game background color
    w.configure(bg=game_colors["window_bg"])
    

    # create g - the layout of the grid ... make it 410 x 410 to fit with resultion
    g = Canvas(window,
               width=410,
               height=410)
    #change bg color to match game
    g.configure(bg=game_colors["grid_bg"])
    
    # create initial rectangles for the grid
    
    # ROW 1
    rect_a_1 = g.create_rectangle(10, 10, 100, 100, fill=tile_colors[ (game_1.grid[0])[0] ], outline="")   
    rect_a_2 = g.create_rectangle(110, 10, 200, 100, fill=tile_colors[ (game_1.grid[0])[1] ], outline="")   
    rect_a_3 = g.create_rectangle(210, 10, 300, 100, fill=tile_colors[ (game_1.grid[0])[2] ], outline="")   
    rect_a_4 = g.create_rectangle(310, 10, 400, 100, fill=tile_colors[ (game_1.grid[0])[3] ], outline="")   
    
    
    # ROW 2
    rect_b_1 = g.create_rectangle(10, 110, 100, 200, fill=tile_colors[ (game_1.grid[1])[0] ], outline="")   
    rect_b_2 = g.create_rectangle(110, 110, 200, 200, fill=tile_colors[ (game_1.grid[1])[1] ], outline="")   
    rect_b_3 = g.create_rectangle(210, 110, 300, 200, fill=tile_colors[ (game_1.grid[1])[2] ], outline="")   
    rect_b_4 = g.create_rectangle(310, 110, 400, 200, fill=tile_colors[ (game_1.grid[1])[3] ], outline="") 
    
    
    # ROW 3
    rect_c_1 = g.create_rectangle(10, 210, 100, 300, fill=tile_colors[ (game_1.grid[2])[0] ], outline="")   
    rect_c_2 = g.create_rectangle(110, 210, 200, 300, fill=tile_colors[ (game_1.grid[2])[1] ], outline="")   
    rect_c_3 = g.create_rectangle(210, 210, 300, 300, fill=tile_colors[ (game_1.grid[2])[2] ], outline="")   
    rect_c_4 = g.create_rectangle(310, 210, 400, 300, fill=tile_colors[ (game_1.grid[2])[3] ], outline="")   
    
    
    # ROW 4
    rect_d_1 = g.create_rectangle(10, 310, 100, 400, fill=tile_colors[ (game_1.grid[3])[0] ], outline="")   
    rect_d_2 = g.create_rectangle(110, 310, 200, 400, fill=tile_colors[ (game_1.grid[3])[1] ], outline="")   
    rect_d_3 = g.create_rectangle(210, 310, 300, 400, fill=tile_colors[ (game_1.grid[3])[2] ], outline="")   
    rect_d_4 = g.create_rectangle(310, 310, 400, 400, fill=tile_colors[ (game_1.grid[3])[3] ], outline="")   
    
    #_________________________________________________________________________
    
    # CREATE INITIAL TEXT FOR GRID
    
    # TEXT ROW 1
    txt_a_1 = g.create_text(55, 55, text=(number_colors_and_text[(game_1.grid[0])[0]])[0], fill=(number_colors_and_text[(game_1.grid[0])[0]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_a_2 = g.create_text(155, 55, text=(number_colors_and_text[(game_1.grid[0])[1]])[0], fill=(number_colors_and_text[(game_1.grid[0])[1]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_a_3 = g.create_text(255, 55, text=(number_colors_and_text[(game_1.grid[0])[2]])[0], fill=(number_colors_and_text[(game_1.grid[0])[2]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_a_4 = g.create_text(355, 55, text=(number_colors_and_text[(game_1.grid[0])[3]])[0], fill=(number_colors_and_text[(game_1.grid[0])[3]])[1], font=('Helvetica 20 bold'), justify="center")
    
    
    # ROW 2
    txt_b_1 = g.create_text(55, 155, text=(number_colors_and_text[(game_1.grid[1])[0]])[0], fill=(number_colors_and_text[(game_1.grid[1])[0]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_b_2 = g.create_text(155, 155, text=(number_colors_and_text[(game_1.grid[1])[1]])[0], fill=(number_colors_and_text[(game_1.grid[1])[1]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_b_3 = g.create_text(255, 155, text=(number_colors_and_text[(game_1.grid[1])[2]])[0], fill=(number_colors_and_text[(game_1.grid[1])[2]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_b_4 = g.create_text(355, 155, text=(number_colors_and_text[(game_1.grid[1])[3]])[0], fill=(number_colors_and_text[(game_1.grid[1])[3]])[1], font=('Helvetica 20 bold'), justify="center")
   
    
    # ROW 3
    txt_c_1 = g.create_text(55, 255, text=(number_colors_and_text[(game_1.grid[2])[0]])[0], fill=(number_colors_and_text[(game_1.grid[2])[0]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_c_2 = g.create_text(155, 255, text=(number_colors_and_text[(game_1.grid[2])[1]])[0], fill=(number_colors_and_text[(game_1.grid[2])[1]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_c_3 = g.create_text(255, 255, text=(number_colors_and_text[(game_1.grid[2])[2]])[0], fill=(number_colors_and_text[(game_1.grid[2])[2]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_c_4 = g.create_text(355, 255, text=(number_colors_and_text[(game_1.grid[2])[3]])[0], fill=(number_colors_and_text[(game_1.grid[2])[3]])[1], font=('Helvetica 20 bold'), justify="center")
    
    
    # ROW 4
    txt_d_1 = g.create_text(55, 355, text=(number_colors_and_text[(game_1.grid[3])[0]])[0], fill=(number_colors_and_text[(game_1.grid[3])[0]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_d_2 = g.create_text(155, 355, text=(number_colors_and_text[(game_1.grid[3])[1]])[0], fill=(number_colors_and_text[(game_1.grid[3])[1]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_d_3 = g.create_text(255, 355, text=(number_colors_and_text[(game_1.grid[3])[2]])[0], fill=(number_colors_and_text[(game_1.grid[3])[2]])[1], font=('Helvetica 20 bold'), justify="center")
    txt_d_4 = g.create_text(355, 355, text=(number_colors_and_text[(game_1.grid[3])[3]])[0], fill=(number_colors_and_text[(game_1.grid[3])[3]])[1], font=('Helvetica 20 bold'), justify="center")
    
    
    
    
    
    # place in center
    g.place(relx=.5, rely=.5, anchor="center")
    
#____________________________________________________
    # title and score draw
    
    
    # create rectangle for title - this sits behind text that reads "Py2048"
    title_square = w.create_rectangle(25,25,175,175,fill=tile_colors[2048],outline="")
    
    # create text for title
    title_text = w.create_text(100,100, text="Py2048", fill="#ffffff", font=('Helvetica 30 bold'), justify="center")
    
    # create box for score section - use color for number 4 on "score" and the white for the number
    score_box = w.create_rectangle(225,25,430,150, fill=game_colors["grid_bg"], outline="")
    
    # create "score" text
    score_title_txt = w.create_text(327.5,50, text="SCORE", fill=tile_colors[4], font=('Helvetica 15 bold'), justify="center")
    
    # create score counter txt
    score_count_txt = w.create_text(327.5,100, text=game_1.total_score, fill="#ffffff", font=('Helvetica 20 bold'), justify="center")
    
    # write instructions at the bottom of the screen
    w.create_text(225,700, text="Use the arrow keys or 'wsad' keys to combine tiles!", fill=game_colors["dark_text_color"], font=('Helvetica 10 bold'), justify="center")
    w.create_text(225,750, text="The goal of the game is to reach the 2048 tile!", fill=game_colors["dark_text_color"], font=('Helvetica 10 bold'), justify="center")

    
    
#____________________________________________________________________
    #  game grid updater

    def grid_update(g):
        """draws a grid based on the grid_list"""
        # before updating, check game_state
        
        # check if game is over ... if over, make screen red and have text say "GAME OVER" and "press 'r' to restart"
        if game_1.game_state == "GAME OVER":
            g.create_rectangle(0,0,410,410,fill=tile_colors[64],outline="")
            g.create_text(205,205, text="GAME OVER", fill="#ffffff", font=('Helvetica 35 bold'), justify="center")
            g.create_text(205,300, text="Press 'r' to restart!", fill="#ffffff", font=('Helvetica 15 bold'), justify="center")
        
        # if game_state = "GAME WIN" ... make text that reads "YOU WIN!!!" and "score: [score]" and "Press 'r' to restart!"
        elif game_1.game_state == "GAME WIN":
            g.create_rectangle(0,0,410,410,fill=tile_colors[2048],outline="")
            g.create_text(205,205, text="YOU WIN", fill="#ffffff", font=('Helvetica 35 bold'), justify="center")
            g.create_text(205,250, text="SCORE: " + str(game_1.total_score), fill="#ffffff", font=('Helvetica 20 bold'), justify="center")
            g.create_text(205,300, text="Press 'r' to restart!", fill="#ffffff", font=('Helvetica 15 bold'), justify="center")


            
       # otherwise ... draw like normal
        else:
    
    
        # UPDATE EACH RECTANGLE - This is done by changing the colors and text within the grid to match the current state of the game
        
            # ROW 1 - UPDATE SQUARE COLORS
            g.itemconfig(rect_a_1, fill=tile_colors[ (game_1.grid[0])[0] ])
            g.itemconfig(rect_a_2, fill=tile_colors[ (game_1.grid[0])[1] ])
            g.itemconfig(rect_a_3, fill=tile_colors[ (game_1.grid[0])[2] ])
            g.itemconfig(rect_a_4, fill=tile_colors[ (game_1.grid[0])[3] ])
        
        
            # ROW 1 - UPDATE TEXT + COLOR
            g.itemconfig(txt_a_1, text=(number_colors_and_text[(game_1.grid[0])[0]])[0], fill=(number_colors_and_text[(game_1.grid[0])[0]])[1])
            g.itemconfig(txt_a_2, text=(number_colors_and_text[(game_1.grid[0])[1]])[0], fill=(number_colors_and_text[(game_1.grid[0])[1]])[1])
            g.itemconfig(txt_a_3, text=(number_colors_and_text[(game_1.grid[0])[2]])[0], fill=(number_colors_and_text[(game_1.grid[0])[2]])[1])
            g.itemconfig(txt_a_4, text=(number_colors_and_text[(game_1.grid[0])[3]])[0], fill=(number_colors_and_text[(game_1.grid[0])[3]])[1])
   

            # ROW 2 - UPDATE
            g.itemconfig(rect_b_1, fill=tile_colors[ (game_1.grid[1])[0] ])
            g.itemconfig(rect_b_2, fill=tile_colors[ (game_1.grid[1])[1] ])
            g.itemconfig(rect_b_3, fill=tile_colors[ (game_1.grid[1])[2] ])
            g.itemconfig(rect_b_4, fill=tile_colors[ (game_1.grid[1])[3] ])
        
        
            # ROW 2 - UPDATE TEXT + COLOR
            g.itemconfig(txt_b_1, text=(number_colors_and_text[(game_1.grid[1])[0]])[0], fill=(number_colors_and_text[(game_1.grid[1])[0]])[1])
            g.itemconfig(txt_b_2, text=(number_colors_and_text[(game_1.grid[1])[1]])[0], fill=(number_colors_and_text[(game_1.grid[1])[1]])[1])
            g.itemconfig(txt_b_3, text=(number_colors_and_text[(game_1.grid[1])[2]])[0], fill=(number_colors_and_text[(game_1.grid[1])[2]])[1])
            g.itemconfig(txt_b_4, text=(number_colors_and_text[(game_1.grid[1])[3]])[0], fill=(number_colors_and_text[(game_1.grid[1])[3]])[1])

        
            # ROW 3 - UPDATE
            g.itemconfig(rect_c_1, fill=tile_colors[ (game_1.grid[2])[0] ])
            g.itemconfig(rect_c_2, fill=tile_colors[ (game_1.grid[2])[1] ])
            g.itemconfig(rect_c_3, fill=tile_colors[ (game_1.grid[2])[2] ])
            g.itemconfig(rect_c_4, fill=tile_colors[ (game_1.grid[2])[3] ])
        
        
            # ROW 3 - UPDATE TEXT + COLOR
            g.itemconfig(txt_c_1, text=(number_colors_and_text[(game_1.grid[2])[0]])[0], fill=(number_colors_and_text[(game_1.grid[2])[0]])[1])
            g.itemconfig(txt_c_2, text=(number_colors_and_text[(game_1.grid[2])[1]])[0], fill=(number_colors_and_text[(game_1.grid[2])[1]])[1])
            g.itemconfig(txt_c_3, text=(number_colors_and_text[(game_1.grid[2])[2]])[0], fill=(number_colors_and_text[(game_1.grid[2])[2]])[1])
            g.itemconfig(txt_c_4, text=(number_colors_and_text[(game_1.grid[2])[3]])[0], fill=(number_colors_and_text[(game_1.grid[2])[3]])[1])

        
            # ROW 4 - UPDATE
            g.itemconfig(rect_d_1, fill=tile_colors[ (game_1.grid[3])[0] ])
            g.itemconfig(rect_d_2, fill=tile_colors[ (game_1.grid[3])[1] ])
            g.itemconfig(rect_d_3, fill=tile_colors[ (game_1.grid[3])[2] ])
            g.itemconfig(rect_d_4, fill=tile_colors[ (game_1.grid[3])[3] ])
        
        
            # ROW 4 - UPDATE TEXT + COLOR
            g.itemconfig(txt_d_1, text=(number_colors_and_text[(game_1.grid[3])[0]])[0], fill=(number_colors_and_text[(game_1.grid[3])[0]])[1])
            g.itemconfig(txt_d_2, text=(number_colors_and_text[(game_1.grid[3])[1]])[0], fill=(number_colors_and_text[(game_1.grid[3])[1]])[1])
            g.itemconfig(txt_d_3, text=(number_colors_and_text[(game_1.grid[3])[2]])[0], fill=(number_colors_and_text[(game_1.grid[3])[2]])[1])
            g.itemconfig(txt_d_4, text=(number_colors_and_text[(game_1.grid[3])[3]])[0], fill=(number_colors_and_text[(game_1.grid[3])[3]])[1])
        
        
                # update score
            w.itemconfig(score_count_txt, text=str(game_1.total_score))




    

#______________________________________________________________
#  KEY EVENTS - WHAT HAPPENS WHEN KEYS ARE PRESSED
    def up_press(event):
        """this executes when a button for 'up' is pressed"""
        game_1.godsend("up")
        grid_update(g)


    def down_press(event):
        """this executes when a button for 'down' is pressed"""
        game_1.godsend("down")
        grid_update(g)

    def left_press(event):
        """this executes when a button for 'left' is pressed"""
        game_1.godsend("left")
        grid_update(g)

    def right_press(event):
        """this executes when a button for 'right' is pressed"""
        game_1.godsend("right")
        grid_update(g)
        
    def reset_press(event):
        """this executes when a button for 'reset' is pressed"""
        game_1.godsend("reset")
        window.destroy()
        game_play()
                               
    
    
 #_____________________________________________________________________

# BIINDINGS

    
    # create up bindings ("W", "w", "Up")
    window.bind("<w>",up_press)
    window.bind("<W>",up_press)
    window.bind("<Up>",up_press)
    
    
    # create down bindings ("S", "s", "Down")
    window.bind("<s>",down_press)
    window.bind("<S>",down_press)
    window.bind("<Down>",down_press)
 
    
    # create left bindings ("A", "a", "Left")
    window.bind("<a>",left_press)
    window.bind("<A>",left_press)
    window.bind("<Left>",left_press)

    
    # create right bindings ("D", "d", "right")
    window.bind("<d>",right_press)
    window.bind("<D>",right_press)
    window.bind("<Right>",right_press)

    # create reset bindings ("R", "r")
    window.bind("<r>",reset_press)
    window.bind("<R>",reset_press)

                               
    
    
    
    
    
    
    
    w.pack()
    
    # prevent window resize
    window.resizable(False, False) 
    window.mainloop()


# START THE GAME
game_play()

    
                
            
            
        

        
        
    

   

