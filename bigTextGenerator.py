
#Matan Kedar 
#3/5/20

#code is limited to only 20 characters 

print('Enter phrase:')
w = input()
word = w.lower()
list(word)

length = len(word) 
letters = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],                    
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]



  
letters[1][0]   ='         '
letters[1][1]   ='         '
letters[1][2]   ='         '
letters[1][3]   =' 8888b.  '
letters[1][4]   ='   "88b  '
letters[1][5]   ='.d888888 '
letters[1][6]   ='888  888 '
letters[1][7]   ='"Y888888 '
letters[1][8]   ='         '
letters[1][9]   ='         '
letters[1][10]  ='         '

letters[2][0]  ='888      '
letters[2][1]  ='888      '
letters[2][2]  ='888      '
letters[2][3]  ='88888b.  '
letters[2][4]  ='888 "88b '
letters[2][5]  ='888  888 '
letters[2][6]  ='888 d88P '
letters[2][7]  ='88888P"  '
letters[2][8]  ='         '
letters[2][9]  ='         '
letters[2][10] ='         '

letters[3][0]  ='         '
letters[3][1]  ='         '
letters[3][2]  ='         '         
letters[3][3]  =' .d8888b ' 
letters[3][4]  ='d88P"    '
letters[3][5]  ='888      '
letters[3][6]  ='Y88b.    '
letters[3][7]  =' "Y8888P '
letters[3][8]  ='         '
letters[3][9]  ='         '
letters[3][10] ='         '         
         
letters[4][0]  ='     888 '
letters[4][1]  ='     888 '
letters[4][2]  ='     888 '         
letters[4][3]  =' .d88888 ' 
letters[4][4]  ='d88" 888 '
letters[4][5]  ='888  888 '
letters[4][6]  ='Y88b 888 '
letters[4][7]  =' "Y88888 '
letters[4][8]  ='         '
letters[4][9]  ='         '
letters[4][10] ='         '       
         
letters[5][0]  ='         '
letters[5][1]  ='         '
letters[5][2]  ='         '         
letters[5][3]  =' .d88b.  ' 
letters[5][4]  ='d8P  Y8b '
letters[5][5]  ='88888888 '
letters[5][6]  ='Y8b.     '
letters[5][7]  =' "Y8888  '
letters[5][8]  ='         '
letters[5][9]  ='         '
letters[5][10] ='         '       
         
letters[6][0]  =' .d8888 '
letters[6][1]  ='d88P"   '
letters[6][2]  ='888     '         
letters[6][3]  ='888888  ' 
letters[6][4]  ='888     '
letters[6][5]  ='888     '
letters[6][6]  ='888     '
letters[6][7]  ='888     '
letters[6][8]  ='        '
letters[6][9]  ='        '
letters[6][10] ='        '     
       
letters[7][0]  ='         '
letters[7][1]  ='         '
letters[7][2]  ='         '         
letters[7][3]  =' .d88b.  ' 
letters[7][4]  ='d88P"88b '
letters[7][5]  ='888  888 '
letters[7][6]  ='Y88b 888 '
letters[7][7]  =' "Y88888 '
letters[7][8]  ='     888 '
letters[7][9]  ='Y8b d88P '
letters[7][10]  =' "Y88P"  '     
         
letters[8][0]  ='888      '
letters[8][1]  ='888      '
letters[8][2]  ='888      '         
letters[8][3]  ='88888b.  ' 
letters[8][4]  ='888 "88b '
letters[8][5]  ='888  888 '
letters[8][6]  ='888  888 '
letters[8][7]  ='888  888 '
letters[8][8]  ='         '
letters[8][9]  ='         '
letters[8][10]  ='         ' 
         
letters[9][0]  ='d8b '
letters[9][1]  ='q8P '         
letters[9][2]  ='    ' 
letters[9][3]  ='888 '
letters[9][4]  ='888 '
letters[9][5]  ='888 '
letters[9][6]  ='888 '
letters[9][7]  ='888 '
letters[9][8]  ='    '
letters[9][9]  ='    '
letters[9][10] ='    ' 
         
