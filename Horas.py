from collections import _OrderedDictKeysView


Hora=int(input("Introduza a(s) hora(s):"))
Minuto=int(input("Introduza o(s) minuto(s):"))
Duração=int(input("Introduza a duração do evento:"))
#uvycvvgyvgv
MT=Minuto+Duração
#fhbbryvburvrw
HF=Hora+(MT//60)
MF=MT%60
print()
print("Horas do final do evento: " + str(HF))
print("Minutos do final do evento: " + str(MT))
print()
print("Duração Total: " + str(Duração)+ " minutos.")