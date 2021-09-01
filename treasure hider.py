#Hiding the treasure basic coding excercise
row1=['A','B','C']
row2=['A1','B1','C1']
row3=['A2','B2','C2']
# above are the 3 lists where we gonna put X

mapOfTreasure=[row1,row2,row3]
#above is a list[list[Strings]] list of Static lists of Static Strings

print(f'{row1}\n{row2}\n{row3}')

row= input("in which row do you want to put treasure :")
col= input("in which column do you want to put treasure :")

horizontal=int(row[0])
vertical=int(col[0])

mapOfTreasure[horizontal-1][vertical-1]='X'
#putting X in the map of treasures 

print(f'{row1}\n{row2}\n{row3}')
#After putting the X 