letters[10][0]  ='   d8b '
letters[10][1]  ='   Y8P '
letters[10][2]  ='       '         
letters[10][3]  ='  8888 ' 
letters[10][4]  ='  "888 '
letters[10][5]  ='   888 '
letters[10][6]  ='   888 '
letters[10][7]  ='   888 '
letters[10][8]  ='   888 '
letters[10][9]  ='  d88P '
letters[10][10] ='888P"  ' 

letters[11][0]  ='888      '
letters[11][1]  ='888      '         
letters[11][2]  ='888      ' 
letters[11][3]  ='888  888 '
letters[11][4]  ='888 .88P '
letters[11][5]  ='888888K  '
letters[11][6]  ='888 "88b '
letters[11][7]  ='888  888 '
letters[11][8]  ='         '
letters[11][9]  ='         '
letters[11][10] ='         ' 

letters[12][0]  ='888 '
letters[12][1]  ='888 '         
letters[12][2]  ='888 ' 
letters[12][3]  ='888 '
letters[12][4]  ='888 '
letters[12][5]  ='888 '
letters[12][6]  ='888 '
letters[12][7]  ='888 '
letters[12][8]  ='    '
letters[12][9]  ='    '
letters[12][10] ='    ' 

letters[13][0]  ='              '
letters[13][1]  ='              '
letters[13][2]  ='              '         
letters[13][3]  ='88888b.d88b.  ' 
letters[13][4]  ='888 "888 "88b '
letters[13][5]  ='888  888  888 '
letters[13][6]  ='888  888  888 '
letters[13][7]  ='888  888  888 '
letters[13][8]  ='              '
letters[13][9]  ='              ' 
letters[13][10] ='              '    

letters[14][0]  ='         '
letters[14][1]  ='         '
letters[14][2]  ='         '         
letters[14][3]  ='88888b.  ' 
letters[14][4]  ='888 "88b '
letters[14][5]  ='888  888 '
letters[14][6]  ='888  888 '
letters[14][7]  ='888  888 '
letters[14][8]  ='         '
letters[14][9]  ='         ' 
letters[14][10] ='         ' 

letters[15][0]  ='         '
letters[15][1]  ='         '
letters[15][2]  ='         '         
letters[15][3]  =' .d88b.  ' 
letters[15][4]  ='d88""88b '
letters[15][5]  ='888  888 '
letters[15][6]  ='Y88..88P '
letters[15][7]  =' "Y88P"  '
letters[15][8]  ='         '
letters[15][9]  ='         ' 
letters[15][10] ='         ' 

letters[16][0]  ='         '
letters[16][1]  ='         '         
letters[16][2]  ='         ' 
letters[16][3]  ='88888b.  '
letters[16][4]  ='888 "88b '
letters[16][5]  ='888  888 '
letters[16][6]  ='888 d88P '
letters[16][7]  ='88888P"  '
letters[16][8]  ='888      '
letters[16][9]  ='888      '
letters[16][10] ='888      ' 

letters[17][0]  ='         '
letters[17][1]  ='         '         
letters[17][2]  ='         ' 
letters[17][3]  =' .d88888 '
letters[17][4]  ='d88" 888 '
letters[17][5]  ='888  888 '
letters[17][6]  ='Y88b 888 '
letters[17][7]  =' "Y88888 '
letters[17][8]  ='     888 '
letters[17][9]  ='     888 '
letters[17][10] ='     888 '

letters[18][0]  ='        '
letters[18][1]  ='        '
letters[18][2]  ='        '         
letters[18][3]  ='888d888 ' 
letters[18][4]  ='888P"   '
letters[18][5]  ='888     '
letters[18][6]  ='888     '
letters[18][7]  ='888     '
letters[18][8]  ='        '
letters[18][9]  ='        ' 
letters[18][10] ='        ' 

letters[19][0]  ='         '
letters[19][1]  ='         '
letters[19][2]  ='         '         
letters[19][3]  ='.d8888b  ' 
letters[19][4]  ='88K      '
letters[19][5]  ='"Y8888b. '
letters[19][6]  ='     X88 '
letters[19][7]  ='88888P"  '
letters[19][8]  ='         '
letters[19][9]  ='         ' 
letters[19][10] ='         '

