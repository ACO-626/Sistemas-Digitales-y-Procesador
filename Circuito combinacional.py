#Sumador de cuatro dígitos para números binarios XXXX+YYYY

#Construyo función sumadora
def sumadorX4 (bin1,bin2,acarreo):
	resultado = int(bin1,2)+int(bin2,2)+int(acarreo,2);
	if int(bin(resultado),2)>int('1111',2):
		resultado=resultado-16;
		acarreo=1;
	else:
		acarreo=0;
	salida=(bin(resultado),acarreo)
	return salida;


bin1 = input("Numero binario 1: ");
bin2 = input("Numero binario 2: "); 
acarreo = input("Acarreo: ");
entrada = (bin1,bin2,acarreo);
print(sumadorX4(*entrada));
