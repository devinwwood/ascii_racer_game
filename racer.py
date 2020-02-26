#!/usr/bin/python3
'''
taylor@mst.edu
'''

# Do NOT edit the next two lines of code:
import sys
assert ('linux' in sys.platform), "This code should be run on Linux, just a reminder to follow instructions..."


skull = '''
     _.--"""""--._
   .'             '.
  /                 \\
 ;                   ;
 |                   |
 |                   |
 ;                   ;
  \ (`'--,    ,--'`) /
   \ \  _ )  ( _  / /
    ) )(')/  \(')( (
   (_ `""` /\ `""` _)
    \`"-, /  \ ,-"`/
     `\ / `""` \ /`
      |/\/\/\/\/\|
      |\        /|
      ; |/\/\/\| ;
       \`-`--`-`/
        \      /
         ',__,'
          q__p
          q__p
          q__p
          q__p
'''

win = '''
                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\\'/.'_\(/_ '.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\     '   
  '..'  ':::' === * /\ *     .'/.\\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                       ~-~-~-~-~-~-~-~-~-~   /|
                 ~-~-~-~-~-~-~-~  /|~       /_|\\
        ~-~-~-  -~-~-~-~-~-~     /_|\    -~======-~
~-~~~~~~~~~~~~~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~
                        ~-~~-~-~-~-~
'''


light = '''
    _------_
  -~        ~-
 -     _      -
-      |>      -
-      |<      -
 -     |>     -
  -    ||    -
   -   ||   -
    -__||__-
    |______|
    <______>
    <______>
       \/
'''

car = '''
                              _.-=--         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]           : /        \ : |========================|    : /        \ :      :
\___________:|     *    |: |========================|    :|     *    |:   _-"
 \__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
'''

my_track = ['00   |*     *|',
            '01    |*     *|',
            '02     |*     *|',
            '03    |*      *|',
            '04   |*      *|',
            '05  |*      *|',
            '06  |*      *|',
            '07   |*     *|',
            '08    |*     *|',
            '09     |*     *|',
            '10      |*     *|',
            '11       |*     *|',
            '12        |*     *|',
            '13         |*     *|',
            '14        |*     *|',
            '15       |*     *|',
            '16      |*     *|',
            '17     |*     *|',
            '18    |*     *|',
            '19   |*     *|',
            '20  |*     *|',
            '21 |*     *|',
            '22  |*     *|']

# Here's how you clear the screen. 
# To do this before or after what you print?
# This is intended to work on Linux
print("\033[H\033[J")

# Write your code here:


def game():
    print(car)
    print("Welcome to ASCII-racer.")
    print("Navigate through to the light at the end of the tunnel to win!")
    print("Press 'a' for left, 'd' for right', enter for nothing.")
    print("If you hit the walls, you lose.")
    print("To win, you have to complete 2 laps around the tunnel array.")
    input("Press any key to start!")
    print("\033[H\033[J")


    level = 00
    x = 0
    lap = level % 23
    print("ASCII Racer 2.0, level: ", level, "completed rows in lap number ", lap)
    print(light)
    row_top = my_track[(level + 2) % 23]
    row_middle = my_track[(level + 1) % 23]
    row = my_track[level % 23]
    car_pos = 9
    row = row[0:car_pos] + '^' + row[car_pos + 1:]

    print(row_top)
    print(row_middle)
    print(row)

    move = input()
    print("\033[H\033[J")
    car_pos = 9
    while move != quit:
        if move == "d":
            car_pos += 1
            level += 1
            x += 1
            if x < 23:
                lap = 1
            if x >= 23:
                lap = 2
            level = level % 23
            if my_track[level % 23][car_pos] == "*" or my_track[level % 23][car_pos] == "|":
                print("\033[H\033[J")
                print(skull)
                print("You hit the wall, and lose!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()

            if x == 46:
                print("\033[H\033[J")
                print(win)
                print("You win!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()

            row = my_track[level % 23]
            row = row[0:car_pos] + '^' + row[car_pos + 1:]
            row_top = my_track[(level + 2) % 23]
            row_middle = my_track[(level + 1) % 23]
            print("ASCII Racer 2.0, level: ", level, "completed rows in lap number ", lap)
            print(light)
            print(row_top)
            print(row_middle)
            print(row)
            move = input()
            print("\033[H\033[J")

        elif move == "a":
            car_pos -= 1
            level += 1
            x += 1
            if x < 23:
                lap = 1
            if x >= 23:
                lap = 2
            level = level % 23
            if my_track[level % 23][car_pos] == "*" or my_track[level % 23][car_pos] == "|":
                print("\033[H\033[J")
                print(skull)
                print("You hit the wall, and lose!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()

            if x == 46:
                print("\033[H\033[J")
                print(win)
                print("You win!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()

            row = my_track[level % 23]
            row = row[0:car_pos] + '^' + row[car_pos + 1:]
            row_top = my_track[(level + 2) % 23]
            row_middle = my_track[(level + 1) % 23]
            print("ASCII Racer 2.0, level: ", level, "completed rows in lap number ", lap)
            print(light)
            print(row_top)
            print(row_middle)
            print(row)
            move = input()
            print("\033[H\033[J")

        elif move != "a" and move != "d":
            car_pos = car_pos
            level += 1
            x += 1
            if x < 23:
                lap = 1
            if x >= 23:
                lap = 2
            level = level % 23
            if my_track[level % 23][car_pos] == "*" or my_track[level % 23][car_pos] == "|":
                print("\033[H\033[J")
                print(skull)
                print("You hit the wall, and lose!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()
                
            if x == 46:
                print("\033[H\033[J")
                print(win)
                print("You win!")
                print()
                yn = input("Do you want to play again? (y/n):")
                if yn == 'n':
                    quit()
                elif yn == 'y':
                    print("\033[H\033[J")
                    game()
            row = my_track[level % 23]
            row = row[0:car_pos] + '^' + row[car_pos + 1:]
            row_top = my_track[(level + 2) % 23]
            row_middle = my_track[(level + 1) % 23]
            print("ASCII Racer 2.0, level: ", level, "completed rows in lap number ", lap)
            print(light)
            print(row_top)
            print(row_middle)
            print(row)
            move = input()
            print("\033[H\033[J")
        
game()