letters[20][0]  ='888    '
letters[20][1]  ='888    '
letters[20][2]  ='888    '         
letters[20][3]  ='888888 ' 
letters[20][4]  ='888    '
letters[20][5]  ='888    '
letters[20][6]  ='Y88b.  '
letters[20][7]  =' "Y888 '
letters[20][8]  ='       '
letters[20][9]  ='       ' 
letters[20][10] ='       ' 

letters[21][0]  ='         '
letters[21][1]  ='         '
letters[21][2]  ='         '         
letters[21][3]  ='888  888 ' 
letters[21][4]  ='888  888 '
letters[21][5]  ='888  888 '
letters[21][6]  ='Y88b 888 '
letters[21][7]  =' "Y88888 '
letters[21][8]  ='         '
letters[21][9]  ='         ' 
letters[21][10] ='         ' 

letters[22][0]  ='         '
letters[22][1]  ='         '
letters[22][2]  ='         '         
letters[22][3]  ='888  888 ' 
letters[22][4]  ='888  888 '
letters[22][5]  ='Y88  88P '
letters[22][6]  =' Y8bd8P  '
letters[22][7]  ='  Y88P   '
letters[22][8]  ='         '
letters[22][9]  ='         ' 
letters[22][10] ='         ' 

letters[23][0]  ='              '
letters[23][1]  ='              '
letters[23][2]  ='              '
letters[23][3]  ='888  888  888 ' 
letters[23][4]  ='888  888  888 '
letters[23][5]  ='888  888  888 '
letters[23][6]  ='Y88b 888 d88P '
letters[23][7]  =' "Y8888888P"  '
letters[23][8]  ='              '
letters[23][9]  ='              ' 
letters[23][10] ='              ' 

letters[24][0]  ='         '
letters[24][1]  ='         '
letters[24][2]  ='         '
letters[24][3]  ='888  888 ' 
letters[24][4]  ='`Y8bd8P" '
letters[24][5]  ='  X88K   '
letters[24][6]  ='.d8""8b. '
letters[24][7]  ='888  888 '
letters[24][8]  ='         '
letters[24][9]  ='         ' 
letters[24][10] ='         ' 

letters[25][0]  ='         '
letters[25][1]  ='         '
letters[25][2]  ='         '
letters[25][3]  ='888  888 ' 
letters[25][4]  ='888  888 '
letters[25][5]  ='888  888 '
letters[25][6]  ='Y88b 888 '
letters[25][7]  =' "Y88888 '
letters[25][8]  ='     888 '
letters[25][9]  ='Y8b d88P ' 
letters[25][10] =' "Y88P"  ' 

letters[26][0]  ='         '
letters[26][1]  ='         '
letters[26][2]  ='         '
letters[26][3]  ='88888888 ' 
letters[26][4]  ='   d88P  '
letters[26][5]  ='  d88P   '
letters[26][6]  =' d88P    '
letters[26][7]  ='88888888 '
letters[26][8]  ='         '
letters[26][9]  ='         ' 
letters[26][10] ='         ' 

letters[27][0]  ='         '           
letters[27][1]  ='         '    
letters[27][2]  ='         '    
letters[27][3]  ='         '    
letters[27][4]  ='         '    
letters[27][5]  ='         '    
letters[27][6]  ='         '    
letters[27][7]  ='         '    
letters[27][8]  ='         '    
letters[27][9]  ='         '    
letters[27][10] ='         '  

letters[28][0]  ='     '           
letters[28][1]  ='     '    
letters[28][2]  ='     '    
letters[28][3]  ='     '    
letters[28][4]  ='     '    
letters[28][5]  ='     '    
letters[28][6]  ='d8b  '    
letters[28][7]  ='Y8P  '     
letters[28][8]  ='     '    
letters[28][9]  ='     '    
letters[28][10] ='     ' 

letters[29][0]  ='    '           
letters[29][1]  ='    '    
letters[29][2]  ='    '    
letters[29][3]  ='d8b '    
letters[29][4]  ='Y8P '    
letters[29][5]  ='    '    
letters[29][6]  ='d8b '    
letters[29][7]  ='88P '    
letters[29][8]  ='8P  '    
letters[29][9]  ='"   '    
letters[29][10] ='    '  

