utility_db = {
    '111': 'Myymälähallit',
    '112': 'Liike- ja tavaratalot, kauppakeskukset',
    '119': 'Myymälärakennukset',
    '121': 'Hotellit, motellit, matkustajakodit, kylpylähotellit',
    '123': 'Loma- lepo- ja virkistyskodit',
    '124': 'Vuokrattavat lomamökit ja osakkeet (liiketoiminnallisesti)',
    '129': 'Muut majoitusliikerakennukset',
    '131': 'Asuntolat, vanhusten palvelutalot, asuntolahotellit',
    '139': 'Muut majoitusrakennukset',
    '141': 'Ravintolat, ruokalat ja baarit',
    '151': 'Toimistorakennukset',
    '161': 'Rautatie- ja linja-autoasemat, lento- ja satamaterminaalit',
    '162': 'Kulkuneuvojen suoja- ja huoltorakennukset',
    '163': 'Pysäköintitalot',
    '164': 'Tietoliikenteen rakennukset',
    '169': 'Muut liikenteen rakennukset'
}

def create_decimal_timedata(data):
    new_col = data['construction_date'].tolist()
    for i,dt in enumerate(new_col):
        if dt:
            s = dt.split('-')
            new_col[i] = float(s[0])+(float(s[1])-1)/12 + (float(s[2])-1)/365
    return new_col

def match_utility_code(code):
    return utility_db[code]

def kakka():
    print('kakka')
