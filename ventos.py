# -*- coding: utf-8 -*-
##################################### GOAMet-Ventos#############################################
#                                                                                              #
#    Modulo  para classificar e plotar os dados de ventos  #   
#                                                                                              #
################################################################################################
#____________________________________________________________________________________
#             Faça o que tu queres, há de ser tudo da lei!
#GOAMet-Ventos, do GOA, é um aplicativo distribuído sob a A Licença Pública Geral do GNU (CC-GNU GPL).
#Direitos do usuário:
#Resumidamente: executar, estudar, redistribuir e aperfeiçoar o programa.
#Deveres do usuário: resumidamente, redistribuir as alterações porventura realizadas juntamente com uma cópia da licença; distribuir as #alterações incluindo o código-fonte correspondente completo.
#Esse aplicativo não tem nenhuma garantia.
#Veja a licença completa:
#https://creativecommons.org/licenses/GPL/2.0/legalcode.pt

###############################################################################
#Ventos foi criado na linguagem Python e usa as seguintes bibliotecas:
# MatPlotLib
# Numpy
# ConfigParser
###############################################################################

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from classificar import classificar
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from datetime import *
import ConfigParser

###############################################################################
#carrega os parametros de configuraçoes do arquivo config.ini
###############################################################################
try:
 cfg = ConfigParser.ConfigParser()
 cfg.read('config.ini')
 nome_estacao= cfg.get('geral', 'nome_estacao')
 titulo_graf= cfg.get('geral', 'titulo_graf')
 f_data = cfg.get('datas', 'config_data')
 f_vel = cfg.get('unidades', 'config_velocidade') 
 f_div_col= cfg.get('unidades', 'div_col')
 f_fuso = cfg.getint('unidades', 'fuso_horario')
 col_data= cfg.getint('colunas', 'col_data')
 col_horario= cfg.getint('colunas', 'col_horario')
 col_vel= cfg.getint('colunas', 'col_vel')
 col_dir= cfg.getint('colunas', 'col_direcao')
except:
  print "Erro carregando arquivo de configuração inicial (config.ini). Pode ser alguma propriedade mal definida ou faltando"

#Abre o arquivo com os dados de entrada
try:
  dados=open('dados.csv','r')  #Aqui entra o nome do arquivo que contém os dados, que deve estar localizado no mesmo diretório do aplicativo
except:
  print "Erro ao tentar abrir arquivo de dados. Verifique se o arquivo nomeado dados.csv existe."

hoje= date.today() #time.strftime('%x%x%Z') 
hoje= hoje.isoformat()
saida=open("Médias-parâmetros" +hoje+".txt", "w")

vazio=0
vazio2=0
contador=0
linhas=0
vel_negativa=0
valor_direcao_impossivel=0
calmaria=0

cont_dir=0.
cont_vel=0.

u=[]
v=[]
E_O=[]
N_S=[]
lista_vel=[]

vel_med=[0. for j in range(16)]
lista_vel_diaria=[0. for j in range(24)]
lista_dir_diaria_x=[0. for j in range(24)]
lista_dir_diaria_y=[0. for j in range(24)]
theta_horario=[0. for j in range(24)]
contador_vel_diaria=[0 for j in range(24)]
media_vel_diaria=[0. for j in range(24)]
media_dir_diaria=[0. for j in range(24)]

lista_horarios=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

contador_media=0

contador_direcoes=[0. for x in range(16)]
somatorio_velocidades_dir=[0. for x in range(16)]
contador_beaufort=[0. for x in range(13)]

Matrix = [[0. for x in range(16)] for x in range(13)]

etiquetas_dir=('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSO', 'SO', 'OSO', 'O', 'ONO', 'NO', 'NNO')
etiquetas_beaufort=('B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12')

##############################################################################
#			SEÇÃO FUNÇÕES
##############################################################################

lista_pos_data=[] # lista gerada pela funcao "def_col_data" com as posições da colunas de inicio e fim do ano e mes, respectivamente (4 itens).

def def_col_data(formato_data):
	if formato_data == "aaaa/mm/dd": 
	  col_ano_inicio=0
	  col_ano_fim=4
	  col_mes_inicio=5
	  col_mes_fim=7
	elif formato_data == "dd/mm/aa":
	  col_ano_inicio=6
	  col_ano_fim=8
	  col_mes_inicio=3
	  col_mes_fim=5
	elif formato_data == "dd/mm/aaaa":
	  col_ano_inicio=6
	  col_ano_fim=10
	  col_mes_inicio=3
	  col_mes_fim=5
	elif formato_data == "aa/mm/dd":
	  col_ano_inicio=0
	  col_ano_fim=2
	  col_mes_inicio=3
	  col_mes_fim=5
	return col_ano_inicio, col_ano_fim, col_mes_inicio, col_mes_fim

