#msgbx.rb
# Author: Akito D. Kawamura (aDAVISk)
# Working on Ruby in gnupack_devel-13.06-2015.11.08
# This program is published under BSD 3-Clause License
# Description: A class of message box of arbitary 
#   dimension. Method write promises the string would
#   not exceed the width of the box.
# Last Update: 2018/06/15
########################################################
class Msgbx
  def initialize(width=30,height=30,hrMargin=2,vtMargin=1)
    @width = width
    @height = height
    @hrMargin = hrMargin
    @vtMargin = vtMargin
    @txtHeight = @height-2*@vtMargin
    @txtWidth = @width - 2*@hrMargin
    @box = "-"*@width+"\n"+("|"+" "*(@width-2)+"|\n")*(@height-2)+"-"*@width
    printf(@box)
  end

  def initialPos
    printf("\r\e[#{@height-1}A\e[#{@vtMargin}B\e[#{@hrMargin}C")
  end

  def clear
    printf("\e[#{@height}B")
    printf("\e[#{@height-1}A\r")
    printf(@box)
  end
  
  def write(instr)
    instr.scan(/.{1,#{@txtWidth}}/).each{|w| printf("#{w}\r\e[1B\e[#{@hrMargin}C")}
  end

  def writeNew(istr)
    clear
    initialPos
    write(istr)
  end

  def kill
    clear
    initialPos
    write("END")
    printf("\e[#{@height}B\n")
  end
end

# Test code
myMsgbx = Msgbx.new(50,10)
sleep(2)
myMsgbx.writeNew("2 seconds passed")
sleep(2)
myMsgbx.write("2 seconds passed: I do not need this space... just filling space...")
sleep(2)
myMsgbx.kill
