import random

def primary():
  #print("Keep it logically awesome")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  i = int(input("How many quotes do you want?"))
  count = 0
  while i > count:
      last = 15
      rnd = random.randint(0, last)
      print(quotes[rnd].rstrip())
      count += 1

if __name__== "__main__":
  primary()
