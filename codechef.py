def codechef(username):
    head = "https://wwww.codechef.com/users/"
    URL = head + username

    page  = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')

    #These three lines give the Rating of the user.
    listRating = list(soup.findAll('div',class_="rating-number"))
    rating = list(listRating[0].children)
    rating = rating[0]
    out = str(rating)
    #print ("Rating: "+rating)

    listGCR = []  #Global and country ranking.
    listRanking = list(soup.findAll('div',class_="rating-ranks"))
    rankingSoup = listRanking[0] 
    for item in rankingSoup.findAll('a'):
            listGCR.append(item.get_text()) #Extracting the text from all anchor tags
    #print ("Global Ranking: "+listGCR[0])
    #print ("Country Ranking: "+listGCR[1])
    out = out + " " + str(listGCR[0])
    return out
