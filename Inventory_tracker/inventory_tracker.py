from datetime import datetime
import os
import csv

default_file = "inventory.csv"
#
while True:
	
	#Input details
	#input item name
	item_name = input("Item name: ").strip().title()
	#input quantity received
	quantity = int(input("quantity: "))
	#input unit value
	unit_value = int(input("Item value: "))
	#timestamp
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	#compute the cost
	total_cost = unit_value*quantity

	#add row to csv file
	row = f"{timestamp},{item_name},{quantity},{unit_value},{total_cost}\n"

	file_check = os.path.isfile(default_file)

	#save as csv file
	with open(default_file, "a", newline="") as file:
		#check if file exist
		if not file_check:
			file.write("Timestamp,Item Name,Quantity,Unit Value,Total Value\n")
		file.write(row)
	#prompt to add another item
	input_again = input("Do you want to add another item? ")
	if input_again.lower() == "n":
		#show the file content
		#create dictionary
		
		item_totals = {}
		#read the csv file rows 
		with open(default_file, 'r') as file:
			#skip the header
			header = next(file)
			
			inventory = csv.reader(file)
			#iterate over each row and extract the item and store it.
			for row in inventory:
				item = row[1]
				qty = int(row[2])
				values = int(row[4])
				if item not in item_totals:
					item_totals[item] = {"stock": qty, "value": values}
				else:
					item_totals[item]["stock"] += qty
					item_totals[item]["value"] += values 
			#iterate rows in dictionary
			grandtotal = 0
			for item, data in  item_totals.items():
				print(f"{item} | Stock: {data['stock']} | Total Value: {data['value']:,.2f}")
				grandtotal += data['value']
			print(f"\nThe Grand Total Inventory value: {grandtotal:,.2f}")
		break
