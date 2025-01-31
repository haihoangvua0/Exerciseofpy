dictionary_goc = {
	"tu_goc_1" : "Hello",
	"tu_goc_2" : "Accessibility",
	"tu_goc_3" : "Refuse",
	"tu_goc_4" : "Abandon",
}

dict_dich = {
	"tu_dich_1": "Xin Chao",
	"tu_dich_2": "Kha nang tiep can",
	"tu_dich_3": "Tu Choi",
	"tu_dich_4": "Bo hoang, vut bo"
}

trans = input("1. En-vi; 2. Vi-en (Enter 1 or 2): ")
inp = input("Enter Word: ")


if trans == "1":
	if inp == dictionary_goc["tu_goc_1"]:
		print(f"Translation: {dict_dich["tu_dich_1"]}")
	elif inp == dictionary_goc["tu_goc_2"]:
		print(f"Translation: {dict_dich["tu_dich_2"]}")
	elif inp == dictionary_goc["tu_goc_3"]:
		print(f"Translation: {dict_dich["tu_dich_3"]}")
	elif inp == dictionary_goc["tu_goc_4"]:
		print(f"Translation: {dict_dich["tu_dich_4"]}")
elif trans == "2":
	if inp == dictionary_goc["tu_dich_1"]:
		print(f"Translation: {dictionary_goc["tu_goc_1"]}")
	elif inp == dictionary_goc["tu_dich_2"]:
		print(f"Translation: {dictionary_goc["tu_goc_2"]}")
	elif inp == dictionary_goc["tu_dich_3"]:
		print(f"Translation: {dictionary_goc["tu_goc_3"]}")
	elif inp == dictionary_goc["tu_dich_4"]:
		print(f"Translation: {dictionary_goc["tu_goc_4"]}")
	else:
		print("Invalid Input")
else:
	while True:	
		trans = input("Invalid input: ")
		if trans == "1":
			if inp == dictionary_goc["tu_goc_1"]:
				print(f"Translation: {dict_dich["tu_dich_1"]}")
			elif inp == dictionary_goc["tu_goc_2"]:
				print(f"Translation: {dict_dich["tu_dich_2"]}")
			elif inp == dictionary_goc["tu_goc_3"]:
				print(f"Translation: {dict_dich["tu_dich_3"]}")
			elif inp == dictionary_goc["tu_goc_4"]:
				print(f"Translation: {dict_dich["tu_dich_4"]}")
			else:
				print("Invalid Input")
			break
		elif trans == "2":
			if inp == dictionary_goc["tu_dich_1"]:
				print(f"Translation: {dictionary_goc["tu_goc_1"]}")
			elif inp == dictionary_goc["tu_dich_2"]:
				print(f"Translation: {dictionary_goc["tu_goc_2"]}")
			elif inp == dictionary_goc["tu_dich_3"]:
				print(f"Translation: {dictionary_goc["tu_goc_3"]}")
			elif inp == dictionary_goc["tu_dich_4"]:
				print(f"Translation: {dictionary_goc["tu_goc_4"]}")
			else:
				print("Invalid Input")
		break
		
		
	
	
