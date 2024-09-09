nome = 'pedro'
altura = 1.83
peso = 84
imc = peso / (altura * altura)

print(nome,'tem', altura,'de altura',)
print('peso', peso,'quilos e seu imc é',)
print(imc)

#Exemple

exemplo = f'{nome} tem {altura:,.2f} de altura com o peso de {peso}'
string = 'nome={} tem altura={} de altura com o peso de peso={}'
formato = string.format(nome, altura, peso)
#print("Parabéns "+nome+", seu "+peso+" está na media")

print("Parabéns "+nome+", seu "+peso+" está na media")