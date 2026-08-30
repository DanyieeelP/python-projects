from datetime import datetime
import os
import csv


# Ask the user for the minimum stock threshold.
stock_threshold = int(input("Enter minimum stock threshold: "))

total_qty = {}
# Open inventory.csv.
with open('inventory.csv', 'r', encoding = 'utf-8') as file:
	reader = csv.DictReader(file)
	for row in reader:
		item = row['Item Name'].strip().title()
		stock = int(row['Quantity'])
		if item not in total_qty:
			total_qty[item] = stock
		else:
			#total_qty[item] is equals to get the value of [item]. Outer key => inner key. [item] - outer key
			total_qty[item] += stock

#store summary of Inventory.
headers = ["Item", "Quantity"]
with open('inventory_summary.csv', 'w', newline ="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(headers)
	for items, stock in total_qty.items():
		writer.writerow([items.strip(), stock])

#store csv file to variable
low_stock = 'low_stock_report.csv'
#read the summary of inventory
with open('inventory_summary.csv', 'r', encoding = 'utf-8') as file:
	read = csv.reader(file)
	header = next(read)
	print("LOW STOCK ALERT!\n")
	print(f"Threshold:{stock_threshold}")
	print("============================")
	found_low_stock = False
	for row in read:
		#get the data from the csv file
		name = row[0]
		qty = int(row[1])
		if qty < stock_threshold:
			#display low stock items
			found_low_stock = True
			print(f"{name.strip()} | Stock: {qty}")
			#check if file exist
			file_check = os.path.isfile('low_stock_report.csv')
			time_stamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")

			#write report to low_stock_report.csv
			with open(low_stock, 'a', newline ="", encoding="utf-8") as file:
				if not file_check:	
					file.write("Timestamp,Item name,Quantity\n")
#					file.write(f"{time_stamp},{name.strip()},{qty}\n")
				file.write(f"{time_stamp},{name.strip()},{qty}\n")
	print(f"Successfully logged to {low_stock} file")
	#if there's no low stock in files.
	if not found_low_stock: 
		print("No low stock item found")


