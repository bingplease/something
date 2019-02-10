
"""
shooter_v3 (crittercatcher)

Description:
"""
#Setup
from pygame import *
from random import *
from tsk import *
init()
print("Critter Catcher " + str(randint(1, 1000000)) + "." + str(randint(1, 1000000)) + "." + str(randint(1, 1000000)))
print("Owen Fei")
print("This is an FPS game.")
print("The purpose of this game is to shoot down as many critters as you can!")
print("The game progresses from extremely easy to impossible.")
print()
time.wait(1000)


print("Some tips:")
print("The blue critter is slightly darker than the lake")
print("Shooting the wings will not help")
print("Watch out for bush campers!")
time.wait(3000)
w = display.set_mode([800, 600])

#Defines lots of variables

d = True
h = True
total_time = 0
wins = 0
now_time = 0
limit = 10000
shots = 0
kills = 0
best_time = 56237823478957238958239768923578923783333333333333333333333333333333333392372385
critter_speed = 0

bush_count = -1
c = time.Clock()
#Main loop
while d:
    
    h = True
    #Wait time
    wait_time = randint(0, 2000)
    
    #Gives things if wins is enough
    if wins == 6:
        limit = 20000
    bush_locations = []
    if wins % 3 == 0:
        bush_count += 1
    
    #Makes critter faster when game gets harder
    if wins % 10 == 0:
        critter_speed += 1
    #Add items to the bush_locations list (youll see what this is about later)
    for i in range(0, bush_count):
        bush_locations.append(randint(0, 800))
        bush_locations.append(randint(300, 600))
    print(bush_count, "bushes will appear.")
    #Defines critter starting positions
    t2_shot = True
    t_pos_x = randint(150, 650)
    t_pos_y = randint(150, 450)
    t = Rect(t_pos_x, t_pos_y, 20, 20)
    t_ellipse = Rect(t_pos_x - 20, t_pos_y + 5, 60, 10)
    if wins > 5:
        t2_pos_x = randint(150, 650)
        t2_pos_y = randint(150, 450)
        t2 = Rect(t2_pos_x, t2_pos_y, 20, 20)
        t2_shot = False
        t2_ellipse = Rect(t2_pos_x - 20, t2_pos_y + 5, 60, 10)
        
    
    
    #How many bullets determined by number of wins
    bullets = 5
    if wins > 5:
        bullets = 10
    
    
    d = True
    f = 0
    t_shot = False
    #Intro to each round
    mouse.set_visible(True)
    print("Welcome to the critter catcher game! Level", wins)
    print("Press R at any time to run away")
    print(3)
    time.wait(1000)
    print(2)
    time.wait(1000)
    print(1)
    time.wait(1000)
    print("Start shooting")
    
    
    
    time.wait(wait_time)
    start_time = time.get_ticks()
    
    limit -= 400

    if limit < 4000:
        limit = 4000
    mouse.set_visible(False)
    #Sub-main loop
    while d and h:
        #Event loop
        for e in event.get():
            if e.type == QUIT:
                d = False
            #MOuse
            elif e.type == MOUSEBUTTONDOWN:
                x, y = mouse.get_pos()
                #Checks if enough bullets
                
                if bullets > 0:
                    #Increment shots
                    shots += 1
                    #Checks if mouse is at correct pos (BTW this is very precise math)
                    
                    #if x < t.x + 20 and x > t.x:
                    #    if y < t.y + 20 and y > t.y:
                    if pow(x - (t.x + 10), 2) + pow(y - (t.y + 10), 2) < 400:
                        if wins <= 5:
                            t_shot = True
                            
                            kills += 1
                            print("You shot him!")
                            bullets -= 1
                            
                            h = False
                            break
                        elif wins > 5:
                            if t2_shot == False:
                                print("You shot one of them! 1 more to go!")
                            
                            kills += 1
                            t_shot = True
                            bullets -= 1
                            break
                        else:
                            print("You missed")
                            shots += 1
                            if bullets == 1:
                                print("You ran out of bullets.")
                            
                            
                    
                    #elif wins > 5 and y < t2.y + 20 and y > t2.y:
                    #    if x < t2.x + 20 and x > t2.x:
                    
                    elif wins > 5 and pow(y - (t2.y + 10), 2) + pow(x - (t2.x + 10), 2) < 400:
                        if t_shot == False:
                            print("You shot one of them! 1 more to go!")
                        t2_shot = True
                        
                        kills += 1
                        bullets -= 1
                        break
                    else:
                        print("You missed")
                        
                        if bullets == 1:
                            print("You ran out of bullets.")
                            bullets = 0
                        else:
                            bullets -= 1
                            print("You have " + str(bullets) + " bullets")
                #If no more bullets
                else:
                    print("You have no bullets.")

            #If r is pressed game ends
            elif e.type == KEYDOWN:
                if get_key_pressed(K_r):
                    print("You ran away.")
                    time.wait(1000)
                    h = False
                    d = False
        #Red critter position changes
        t_x_offset = randint(-3 - critter_speed, 3 + critter_speed)
        t_y_offset = randint(-3 - critter_speed, 3 + critter_speed)
        t.x += t_x_offset
        t.y += t_y_offset
        t_ellipse.x += t_x_offset
        t_ellipse.y += t_y_offset
        
        #BLue critter position changes a little more than the red critter
        if wins > 5:
            t2_x_offset = randint(-4 - critter_speed, 4 + critter_speed)
            t2_y_offset = randint(-4 - critter_speed, 4 + critter_speed)
            t2.x += t2_x_offset
            t2.y += t2_y_offset
            t2_ellipse.x += t2_x_offset
            t2_ellipse.y += t2_y_offset
        
        w.fill((255, 255, 255))
        #Checks if time is up
        add_time = c.get_time()
        f += add_time
        
        
        if f > limit:
    
            print("He escaped.")
            for i in range(50, 255):
                w.fill((i, 0, 0))
                display.flip()
            time.wait(500)
            
            display.flip()
            time.wait(2000)
            h = False
            d = False
            print("You lost the game!")
            time.wait(2000)
        #If critters are shot
        if t_shot and t2_shot:
            if wins <= 5:
                print("You shot him!")
                wins += 1
                now_time = time.get_ticks()
                actual_time = -(start_time - now_time)
                if actual_time < best_time:
                    best_time = actual_time
                    
                total_time += actual_time
                break
            else:
                print("You shot both of them!")
                now_time = time.get_ticks()
                actual_time = -(start_time - now_time)
                if actual_time < best_time:
                    best_time = actual_time
                wins += 1
                total_time += actual_time
                break
        #Draw ground
        draw.rect(w, (150, 255, 150), Rect(0, 300, 800, 300))
        draw.ellipse(w, (50, 50, 200), Rect(-200, 350, 1200, 500))
        #Checks if red critter is dead already
        if not t_shot:
            draw.ellipse(w, (200, 0, 0), t_ellipse)
            draw.ellipse(w, (255, 0, 0), t)
        #Checks if blue critter is dead already
        if wins > 5:
            if not t2_shot:
                draw.ellipse(w, (0, 0, 200), t2_ellipse)
                draw.ellipse(w, (0, 0, 255), t2)
        
                
        

        #DRaw bushes using the bush_locations list
        for i in range(0, bush_count):
            draw.circle(w, (50, 200, 20), (bush_locations[2 * i], bush_locations[2 * i + 1]), 30)
        
        
        x, y = mouse.get_pos()
        #Draw crosshairs over the mouse
        draw.line(w, (0, 0, 0), (x - 20, y), (x + 20, y), 2)
        draw.line(w, (0, 0, 0), (x, y - 20), (x, y + 20), 2)
        draw.circle(w, (0, 0, 0), (x, y), 20, 2)
        draw.circle(w, (255, 255, 0), (600, 100), 50)
        display.flip()
            
        #Tick the clock
        c.tick(60)
    print("\n" * 10)
