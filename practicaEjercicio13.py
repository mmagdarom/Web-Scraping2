Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def numeroprimo(numerop):
	if numerop < 2:
		return False
	for i in range(2,numerop):
		if (numerop%i)==0:
			return False
	return True;

>>> def seleccionarFuncion(numero):
	def listainversa(listain):
		listaInv = [];
		i = len(listain);
		while i <= len(listain):
			listaInv.append(listain[i-1:i])
			i = i-1
			if i==0: break
		return listaInv;
	def primosN(numeroN):
		listaN = [];
		for i in range(1,numeroN):
			if numeroprimo(i):
				listaN.append(i)
		return listaN;
	def tuplasMayuscula (tuplanom):
		listaTu = [];
		for i in range(0,len(tuplanom)):
			listaTu.append(tuplanom[i].upper())
		return listaTu;
	def convertirTuplaaLista(texto):
		listaEjem = list(texto);
		tuplaEjem = tuple(listaEjem);
		listaMayus = [];
		listaMayus = tuplasMayuscula(tuplaEjem);
		return listaMayus;
	def NumerosPares(listaNum):
		listaNuP = [];
		for i in range(0,len(listaNum)):
			if (i%2) == 0:
				listaNuP.append(listaNum[i:i+1])
		return listaNuP;
	functor_selefunc = {'1':listainversa(lista), '2':primosN(numeroN), '3':tuplasMayuscula (tuplanom), '4':convertirTuplaaLista(texto), '5':NumerosPares(listaNum)}
	return functor_selefunc[numero]

>>> lista = [1,2,3,4,5,6,7,8,9,10];
>>> numeroN = 30
>>> tuplanom = ('a','b','c','d','e','f');
>>> texto = 'ejemplo';
>>> listaNum = [6,7,8,9,10,11,12];
>>> f1 = seleccionarFuncion('1')
>>> f2 = seleccionarFuncion('2')
>>> f3 = seleccionarFuncion('3')
>>> f4 = seleccionarFuncion('4')
>>> f5 = seleccionarFuncion('5')
>>> f1
[[10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
>>> f2
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> f3
['A', 'B', 'C', 'D', 'E', 'F']
>>> f4
['E', 'J', 'E', 'M', 'P', 'L', 'O']
>>> f5
[[6], [8], [10], [12]]
>>> 
