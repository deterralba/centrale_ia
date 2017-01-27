def attack_humans(units, enemies):
    result = units
    if (units/enemies >= 1):
        result += enemies
        #mettre à jour ennemis aussi
    else:
        p = units / (2 * enemies)
        #si victoire (proba p) : chaque attaquant a une proba (p) de survivre
        #                        chaque humain a une proba (p) de devenir allié
        #si défaite (1-p) : aucun survivant coté attaquant
        #                   chaque humain a une proba (1-p) de survivre


def attack_monsters(units, enemies):
    result = units
    
    if (units/enemies >= 1.5):
        p = 1
    elif (units == enemies):
        p = 0.5
    elif (units > enemies):
        p = units / enemies - 0.5
    else:
        p = units / (2 * enemies)

    #si victoire (proba p) : chaque attaquant a une proba (p) de survivre
    #                        aucun survivant coté ennemi
    #si défaite (1-p) : aucun survivant coté attaquant
    #                   chaque ennemi a une proba (1-p) de survivre
