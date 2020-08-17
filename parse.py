def parse(filename):
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()
  words.sort()
  print(words)
  uniue_char = []
  for c in words:
      for d in c:
          
        if not d in uniue_char:
           uniue_char.append(d)
  print(uniue_char)
sorting("sample.txt")
