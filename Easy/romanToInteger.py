class Solution:
    def romanToInt(self, s):
        convertNumber = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50,
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        valorTotal = 0
        while len(s) > 1:
            i = len(s) - 1
            valRomanAtual = s[i]
            valIntAtual = convertNumber[valRomanAtual]
            valRomanProx = s[i-1]
            valIntProx = convertNumber[valRomanProx]

            if (valIntProx == 1 and (valIntAtual == 5 or valIntAtual == 10)) or (valIntProx == 10 and (valIntAtual == 50 or valIntAtual == 100)) or (valIntProx == 100 and (valIntAtual == 500 or valIntAtual == 1000)):
                s = s[:-2]
                sub = valIntAtual - valIntProx
                valorTotal += sub
                print(valRomanAtual)
                print(valRomanProx)
            else:
                s = s[:-1]
                valorTotal += valIntAtual
        if s:
            valorTotal += convertNumber[s[0]]
        return valorTotal

