import random
from pypdf import PdfMerger
import os

ALPHALIST = ['A','B','C','D','E']

def main():
  num_cards = get_cardnums()
  for i in range(num_cards):
    card = generate_nums()
    print_card(card, i)
    #print_nums(card) # included for testing

  # merge pdfs
  merger = PdfMerger()
  for i in range(num_cards):
    os.system("pdflatex bingoCard"+str(i)+".tex")
    merger.append("bingoCard"+str(i)+".pdf")
  merger.write("allCards.pdf")
  merger.close()

  # clean up all remaining files
  os.system("rm bingoCard*")
  
def get_cardnums():
  while True:
    GET_CARDNUMS = int(input('Enter the number of Bingo cards to generate: '))
    return GET_CARDNUMS

    

def generate_nums():
  B = random.sample(range(1, 16), 5)
  I = random.sample(range(16, 31), 5)
  N = random.sample(range(31, 46), 5)
  G = random.sample(range(46, 61), 5)
  O = random.sample(range(61, 76), 5)
  return [B,I,N,G,O]

def print_nums(card):
  print ('   B   I   N   G   O   ')
  print (f' {card[0][0]:>3} {card[1][0]:>3} {card[2][0]:>3} {card[3][0]:>3} {card[4][0]:>3}')
  print (f' {card[0][1]:>3} {card[1][1]:>3} {card[2][1]:>3} {card[3][1]:>3} {card[4][1]:>3}')
  print (f' {card[0][2]:>3} {card[1][2]:>3} {card[2][2]:>3} {card[3][2]:>3} {card[4][2]:>3}')
  print (f' {card[0][3]:>3} {card[1][3]:>3} {card[2][3]:>3} {card[3][3]:>3} {card[4][3]:>3}')
  print (f' {card[0][4]:>3} {card[1][4]:>3} {card[2][4]:>3} {card[3][4]:>3} {card[4][4]:>3}')

def print_card(card:str, cardNum:int):
  cmdLine = [["" for i in range(5)] for j in range(5)]
  for j in range(5):
    for k in range(5):
      cmdLine[j][k] = f"\\newcommand{{\\Node{ALPHALIST[j]}{ALPHALIST[k]}}}{{\\textbf{{{str(card[k][j])}}}}}"
  fh = open("firsthalf", "r")
  sh = open("secondhalf", "r")
  out = open("bingoCard"+str(cardNum)+".tex", "w")
  out.write(fh.read())
  out.write("\n")
  for i in range(5):
    for j in range(5):
      out.write(cmdLine[i][j])
      out.write("\n")
  out.write(sh.read())
  fh.close()
  sh.close()
  out.close()

    

main ()