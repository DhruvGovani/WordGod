import os
import time

os.system('clear')

print('##################################################################################################')
print('################################## WORD GOD  #####################################################')
print('##################################################################################################')
print('##################################################################################################')
print('############################ MADE BY DHRUV GOVANI ################################################')
print('##################################################################################################')
print('##################################################################################################')
print('################################# Version 1.0 ####################################################')
print('##################################################################################################')
print('##################################################################################################')
print('\nFeatures : This Program Will read a single word from you and fetch other words from specified source file \n \t    to genrate all possible combination of password and stores all of them in file.')
print('\nprogram initiated..')

mainString = input('\nEnter Main Word: ')


fileDataList = []
fileDataList2 = []
fileDataList3 = []
fileDataList4 = []
fileDataList5 = []
fileDataList6 = []
fileDataList7 = []
fileDataList8 = []
fileDataList9 = []
fileDataList10 = []
fileDataListSpeChar = []


fileName = input('\nEnter Source File Name: ')
fcheck = open(fileName)



desfile = input('\nEnter destination file name: ')
desf = open(desfile,'w+')
print('\nnew file created successfully..')
choice = input('\ndo you want any special character included? (Y/N) : ')

while choice == 'Y':
 spechar = input('\nenter special character : ')

 for word in open(fileName).read().split():
  fileDataListSpeChar.append(mainString + spechar + word)
  fileDataListSpeChar.append(word + spechar + mainString)
  fileDataListSpeChar.append(spechar + word  + mainString)
  fileDataListSpeChar.append(spechar + mainString + word)
  fileDataListSpeChar.append(word + mainString + spechar)
  fileDataListSpeChar.append(mainString + word + spechar)

  fileDataListSpeChar.append(mainString.capitalize()  + spechar + word)
  fileDataListSpeChar.append(word + spechar + mainString.capitalize() )
  fileDataListSpeChar.append(spechar + word  + mainString.capitalize() )
  fileDataListSpeChar.append(spechar + mainString.capitalize()  + word)
  fileDataListSpeChar.append(word + mainString.capitalize()  + spechar)
  fileDataListSpeChar.append(mainString.capitalize()  + word + spechar)

  fileDataListSpeChar.append(mainString + spechar + word.capitalize())
  fileDataListSpeChar.append(word.capitalize() + spechar + mainString)
  fileDataListSpeChar.append(spechar + word.capitalize() + mainString)
  fileDataListSpeChar.append(spechar + mainString + word.capitalize())
  fileDataListSpeChar.append(word.capitalize() + mainString + spechar)
  fileDataListSpeChar.append(mainString + word.capitalize() + spechar)

  fileDataListSpeChar.append(mainString + spechar + word.upper())
  fileDataListSpeChar.append(word.upper() + spechar + mainString)
  fileDataListSpeChar.append(spechar + word.upper() + mainString)
  fileDataListSpeChar.append(spechar + mainString + word.upper())
  fileDataListSpeChar.append(word.upper() + mainString + spechar)
  fileDataListSpeChar.append(mainString + word.upper() + spechar)

  fileDataListSpeChar.append(mainString + spechar + word.lower())
  fileDataListSpeChar.append(word.lower() + spechar + mainString)
  fileDataListSpeChar.append(spechar + word.lower() + mainString)
  fileDataListSpeChar.append(spechar + mainString + word.lower())
  fileDataListSpeChar.append(word.lower() + mainString + spechar)
  fileDataListSpeChar.append(mainString + word.lower() + spechar)

 for i in range(len(fileDataListSpeChar)):
  desf.write(fileDataListSpeChar[i] + '\n')


 choice = input('\ndo you want any other special character included? (Y/N): ')

for word in open(fileName).read().split():#combinationloop
 fileDataList.append(mainString + word)
 fileDataList2.append( word + mainString)
 fileDataList3.append( word.capitalize() + mainString)
 fileDataList4.append( word + mainString.capitalize())
 fileDataList5.append(mainString.capitalize() + word)
 fileDataList6.append(mainString + word.capitalize())
 fileDataList7.append(mainString.upper() + word)
 fileDataList8.append(mainString + word.upper())
 fileDataList9.append(mainString.lower() + word)
 fileDataList10.append(mainString + word.lower())


for i in range(len(fileDataList)):#writefileloop
 desf.write(fileDataList[i] + '\n')
 desf.write(fileDataList2[i] + '\n')
 desf.write(fileDataList3[i] + '\n')
 desf.write(fileDataList4[i] + '\n')
 desf.write(fileDataList5[i] + '\n')
 desf.write(fileDataList6[i] + '\n')
 desf.write(fileDataList7[i] + '\n')
 desf.write(fileDataList8[i] + '\n')
 desf.write(fileDataList9[i] + '\n')
 desf.write(fileDataList10[i] + '\n')

print('\nall possible passwords written succesfully')


