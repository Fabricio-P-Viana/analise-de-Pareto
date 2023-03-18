# ================================================================================================================================
#
# FATEC FERRAZ DE VASCONCELOS 2023
# ATIVIDADE : TABELA DE PARETO
# PROFESSOR : LUIZ CARLOS DOS SANTOS FILHO
# PROGRAMADORES:
# CINDY DOS SANTOS COIMBRA - RA 2920482121029
# FABRICIO PEREIRA VIANA - RA 292048222031
# KARINA OLIVEIRA NUNES - RA 2920482121031
#
# layout (tabela) ================================================================================================================

_= ("{}______{}".format('\033[4;34m', '\033[m')*23) #linhas
ESP = "     "*13 # espaço vazio
titulos =["TIPO","QUANTIDADE","PORCENTAGEM(%)","PORCENTAGEM ACUMULATIVA(%)"] #Titulos da lista

# lendo dados TXT ================================================================================================================

dados = open("dados.txt","r") # iniciando a leitura dos dados
Listageral=dados.readlines() # Lendo todos os arquivos TXT e adicionando numa lista
dados.close # fechando dados

# listas para organizar itens ===================================================================================================

listarstrip = [] # lista tirando os \n dos dados
listaespecifica =[] # lista com um exemplar de cada
listacont =[] # lista para contar quantidade de cada exemplar
porcentagem = [] # lista das porcentagens
porcentagemacumulativa =[] # lista das porcentagens acumulativas

# variaveis usadas ===============================================================================================================

total = 0 # total de ocorrências
acum = 0 # declarando valor inicial da porcentagem acumulativa

# Processos do programa ==========================================================================================================

# for para tirar os \n dos dados
for i in Listageral:
    listarstrip.append(i.rstrip())
    
# for para pegar um exemplar de cada
for i in set(listarstrip):
    listaespecifica.append(i)

# for para contar a quantidade de cada exemplar no arquivo TXT
totalporcent = 0
for i in listaespecifica:
    listacont.append(listarstrip.count(i))

# for para obter o total de itens
for i in listacont:
    total= total + i

# for para obter a porcentagem de cada exemplar
for i in listacont:
    porcentagem.append((i/total)*100)
porcentagem= sorted(porcentagem, reverse=True)

#for para obter a porcentagem acumulativa de cada exemplar
for i in porcentagem:
    totalporcent= totalporcent+i 

#for para obter a total da porcentagem
for i in porcentagem:
    acum = acum+i
    porcentagemacumulativa.append(acum)
porcentagemacumulativa= sorted(porcentagemacumulativa, reverse=False)

# utlizando lambda para ordenar de forma correta as informações
listactudo= []
for i in range(0,len(listaespecifica)):
    listavazia = []
    listavazia.append(listaespecifica[i])
    listavazia.append(listacont[i])
    listactudo.append(listavazia)
listactudo2 = sorted(listactudo, key= lambda l : l[1], reverse= True)

# TABELA DE PARETO ========================================================================================================

# PARTE DE CIMA TITULOS E CATEGORIAS
print("%s\n\n%sTABELA DE PARETO\n%s" %(_,ESP,_))
print()
print('{:^50} | {:^20} | {:^20} | {:^30}  '.format(*titulos))
print(_)

# MEIO DA LISTA, PASSANDO O FOR PARA PERCORRER TODOS OS ITENS
for i in range(0, len(listaespecifica)):
    
    # ADICIONANDO NUMA LISTA QUE ZERA ACADA CICLO PARA USAR O .FORMAT
    tabelainfo = []
    tabelainfo.append(listactudo2[i][0])
    tabelainfo.append(listactudo2[i][1])
    tabelainfo.append(porcentagem[i])
    tabelainfo.append(porcentagemacumulativa[i])

    # PRINTANDO AQUI
    print()
    print('{:^50} | {:^20} | {:^20.2f} | {:^30.2f}  '.format(*tabelainfo))
    print(_)

# FIM DA TABELA COM TOTAIS E CONCLUSÃO

print()
tabelafim =[ "TOTAL", total, totalporcent, "-"]
print('{:^50} | {:^20} | {:^20} | {:^30}  '.format(*tabelafim))
print(_)
print("\nCONCLUSÃO DA ANÁLISE\n")
print("foi observado que a maior causa de incidentes é por conta da %s com %.2f porcento o ponto onde devemos repensar \ne tratar com uma solução mais cudadosa, e 80 porcento de procentagem acumulativa das causas foram por conta de:" %(listactudo2[0][0],porcentagem[0]))
print("\n1. %s --- %.2f\n2. %s --- %.2f\n3. %s --- %.2f" %(listactudo2[0][0],porcentagemacumulativa[0],listactudo2[1][0],porcentagemacumulativa[1],listactudo2[2][0],porcentagemacumulativa[2]))
print(_)

#===================================================================================================================