letters[30][0]  ='    '           
letters[30][1]  ='    '    
letters[30][2]  ='    '    
letters[30][3]  ='    '    
letters[30][4]  ='    '    
letters[30][5]  ='    '    
letters[30][6]  ='d8b '    
letters[30][7]  ='88P '    
letters[30][8]  ='8P  '    
letters[30][9]  ='"   '    
letters[30][10] ='    '  

letters[31][0]  ='88 88 '           
letters[31][1]  ='8P 8P '    
letters[31][2]  ='"  "  '    
letters[31][3]  ='      '    
letters[31][4]  ='      '    
letters[31][5]  ='      '    
letters[31][6]  ='      '     
letters[31][7]  ='      '    
letters[31][8]  ='      '    
letters[31][9]  ='      '    
letters[31][10] ='      ' 

letters[32][0]  ='8888888 '           
letters[32][1]  ='888     '    
letters[32][2]  ='888     '    
letters[32][3]  ='888     '    
letters[32][4]  ='888     '    
letters[32][5]  ='888     '    
letters[32][6]  ='888     '     
letters[32][7]  ='8888888 '    
letters[32][8]  ='        '    
letters[32][9]  ='        '    
letters[32][10] ='        ' 

letters[33][0]  ='8888888 '           
letters[33][1]  ='    888 '    
letters[33][2]  ='    888 '    
letters[33][3]  ='    888 '    
letters[33][4]  ='    888 '    
letters[33][5]  ='    888 '    
letters[33][6]  ='    888 '     
letters[33][7]  ='8888888 '    
letters[33][8]  ='        '    
letters[33][9]  ='        '    
letters[33][10] ='        ' 

letters[34][0]  ='   d88P '           
letters[34][1]  ='  d88P  '    
letters[34][2]  =' d88P   '    
letters[34][3]  ='d88P    '    
letters[34][4]  ='Y88b    '    
letters[34][5]  =' Y88b   '    
letters[34][6]  ='  Y88b  '     
letters[34][7]  ='   Y88b '    
letters[34][8]  ='        '    
letters[34][9]  ='        '    
letters[34][10] ='        ' 

letters[35][0]  ='Y88b    '           
letters[35][1]  =' Y88b   '    
letters[35][2]  ='  Y88b  '    
letters[35][3]  ='   Y88b '    
letters[35][4]  ='   d88P '    
letters[35][5]  ='  d88P  '    
letters[35][6]  =' d88P   '     
letters[35][7]  ='d88P    '    
letters[35][8]  ='        '    
letters[35][9]  ='        '    
letters[35][10] ='        ' 

letters[36][0]  =' .d8888b.  '           
letters[36][1]  ='d88P  Y88b '    
letters[36][2]  ='     .d88P '    
letters[36][3]  ='   .d88P"  '    
letters[36][4]  ='   888"    '    
letters[36][5]  ='   888     '    
letters[36][6]  ='           '     
letters[36][7]  ='   888     '    
letters[36][8]  ='           '    
letters[36][9]  ='           '    
letters[36][10] ='           ' 

letters[37][0]  ='Y88b        '           
letters[37][1]  =' Y88b       '    
letters[37][2]  ='  Y88b      '    
letters[37][3]  ='   Y88b     '    
letters[37][4]  ='    Y88b    '    
letters[37][5]  ='     Y88b   '    
letters[37][6]  ='      Y88b  '     
letters[37][7]  ='       Y88b '    
letters[37][8]  ='            '    
letters[37][9]  ='            '    
letters[37][10] ='            ' 

letters[38][0]  ='       d88P '           
letters[38][1]  ='      d88P  '    
letters[38][2]  ='     d88P   '    
letters[38][3]  ='    d88P    '    
letters[38][4]  ='   d88P     '    
letters[38][5]  ='  d88P      '    
letters[38][6]  =' d88P       '     
letters[38][7]  ='d88P        '    
letters[38][8]  ='            '    
letters[38][9]  ='            '    
letters[38][10] ='            ' 

letters[39][0]  ='    '           
letters[39][1]  ='    '    
letters[39][2]  ='    '    
letters[39][3]  ='d8b '    
letters[39][4]  ='Y8P '    
letters[39][5]  ='    '    
letters[39][6]  ='d8b '    
letters[39][7]  ='Y8P '     
letters[39][8]  ='    '    
letters[39][9]  ='    '    
letters[39][10] ='    ' 

