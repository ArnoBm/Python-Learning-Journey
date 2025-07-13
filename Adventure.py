name = ["Arnob", "Raya", "Tabsheer", "Tonima"]
searching_name = ""
while searching_name not in name:
    searching_name = input("Enter a name to search: ")
    if searching_name == "Arnob":
        print (f"{searching_name} lives in Rajshahi")
        break
    elif searching_name == "Raya":
        print (f"{searching_name} lives in Dinajpur")
        break
    elif searching_name == "Tabsheer":
        print (f"{searching_name} lives in Dhaka")
        break
    elif searching_name == "Tonima":
        print (f"{searching_name} lives in Chittagong")
        break
    else:
        print(f"{searching_name} not found in the list")
        #break
print("Thank you for using the search program!")