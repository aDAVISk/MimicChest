# generate.rb
require "json"

data = JSON.parse(File.read("floormap.json"))
#p data

shape = {
  "Rectangle"=>'<rect x="%d" y="%d" width="%d" height="%d" ',
  "text"=>'<text x="%d" y="%d" '
}
style = {
  "exterior"=>'stroke="black" stroke-width="8" fill="none"/>',
  "room"=>'stroke="black" stroke-width="4" fill="lightblue"/>',
  "text"=>'stroke="black" text-anchor="middle" stroke-width="0.5" >'
}

output = <<'EOS'
</<!DOCTYPE html>
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title></title>
    </head>
    <body>
      <svg width="%d" height="%d">
EOS

output = output % data["canvas"]
#p output

data["rooms"].each do |room|
  x, y = room["position"]
  w, h = room["shape"]
  output += shape[room["type"]] % (room["position"] + room["shape"]) + style["room"] + "\n"
  output += shape["text"] % [x+w/2, y+h/2] + style["text"] + room["name"] + "</text>\n"
end

if data.has_key?("exterior")
  temp = data["exterior"]
  output += shape[temp["type"]] % (temp["position"] + temp["shape"]) + style["exterior"] + "\n"
end

output += <<'EOS'
      </svg>
    </body>
  </html>
EOS

#p output
File.write("test_HTMLmap.html", output)
