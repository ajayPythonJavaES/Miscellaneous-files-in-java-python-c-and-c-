import keyword

def checkIfKeyword():
    usr_str = input("Please enter a word")
    if(keyword.iskeyword(usr_str)):
        print usr_str,"is a keyword"
    else:
        print usr_str,"is not a keyword"
