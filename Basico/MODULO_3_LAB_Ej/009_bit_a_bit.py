#Diferencia entre operaciones logicas y bit a bit

i= 15 # 00000000000000000000000000001111
j= 22 # 00000000000000000000000000010110

log = i and j
print(log)

k=16
l=15 # 00000000000000000000000000001111
#~l    11111111111111111111111111110000

log_neg = not k
print(log_neg) #False

bit_neg = ~l  #Negacion
print(bit_neg)