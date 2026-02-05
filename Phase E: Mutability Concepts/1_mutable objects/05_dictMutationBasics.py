# Goal: Add, update, and delete keys in a dictionary.
# Expected outcome: prints exactly: {'name': 'Ada', 'age': 37}

def main():
    person = {"name": "Ada"}

    # TODO: add key "age" with value 36
    
    # TODO: update "age" to 37

    # TODO: add a temporary key "temp" then delete it
    person["age"] = 36          
    person["age"] = 37          

    person["temp"] = True       
    del person["temp"] 
    print(person)


if __name__ == "__main__":
    main()
