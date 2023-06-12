# CREANDO UN CONJUNTO CON set()
conjunto = set(["dato-1","dato-2"])

# COMO METER UN CONJUNTO DENTRO DE OTRO CONJUNTO (DEBE SER FROZENSETS (CONJUNTOS CCONGELADOS))
conjunto1 = frozenset(["dato-3","dato-4"])
conjunto2 = set(["dato-5",conjunto1])

# TEORIA DE CONJUNTOS
conjunto1 = {1,2,5,7}
conjunto2 = {1,2,7}

# VERIFICANDO SI ES UN SUBCONJUNTO
resultado = conjunto2.issubset(conjunto1)

# VERIFICANDO SI ES UN SUPERCONJUNTO
resultado2 = conjunto1.issuperset(conjunto2)

# VERIFICAR SI HAY ALGUN NUMERO EN COMUN (SOLO SERA TRUE CUANDO NO TENGA NADA EN COMUN)
resultado3 = conjunto1.isdisjoint(conjunto2)
