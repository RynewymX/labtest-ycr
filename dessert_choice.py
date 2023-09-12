badChoiceCounter = 0

def dessert_choice():
  choice = input("Would you like dessert? ")
  if choice.lower()=="yes":
    print("Awesome. I'll grab you the dessert menu.")
    def dessert_name_choice():
      print("-----------------------------------")
      print("Rose Water Rice Pudding - Input 1")
      print("Tres Leches Cake - Input 2")
      print("Kulfi - Input 3")
      print("Bread Pudding - Input 4")
      print("Beignets - Input 5")
      print("Dirty Sewer Water - Input 6")
      print("Dragon Eyeballs - Input 7")
      print("-----------------------------------")
      dessert_name = input("What dessert would you like? ")
      if dessert_name.lower()=="1":
          print("Excellent choice. I will grab you some Rose Water Rice Pudding right away.")
      elif dessert_name.lower()=="2":
          print("Excellent choice. I will grab you some Tres Leches Cake right away.")
      elif dessert_name.lower()=="3":
          print("Excellent choice. I will grab you some Kulfi right away.")
      elif dessert_name.lower()=="4":
          print("Excellent choice. I will grab you some Bread Pudding right away.")
      elif dessert_name.lower()=="5":
          print("Excellent choice. I will grab you some Beignets right away.")
      elif dessert_name.lower()=="6":
          print("Uhhh... We don't have that on the menu. Try something else?")
          badChoiceCounter + 1
          if badChoiceCounter >= 3:
            print("GET OUT OF MY RESTURANT")
          dessert_name_choice()
      elif dessert_name.lower()=="7":
          print("Are you trying to be funny? We don't have those, try something else.")
          if badChoiceCounter >= 3:
            print("GET OUT OF MY RESTURANT")
          dessert_name_choice()
      else:
        print("Please input a number from 1-7.")
        dessert_name_choice()
    dessert_name_choice()
  elif choice.lower()=="no":
    print("No worries. I'll grab you the check.")
  else:
    print("A fatal error has occured. (Please say yes or no!)")
    dessert_choice()

dessert_choice()