letters[40][0]  ='888 '           
letters[40][1]  ='888 '    
letters[40][2]  ='888 '    
letters[40][3]  ='888 '    
letters[40][4]  ='888 '    
letters[40][5]  ='Y8P '    
letters[40][6]  ='d8b '    
letters[40][7]  =' "  '     
letters[40][8]  ='888 '    
letters[40][9]  ='    '    
letters[40][10] ='    ' 

letters[41][0]  =' d888   '           
letters[41][1]  ='d8888   '    
letters[41][2]  ='  888   '    
letters[41][3]  ='  888   '    
letters[41][4]  ='  888   '    
letters[41][5]  ='  888   '    
letters[41][6]  ='  888   '    
letters[41][7]  ='8888888 '     
letters[41][8]  ='        '    
letters[41][9]  ='        '    
letters[41][10] ='        '  

letters[42][0]  =' .d8888b.  '           
letters[42][1]  ='d88P  Y88b '    
letters[42][2]  ='       888 '    
letters[42][3]  ='     .d88P '    
letters[42][4]  =' .od888P"  '    
letters[42][5]  ='d88P"      '    
letters[42][6]  ='888"       '    
letters[42][7]  ='888888888  '     
letters[42][8]  ='           '    
letters[42][9]  ='           '    
letters[42][10] ='           '  

letters[43][0]  =' .d8888b.  '           
letters[43][1]  ='d88P  Y88b '    
letters[43][2]  ='     .d88P '    
letters[43][3]  ='    8888"  '    
letters[43][4]  ='     "Y8b. '    
letters[43][5]  ='888    888 '    
letters[43][6]  ='Y88b  d88P '    
letters[43][7]  =' "Y8888P"  '     
letters[43][8]  ='           '    
letters[43][9]  ='           '    
letters[43][10] ='           '  

letters[44][0]  ='    d8888  '           
letters[44][1]  ='   d8P888  '    
letters[44][2]  ='  d8P 888  '    
letters[44][3]  =' d8P  888  '    
letters[44][4]  ='d88   888  '    
letters[44][5]  ='8888888888 '   
letters[44][6]  ='      888  '    
letters[44][7]  ='      888  '     
letters[44][8]  ='           '    
letters[44][9]  ='           '    
letters[44][10] ='           '  

letters[45][0]  ='888888888  '           
letters[45][1]  ='888        '    
letters[45][2]  ='888        '    
letters[45][3]  ='8888888b.  '    
letters[45][4]  ='     "Y88b '    
letters[45][5]  ='       888 '   
letters[45][6]  ='Y88b  d88P '    
letters[45][7]  =' "Y8888P"  '     
letters[45][8]  ='           '    
letters[45][9]  ='           '    
letters[45][10] ='           '  

letters[46][0]  =' .d8888b.  '           
letters[46][1]  ='d88P  Y88b '    
letters[46][2]  ='888        '    
letters[46][3]  ='888d888b.  '    
letters[46][4]  ='888P "Y88b '    
letters[46][5]  ='888    888 '   
letters[46][6]  ='Y88b  d88P '    
letters[46][7]  =' "Y8888P"  '     
letters[46][8]  ='           '    
letters[46][9]  ='           '    
letters[46][10] ='           ' 

letters[47][0]  ='8888888888 '           
letters[47][1]  ='      d88P '    
letters[47][2]  ='     d88P  '    
letters[47][3]  ='    d88P   '    
letters[47][4]  =' 88888888  '    
letters[47][5]  ='  d88P     '   
letters[47][6]  =' d88P      '    
letters[47][7]  ='d88P       '     
letters[47][8]  ='           '    
letters[47][9]  ='           '    
letters[47][10] ='           ' 

letters[48][0]  =' .d8888b.  '           
letters[48][1]  ='d88P  Y88b '    
letters[48][2]  ='Y88b. d88P '    
letters[48][3]  =' "Y88888"  '    
letters[48][4]  ='.d8P""Y8b. '    
letters[48][5]  ='888    888 '   
letters[48][6]  ='Y88b  d88P '    
letters[48][7]  =' "Y8888P"  '     
letters[48][8]  ='           '    
letters[48][9]  ='           '    
letters[48][10] ='           ' 

