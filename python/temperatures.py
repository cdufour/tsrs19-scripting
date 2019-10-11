# temperatures.py

temp = float(input('Saisir une température: '))

if temp > 40:
    print('Canicule')
elif temp > 30:
    print('Très chaud')
elif temp > 20:
    print('Chaud')
elif temp > 10:
    print('Tempéré')
elif temp > 5:
    print('Doux')
elif temp < -40:
    print('Glacial')
else:
    print('Froid')