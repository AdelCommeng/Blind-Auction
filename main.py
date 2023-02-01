from replit import clear
from art import logo

end_auction = False
print(logo)
auc = {}
def auction():  
  name = input("What is your name?:")
  bid = input("What's your bid?:$")
  auc[name] = bid
  clear()
 
def winner(dic):
  values=[]
  highest =0
  for value in dic:
    first = int(dic[value])
    if first > highest:
      winner =value
      highest = first
  print(f"The winner is {winner} with {highest}")
  
auction()
while not end_auction:
  decision = input("Are there any other bidders? Type yes or no.")
  if decision =="yes":
    clear()
    auction()

  elif decision =="no":
    clear()
    winner(auc)
    end_auction=True

  else:
    decision =input("Please enter yes or no.")
  
  
