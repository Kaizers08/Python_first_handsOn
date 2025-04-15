
bag = ["wallet", "gun", "handkerchief"]

while True:
  bag = input("type a word: ")
  if "gun" in bag:
    print("Controlband!")
    
  elif "wallet" in bag:
    print("You Have More Money")
  else:
    print("All clear")    