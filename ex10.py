#area = largura*altura
#tinta = area/2

largura = float( input("DIgite a largura da parede em metros: "))
altura = float( input("Digite a altura da parede em metros"))
area = largura*altura
print("A area da parede e de: {}".format(area))

print("Para pintar a oaarede sao necessarias {} latas de tinta. ".format(area/2))