lista_pos_data = def_col_data(f_data)

#Seleciona os filtros desejados
print 'Para utilizar os dados de apenas um determinado mês, digite o número do mês desejado. (O nome do mês será incluso nos títulos dos gráficos): \n(digite 0 para o período completo | digite 13 se for anual)' 
mes_fornecido=input()
ano_fornecido=''
if mes_fornecido==13:
 print 'Digite qual o ano desejado:'
 ano_fornecido=input()              
elif mes_fornecido>13:
 raise "Erro - Digite um número entre 0 e 13"

#Lê as linhas do arquivo de entrada
for linha in dados.readlines(): 
 linhas=linhas+1
 
 # Define qual o caracter separa os campos, ou colunas, no arquivo de entrada. Padrao "|"
 col=linha.split(f_div_col)           
 
 # Atribui qual a coluna contem cada campo.
 data=col[col_data]		 # campo data
 horario=col[col_horario]	 # campo hora
 velocidade=col[col_vel]         # campo velocidade   
 direcao=col[col_dir]            # campo direçao   

 try:                           #verifica se existe a direcao
    if direcao!='':
     direcao=float(direcao)
    else:
     direcao=-999
 except:
    vazio=vazio+1	        #contagem das dir. estranhas ou vazias
    direcao=-999

 try:   #verifica se existe a velocidade transforma em m/s, caso nao esteja
   if f_vel == 'km/h':
     velocidade=float(velocidade)/3.6
   else:
     velocidade=float(velocidade)
 except:
   vazio2+=1 	        #contagem das vel. estranhas ou vazias
   velocidade=-999
 if velocidade==0.0:
   calmaria+=1

 try: # intervalo onde está impresso o horario                          
    horario_coluna=horario[0:2]
    horario_coluna=str(horario_coluna)
 except:
    horario_coluna='NULL'
 
 try: # intervalo (colunas) onde está gravado mês
    mes_coluna=data[lista_pos_data[2]:lista_pos_data[3]]
    mes_coluna=int(mes_coluna)
 except:
    mes_coluna='NULL'

 try: # intervalo (colunas) onde está gravado mês
    ano_coluna=data[lista_pos_data[0]:lista_pos_data[1]]
    ano_coluna=int(ano_coluna)
 except:
    ano_coluna=''

#Entra na função 'classificar' que separa os dados de acordo com a velocidade e direção do vento 
 if mes_fornecido==0:
  classificar(direcao, velocidade, Matrix, contador_direcoes, somatorio_velocidades_dir, contador_beaufort, vazio, vazio2, calmaria, vel_negativa)
 elif mes_fornecido==13:
  if ano_coluna==ano_fornecido:
   classificar(direcao, velocidade, Matrix, contador_direcoes, somatorio_velocidades_dir, contador_beaufort, vazio, vazio2, calmaria, vel_negativa)
 elif mes_coluna==mes_fornecido:
  classificar(direcao, velocidade, Matrix, contador_direcoes, somatorio_velocidades_dir, contador_beaufort, vazio, vazio2, calmaria, vel_negativa)


#Decompoe a direcao e velocidade do Vento, escalar e vetorial
 if 0<=velocidade<75 and 0<=direcao<=360: 
  u.append(velocidade*mt.sin(mt.radians(direcao)))
  v.append(velocidade*mt.cos(mt.radians(direcao)))
  E_O.append(mt.sin(mt.radians(direcao)))
  N_S.append(mt.cos(mt.radians(direcao)))
  contador_media+=1
  lista_vel.append(velocidade)

#Soma o perfil ou ciclo diário da velocidade e decompoe a direcao media
 for j in range(24):
  if 0<=velocidade<75:
   if horario_coluna==lista_horarios[j]:
    lista_vel_diaria[j]+=velocidade
    contador_vel_diaria[j]+=1
  if 0<=direcao<=360:
   if horario_coluna==lista_horarios[j]:
    lista_dir_diaria_x[j]+=velocidade*mt.sin(mt.radians(direcao))
    lista_dir_diaria_y[j]+=velocidade*mt.cos(mt.radians(direcao))

#Calcula a velocidade vetorial e o angulo medio de todo o periodo 
V_E_O=sum(u)/contador_media
V_N_S=sum(v)/contador_media
V_med=mt.sqrt(V_E_O**2+V_N_S**2)
alfa=mt.degrees(mt.atan2(V_E_O,V_N_S))

