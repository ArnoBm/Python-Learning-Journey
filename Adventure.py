name = ["Arnob", "Raya", "Tabsheer", "Tonima"]
searching_name = ""
while searching_name not in name:
    searching_name = input("Enter a name to search: ")
    if searching_name.casefold() == "arnob":
        print (f"{searching_name} lives in Rajshahi")
        break
    elif searching_name.casefold() == "raya":
        print (f"{searching_name} lives in Dinajpur")
        break
    elif searching_name.casefold() == "tabsheer":
        print (f"{searching_name} lives in Dhaka")
        break
    elif searching_name.casefold() == "tonima":
        print (f"{searching_name} lives in Chittagong")
        break
    else:
        print(f"{searching_name} not found in the list")
        #break
print("Thank you for using the search program!")