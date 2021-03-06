

def classificar(direcao, velocidade, Matrix, contador_direcoes, somatorio_velocidades_dir, contador_beaufort, vazio, vazio2, calmaria, vel_negativa):
 
 if 0<=direcao<=360 and 0<=velocidade<75:
    if (direcao <= 11.25) or (direcao > 348.75):  #N   
         contador_direcoes[0]+=1
         somatorio_velocidades_dir[0]+=velocidade
    elif(direcao > 11.25) and (direcao <= 33.75):  #NNE
         contador_direcoes[1]+=1
         somatorio_velocidades_dir[1]+=velocidade
    elif(direcao > 33.75) and (direcao <= 56.25):  #NE
         contador_direcoes[2]+=1
         somatorio_velocidades_dir[2]+=velocidade
    elif(direcao > 56.25) and (direcao <= 78.25):  #ENE
         contador_direcoes[3]+=1
         somatorio_velocidades_dir[3]+=velocidade
    elif(direcao > 78.25) and (direcao <= 101.25): #E
         contador_direcoes[4]+=1
         somatorio_velocidades_dir[4]+=velocidade
    elif(direcao > 101.25) and (direcao <= 123.75): #ESE
         contador_direcoes[5]+=1
         somatorio_velocidades_dir[5]+=velocidade
    elif(direcao > 123.75) and (direcao <= 146.25): #SE
         contador_direcoes[6]+=1
         somatorio_velocidades_dir[6]+=velocidade
    elif(direcao > 146.25) and (direcao <= 168.75): #SSE
         contador_direcoes[7]+=1
         somatorio_velocidades_dir[7]+=velocidade
    elif(direcao > 168.75) and (direcao <= 191.25):  #S
         contador_direcoes[8]+=1
         somatorio_velocidades_dir[8]+=velocidade
    elif(direcao > 191.25) and (direcao <= 213.75):  #SSO
         contador_direcoes[9]+=1
         somatorio_velocidades_dir[9]+=velocidade
    elif(direcao > 213.75) and (direcao <= 236.25):  #SO
         contador_direcoes[10]+=1
         somatorio_velocidades_dir[10]+=velocidade
    elif(direcao > 236.25) and (direcao <= 258.75):  #OSO
         contador_direcoes[11]+=1
         somatorio_velocidades_dir[11]+=velocidade
    elif(direcao > 258.75) and (direcao <= 281.25):  #O
         contador_direcoes[12]+=1
         somatorio_velocidades_dir[12]+=velocidade
    elif(direcao > 281.25) and (direcao <= 303.75):  #ONO
         contador_direcoes[13]+=1
         somatorio_velocidades_dir[13]+=velocidade
    elif(direcao > 303.75) and (direcao <= 326.25):  #NO
         contador_direcoes[14]+=1
         somatorio_velocidades_dir[14]+=velocidade
    elif(direcao > 326.25) and (direcao <= 348.75):  #NNO
         contador_direcoes[15]+=1
         somatorio_velocidades_dir[15]+=velocidade
 elif 360<direcao:			#encontra as direcoes que sao maiores que 360
     valor_direcao_impossivel=+1
     #linha_dir=linha_dir  + col[0] + ',' + str(direcao)
     #saida_dir.writelines(linha_dir)  
 elif velocidade==0 and direcao!=-999:
     calmaria=calmaria+1