# Calcula o perfil diurno da direcao e velocidade media
for j in range(24):
  media_vel_diaria[j]=lista_vel_diaria[j]/contador_vel_diaria[j]
  theta_horario[j]= mt.degrees(mt.atan2(lista_dir_diaria_x[j], lista_dir_diaria_y[j]))
  if theta_horario[j]<0:
    #print "theta horairo ", j, theta_horario[j]
    theta_horario[j] = theta_horario[j] +360

#Calcula a velocidade e o angulo medio escalar de todo o periodo 
V_med_arit=sum(lista_vel)/contador_media
D_E_O=sum(E_O)/contador_media
D_N_S=sum(N_S)/contador_media
beta=mt.degrees(mt.atan2(D_E_O,D_N_S))

cont_dir=sum(contador_direcoes)
cont_vel=sum(contador_beaufort)


###############################################################################
#                                                                     
#                          Secao impressões 
#
###############################################################################

print "\nlinhas com direcao estranha :", vazio
print "\nlinhas com velocidade estranha :", vazio2
print "\nlinhas com velocidade negativa :", vel_negativa

print "\n\nnumero de linhas lidos:", linhas

print "Direções contabilizadas: ", cont_dir
print "Velocidades contabilizadas: ",cont_vel, "\n"

print '\nCalmaria (v=0) -> ', calmaria, "\n"

saida.write('Direção | Contagem | Porcentagem \n')
for i in range(16):
 nd=str(etiquetas_dir[i])
 cd=str(contador_direcoes[i])
 pct=str(round(100*contador_direcoes[i]/cont_dir,1))
 line=[nd, '|', cd, '|', pct, "\n"]
 saida.writelines(line)
 

saida.write('\nCategoria | Contagem | Porcentagem \n')
for i in range(13):
 nb=str(etiquetas_beaufort[i])
 cb=str(contador_beaufort[i])
 pct2=str(round(100*contador_beaufort[i]/cont_vel,1))
 line=[ nb, '|', cb, '|', pct2, "\n"]
 saida.writelines(line)

saida.write("\nHora | Velocidade média | Direção média\n")
for i in range(24):
 hl=str(lista_horarios[i])
 vd=str(media_vel_diaria[i])
 dir_hora=str(theta_horario[i])
 line=[ hl, '|', vd, '|', dir_hora, "\n"]
 saida.writelines(line)

saida.writelines("\nVelocidade média por direção\n")
for x,y,z in zip(etiquetas_dir, somatorio_velocidades_dir, contador_direcoes): 
  if z==0:
   linha=[str(x),"|", str(0),"\n" ]
  else:
   linha=[str(x),"|", str(y/z),"\n" ]
  saida.writelines(linha)

saida.write('\nPorcentagem de dados aproveitados:\n')
pctd=str(100*cont_dir/linhas)
pctv=str(100*cont_vel/linhas)
line=['Direção: ', pctd, '\n', 'Velocidade: ', pctv, '\n']
saida.writelines(line)

''' 
refazer abaixo
for i in range(16):
  for j in range(13):
  linha = ["\nEscala B", str(j), ""]
   linha= str(Matrix[j][i])
   saida.writelines(linha)
'''

print "\nMédias Vetoriais do Vento"
print "Direção (°):   ", alfa
print "Magnitude da velocidade (m/s):   ", V_med
print "\nMédias escalares  do Vento:"
print "Direção (°):   ", beta
print "Média aritmética das velocidades (m/s):   ", V_med_arit
print "Desvio padrão da velocidade:  ", np.std(lista_vel)
direcaomedia=str(alfa)
velmedia=str(V_med)
direcaomedia2=str(beta)
velmedia2=str(V_med_arit)
desviopadrao=str(np.std(lista_vel))

parametros=["\n","Médias Vetoriais do Vento","\n","Direção (°):   ", direcaomedia, "\n", "Magnitude da velocidade (m/s):   ", velmedia,"\n\n", "Médias escalares  do Vento:","\n","Direção (°):   ", direcaomedia2, "\n","Média aritmética das velocidades (m/s):   ", velmedia2, "\n\n", "Desvio padrão da velocidade:  ", desviopadrao]

saida.writelines(parametros)

##########################################################
#                                                        #
#                    Seção gráficos                      #
#                                                        #
##########################################################

numero_barras_dir=16
numero_barras_vel=13

