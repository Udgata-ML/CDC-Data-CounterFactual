
# importing pandas
import pandas as pd

# read text file into pandas DataFrame
df_csv1= pd.read_csv("/home/satyajit/Downloads/Delivery_data/part01",header=None)

print(len(df_csv1))




'''



data_list=[]


# Adding all the arrays to the list




for i in range(len(df_csv1)):
  data_list.append(df_csv1[0][i].split())


# print(len(data_list)) 


a=df_csv1[0][0].replace(" ","")  

b=df_csv1[0][1].replace(" ","")  


for i in data_list:
	print(len(df_csv1[0][i].replace(" ","")))
	
'''	


# Creating a data list for storing all the rows in form of string and then split the string into a list

string_list=[] 
len_list=[] 


for i in range(len(df_csv1)): 
	a=df_csv1[0][i].replace(" ","") 
	# print(len(a))  
	string_list.append(a)
	len_list.append(len(a))
	
	
#	if len(a)==275:
		# print(a)   
#		string_list.append(a)
#	if len(a)==273:
# 		string_list.append(a)
		
# print(len(string_list))
# print(len(len_list))



def unique(list1):
	#initialize a null list
	unique_list=[]
	# traverse for all the elements
	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	for x in unique_list:
		print(x)
				
# print(unique(len_list)) 

# Converting the 275 length of the list to .txt file . 


list_273=[]
list_274=[]
list_275=[]
list_276=[]
list_277=[]
list_278=[]



# for i in string_list:
	# print(len(i)) 



# print(string_list[-1])  
print(len(string_list[-1]))



#print(len(list_273))
#print(len(list_274))
#print(len(list_275))
#print(len(list_276))
#print(len(list_277)) 
#print(len(list_278))


























