def main_menu(): 
  print("/n=== RedThread Habit Tracker ===")
  print("1. Incorporate a habit")
  print("2. View habits")
  print("3. Mark hhabit as completed")
  print("4. Exit")
def main (): 
  while True:
    display_menu()
    choice = input ("select an option (1-4):") 
    if choice == "1":
      print("Add habit selected")
    elif choice == "2":
      print ("View habits selected")
    elif choice == "3":
      print("Mark habit selected")
    elif choice == "4":
      print("Exiting program...")
      break
    else: 
      print("Invalid choice. Please try again.")
if__name__=="__main__":
  main()