meses=['Período Completo', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', 'Anual']

           #médias vetoriais


plt.figure(4)               
ax = plt.subplot(111, polar=True)      # add subplot in polar coordinates 
ax.set_rmax(5)                         # r maximum value
ax.grid(True)				# add the grid
ax.set_theta_offset(mt.pi/2)          #gira os eixos  
ax.set_xticklabels(['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE'])              
arr1 = plt.arrow(-mt.radians(alfa)+mt.pi, 0, 0, V_med, length_includes_head=True, head_width=0.10, head_length=0.2, fc='k', ec='k')
if titulo_graf=='sim':
 plt.title('Média Vetorial - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' + str(ano_fornecido) )
plt.savefig("Média Vetorial - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)


plt.figure(5)
ax = plt.subplot(111, polar=True)      # add subplot in polar coordinates 
ax.set_rmax(6)                       # r maximum value
ax.grid(True) 				# add the grid
ax.set_theta_offset(mt.pi/2)
ax.set_xticklabels(['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE'])                            
arr1 = plt.arrow( -mt.radians(beta)+mt.pi, 0, 0, V_med_arit, length_includes_head=True, head_width=0.10, head_length=0.2, fc='k', ec='k')
#, alpha = 0.5, width = 0.015, edgecolor = 'black', facecolor = 'green', lw = 2, zorder = 5)
#ax.polar(Dir_med_norm, V_med_arit, color='Tomato', ls='--', lw=6)
if titulo_graf=='sim':
 plt.title('Média Escalar - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' + str(ano_fornecido) )
plt.savefig("Média Escalar - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)


#Perfil do vento
plt.figure(6)
plt.plot(media_vel_diaria)
plt.grid(True)
plt.xlim(0,23)
plt.ylim(0,9)
plt.xticks(np.arange(0,24,3), ('00', '03', '06', '09', '12', '15', '18', '21'))
plt.xlabel('Hora')
plt.ylabel('Velocidade (m/s)')
if titulo_graf=='sim':
 plt.title('Perfil diurno da velocidade do vento '+nome_estacao + ' - '+ meses[mes_fornecido] + '' + str(ano_fornecido) )
plt.savefig("Perfil diurno da velocidade do vento " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=120)


#Perfil diurno da direcao do vento
#p1=plt.bar(24, _direcao, 0.35, color='b')
plt.figure(7)
plt.plot(theta_horario, 'rD')
plt.grid(True)
plt.xlim(0,23)
plt.ylim(0,360,90)
plt.xticks(np.arange(0,24,3), ('00', '03', '06', '09', '12', '15', '18', '21'))
plt.yticks(np.arange(0,360,90) )
plt.ylabel('Direção (°)')
plt.xlabel('Hora')
if titulo_graf=='sim':
 plt.title('Perfil diurno da direção do vento '+nome_estacao + ' - '+ meses[mes_fornecido] + '' + str(ano_fornecido) )
plt.savefig("Perfil diurno da direção do vento -" + nome_estacao + " " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=120)


           #direcao em barras

porcentagem_direcao = [100*x/cont_dir for x in contador_direcoes]
ind = np.arange(numero_barras_dir)    # the x locations for the groups
largura = 0.35       # the width of the bars: can also be len(x) sequence

#plt.figure(1)
#p1=plt.bar(ind, porcentagem_direcao, largura, color='r')
#plt.ylabel('Porcentagem')
#plt.xlabel('Direção do vento')
#plt.xticks(ind + largura/2., etiquetas_dir)
#plt.yticks( np.arange(0,max(porcentagem_direcao)+5,5) )
#plt.title('Frequência da Direção do Vento - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' + str(ano_fornecido) )
#plt.savefig("Frequência da direção do vento em barra - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

               #velocidade em barras

var_graf_vel = [100*x/cont_vel for x in contador_beaufort] 
ind2 = np.arange(numero_barras_vel)    
largura = 0.35       

plt.figure(2)
p2=plt.bar(ind2, var_graf_vel, largura, color='g')
plt.ylabel('Porcentagem')
plt.xlabel('Índice de Beaufort')
if titulo_graf=='sim':
 plt.title('Frequência da Velocidade do Vento - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' +  str(ano_fornecido) )
plt.xticks(ind + largura/2., etiquetas_beaufort)
plt.yticks( np.arange(0,max(var_graf_vel)+5,5))
plt.savefig("Frequência da velocidade do vento escola Beaufort - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

                #velocidade Média em barras

for i,x,y in zip(range(16),somatorio_velocidades_dir,contador_direcoes):
  if y==0:
   vel_med[i]=0
  else: 
   vel_med[i]=x/y

#plt.figure(3)
#p1=plt.bar(ind, vel_med, largura, color='b')
#plt.ylabel('Velocidade (m/s)')
#plt.xlabel('Direcao do vento')
#plt.title('Velocidade Média para cada Direção - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' +  str(ano_fornecido) )
#plt.xticks(ind + largura/2., etiquetas_dir)
#plt.yticks( np.arange(0,max(vel_med)+1,1) )
#plt.savefig("Velocidade Média por direcao em barras - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

              #velocidade Média em radar

from radar import radar_graph

labels = ['N','NNO','NO','ONO','O','OSO','SO','SSO','S','SSE','SE','ESE','E','ENE','NE','NNE']
for i in range(8):
 vel_med[i+1], vel_med[15-i]=vel_med[15-i],vel_med[i+1]
radar_graph(labels, vel_med)
if titulo_graf=='sim':
 plt.title('Velocidade Média para Cada Direção (m/s) - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' +  str(ano_fornecido) )
plt.savefig("Velocidade Média por direcao radar - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

              #Distribuição da direcao do vento em radar
for i in range(8):
 porcentagem_direcao[i+1], porcentagem_direcao[15-i]=porcentagem_direcao[15-i],porcentagem_direcao[i+1]
radar_graph(labels, porcentagem_direcao)
if titulo_graf=='sim':
 plt.title('Frequência da Direção do Vento (%) - '+nome_estacao + ' - '+ meses[mes_fornecido] + '' +  str(ano_fornecido) )
plt.savefig("Frequência da direção do vento radar - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

             #Rosa dos ventos completa

from radarmodificado import radar_graph

labels = ['N','NNO','NO','ONO','O','OSO','SO','SSO','S','SSE','SE','ESE','E','ENE','NE','NNE']
valores0=[x*100/cont_dir for x in Matrix[0]]
valores1=[x*100/cont_dir for x in Matrix[1]]
valores2=[x*100/cont_dir for x in Matrix[2]]                                   
valores3=[x*100/cont_dir for x in Matrix[3]]
valores4=[x*100/cont_dir for x in Matrix[4]]
valores5=[x*100/cont_dir for x in Matrix[5]]
valores6=[x*100/cont_dir for x in Matrix[6]]
valores7=[x*100/cont_dir for x in Matrix[7]]
valores8=[x*100/cont_dir for x in Matrix[8]]
valores9=[x*100/cont_dir for x in Matrix[9]]
valores10=[x*100/cont_dir for x in Matrix[10]]
valores11=[x*100/cont_dir for x in Matrix[11]]
valores12=[x*100/cont_dir for x in Matrix[12]]
valores=[valores0,valores1,valores2,valores3,valores4,valores5,valores6,valores7,valores8,valores9,valores10,valores11,valores12]
radar_graph(labels, valores0, valores1, valores2,valores3,valores4,valores5,valores6,valores7,valores8,valores9,valores10,valores11,valores12)
if titulo_graf=='sim':
 plt.title('Rosa dos Ventos (%) - '+nome_estacao + ' - '+ meses[mes_fornecido])
legenda = ['B0 (0-0.3)', 'B1 (0.3-1.5)', 'B2 (1.5-3.3)', 'B3 (3.3-5.4)', 'B4 (5.4-7.9)', 'B5 (7.9-10.7)', 'B6 (10.7-13.8)', 'B7 (13.8-17.1)', 'B8 (17.1-20.7)', 'B9 (20.7-24.4)', 'B10 (24.4-28.4)', 'B11 (28.4-32.6)', 'B12 (>32.6)']
indices = [x for x,y in zip(legenda,valores) if y!=[0. for n in range(16)]]
#se tiver muitos indices, a legenda sobe, então, abaixo caso seja maior que 
if len(indices) >= 7: 
  posicao_y_titulo_legenda = 0.93
#  posicao_y_legenda = 0.25
elif len(indices) >= 4:
  posicao_y_titulo_legenda = 0.75
else:
  posicao_y_titulo_legenda = 0.65
legend = plt.legend(indices, loc=(1.05, .52), labelspacing=0.5)
plt.setp(legend.get_texts(), fontsize='medium')
plt.figtext(0.8, posicao_y_titulo_legenda, 'Escala de Beaufort (m/s)', fontdict=None)
plt.savefig("Rosa dos ventos - " + nome_estacao + " - " + meses[mes_fornecido] + '' +  str(ano_fornecido)  + ".png", dpi=100)

#plt.show()

dados.close()
saida.close()

