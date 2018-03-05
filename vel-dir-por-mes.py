# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math as mt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

dados=open('dados.csv','r') # le o arquivo de dados de entrada

contador=0
linhas=0

cont_vel=0
vel_vazia=0
dir_vazia=0

n_mes = [0 for i in range(12)]
soma_velocidade = [0. for i in range(12)]
u=[[] for i in range(12)]
v=[[] for i in range(12)]
E_O=[[] for i in range(12)]
N_S=[[] for i in range(12)]
contador_media=[0 for i in range(12)]
lista_vel=[[] for i in range(12)]

V_E_O=[0. for i in range(12)]
V_N_S=[0. for i in range(12)]
V_med=[0. for i in range(12)]
alfa=[0. for i in range(12)]
beta=[0. for i in range(12)]
V_med_arit=[0. for i in range(12)]
D_E_O=[0. for i in range(12)]
D_N_S=[0. for i in range(12)]

nome_meses=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

#print 'Digite qual o ano desejado:'
#ano_fornecido=input() 

for linha in dados.readlines(): 
 linhas=linhas+1
 col=linha.split(',')
 data=col[1] # posição do campo data
 velocidade=col[5] # posição do campo velocidade
 direcao=col[4] #posição do campo direção

 try:                           #verifica se existe a direcao
    direcao=float(direcao)
 except:
    dir_vazia+=1	        #contagem das dir. estranhas ou vazias
    direcao=-999

 try:
     velocidade=float(velocidade)
     cont_vel+=1
 except:
     vel_vazia+=+1         #contagem das temp. estranhas ou vazias
     velocidade=-999
 try:
    mes_coluna=int(data[5:7])
    ano_coluna=int(data[0:4])
 except:
    mes_coluna='NULL'

 
 #and ano_coluna==ano_fornecido
 if velocidade!=-999 and mes_coluna != 'NULL' and direcao!=-999:
     for k in range(1,13,1):
      if mes_coluna==k:  
         n_mes[k-1]+=1
         soma_velocidade[k-1]+=velocidade
         
         u[k-1].append(velocidade*mt.sin(mt.radians(direcao)))
         v[k-1].append(velocidade*mt.cos(mt.radians(direcao)))
         E_O[k-1].append(mt.sin(mt.radians(direcao)))
         N_S[k-1].append(mt.cos(mt.radians(direcao)))
         contador_media[k-1]+=1
         lista_vel[k-1].append(velocidade)


for k in range(12):
 if contador_media[k]!=0:
  V_E_O[k]=sum(u[k])/contador_media[k]
  V_N_S[k]=sum(v[k])/contador_media[k]
  V_med[k]=mt.sqrt(V_E_O[k]**2+V_N_S[k]**2)
  alfa[k]=mt.degrees(mt.atan2(V_E_O[k],V_N_S[k]))
  if alfa[k]<0:
   alfa[k]=alfa[k]+360
 


  V_med_arit[k]=sum(lista_vel[k])/contador_media[k]
  D_E_O[k]=sum(E_O[k])/contador_media[k]
  D_N_S[k]=sum(N_S[k])/contador_media[k]
  beta[k]=mt.degrees(mt.atan2(D_E_O[k],D_N_S[k]))
  if beta[k]<0:
   beta[k]=beta[k]+360
 

###############################################################################
#
#Secao impressoes
#
###############################################################################

#"+str(ano_fornecido)+"
saida=open("TabelaVelDirporMes.txt", "w")
saida.write('Mes| Vel media | Dir.media| Dir Media Norm \n')

for k in range(12): 
 if n_mes[k]!=0:
  nomemes=str(nome_meses[k])
  velmedia=str(round(soma_velocidade[k]/n_mes[k],2))
  dirmedia=str(int(alfa[k]))
  dirmedianorm=str(int(beta[k]))
  parametros=[nomemes,"|",velmedia,"|",dirmedia,"|",dirmedianorm,"\n"]
  saida.writelines(parametros)

saida.close()
dados.close()
