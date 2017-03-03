def enemy_race(self):
    if(self.currentPlayer == 'vamp'):
        return 'wolv'
    elif(self.currentPlayer == 'wolv'):
        return 'vamp'
    else:
        raise ValueError('Invalid player')

    


def attack_humans(units, enemies, probabilistic):
    result = (units, enemies)
    if (units/enemies >= 1):
        result[0] += result[1]
        result[1] = 0
    else:
        if(probabilistic):
            p = units / (2 * enemies)

            
            
        else:
            
        
        #si victoire (proba p) : chaque attaquant a une proba (p) de survivre
        #                        chaque humain a une proba (p) de devenir allié
        #si défaite (1-p) : aucun survivant coté attaquant
        #                   chaque humain a une proba (1-p) de survivre

    return result






def attack_monsters(units, enemies):
    result = (units, enemies)
    
    if (units/enemies >= 1.5):
        result[1] = 0
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




    def resolve(self, square):
        assert self.currentPlayer is not None
        nb_zeros = square.count(0)
        if(nb_zeros == 1):
            if(square[RACE_ID['hum']] > 0):
                rslt = attack_humans(square[RACE_ID[self.currentPlayer]], square[RACE_ID['hum']])
                square[RACE_ID[self.currentPlayer]] = rslt[0]
                square[RACE_ID['wolv']] = rslt[1]
            else:
                if(self.currentPlayer == 'vamp'):
                    rslt = attack_monsters(square[RACE_ID[self.currentPlayer]], square[RACE_ID['wolv']])
                    square[RACE_ID[self.currentPlayer]] = rslt[0]
                    square[RACE_ID['wolv']] = rslt[1]
                else:
                    rslt = attack_monsters(square[RACE_ID[self.currentPlayer]], square[RACE_ID['vamp']])
                    square[RACE_ID[self.currentPlayer]] = rslt[0]
                    square[RACE_ID['vamp']] = rslt[1]
