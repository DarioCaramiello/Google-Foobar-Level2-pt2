def is_equal(lista):
    tmp = lista[0]
    for i in lista:
        if i != tmp:
            return False
    return True

def controlla_lato(lista):

    tmp = ""
    for i in lista:
        if i != "-":
            tmp = i
    for i in lista:
        if i != "-" and i is not tmp:
            return False
    return True


def solution(s):
    flag = False
    hi = 0

    stringa_list = []
    for i in s:
        stringa_list.append((i))

    i = 0
    while len(stringa_list) != 1:
        if is_equal(stringa_list) is True or controlla_lato(stringa_list) is True:
            break
        if flag is True:
            i = i + 1
        else:
            i = 0
        if stringa_list[i] == "-":
            if stringa_list[i + 1] == "-" or stringa_list[i + 1] == ">" or stringa_list[i + 1] == "<":
                stringa_list = stringa_list[1:]

        elif stringa_list[i] == ">":
            if stringa_list[i + 1] == "<":
                # caso " >  < " -- > " < > "
                # si salutano
                # si scambiano di posto
                hi += 2
                # impiegano 10 sec -- sleep(10s)
                tmp = stringa_list[i]
                stringa_list[i] = stringa_list[i + 1]
                stringa_list[i + 1] = tmp
                flag = False
            elif stringa_list[i + 1] == ">":
                # caso " > > "  --> " > "
                flag = True
                # stringa_list = stringa_list[1:]
            elif stringa_list[i + 1] == "-":
                # caso " > - " --> " - > "
                tmp = stringa_list[i]
                stringa_list[i] = stringa_list[i + 1]
                stringa_list[i + 1] = tmp
            elif stringa_list[i + 1] == "-":
                # caso " > - " --> " - > "
                tmp = stringa_list[i]
                stringa_list[i] = stringa_list[i + 1]
                stringa_list[i + 1] = tmp


        elif stringa_list[i] == "<":
            if stringa_list[i + 1] == "<":
                # caso " < < " --> " <"
                stringa_list = stringa_list[1:]
            elif stringa_list[i + 1] == "-":
                # caso " < - " -- " - > "
                tmp = stringa_list[i]
                stringa_list[i] = stringa_list[i + 1]
                stringa_list[i + 1] = tmp
            elif stringa_list[i + 1] == ">":
                # caso " < > " -- " > "
                stringa_list = stringa_list[1:]
        print(stringa_list)
        #print(is_equal(stringa_list))

    return hi


print(solution("<<>><"))