letters[49][0]  =' .d8888b.  '           
letters[49][1]  ='d88P  Y88b '    
letters[49][2]  ='888    888 '    
letters[49][3]  ='Y88b. d888 '    
letters[49][4]  =' "Y888P888 '    
letters[49][5]  ='       888 '   
letters[49][6]  ='Y88b  d88P '    
letters[49][7]  =' "Y8888P"  '     
letters[49][8]  ='           '    
letters[49][9]  ='           '    
letters[49][10] ='           '

letters[50][0]  =' .d8888b.  '           
letters[50][1]  ='d88P  Y88b '    
letters[50][2]  ='888    888 '    
letters[50][3]  ='888    888 '    
letters[50][4]  ='888    888 '    
letters[50][5]  ='888    888 '   
letters[50][6]  ='Y88b  d88P '    
letters[50][7]  =' "Y8888P"  '     
letters[50][8]  ='           '    
letters[50][9]  ='           '    
letters[50][10] ='           '

letters[51][0]  =' .d8888888b.  '           
letters[51][1]  ='d88P"   "Y88b '    
letters[51][2]  ='888  d8b  888 '    
letters[51][3]  ='888  888  888 '    
letters[51][4]  ='888  888bd88P '    
letters[51][5]  ='888  Y8888P"  '   
letters[51][6]  ='Y88b.     .d8 '    
letters[51][7]  =' "Y88888888P" '     
letters[51][8]  ='              '    
letters[51][9]  ='              '    
letters[51][10] ='              '

letters[52][0]  ='  888  888   '           
letters[52][1]  ='  888  888   '    
letters[52][2]  ='888888888888 '    
letters[52][3]  ='  888  888   '    
letters[52][4]  ='  888  888   '    
letters[52][5]  ='888888888888 '   
letters[52][6]  ='  888  888   '    
letters[52][7]  ='  888  888   '     
letters[52][8]  ='             '    
letters[52][9]  ='             '    
letters[52][10] ='             '

letters[53][0]  ='     88     '           
letters[53][1]  =' .d88888b.  '    
letters[53][2]  ='d88P 88"88b '    
letters[53][3]  ='Y88b.88     '    
letters[53][4]  =' "Y88888b.  '    
letters[53][5]  ='     88"88b '   
letters[53][6]  ='Y88b 88.88P '    
letters[53][7]  =' "Y88888P"  '     
letters[53][8]  ='     88     '    
letters[53][9]  ='            '    
letters[53][10] ='            '

letters[54][0]  ='d88b   d88P '           
letters[54][1]  ='Y88P  d88P  '    
letters[54][2]  ='     d88P   '    
letters[54][3]  ='    d88P    '    
letters[54][4]  ='   d88P     '    
letters[54][5]  ='  d88P      '   
letters[54][6]  =' d88P  d88b '    
letters[54][7]  ='d88P   Y88P '     
letters[54][8]  ='            '    
letters[54][9]  ='            '    
letters[54][10] ='            '

letters[55][0]  ='    o    '           
letters[55][1]  ='   d8b   '    
letters[55][2]  ='  d888b  '    
letters[55][3]  =' d8P"Y8b '    
letters[55][4]  ='         '    
letters[55][5]  ='         '   
letters[55][6]  ='         '    
letters[55][7]  ='         '     
letters[55][8]  ='         '    
letters[55][9]  ='         '    
letters[55][10] ='         '

letters[56][0]  =' .d8888b.      '           
letters[56][1]  ='d88P  "88b     '    
letters[56][2]  ='Y88b. d88P     '    
letters[56][3]  =' "Y8888P"      '    
letters[56][4]  ='.d88P88K.d88P  '     
letters[56][5]  ='888"  Y888P"   '   
letters[56][6]  ='Y88b .d8888b   '    
letters[56][7]  =' "Y8888P" Y88b '     
letters[56][8]  ='               '    
letters[56][9]  ='               '    
letters[56][10] ='               '

letters[57][0]  ='              '                
letters[57][1]  ='      o       '    
letters[57][2]  ='     d8b      '    
letters[57][3]  ='    d888b     '    
letters[57][4]  ='"Y888888888P" '     
letters[57][5]  ='  "Y88888P"   '   
letters[57][6]  ='  d88P"Y88b   '    
letters[57][7]  =' dP"     "Yb  '     
letters[57][8]  ='              '    
letters[57][9]  ='              '    
letters[57][10] ='              '

