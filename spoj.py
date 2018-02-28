def spoj(username):
    base = "https://spoj.com/users/"
    var = username
    url = base + var
    sauce = requests.get(url) 
    soup = BeautifulSoup(sauce.content,'lxml')     # lxml is a parser
    #print(soup.prettify())
    iList = []
    info = (soup.find_all('p'))
    for i in info:
        iList.append(i.text)

    #print (iList[2]) #World rank
    #print (iList[3]) #Institution
    no_of_questions = int(soup.find('dd').text)
    #print(" no. of questions = ",no_of_questions)
    s = str(iList[2].lstrip())+" "+str(no_of_questions)
    return s
