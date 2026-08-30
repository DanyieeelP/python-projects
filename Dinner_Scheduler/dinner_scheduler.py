import os
import random

#Check if file exist. If not file exist, create a file.
file_path = "dinner_sched.txt"

if not os.path.isfile(file_path):
    with open(file_path, "w") as f:
        pass

with open(file_path, "r") as mainfile:
     content = mainfile.readlines()
     #If the dish_sched.txt is empty, read every dish from dish_selected.txt and copy to dish_sched.txt
     if len(content) == 0:
        with open("dish_selected.txt", "r") as used_file:
            dish_list = used_file.readlines()
            for everyDish in dish_list:
                with open(file_path, "a") as mainfile:
                    mainfile.write(everyDish)
             #remove the content of dish_selected.txt after copying to dinner_sched.txt
            with open("dish_selected.txt", "w") as used_file:
                pass
    #Refill the dinner_sched.txt with the content of dish_selected.txt
     with open(file_path, "r") as mainfile:
        content = mainfile.readlines()
        #to remove new line character when reading the content of the textfile
        content = [line.strip() for line in content]
        dish = random.choice(content)
        print(f"Your dinner for tonight is: {dish}")
        content.remove(dish)
        with open(file_path, 'w') as mainfile:
            for everyLine in content:
                #to add new line character when writing the content to the textfile
                mainfile.writelines(everyLine + "\n")
        with open("dish_selected.txt", "a") as used_Dish:
            used_Dish.writelines(dish + "\n")


#remove the new input dish and save to dish_selected.txt. 

#with open(file_path, "r") as f:
 #   content = f.readlines()
    #If the textfile is empty, copy the content of dish_selected.txt to dinner_sched.txt
  #  if not content:
   #     with open("dish_selected.txt", "r") as mainfile, open(file_path, "w") as selectfile:
    #        selectfile.write(mainfile.read())
        #remove the content of dish_selected.txt after copying to dinner_sched.txt
     #   with open("dish_selected.txt", "w") as f:
      #      pass
        
 #   else:
        #random select a dish from the textfile
  #      a = [line.strip() for line in content]
   #     dish = random.choice(a)
    #    print(f"Your dinner for tonight is: {dish}")
     #   a.remove(dish)

#Remove the selected dish from the textfile.
  #  with open(file_path, "w") as f:
   #     for line in a:
    #        f.write(line + "\n")

  #  with open("dish_selected.txt", "a") as f:
   #     f.write(dish + "\n")

#Display the selected dish for specific time

#Connect Telegram API to notify user about the selected dish
