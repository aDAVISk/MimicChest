# otoshidama.rb
# Author: Akito D. Kawamura (aDAVISk)
# This is a console-based game to move a ball (player)
# to the bottom floor.
#
# Tested on Ruby 3.0.2p107
# This program is published under BSD 3-Clause License
# Last Update: 2021/11/26
########################################################

require 'io/console'

h = 8 # height
d = 12 # width

$tl = { # map tiles : 表示文字は全角
  0 => "　", # asle
  -1 => "\e[42m　\e[0m", # wall # 背景を色指定
  1 => "\e[33m●\e[0m", # player
} # 色指定する場合は、必ず\e[0mで閉じ、書式をリセットする事

mapDim = [h*2+1,d+2]
mapVal = Array.new(mapDim[0]){ Array.new(mapDim[1], 0) }

# generating map (walls, floors, and holes)
(0...mapDim[0]).each do |jj|
  if jj%2 == 0
    mapVal[jj].map!{|vv| vv=-1} # floor
    if jj != 0 and jj != mapDim[0]-1
      mapVal[jj][Random.rand(1...mapDim[1]-1)] = 0 # hole
    end
  else
    mapVal[jj][0] = -1
    mapVal[jj][-1] = -1
  end
end

#p mapVal
def showMapTxt(mapVal)
  #p $tl
  hh = mapVal.size()
  mapTxt = Array.new(hh)
  (0...hh).each do |jj|
    mapTxt[jj] = mapVal[jj].map{|ww| $tl[ww]}.join()
  end
  #puts "\e[H\e[2J" # clear command line
  puts "\e[H" # moce cursor to top-left
  puts mapTxt
  puts ""
  return mapTxt
end

#puts mapTxt
pos = [1,mapDim[1]/2] # position of player, [vertical, horizontal] from top-left
if mapVal[pos[0]][pos[1]] == 0
  pos[1] += 1
end
mapVal[pos[0]][pos[1]] = 1

#logTxt = ""

puts "\e[H\e[2J" # clear command line
puts "a: move left,  d: move right,     q: quit"
puts ""
(-3..-1).each do |tt|
  puts "\e[1A Starts in #{-tt}"
  sleep(1)
end

puts "\e[H\e[2J" # clear command line
loop do
  showMapTxt(mapVal)
  puts "a: move left,  d: move right,     q: quit"
  key = STDIN.getch
  #p key
  #p logTxt += key +":#{key.class},"
  newPos = pos[1]
  if key == "q"
    #print "\e[1;1H\e[#{mapDim[0]+3}B"
    break
  elsif key == "a" # move left
      newPos -= 1
  elsif key == "d" # move right
      newPos +=1
  end
  if mapVal[pos[0]][newPos] != -1
    mapVal[pos[0]][pos[1]] = 0
    pos[1] = newPos
    mapVal[pos[0]][pos[1]] = 1
  end
  while mapVal[pos[0]+1][pos[1]] == 0 # fall slowly
    showMapTxt(mapVal)
    sleep(0.3)
    mapVal[pos[0]][pos[1]] = 0
    pos[0] += 1
    mapVal[pos[0]][pos[1]] = 1
  end
  if pos[0] == mapDim[0]-2
    puts "\e[H\e[2J" # clear command line
    showMapTxt(mapVal)
    puts "!!! GOAL !!!"
    puts ""
    break
  end
end
