# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('uma distância em metros: '))
centímetro = medida * 100
milímetro = medida * 1000
print('a média de {}m corresponde a {}cm e {}mm'.format(medida, centímetro, milímetro))