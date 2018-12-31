# otoshidama.rb
# Author: Akito D. Kawamura (aDAVISk)
# This is a console-based game to move a ball (player)
# to the bottom floor.
#
# Tested on Ruby 2.5.1p57 in WSL Ubuntu
# This program is published under BSD 3-Clause License
# Last Update: 2018/12/31
########################################################

require 'io/console'

# dimensions of the map
$w = 30 #weight
$h = 15 #height

numHoleMin = 2 #minimum number of holes / floor
numHoleMax = 4 #maximum number of holes / floor

def getStrPos(pos_x,pos_y)
  return ($w+1)*($h-pos_y-1)+pos_x
end

# Font setup
wall = "#" 
ball = "o" 
blank = " " 
if wall == ball
  puts "WRONG SETUP"
  exit 
end

# Generating Map
map = (blank*$w+"\n")*$h
## Setting up surrounding walls
for ii in 0..$h-1
  map[getStrPos(0,ii)] = wall
  map[getStrPos($w-1,ii)] = wall
end
map[0..$w-1] = wall*$w
map[getStrPos(0,0)..getStrPos($w-1,0)] = wall*$w
## Generating Floors with holes
for ii in 0..($h/2-2)
  numHole = rand(numHoleMin..numHoleMax)
  floorpos = getStrPos(1,$h-2*ii-3)
  map[floorpos..(floorpos+$w-2)] = wall*($w-1)
  trypos = rand($w-1)
  while numHole > 0
    if map[floorpos+trypos] == wall
      map[floorpos+trypos] = blank
      numHole -=1
      trypos = rand($w-1)
    else
      trypos = (trypos + 1)%($w-1)
    end
  end
end

# Initial position setup
pos_x = $w/2
pos_y = $h-2
strpos = getStrPos(pos_x,pos_y)
floorpos = getStrPos(pos_x,pos_y-1)
map[floorpos] = wall
screen = map.dup
screen[strpos] = ball

# Initial Screen Setup
print "OTOSHIDAMA GAME\n"
print "Use arrow keys <-/-> to move your ball,\n"
print "and reach to the bottom floor.\n"
print "Press 'q' to quit the game.\n"
print "\n"*$h
print "\e[#{$h}A"
print screen

# Game Controll
while key = STDIN.getch
  case key
  when "\e"
    if STDIN.getch == "["
      screen[strpos] = map[strpos]
      case STDIN.getch
      when "C" #Right
        if pos_x < $w-2
          pos_x += 1
        end
      when "D" #Left
        if pos_x > 1
          pos_x -= 1
        end
      end
      strpos = getStrPos(pos_x,pos_y)
      screen[strpos] = ball
    end
  when "q"
    break
  end
  print "\e[#{$h}A\r"
  print screen
  floorpos = getStrPos(pos_x,pos_y-1)
  while map[floorpos] != wall
    screen[strpos] = map[strpos]
    pos_y -= 1
    strpos = getStrPos(pos_x,pos_y)
    screen[strpos] = ball
    print "\e[#{$h}A\r"
    print screen
    floorpos = getStrPos(pos_x,pos_y-1)
    sleep(0.02)
  end
  if pos_y == 1
    puts "CONGRATULATIONS!!"
    break
  end
  #  sleep(0.1)
end
#end
