from Silla import Silla 
SILLAS_EJECUTIVAS = 8
SILLAS_ECONOMICAS = 42
sillasEjecutivas = []
sillasEconomicas = []

for i in range(1, SILLAS_ECONOMICAS + 1):
    if i % 3 == 1:
        sillasEconomicas.append(Silla(i, True, 'ventana'))
    elif i % 3 == 2:
        sillasEconomicas.append(Silla(i, True, 'centro'))
    else:
        sillasEconomicas.append(Silla(i, True, 'pasillo'))

print (sillasEconomicas[6])