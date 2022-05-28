itera = 0
melhor_i = 0
lista_tabu = []
houve_movimento_proibido = False

s = input("Solução corrente: ")
bt_max = int(input("BTMax: "))
T = int(input("T: "))

while bt_max > (itera - melhor_i):
    itera += 1
    sn = []
    fs = []

    for i in range(len(s)):
        sn.append(s)
        fs.append(0)

    for i in range(len(sn)):
        s = list(sn[i])
        if s[i] == '0':
            s[i] = '1'
        else:
            s[i] = '0'

        sn[i] = "".join(s)

    count = 0
    for bits in sn:
        for bit in bits:
            if bit == "1":
                fs[count] += 1
        count += 1

    for i in range(len(sn)):
        print("s" + str(i) + " -> " + str(sn[i]) + ", f(s" + str(i) + ") = " + str(fs[i]))
        # print("s%i -> %s, f(s%i) = %i", i, sn[i], i, fs[i])

    max_value = max(fs)
    max_index = fs.index(max_value)

    fs_index_ordenado = sorted(range(len(fs)), key=lambda k: fs[k])

    houve_movimento_proibido = False
    if max_index in lista_tabu:
        print("s"+str(max_index)+" foi gerado por um movimento proibido")
        fs_index_ordenado.pop()
        houve_movimento_proibido = True

    lista_tabu = [fs_index_ordenado[-1]]

    s = sn[fs_index_ordenado[-1]]

    if not houve_movimento_proibido:
        melhor_i = itera

    print("Nova solução: " + s)
    print("Lista Tabu = {" + str(lista_tabu) + "}")
    print("Iter - Melhor_Iter = " + str(itera) + "-" + str(melhor_i) + " <= BTMax")

print("-----------------------------------------")
print("s* = " + s, "f(s*) = " + str(fs[fs_index_ordenado[-1]]))
print("Iter - Melhor_Iter = " + str(itera) + "-" + str(melhor_i) + " > BTMax")