letters[58][0]  ='  .d88 '                
letters[58][1]  =' d88P" '    
letters[58][2]  ='d88P   '    
letters[58][3]  ='888    '    
letters[58][4]  ='888    '     
letters[58][5]  ='Y88b   '   
letters[58][6]  =' Y88b. '    
letters[58][7]  ='  "Y88 '     
letters[58][8]  ='       '    
letters[58][9]  ='       '    
letters[58][10] ='       '

letters[59][0]  ='88b.   '                
letters[59][1]  ='"Y88b  '    
letters[59][2]  ='  Y88b '    
letters[59][3]  ='   888 '    
letters[59][4]  ='   888 '     
letters[59][5]  ='  d88P '   
letters[59][6]  ='.d88P  '    
letters[59][7]  ='88P"   '     
letters[59][8]  ='       '    
letters[59][9]  ='       '    
letters[59][10] ='       '

letters[60][0]  ='       '                
letters[60][1]  ='       '          
letters[60][2]  ='       '    
letters[60][3]  ='       '    
letters[60][4]  ='       '     
letters[60][5]  ='888888 '   
letters[60][6]  ='       '    
letters[60][7]  ='       '     
letters[60][8]  ='       '    
letters[60][9]  ='       '    
letters[60][10] ='       '

letters[61][0]  ='         '                
letters[61][1]  ='         '          
letters[61][2]  ='         '    
letters[61][3]  ='         '    
letters[61][4]  ='         '     
letters[61][5]  ='         '   
letters[61][6]  ='         '    
letters[61][7]  ='88888888 '     
letters[61][8]  ='         '    
letters[61][9]  ='         '    
letters[61][10] ='         '

letters[62][0]  ='        '                
letters[62][1]  ='        '          
letters[62][2]  ='        '    
letters[62][3]  ='  888   '    
letters[62][4]  ='8888888 '     
letters[62][5]  ='  888   '   
letters[62][6]  ='        '    
letters[62][7]  ='        '     
letters[62][8]  ='        '    
letters[62][9]  ='        '    
letters[62][10] ='        '

letters[63][0]  ='       '                
letters[63][1]  ='       '          
letters[63][2]  ='       '    
letters[63][3]  ='888888 '    
letters[63][4]  ='       '     
letters[63][5]  ='888888 '   
letters[63][6]  ='       '    
letters[63][7]  ='       '     
letters[63][8]  ='       '    
letters[63][9]  ='       '    
letters[63][10] ='       '

letters[64][0]  ='  888  '                
letters[64][1]  ='  888  '          
letters[64][2]  ='  888  '    
letters[64][3]  ='  888  '    
letters[64][4]  ='       '     
letters[64][5]  ='  888  '   
letters[64][6]  ='  888  '    
letters[64][7]  ='  888  '     
letters[64][8]  ='  888  '    
letters[64][9]  ='       '    
letters[64][10] ='       '



