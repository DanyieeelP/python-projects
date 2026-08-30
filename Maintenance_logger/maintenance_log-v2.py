from datetime import datetime
import os

default_file = "maintenance_log.csv"
file_name = input(f"Save as [{default_file}]?: ")
if file_name.lower() == "":
	default_file = "maintenance_log.csv"
else:
	default_file = new_file
while True:
	print(f"Using [{default_file}]")
	kiosk_terminal = input("Kiosk Terminal: ").strip()
	kiosk_name = input("Kiosk name: ").strip()
	technician = input("Technician: ").strip()
	task = input("Task: ").strip()
	remarks = input("Remarks: " ).strip()
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	line = f"{time_now}, {kiosk_terminal}, {kiosk_name}, {technician}, {task.upper()}, {remarks}\n"

	file_exist = os.path.isfile(default_file)
	if not file_exist:
		with open(default_file, "a") as file:
			file.write("Timestamp, Kiosk_terminal, Kiosk_name, Technician, Task, Remarks\n") 
			file.write(line)
			print("Log saved to", default_file)
	else:
		with open(default_file, "a") as file:
			file.write(line)
			print("Log saved to", default_file)
	again = input("Do you want to add another log? ")
	if again.lower() == "n":
		break
