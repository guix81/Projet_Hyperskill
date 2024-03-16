def valide_input(chaine_input, chaine_auto, chaine_no_auto):
    token_chaine = False
    token_num = False
    token_auto = None
    token_no_auto = None
    try:  #True si chaine_input = numeric [token_num]
        chaine_input = int(chaine_input)
        token_num = True
    except(ValueError):
        token_num = False
    if type(chaine_input) == type('a'):  ##True si chaine_input = str [token_chaine]
        token_chaine = True
    chaine_input = str(chaine_input)
    #if autorisation_chaine == True:  #True si chaine_input est dans la liste des caractère autoriser(chaine_auto) [token_auto]
    chaine_auto = set(chaine_auto)
    for str_in in chaine_input:
        if str_in not in chaine_auto:
            token_auto = False
        else:
            token_auto = True
    #elif autorisation_chaine == False:  #True si chaine_input est dans la liste des caractère non-autoriser(chaine_no_auto) [token_no_auto]
    chaine_no_auto = set(chaine_no_auto)
    for str_in in chaine_input:
            if str_in in chaine_no_auto:
                token_no_auto = True
            else:
                token_no_auto = False
    return token_num, token_chaine, token_auto, token_no_auto  #revoie une liste bool [token_num, token_chaine, token_auto, token_no_auto]