def findNumber(word):
    for z in range(0, 1):
        if word[z].find('a') == 0:
            return 1
        if word[z].find('b') == 0:
            return 2
        if word[z].find('c') == 0:
            return 3
        if word[z].find('d') == 0:
            return 4
        if word[z].find('e') == 0:
            return 5
        if word[z].find('f') == 0:
            return 6
        if word[z].find('g') == 0:
            return 7
        if word[z].find('h') == 0:
            return 8
        if word[z].find('i') == 0:
            return 9
        if word[z].find('j') == 0:
            return 10
        if word[z].find('k') == 0:
            return 11
        if word[z].find('l') == 0:
            return 12
        if word[z].find('m') == 0:
            return 13
        if word[z].find('n') == 0:
            return 14
        if word[z].find('o') == 0:
            return 15
        if word[z].find('p') == 0:
            return 16
        if word[z].find('q') == 0:
            return 17
        if word[z].find('r') == 0:
            return 18
        if word[z].find('s') == 0:
            return 19
        if word[z].find('t') == 0:
            return 20
        if word[z].find('u') == 0:
            return 21
        if word[z].find('v') == 0:
            return 22
        if word[z].find('w') == 0:
            return 23
        if word[z].find('x') == 0:
            return 24
        if word[z].find('y') == 0:
            return 25
        if word[z].find('z') == 0:
            return 26
        if word[z].find(' ') == 0:
            return 27
        if word[z].find('.') == 0:
            return 28
        if word[z].find(';') == 0:
            return 29
        if word[z].find(',') == 0:
            return 30
        if word[z].find('"') == 0:
            return 31
        if word[z].find('[') == 0:
            return 32
        if word[z].find(']') == 0:
            return 33
        if word[z].find('<') == 0:
            return 34
        if word[z].find('>') == 0:
            return 35
        if word[z].find('?') == 0:
            return 36
        if word[z].find('\\') == 0:
            return 37
        if word[z].find('/') == 0:
            return 38
        if word[z].find(':') == 0:
            return 39
        if word[z].find('!') == 0:
            return 40
        if word[z].find('1') == 0:
            return 41
        if word[z].find('2') == 0:
            return 42
        if word[z].find('3') == 0:
            return 43
        if word[z].find('4') == 0:
            return 44
        if word[z].find('5') == 0:
            return 45
        if word[z].find('6') == 0:
            return 46
        if word[z].find('7') == 0:
            return 47
        if word[z].find('8') == 0:
            return 48
        if word[z].find('9') == 0:
            return 49
        if word[z].find('0') == 0:
            return 50
        if word[z].find('@') == 0:
            return 51
        if word[z].find('#') == 0:
            return 52
        if word[z].find('$') == 0:
            return 53
        if word[z].find('%') == 0:
            return 54
        if word[z].find('^') == 0:
            return 55
        if word[z].find('&') == 0:
            return 56
        if word[z].find('*') == 0:
            return 57
        if word[z].find('(') == 0:
            return 58
        if word[z].find(')') == 0:
            return 59
        if word[z].find('-') == 0:
            return 60
        if word[z].find('_') == 0:
            return 61
        if word[z].find('+') == 0:
            return 62
        if word[z].find('=') == 0:
            return 63
        if word[z].find('|') == 0:
            return 64

def printText(letters, word, length):
    
    print(' ')
    print(' ')

    # there is probably a better way to this 

    for x in range(0, 10):
        if length == 1:
           print(letters[findNumber(word[0])][x])
        if length == 2:
            print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x])  
        if length == 3:
            print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x])  
        if length == 4:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x])  
        if length == 5:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x])  
        if length == 6:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x])
        if length == 7:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x]) 
        if length == 8:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x]
            + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x]) 
        if length == 9:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x]) 
        if length == 10:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x])
        if length == 11:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x]  + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x]) 
        if length == 12:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x]  + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]) 
        if length == 13:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x]) 
        if length == 14:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x])
        if length == 15:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x])

        if length == 16:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x] + letters[findNumber(word[15])][x])           
        if length == 17:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x] + letters[findNumber(word[15])][x]
           + letters[findNumber(word[16])][x])
        if length == 18:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x] + letters[findNumber(word[15])][x]
           + letters[findNumber(word[16])][x] + letters[findNumber(word[17])][x])
        if length == 19:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x] + letters[findNumber(word[15])][x]
           + letters[findNumber(word[16])][x] + letters[findNumber(word[17])][x] + letters[findNumber(word[18])][x])
        if length == 20:
           print(letters[findNumber(word[0])][x] + letters[findNumber(word[1])][x] + letters[findNumber(word[2])][x] + letters[findNumber(word[3])][x] 
           + letters[findNumber(word[4])][x] + letters[findNumber(word[5])][x] + letters[findNumber(word[6])][x] + letters[findNumber(word[7])][x] + 
           letters[findNumber(word[8])][x] + letters[findNumber(word[9])][x]  + letters[findNumber(word[10])][x] + letters[findNumber(word[11])][x]
           + letters[findNumber(word[12])][x] + letters[findNumber(word[13])][x] + letters[findNumber(word[14])][x] + letters[findNumber(word[15])][x]
           + letters[findNumber(word[16])][x] + letters[findNumber(word[17])][x] + letters[findNumber(word[18])][x] + letters[findNumber(word[19])][x])
        




printText(letters, word, length)