'''
columns=[]
length=[]

value_list=[]







for i in range(len(df_csv1)):
  if len(df_csv1[0][i].replace(" ",""))==275:
    value=[]

    a=df_csv1[0][i].replace(" ","")

    # length.append(4)
    value.append(a[0:4])

    # values.append(data_list[0][0][0:4])


    length.append(2)
    # values.append(data_list[0][0][4:6])
    value.append(a[4:6])


    length.append(4)
    # values.append(data_list[0][1][0:4])
    value.append(a[6:10])


    length.append(1)
    # values.append(data_list[0][1][4:5])
    value.append(a[10:11])


    length.append(1)
    # values.append(data_list[0][2][0])
    value.append(a[11:12])


    length.append(1)
    # values.append(data_list[0][2][1])
    value.append(a[12:13])


    length.append(1)
    # values.append(data_list[0][3])
    value.append(a[13:14])

    # columns.append('Mother Age Imputed')
    # length.append(1)
    # a[14:15]

    # columns.append('Reported Age of Mother Used Flag')
    # length.append(1)
    # a[15:16]




    # length.append(2)
    value.append(a[14:16])

    # values.append(data_list[0][4][0:2])


    length.append(2)
    value.append(a[16:18])
    # values.append(data_list[0][4][2:4])


    length.append(1)
    value.append(a[18:19])
    # values.append(data_list[0][4][4:5])


    length.append(1)
    value.append(a[19:20])
    # values.append(data_list[0][5])


    length.append(1)
    value.append(a[20:21])
    # values.append(data_list[0][6][0])


    length.append(2)
    value.append(a[21:23])
    # values.append(data_list[0][6][1:3])


    length.append(2)
    # len=1
    value.append(a[23:25])
    # values.append(data_list[0][6][3:4])




    length.append(2)
    value.append(a[25:27])
    # values.append(data_list[0][6][4:7])


    # length.append(1)
    value.append(a[27:28])


    length.append(1)
    value.append(a[28:29])

    # values.append(data_list[0][7])



    # columns.append('Mother’s Hispanic Origin Recode')
    # length.append(1)
    # a[29:30]
    # values.append(data_list[0][8][0])

    # columns.append('Reporting Flag for Mother’s Origin')
    # length.append(1)
    # a[30:31]
    # values.append(data_list[0][8][1])


    length.append(1)
    value.append(a[29:30])
    # values.append(data_list[0][8][2])

    # data_list[0][9]


    length.append(1)
    value.append(a[30:31])
    # values.append(data_list[0][9][0])


    length.append(1)
    value.append(a[31:32])
    # values.append(data_list[0][9][1])




    length.append(1)
    value.append(a[32:33])



    # columns.append('Reporting Flag for Paternity Acknowledged')
    # length.append(1)
    # a[33:34]




    length.append(1)
    value.append(a[33:34])




    length.append(1)
    value.append(a[34:35])



    # data_list[0][12]

    # columns.append('Father’s Reported Age Used')
    # length.append(1)
    # # values.append(data_list[0][12][0:2])
    # a[35:36]


    length.append(2)
    value.append(a[35:37])


    length.append(2)
    # values.append(data_list[0][12][2:4])
    value.append(a[37:39])


    length.append(2)
    # values.append(data_list[0][12][4:6])
    value.append(a[39:41])


    length.append(1)
    # values.append(data_list[0][12][6])
    value.append(a[41:42])


    length.append(2)
    # values.append(data_list[0][12][7:9])
    value.append(a[42:44])

    # data_list[0][13]


    length.append(1)
    value.append(a[44:45])

    # values.append(data_list[0][13][0])


    length.append(1)
    value.append(a[45:46])
    # values.append(data_list[0][13][1])


    length.append(1)
    value.append(a[46:47])
    # values.append(data_list[0][13][2])


    length.append(1)
    # values.append(data_list[0][13][3])
    value.append(a[47:48])


    length.append(1)
    # values.append(data_list[0][13][4])
    value.append(a[48:49])


    length.append(1)
    # values.append(data_list[0][14])
    value.append(a[49:50])


    length.append(2)
    # values.append(data_list[0][15][0:2])
    value.append(a[50:52])


    # values.append(data_list[0][15][2:4])
    length.append(2)
    value.append(a[52:54])


    # values.append(data_list[0][15][4:6])
    length.append(2)
    value.append(a[54:56])


    length.append(1)
    value.append(a[56:57])


    length.append(1)
    value.append(a[57:58])


    length.append(3)
    value.append(a[58:61])


    length.append(2)
    value.append(a[61:63])


    length.append(3)
    value.append(a[63:66])


    length.append(2)
    value.append(a[66:68])


    length.append(3)
    value.append(a[68:71])


    length.append(2)

    value.append(a[71:73])


    length.append(2)
    value.append(a[73:75])


    length.append(1)
    value.append(a[75:76])


    length.append(1)
    value.append(a[76:77])


    length.append(2)
    value.append(a[77:79])


    length.append(2)
    value.append(a[79:81])



    length.append(1)
    value.append(a[81:82])




    length.append(1)

    # data_list[0][24][0]
    value.append(a[82:83])



    length.append(1)
    # data_list[0][24][1]
    value.append(a[83:84])


    length.append(2)
    # data_list[0][24][2:4]
    value.append(a[84:86])


    length.append(2)
    # data_list[0][24][4:6]
    value.append(a[86:88])


    length.append(2)
    # data_list[0][24][6:8]
    value.append(a[88:90])


    length.append(2)
    # data_list[0][24][8:10]
    value.append(a[90:92])


    length.append(1)
    # data_list[0][24][10]
    value.append(a[92:93])


    length.append(1)
    # data_list[0][24][11]
    value.append(a[93:94])


    length.append(1)
    # data_list[0][24][12]
    value.append(a[94:95])


    length.append(1)
    # data_list[0][24][13]
    value.append(a[95:96])


    length.append(1)
    # data_list[0][24][14]
    value.append(a[96:97])


    length.append(1)
    # data_list[0][24][15]
    value.append(a[97:98])


    length.append(1)
    # data_list[0][24][16]
    value.append(a[98:99])

    length.append(1)
    # data_list[0][24][17]
    value.append(a[99:100])


    length.append(1)
    # data_list[0][24][18]
    value.append(a[100:101])


    length.append(1)
    # data_list[0][24][19]
    value.append(a[101:102])



    length.append(2)
    value.append(a[102:104])


    length.append(1)
    # data_list[0][25][2]
    value.append(a[104:105])


    length.append(4)

    # data_list[0][25][3:8]
    value.append(a[105:109])


    length.append(1)
    # data_list[0][26][0]
    value.append(a[109:110])


    length.append(3)
    # data_list[0][26][0:3]
    value.append(a[110:113])


    length.append(1)
    # data_list[0][26][0:3]
    value.append(a[113:114])




    length.append(3)
    # data_list[0][27]
    value.append(a[114:117])


    length.append(1)
    # data_list[0][28][0]
    value.append(a[117:118])


    length.append(2)
    # data_list[0][28][1:3]
    value.append(a[118:120])


    length.append(1)
    # data_list[0][28][3]
    value.append(a[120:121])


    length.append(1)

    # data_list[0][28][4]
    value.append(a[121:122])

    # data_list[0][29]


    length.append(1)

    # data_list[0][29][0]
    value.append(a[122:123])


    length.append(1)
    # data_list[0][29][1]
    value.append(a[123:124])


    length.append(1)
    # data_list[0][29][2]
    value.append(a[124:125])


    length.append(1)
    # data_list[0][29][3]
    value.append(a[125:126])


    length.append(1)
    # data_list[0][29][4]
    value.append(a[126:127])


    length.append(1)
    # data_list[0][29][5]
    value.append(a[127:128])


    length.append(1)
    # data_list[0][29][6]
    value.append(a[128:129])


    length.append(1)
    # data_list[0][29][7]
    value.append(a[129:130])


    length.append(1)
    # data_list[0][29][8]
    value.append(a[130:131])


    length.append(1)
    # data_list[0][29][9]
    value.append(a[131:132])


    length.append(1)
    # data_list[0][29][10]
    value.append(a[132:133])


    length.append(1)
    # data_list[0][29][11]
    value.append(a[133:134])


    length.append(1)
    # data_list[0][29][12]
    value.append(a[134:135])


    length.append(1)
    # data_list[0][29][13]
    value.append(a[135:136])


    length.append(1)
    # data_list[0][29][14]
    value.append(a[136:137])


    length.append(1)
    # data_list[0][29][15]
    value.append(a[137:138])


    length.append(1)
    # data_list[0][29][16]
    value.append(a[138:139])


    length.append(1)
    # data_list[0][29][17]
    value.append(a[139:140])


    length.append(1)
    # data_list[0][29][18]
    value.append(a[140:141])




    length.append(2)
    # data_list[0][29][19:21]
    value.append(a[141:143])




    length.append(1)
    # data_list[0][30][0]
    value.append(a[141:142])


    length.append(1)
    # data_list[0][30][1]
    value.append(a[142:143])


    length.append(1)
    # data_list[0][30][2]
    value.append(a[143:144])


    # columns.append('Infections Present')
    # length.append(2)

    # data_list[0][31]


    length.append(1)
    value.append(a[146:147])

    # data_list[0][31][0]


    length.append(1)

    # data_list[0][31][1]
    value.append(a[147:148])


    length.append(1)
    # data_list[0][31][2]
    value.append(a[148:149])


    length.append(1)
    # data_list[0][31][3]
    value.append(a[149:150])


    length.append(1)
    # data_list[0][31][4]
    value.append(a[150:151])




    length.append(1)
    # data_list[0][31][5]
    value.append(a[151:152])


    length.append(1)
    # data_list[0][31][6]
    value.append(a[152:153])


    length.append(1)
    # data_list[0][31][7]
    value.append(a[153:154])


    length.append(1)
    # data_list[0][31][8]
    value.append(a[153:154])


    length.append(1)
    # data_list[0][31][9]
    value.append(a[155:156])


    length.append(1)
    # data_list[0][31][10]
    value.append(a[156:157])


    length.append(1)
    # data_list[0][32]
    value.append(a[157:158])


    length.append(1)
    # data_list[0][32][1]
    value.append(a[158:159])


    length.append(1)
    # data_list[0][33][0]
    value.append(a[159:160])


    length.append(1)
    # data_list[0][33][1]
    value.append(a[160:161])




    length.append(1)
    # data_list[0][34][0]
    value.append(a[161:162])


    length.append(1)
    # data_list[0][34][1]
    value.append(a[162:163])


    length.append(1)
    # data_list[0][34][2]
    value.append(a[163:164])


    length.append(1)
    # data_list[0][34][3]
    value.append(a[164:165])


    length.append(1)
    # data_list[0][34][4]
    value.append(a[165:166])


    length.append(1)
    # data_list[0][34][5]
    value.append(a[166:167])


    length.append(1)
    # data_list[0][34][6]
    value.append(a[167:168])


    length.append(1)
    # data_list[0][34][7]
    value.append(a[168:169])


    length.append(1)
    # data_list[0][34][8]
    value.append(a[169:170])


    length.append(1)
    # data_list[0][34][9]
    value.append(a[170:171])


    length.append(1)
    # data_list[0][34][10]
    value.append(a[171:172])


    length.append(1)
    # data_list[0][34][11]
    value.append(a[172:173])


    length.append(1)
    # data_list[0][34][12]
    value.append(a[173:174])


    length.append(1)
    # data_list[0][35]
    value.append(a[174:175])


    length.append(1)
    # data_list[0][35][1]
    value.append(a[175:176])


    length.append(1)
    # data_list[0][35][2]
    value.append(a[176:177])


    length.append(1)
    # data_list[0][35][3]
    value.append(a[177:178])


    length.append(1)
    # data_list[0][35][4]
    value.append(a[178:179])


    length.append(1)
    # data_list[0][35][5]
    value.append(a[179:180])


    length.append(1)
    # data_list[0][35][6]
    value.append(a[180:181])


    length.append(1)
    value.append(a[181:182])


    length.append(1)
    # data_list[0][35][8]
    value.append(a[182:183])


    length.append(1)
    # data_list[0][36][0]
    value.append(a[183:184])


    length.append(1)
    # data_list[0][36][1]
    value.append(a[184:185])


    length.append(1)
    # data_list[0][36][2]
    value.append(a[185:186])


    length.append(1)
    # data_list[0][36][3]
    value.append(a[186:187])


    length.append(1)
    # data_list[0][36][4]
    value.append(a[187:188])




    length.append(1)
    # data_list[0][37][0]
    value.append(a[188:189])


    length.append(1)
    # data_list[0][37][1]
    value.append(a[189:190])


    length.append(1)
    # data_list[0][37][2]
    value.append(a[190:191])


    length.append(1)
    # data_list[0][37][3]
    value.append(a[191:192])


    length.append(1)
    # data_list[0][37][4]
    value.append(a[192:193])


    length.append(1)
    # data_list[0][38]
    value.append(a[193:194])




    length.append(1)
    # data_list[0][39][0]
    value.append(a[194:195])


    length.append(1)
    # data_list[0][39][1]
    value.append(a[195:196])


    length.append(1)
    # data_list[0][39][2]
    value.append(a[196:197])


    length.append(1)
    # data_list[0][39][3]
    value.append(a[197:198])


    length.append(1)
    # data_list[0][39][4]
    value.append(a[198:199])


    length.append(1)

    # data_list[0][39][5]
    value.append(a[199:200])




    length.append(2)
    # data_list[0][40][0:2]
    value.append(a[200:202])


    length.append(1)
    # data_list[0][40][2]
    value.append(a[202:203])


    length.append(1)
    # data_list[0][40][3]
    value.append(a[203:204])


    length.append(2)
    # data_list[0][40][4:6]
    value.append(a[204:206])


    length.append(1)
    # data_list[0][40][6]
    value.append(a[206:207])

    # columns.append('Plurality Recode')
    # length.append(1)
    # # data_list[0][41]
    # a[206:207]


    length.append(1)
    # data_list[0][41]
    value.append(a[207:208])


    length.append(1)
    # data_list[0][42]
    value.append(a[208:209])


    length.append(1)
    # data_list[0][43]
    value.append(a[209:210])

    # columns.append('Imputed Sex')
    # length.append(1)
    # # data_list[0][43]
    # a[208:209]


    length.append(2)
    # data_list[0][44]
    value.append(a[210:212])


    length.append(4)
    # data_list[0][45]
    value.append(a[212:216])



    # columns.append('Combined Gestation Imputation Flag')
    # length.append(1)
    # # data_list[0][46][0:2]
    # a[216:217]

    # columns.append('Obsteric Estimate of Gestation Used Flag')
    # length.append(1)
    # # data_list[0][46][0:2]
    # a[217:218]


    length.append(2)
    # data_list[0][46][0:2]
    value.append(a[216:218])


    length.append(2)
    value.append(a[218:220])
    # data_list[0][46][2:4]


    length.append(1)
    value.append(a[220:221])
    # data_list[0][46][4]

    # columns.append('Combined Gestation Used Flag')
    # length.append(1)

    # a[221:222]




    length.append(2)
    # data_list[0][47][0:2]
    value.append(a[221:223])


    length.append(2)
    # data_list[0][47][2:4]
    value.append(a[223:225])


    length.append(1)
    value.append(a[225:226])


    length.append(4)
    value.append(a[226:230])


    length.append(2)
    value.append(a[230:232])


    length.append(1)
    value.append(a[232:233])


    # Abnormal Conditions of the Newborn


    length.append(1)
    # data_list[0][49][0]
    value.append(a[233:234])


    length.append(1)
    # data_list[0][49][1]
    value.append(a[234:235])


    length.append(1)
    # data_list[0][49][2]
    value.append(a[235:236])


    length.append(1)
    # data_list[0][49][3]
    value.append(a[236:237])


    length.append(1)
    # data_list[0][49][4]
    value.append(a[237:238])


    length.append(1)
    # data_list[0][49][5]
    value.append(a[238:239])




    length.append(1)
    # data_list[0][50][0]
    value.append(a[239:240])


    length.append(1)
    # data_list[0][50][1]
    value.append(a[240:241])


    length.append(1)
    # data_list[0][50][2]
    value.append(a[241:242])


    length.append(1)
    # data_list[0][50][3]
    value.append(a[242:243])


    length.append(1)
    # data_list[0][50][4]
    value.append(a[243:244])


    length.append(1)
    # data_list[0][50][5] a[239:240]
    value.append(a[244:245])


    length.append(1)
    # data_list[0][51]
    value.append(a[245:246])


    length.append(1)
    # data_list[0][52][0]
    value.append(a[246:247])


    length.append(1)
    # data_list[0][52][1]
    value.append(a[247:248])


    length.append(1)
    # data_list[0][52][2]
    value.append(a[248:249])


    length.append(1)
    # data_list[0][52][3]
    value.append(a[249:250])


    length.append(1)
    # data_list[0][52][4]
    value.append(a[250:251])


    length.append(1)
    # data_list[0][52][5]
    value.append(a[251:252])


    length.append(1)
    # data_list[0][52][6]
    value.append(a[252:253])

    length.append(1)
    # data_list[0][52][7]
    value.append(a[253:254])


    length.append(1)
    # data_list[0][52][8]
    value.append(a[254:255])


    length.append(1)
    # data_list[0][52][9]
    value.append(a[255:256])


    length.append(1)
    # data_list[0][52][10]
    value.append(a[256:257])


    length.append(1)
    # data_list[0][52][11]
    value.append(a[257:258])


    length.append(1)
    # data_list[0][52][12]
    value.append(a[258:259])


    length.append(1)
    # data_list[0][52][13]
    value.append(a[259:260])


    length.append(1)
    # data_list[0][52][14]
    value.append(a[260:261])


    length.append(1)
    # data_list[0][52][15]
    value.append(a[261:262])


    length.append(1)
    # data_list[0][52][16]
    value.append(a[262:263])


    length.append(1)
    # data_list[0][52][17]
    value.append(a[263:264])


    length.append(1)
    # data_list[0][52][18]
    value.append(a[264:265])


    length.append(1)
    # data_list[0][52][19]
    value.append(a[265:266])


    length.append(1)
    # data_list[0][52][20]
    value.append(a[266:267])


    length.append(1)
    # data_list[0][52][21]
    value.append(a[267:268])


    length.append(1)
    # data_list[0][52][22]
    value.append(a[268:269])


    length.append(1)
    # data_list[0][52][23]
    value.append(a[269:270])


    length.append(1)
    # data_list[0][52][24]
    value.append(a[270:271])


    length.append(1)
    value.append(a[271:272])


    length.append(1)
    # data_list[0][53][1]
    value.append(a[272:273])


    # data_list[0][53][2]

    value.append(a[273:274])


    # data_list[0][53][3]
    value.append(a[274:275])

    value_list.append(value)



len(value_list)



columns=[]



columns.append('Birth Year')

columns.append('Birth Month')

columns.append('Time of Birth')


columns.append('Birth Day of Week')

columns.append('Birth Place')

columns.append('Reporting Flag for Birth Place')

columns.append('Birth Place Recode')


columns.append('Mother’s Single Years of Age')

columns.append('Mother’s Age Recode 14')


columns.append('Mother’s Age Recode 9')


columns.append('Mother’s Nativity')

columns.append('Residence Status')

columns.append('Mother’s Race Recode 31')

columns.append('Mother’s Race Recode 6')

columns.append('Mother’s Race Recode 15')

columns.append('Mother’s Race Imputed Flag')

columns.append('Mother’s Hispanic Origin')

columns.append('Mother’s Race/Hispanic Origin')

columns.append('Paternity Acknowledged')

columns.append('Marital Status')

columns.append('Mother Marital Status Imputed')

columns.append('Mother’s Education')

columns.append('Reporting Flag for Education of Mother')

columns.append('Father’s Combined Age')

columns.append('Father’s Age Recode 11')

columns.append('Father’s Race Recode 31')

columns.append('Father’s Race Recode 6')

columns.append('Father’s Race Recode 15')


columns.append('Father’s Hispanic Origin')

columns.append('Father’s Hispanic Origin Recode')

columns.append('Reporting Flag for Father’s Origin')


columns.append('Father’s Race/Hispanic Origin')

columns.append('Father’s Education')


columns.append('Reporting Flag for Education of Father')


columns.append('Prior Births Now Living')


columns.append('Prior Births Now Dead')

columns.append('Prior Other Terminations')


columns.append('Live Birth Order Recode')


columns.append('Total Birth Order Recode')


columns.append('Interval Since Last Live Birth Recode')


columns.append('Interval Since Last Live Birth Recode 11')


columns.append('Interval Since Last Other Pregnancy Recode')

columns.append('Interval Since Last Other Pregnancy Recode 11')


columns.append('Interval Since Last Pregnancy Recode')

columns.append('Interval Since Last Pregnancy Recode 11')


columns.append('Month Prenatal Care Began')

columns.append('Reporting Flag for Month Prenatal Care Began')

columns.append('Month Prenatal Care Began Recode')


columns.append('Number of Prenatal Visits')


columns.append('Number of Prenatal Visits Recode')

columns.append('Reporting Flag for Prenatal Care Visits')

columns.append('WIC')

columns.append('Reporting Flag for WIC')

columns.append('Cigarettes Before Pregnancy')

columns.append('Cigarettes 1st Trimester')

columns.append('Cigarettes 2nd Trimester')

columns.append('Cigarettes 3rd Trimester')

columns.append('Cigarettes Before Pregnancy Recode')

columns.append('Cigarettes 1st Trimester Recode')

columns.append('Cigarettes 2nd Trimester Recode')

columns.append('Cigarettes 3rd Trimester Recode')

columns.append('Reporting Flag for Cigarettes before Pregnancy')

columns.append('Reporting Flag for Cigarettes 1st Trimester')

columns.append('Reporting Flag for Cigarettes 2nd Trimester')

columns.append('Reporting Flag for Cigarettes 3rd Trimester')

columns.append('Cigarette Recode')

columns.append('Reporting Flag for Tobacco use')


columns.append('Mother’s Height in Total Inches')


columns.append('Reporting Flag for Mother’s Height')

columns.append('Body Mass Index')


columns.append('Body Mass Index Recode')


columns.append('Pre-pregnancy Weight Recode')

columns.append('Reporting Flag for Pre-pregnancy Weight')

columns.append('Delivery Weight Recode')

columns.append('Reporting Flag for Delivery Weight')


columns.append('Weight Gain')


columns.append('Weight Gain Recode')


columns.append('Reporting Flag for Weight Gain ?')


columns.append('Pre-pregnancy Diabetes')


columns.append('Gestational Diabetes')


columns.append('Pre-pregnancy Hypertension')


columns.append('Gestational Hypertension')

columns.append('Hypertension Eclampsia')


columns.append('Previous Preterm Birth')


columns.append('Reporting Flag for Pre-pregnancy Diabetes')


columns.append('Reporting Flag for Gestational Diabetes')


columns.append('Reporting Flag for Pre-pregnancy Hypertension')


columns.append('Reporting Flag for Gestational Hypertension')


columns.append('Reporting Flag for Hypertension Eclampsia')


columns.append('Reporting Flag for Previous Preterm Birth')


columns.append('Infertility Treatment Used')


columns.append('Fertility Enhancing Drugs')


columns.append('Asst. Reproductive Technology')


columns.append('Reporting Flag for Infertility Treatment')


columns.append('Reporting Flag for Fertility Enhance Drugs')

columns.append('Reporting Flag for Reproductive Technology')

columns.append('Previous Cesarean')


columns.append('Number of Previous Cesareans')


columns.append('Reporting Flag for Previous Cesarean')


columns.append('Reporting Flag for Number of Previous Cesareans')

columns.append('No Risk Factors Reported')


columns.append('Gonorrhea')


columns.append('Syphilis')

columns.append('Chlamydia')

columns.append('Hepatitis B')


columns.append('Hepatitis C')


columns.append('Reporting Flag for Gonorrhea')


columns.append('Reporting Flag for Syphilis')


columns.append('Reporting Flag for Chlamydia')


columns.append('Reporting Flag for Hepatitis B')

columns.append('Reporting Flag for Hepatitis C')

columns.append('No Infections Reported')


columns.append('Successful External Cephalic Version')


columns.append('Failed External Cephalic Version')


columns.append('Reporting Flag for Successful External Cephalic Version')

columns.append('Reporting Flag for Failed External Cephalic Version')


columns.append('Induction of Labor')

columns.append('Augmentation of Labor')

columns.append('Steroids')


columns.append('Antibiotics')


columns.append('Chorioamnionitis')


columns.append('Anesthesia')


columns.append('Reporting Flag for Induction of Labor')

columns.append('Reporting Flag for Augmentation of Labor')


columns.append('Reporting Flag for Steroids')


columns.append('Reporting Flag for Antibiotics')


columns.append('Reporting Flag for Chorioamnionitis')


columns.append('Reporting Flag for Anesthesia')


columns.append('No Characteristics of Labor Reported')


columns.append('Fetal Presentation at Delivery')


columns.append('Final Route & Method of Delivery')


columns.append('Trial of Labor Attempted (if cesarean)')


columns.append('Reporting Flag for Fetal Presentation')

columns.append('Reporting Flag for Final Route and Method of Deliver')


columns.append('Reporting Flag for Trial of Labor Attempted')


columns.append('Delivery Method Recode')


columns.append('Delivery Method Recode')


columns.append('Reporting Flag for Method of Delivery Recode')


columns.append('Maternal Transfusion')


columns.append('Perineal Laceration')


columns.append('Ruptured Uterus')

columns.append('Unplanned Hysterectomy')


columns.append('Admit to Intensive Care')


columns.append('Reporting Flag for Maternal Transfusion')


columns.append('Reporting Flag for Perineal Laceration')


columns.append('Reporting Flag for Ruptured Uterus')


columns.append('Reporting Flag for Unplanned Hysterectomy')

columns.append('Reporting Flag for Admission to Intensive Care')

columns.append('No Maternal Morbidity Reported')


columns.append('Attendant at Birth')


columns.append('Mother Transferred')

columns.append('Payment Source for Delivery')


columns.append('Payment Recode')

columns.append('Reporting Flag for Source of Payment')

columns.append('Reporting Flag for Payment Recode')

columns.append('Five Minute APGAR Score')


columns.append('Five Minute APGAR Recode')

columns.append('Reporting Flag for Five minute APGAR')

columns.append('Ten Minute APGAR Score')

columns.append('Ten Minute APGAR Recode')


columns.append('Plurality Imputed')


columns.append('Set Order Recode')

columns.append('Sex of Infant')


columns.append('Last Normal Menses Month')


columns.append('Last Normal Menses Year')


columns.append('Combined Gestation – Detail in Weeks')


columns.append('Combined Gestation Recode 10')

columns.append('Combined Gestation Recode 3')


columns.append('Obstetric Estimate Edited')


columns.append('Obstetric Estimate Recode10')


columns.append('Obstetric Estimate Recode 3')


columns.append('Birth Weight – Detail in Grams (Edited)')

columns.append('Birth Weight Recode 12')

columns.append('Birth Weight Recode 4')

columns.append('Assisted Ventilation (immediately)')

columns.append('Assisted Ventilation > 6 hrs')


columns.append('Admission to NICU')

columns.append('Surfactant')


columns.append('Antibiotics for Newborn')

columns.append('Seizures')


columns.append('Reporting Flag for Assisted Ventilation (immediately)')


columns.append('Reporting Flag for Assisted Ventilation >6 hrs')


columns.append('Reporting Flag for Admission to NICU')


columns.append('Reporting Flag for Surfactant')


columns.append('Reporting Flag for Antibiotics')


columns.append('Reporting Flag for Seizures')

columns.append('No Abnormal Conditions Checked')


columns.append('Anencephaly')


columns.append('Meningomyelocele / Spina Bifida')


columns.append('Cyanotic Congenital Heart Disease')


columns.append('Congenital Diaphragmatic Hernia')


columns.append('Omphalocele')


columns.append('Gastroschisis')


columns.append('Reporting Flag for Anencephaly')


columns.append('Reporting Flag for Meningomyelocele/Spina Bifida')


columns.append('Reporting Flag for Cyanotic Congenital Heart Disease')


columns.append('Reporting Flag for Congenital Diaphragmatic Hernia')


columns.append('Reporting Flag for Omphalocele')


columns.append('Reporting Flag for Gastroschisis')

columns.append('Limb Reduction Defect')

columns.append('Cleft Lip w/ or w/o Cleft Palate')


columns.append('Cleft Palate alone')

columns.append('Down Syndrome')


columns.append('Suspected Chromosomal Disorder')


columns.append('Hypospadias')


columns.append('Reporting Flag for Limb Reduction Defect')


columns.append('Reporting Flag for Cleft Lip with or without Cleft Palate')


columns.append('Reporting Flag for Cleft Palate Alone')


columns.append('Reporting Flag for Down Syndrome')


columns.append('Reporting Flag for Suspected Chromosomal Disorder')

columns.append('Reporting Flag for Hypospadias')

columns.append('No Congenital Anomalies Checked')

columns.append('Infant Transferred')

columns.append('Infant Living at Time of Report')

columns.append('Infant Breastfed at Discharge')

columns.append('Reporting Flag for Breastfed at Discharge')



len(columns)

len(value_list)



list_dict=[]

for i in (value_list):
  dictionary = {}
  for key,value in zip(columns,i):
    dictionary[key] = value
  list_dict.append(dictionary)

list_dict

len(list_dict)



# Will create a pandas dataframe from the dictionary

with open('part1.csv', 'w') as f:
  f.write(','.join(list_dict[0].keys()))
  f.write('\n')
  for row in list_dict:
    f.write(','.join(str(x) for x in row.values()))
    f.write('\n')



# importing pandas
# import pandas as pd

# read text file into pandas DataFrame
# file1= pd.read_csv("/content/part1.csv",header=None)


'''































