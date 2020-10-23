import sys
from copy import deepcopy

# Python3 code for the above approach. 
def areBookingsPossible(arrival, departure, k): 
    ans = []
    numero_quartos = k
    quartos = {}
    log = []
    for i in range(1, numero_quartos + 1):
        quartos[i] = ['Vazio', (0, 0)]
    for i in range(0, len(arrival)): 
        ans.append((arrival[i], departure[i])) 
    ans.sort()
    curr_active, max_active = 0, 0
    ans_iter = deepcopy(ans)
    for m in ans_iter:
        for quarto in quartos:
            if quartos[quarto][0] == 'Vazio':
                quartos[quarto] = ['Ocupado', m]
                curr_active += 1
                ans.remove(m)
                max_active = max(max_active, curr_active) 
                log.append(str(quartos))
                break
            elif quartos[quarto][1][1] < m[0]:
                quartos[quarto] = ['Ocupado', m]
                ans.remove(m)

                curr_active -= 1
                log.append(str(quartos))
                break                
    print("Para " + str(numero_quartos) + " o log de ocupação é: " )
    for j in log:
        print(j)
    if not ans:
        return k >= max_active, ans, log 
        print("------------------------------------------------------------------------------------------")
    else:
        print("Horarios não encaixados: ", ans)
        print("------------------------------------------------------------------------------------------")
        return k < max_active, ans, log

# Driver Code 
if __name__ == "__main__": 
    arrival = [1, 3, 5, 6] 
    departure = [2, 6, 8, 8] 
    arrival = [1, 3, 0, 5, 6, 5, 7, 8, 11, 2, 13]
    departure = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    report = []
    for n in range(1, 99999):
        bol, salas, hist = areBookingsPossible(arrival, departure, n)
        if bol:
            # print("O numero de salas ideal é:", n)
            report.append("O numero de salas ideal é: " + str(n))
            break
        report.append("Para " + str(n) + " salas é necessario alterar os horarios: " + str(salas))
    print("------------------------------------------------------------------------------------------")
    for j in report:
        print(j)
        print("------------------------------------------------------------------------------------------")