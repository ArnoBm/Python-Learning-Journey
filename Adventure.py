name = ["Arnob", "Raya", "Tabsheer", "Tonima"]
searching_name = ""
while searching_name not in name:
    searching_name = input("Enter a name to search: ")
    if searching_name == "Arnob":
        print (f"{searching_name} lives in Rajshahi")
    elif searching_name == "Raya":
        print (f"{searching_name} lives in Dinajpur")
    elif searching_name == "Tabsheer":
        print (f"{searching_name} lives in Dhaka")
    elif searching_name == "Tonima":
        print (f"{searching_name} lives in Chittagong")
    else:
        print(f"{searching_name} not found in the list")