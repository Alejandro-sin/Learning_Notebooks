    '''
    
    Revisar este código, pertenece a la págian 64 del libro de Ryan Mitchell de webscraping.
    
    
    '''

    from urllib.request import urlopen
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup
    import re
    import datetime
    import random


    pages = set()

    #  Random seeds.

    random.seed(datetime.datetime.now())

    # Retorna todos los links internos encotnrados en una página.
    def getInternalLinks(bs,includeUrl):
        '''

        :param bs:
        :param includeUrl:
        :return: internalLinks

        Esta función recibe un objeto bs4 y una URL.
        Vuelvo esta variable una porción de lo que las partes d ela url ofrecen.
        Esta función consigue los links internos de la página, según unas condiciones dadas


        '''

        includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)
        internalLinks = []

        # Encuentra todos los links que empiezan con "/"
        for link in bs.find_all('a', href=re.compile('^(/|.*'+ includeUrl +')')):
            if link.attrs['href'] is not None:
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in internalLinks:
                        if(link.attrs['href'].startwith('/')):
                            internalLinks.append(includeUrl+link.attrs['href'])
                        else:
                            internalLinks.append(link.attrs['href'])
        return internalLinks


    # Recupera una lista de todos los links externos encontrados en la página.
    allExtLinks =set()
    allIntLinks =set()

    def getAllExternalLinks(siteUrl):
        html = urlopen(siteUrl)
        domain ='{}//{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
        bs= BeautifulSoup(html, 'html.parser')
        internalLinks= getInternalLinks(bs,domain)
        externalLinks = getAllExternalLinks(bs, domain)

        for link in externalLinks:
            if link not in allExtLinks:
                allExtLinks.add(link)
                print(link)
        for link in internalLinks:
            if link not in allIntLinks:
                allIntLinks.add(link)
                getAllExternalLinks(link)

    allIntLinks.add('https://es.wikipedia.org/wiki/Neuroteolog%C3%ADa')
    getAllExternalLinks('https://es.wikipedia.org/wiki/Neuroteolog%C3%ADa')



    def getRandomExternalLink(startingPage):
        html = urlopen(startingPage)
        bs = BeautifulSoup(html,'html.parser')
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
        if len(externalLinks) ==0:
            print("No external links, looking around the site...")
            domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
            internalLinks = getInternalLinks(bs, domain)
            return  getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
        else:
            return externalLinks[random.randint(0,len(externalLinks)-1)]


    def followExternalOnly(startingSite):
        externalLink = getRandomExternalLink(startingSite)
        print('Random external link is: {}'.format(externalLink))
        followExternalOnly(externalLink)


    followExternalOnly('https://es.wikipedia.org/wiki/Neuroteolog%C3%ADa')