###############################################################################
#
# 		SECAO VELOCIDADE NA ESCALA BEAUFORT
#
##############################################################################
 if 0<=direcao<=360 and 0<=velocidade<75:
  if velocidade<=0.3:
    contador_beaufort[0]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[0][0]=Matrix[0][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[0][15]=Matrix[0][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[0][14]=Matrix[0][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[0][13]=Matrix[0][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[0][12]=Matrix[0][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[0][11]=Matrix[0][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[0][10]=Matrix[0][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[0][9]=Matrix[0][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[0][8]=Matrix[0][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[0][7]=Matrix[0][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[0][6]=Matrix[0][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[0][5]=Matrix[0][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[0][4]=Matrix[0][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[0][3]=Matrix[0][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[0][2]=Matrix[0][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[0][1]=Matrix[0][1]+1
  elif 0.3<velocidade<=1.5:
    contador_beaufort[1]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[1][0]=Matrix[1][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[1][15]=Matrix[1][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[1][14]=Matrix[1][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[1][13]=Matrix[1][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[1][12]=Matrix[1][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[1][11]=Matrix[1][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[1][10]=Matrix[1][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[1][9]=Matrix[1][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[1][8]=Matrix[1][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[1][7]=Matrix[1][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[1][6]=Matrix[1][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[1][5]=Matrix[1][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[1][4]=Matrix[1][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[1][3]=Matrix[1][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[1][2]=Matrix[1][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[1][1]=Matrix[1][1]+1
  elif 1.5<velocidade<=3.3:
    contador_beaufort[2]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[2][0]=Matrix[2][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[2][15]=Matrix[2][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[2][14]=Matrix[2][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[2][13]=Matrix[2][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[2][12]=Matrix[2][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[2][11]=Matrix[2][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[2][10]=Matrix[2][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[2][9]=Matrix[2][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[2][8]=Matrix[2][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[2][7]=Matrix[2][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[2][6]=Matrix[2][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[2][5]=Matrix[2][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[2][4]=Matrix[2][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[2][3]=Matrix[2][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[2][2]=Matrix[2][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[2][1]=Matrix[2][1]+1
  elif 3.3<velocidade<=5.4:
    contador_beaufort[3]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[3][0]=Matrix[3][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[3][15]=Matrix[3][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[3][14]=Matrix[3][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[3][13]=Matrix[3][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[3][12]=Matrix[3][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[3][11]=Matrix[3][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[3][10]=Matrix[3][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[3][9]=Matrix[3][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[3][8]=Matrix[3][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[3][7]=Matrix[3][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[3][6]=Matrix[3][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[3][5]=Matrix[3][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[3][4]=Matrix[3][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[3][3]=Matrix[3][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[3][2]=Matrix[3][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[3][1]=Matrix[3][1]+1
  elif 5.4<velocidade<=7.9:
    contador_beaufort[4]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[4][0]=Matrix[4][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[4][15]=Matrix[4][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[4][14]=Matrix[4][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[4][13]=Matrix[4][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[4][12]=Matrix[4][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[4][11]=Matrix[4][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[4][10]=Matrix[4][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[4][9]=Matrix[4][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[4][8]=Matrix[4][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[4][7]=Matrix[4][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[4][6]=Matrix[4][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[4][5]=Matrix[4][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[4][4]=Matrix[4][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[4][3]=Matrix[4][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[4][2]=Matrix[4][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[4][1]=Matrix[4][1]+1   
  elif 7.9<velocidade<=10.7:
    contador_beaufort[5]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[5][0]=Matrix[5][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[5][15]=Matrix[5][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[5][14]=Matrix[5][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[5][13]=Matrix[5][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[5][12]=Matrix[5][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[5][11]=Matrix[5][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[5][10]=Matrix[5][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[5][9]=Matrix[5][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[5][8]=Matrix[5][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[5][7]=Matrix[5][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[5][6]=Matrix[5][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[5][5]=Matrix[5][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[5][4]=Matrix[5][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[5][3]=Matrix[5][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[5][2]=Matrix[5][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[5][1]=Matrix[5][1]+1
  elif 10.7<velocidade<=13.8:
    contador_beaufort[6]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[6][0]=Matrix[6][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[6][15]=Matrix[6][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[6][14]=Matrix[6][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[6][13]=Matrix[6][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[6][12]=Matrix[6][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[6][11]=Matrix[6][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[6][10]=Matrix[6][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[6][9]=Matrix[6][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[6][8]=Matrix[6][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[6][7]=Matrix[6][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[6][6]=Matrix[6][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[6][5]=Matrix[6][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[6][4]=Matrix[6][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[6][3]=Matrix[6][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[6][2]=Matrix[6][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[6][1]=Matrix[6][1]+1
  elif 13.8<velocidade<=17.1:
    contador_beaufort[7]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[7][0]=Matrix[7][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[7][15]=Matrix[7][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[7][14]=Matrix[7][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[7][13]=Matrix[7][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[7][12]=Matrix[7][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[7][11]=Matrix[7][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[7][10]=Matrix[7][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[7][9]=Matrix[7][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[7][8]=Matrix[7][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[7][7]=Matrix[7][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[7][6]=Matrix[7][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[7][5]=Matrix[7][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[7][4]=Matrix[7][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[7][3]=Matrix[7][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[7][2]=Matrix[7][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[7][1]=Matrix[7][1]+1
  elif 17.1<velocidade<=20.7:
    contador_beaufort[8]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[8][0]=Matrix[8][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[8][15]=Matrix[8][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[8][14]=Matrix[8][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[8][13]=Matrix[8][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[8][12]=Matrix[8][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[8][11]=Matrix[8][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[8][10]=Matrix[8][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[8][9]=Matrix[8][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[8][8]=Matrix[8][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[8][7]=Matrix[8][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[8][6]=Matrix[8][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[8][5]=Matrix[8][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[8][4]=Matrix[8][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[8][3]=Matrix[8][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[8][2]=Matrix[8][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[8][1]=Matrix[8][1]+1
  elif 20.7<velocidade<=24.4:
    contador_beaufort[9]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[9][0]=Matrix[9][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[9][15]=Matrix[9][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[9][14]=Matrix[9][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[9][13]=Matrix[9][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[9][12]=Matrix[9][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[9][11]=Matrix[9][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[9][10]=Matrix[9][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[9][9]=Matrix[9][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[9][8]=Matrix[9][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[9][7]=Matrix[9][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[9][6]=Matrix[9][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[9][5]=Matrix[9][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[9][4]=Matrix[9][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[9][3]=Matrix[9][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[9][2]=Matrix[9][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[9][1]=Matrix[9][1]+1
  elif 24.4<velocidade<=28.4:
    contador_beaufort[10]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[10][0]=Matrix[10][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[10][15]=Matrix[10][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[10][14]=Matrix[10][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[10][13]=Matrix[10][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[10][12]=Matrix[10][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[10][11]=Matrix[10][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[10][10]=Matrix[10][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[10][9]=Matrix[10][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[10][8]=Matrix[10][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[10][7]=Matrix[10][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[10][6]=Matrix[10][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[10][5]=Matrix[10][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[10][4]=Matrix[10][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[10][3]=Matrix[10][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[10][2]=Matrix[10][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[10][1]=Matrix[10][1]+1
  elif 28.4<velocidade<=32.6:
    contador_beaufort[11]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[11][0]=Matrix[11][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[11][15]=Matrix[11][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[11][14]=Matrix[11][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[11][13]=Matrix[11][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[11][12]=Matrix[11][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[11][11]=Matrix[11][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[11][10]=Matrix[11][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[11][9]=Matrix[11][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[11][8]=Matrix[11][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[11][7]=Matrix[11][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[11][6]=Matrix[11][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[11][5]=Matrix[11][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[11][4]=Matrix[11][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[11][3]=Matrix[11][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[11][2]=Matrix[11][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[11][1]=Matrix[11][1]+1
  elif velocidade>32.6:
    contador_beaufort[12]+=1
    if direcao <= 11.25 or direcao > 348.75:
      Matrix[12][0]=Matrix[12][0]+1
    elif(direcao > 11.25) and (direcao <= 33.75):
      Matrix[12][15]=Matrix[12][15]+1
    elif(direcao > 33.75) and (direcao <= 56.25):
      Matrix[12][14]=Matrix[12][14]+1
    elif(direcao > 56.25) and (direcao <= 78.25):
      Matrix[12][13]=Matrix[12][13]+1
    elif(direcao > 78.25) and (direcao <= 101.25):
      Matrix[12][12]=Matrix[12][12]+1
    elif(direcao > 101.25) and (direcao <= 123.75):
      Matrix[12][11]=Matrix[12][11]+1
    elif(direcao > 123.75) and (direcao <= 146.25):
      Matrix[12][10]=Matrix[12][10]+1
    elif(direcao > 146.25) and (direcao <= 168.75):
      Matrix[12][9]=Matrix[12][9]+1
    elif(direcao > 168.75) and (direcao <= 191.25):
      Matrix[12][8]=Matrix[12][8]+1
    elif(direcao > 191.25) and (direcao <= 213.75):
      Matrix[12][7]=Matrix[12][7]+1
    elif(direcao > 213.75) and (direcao <= 236.25):
      Matrix[12][6]=Matrix[12][6]+1
    elif(direcao > 236.25) and (direcao <= 258.75):
      Matrix[12][5]=Matrix[12][5]+1
    elif(direcao > 258.75) and (direcao <= 281.25):
      Matrix[12][4]=Matrix[12][4]+1
    elif(direcao > 281.25) and (direcao <= 303.75):
      Matrix[12][3]=Matrix[12][3]+1
    elif(direcao > 303.75) and (direcao <= 326.25):
      Matrix[12][2]=Matrix[12][2]+1
    elif(direcao > 326.25) and (direcao <= 348.75):
      Matrix[12][1]=Matrix[12][1]+1
  elif velocidade<0:
       vel_negativa=vel_negativa +1

 return Matrix, contador_direcoes, somatorio_velocidades_dir, contador_beaufort, vazio, vazio2, calmaria, vel_negativa

