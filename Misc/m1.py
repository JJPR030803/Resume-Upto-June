segundos = 129800
segs_dia = 1440 *60

segundos_restantes = segundos%segs_dia
horas = (segundos_restantes)//(60*60)
mins = (segundos_restantes//60)%60
segs = segundos%60


formatted_horas = f"{horas:02}"
formatted_mins = f"{mins:02}"
formatted_segs = f"{segs:02}"


#print(f"{formatted_horas}:{formatted_mins}:{formatted_segs}")
print(bin(segundos) == bin(int))