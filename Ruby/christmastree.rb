# christmastree.rb
# Author: Akito D. Kawamura (aDAVISk)
# Working on Ruby in gnupack_devel-13.06-2015.11.08
# 2-byte character (Japanese) is required.
# This program is published under BSD 3-Clause License
# Last Update: 2018/01/04
########################################################
totalTime = 100 #(second) to delay
dt = 0.4 #(second) to delay

# list of half periods of the controled lines (in unit of dt)
ph1 = 7 #(dt)
ph2 = 2 #(dt)

# list of third periods of the controled lines (in unit of dt)
pt1 = 5 #(dt)
pt2 = 3 #(dt)

# list of quarter periods of the controled line (in units of dt)
pq1 = 4

loopnum = (totalTime/dt).to_i

empty = "\n\n\n\n\n\n\n\n\n\n\n"

print empty

for i in 0 .. loopnum
  ch1 = 33 *(i/ph1 % 2) # yellow => white
  ch2 = 30 + 6 *(i/ph2 % 2) # cyan => black
  ct1 = 30 + (3.5 *(i/pt1 % 3)).to_i # yellow => white => black
  ct2 = 30 + (i/pt2 % 3) # red => green => black
  cq1 = 36 - (i/pq1 % 4)*((i/pq1 % 4)+1)/2 # cyan => magenta => yellow => black
  tree = "　\e[#{ct1}m＋\e[0m　　　　\e[#{ch1}m★\e[0m　　　　\n"\
        +"　　　　　／\e[#{cq1}m。\e[0m＼　　\e[#{ct1}m＋\e[0m　\n"\
        +"　　　　／\e[#{ct2}m。\e[0m　\e[#{ch2}m＊\e[0m＼　　　\n"\
        +"　　　／　\e[#{ch2}m。\e[0m　　\e[#{cq1}m。\e[0m＼　　　\n"\
        +"　　\e[#{ct1}m＋\e[0m　／　　\e[#{ct2}m。\e[0m＼　　　\n"\
        +"　　　／\e[#{cq1}m。\e[0m　\e[#{ch2}m。\e[0m　\e[#{ch2}m＊\e[0m＼　　\n"\
        +"　　／　\e[#{ct2}m＊\e[0m　　　\e[#{cq1}m。\e[0m　＼　\n"\
        +"　／\e[#{ch2}m。\e[0m　\e[#{ch2}m。\e[0m　\e[#{ct2}m。\e[0m　　\e[#{ct2}m。＊\e[0m＼\n"\
        +"　\e[#{ct2}mｉ　\e[0m\e[#{ch2}mｉ\e[0m｜　\e[#{ct2}mｉ\e[0m　｜\e[#{ct2}mｉ\e[0m　\e[#{ch2}mｉ\e[0m\n"\
        +"　　　　｜　　　｜　　　\n"
  print "\e[10A#{tree}" #\d[10A moves current position 10 lines upward then rewrite the tree part.
  sleep(dt)
end