#Player stats
print("Player stats:")
if wins > 0:
    print("You got", kills, "kills")
    print("Your average reaction time was", total_time / kills, "milliseconds")
    print("Your best reaction time was", best_time, "milliseconds")
    print("Your average bullets used per kill was", shots / kills)
else:
    print("You completely failed")
time.wait(5000)




#### ---- SET UP ---- ####

# --- Libraries --- #

# D1: Import the random library


# A1: Import and initialize PYGAME




# --- Window --- #

# A2: Open a window with size 800 x 600


# A3: Create a variable for whether the game is over
# with value False



# --- Time --- #

# C1: Create a CLOCK


# C2: Create a variable for the reaction timer with
# value 2000


# E1: Create variable for a wait timer with a random
# value between 750 and 1750


# H1: Create variable for the total reaction time with
# value 0



# --- Critter --- #

# D2: Create two variables for the x and y position of
# the critter. For the x position a random number
# between 50 and 750. For the y position a random
# number between 50 and 550.



# H2: Create a variable to track how many critters have
# been caught starting at 0



#### ---- GAME LOOP ---- ####

# A4: Loop while the game is not over



    #### --- EVENT LOOP --- ####

    # A5: Create an EVENT LOOP that checks for the QUIT
    # event TYPE and sets game_over to True
    # ---> TEST AFTER THESE LINES <--- #





    #### --- CALCULATE MOUSE --- ####

    # F1: If the wait timer is less than 0



        # --- Distance between mouse and critter --- #

        # F2: Get the position of the mouse and assign
        # it to x, y


        # F3: Create variables for the difference in
        # horizontal distance and vertical distance
        # between the critter and the mouse




        # --- Mouse is over critter --- #

        # F4: If the horizontal distance between the
        # critter and the mouse is less than 25 and
        # greater than -25


            # F5: If the vertical distance between the
            # critter and the mouse is less than 25 and
            # greater than -25


                # H3: Increment how many critters have
                # been caught by 1


                # F6: Create a variable for how long it
                # took to catch the critter. Assign it
                # the value
                # (2000 - reaction timer variable) / 1000


                # F7: Print the reaction time
                

                # H4: Remove or comment out F7

                # H5: Increment the total reaction time
                # by the currect reaction time


                # F8: Set the game over variable to True

                # G1: Remove or comment out F8


                # --- Re-set for next round --- #

                # G2: Set the reaction timer to 2000
                # and set the wait timer to a new
                # random value between 750 and 1750



                # G3: Get a new random x and y position
                # for the critter. Random x between
                # 50 and 750, and a Random y between
                # 50 and 550.
                # ---> TEST AFTER THESE LINES <--- #




    #### --- DRAW --- ####

    # --- Draw background --- #

    # B1: Fill the window with color (100, 200, 250)


    # B2: Create a rectangle for the ground at position
    # 0, 300 with width 800 and height 300. Then draw
    # it with color (150, 255, 150)



    # B3: Create a rectangle for the water at position
    # -200, 350, with width 1200 and height 500. Then
    # draw it as an ellipse with color (50, 50, 200)




    # --- Draw critter if it's time --- #

    # E2: If the wait timer is less than 0


    # D3: Draw the critter as a circle at the random
    # x and y position with the color of your choice
    # and a radius of 25
    # ---> TEST AFTER THIS LINE <--- #


        # E3: Re-indent D3 above to be inside the block
        # of the E2 if-clause


    #### --- FINISH FRAME --- ####

    # C3: Tick the clock with framerate 60


    # B4: Flip the display
    # ---> TEST AFTER THIS LINE <--- #



    #### --- CALCULATE TIMES --- ####

    # --- Time passes --- #

    # E4: Decrement the wait timer by get_time


    # E5: If the wait timer is less than 0


    # C4: Decrement the reaction timer by get_time


        # E6: Re-indent C4 above to be inside the block
        # of the E5 if-clause
        # ---> TEST AFTER THIS LINE <--- #


    # --- Stop when time runs out --- #

    # C5: If the reaction timer is less than 0, end the
    # game
    # ---> TEST AFTER THESE LINES <--- #



        # F9: Print a message that the critter escaped
        # ---> TEST AFTER THIS LINE <--- #



#### ---- FINAL OUTPUT ---- ####

# H6: Print a blank line, "FINAL SCORE", and a line
# of dashes




# H7: Print the total amount of critters caught and the
# average reaction time
# ---> TEST AFTER THESE LINES <--- #






# Turn in your Coding Project.
