from datetime import datetime
import os

while True:
	kiosk_terminal = input("Kiosk Terminal: ").strip()
	kiosk_name = input("Kiosk name: ").strip()
	technician = input("Technician: ").strip()
	task = input("Task: ").strip()
	remarks = input("Remarks: " ).strip()
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	line = f"{time_now}, {kiosk_terminal}, {kiosk_name}, {technician}, {task.upper()}, {remarks}\n"

	file_name = input("Save as: ")
	file_exist = os.path.isfile(file_name)
	if file_exist:
		with open(file_name, "a") as file:
			file.write(line)
			print("Log saved to", file_name)
	else:
		new_file = input(f"File doesn't exist, Do you want to create this file as {file_name}: ")
		if new_file.lower() == "y":
			with open(file_name, "a") as file:
				file.write("Timestamp, Kiosk_terminal, Kiosk_name, Technician, Task, Remarks\n") 
				file.write(line)
				print("Log saved to", file_name)
	again = input("Do you want to add another log? ")

	if again.lower() == "n":
		break
