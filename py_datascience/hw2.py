#**********************************************************************
#*
#*  	Name :	shou
#*
#*  	Class :	資管三
#*
#*	SID :	S06490001
#*
#*      Program Name : hw2.py
#*
#*  	Functions : 在Python中使用正規表示法處理
#*               
#*	Homework : No.2
#*
#*      Limitations : 依題意
#*                      
#*	Last Modified Date :	2020/3/30
#*
#**********************************************************************


import re                           #引入re模組

#




#***********************************************************************
#*                                                                     *
#*                             資料處理區                              *
#*                                                                     *
#***********************************************************************


# ====== 輸入至少三個英文單字以上的字串 ====== #

Str_1 = input('請輸入任一英文字串(3個以上的英文單字):')                  #標籤Str_1指向一個字串物件內容由使用者所輸入

Temp_1 = re.match('[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+', Str_1)              #標籤Temp_1指向一個物件，找出Srt_1字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件

print()

while(not Temp_1):                                                       #當標籤Temp_1為None時，執行while迴圈

    print('!!少於3個以上的英文單字or輸入格式錯誤!!')                     #印出內容

    print()

    Str_1 = input('請輸入任一英文字串(3個以上的英文單字):')              #標籤Str_1指向一個字串物件內容由使用者所輸入

    Temp_1 = re.match('[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+', Str_1)          #標籤Temp_1指向一個物件，找出Srt_1字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件     

    print()


# ====== (P-1) ====== #

print('(P-1):')                                                          #印出內容              

print()

pattern = '[A-Za-z\s]'                                                   #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-2) ====== #

print('(P-2):')                                                          #印出內容

print()

pattern = '[A-Za-z]'                                                     #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-3) ====== #

print('(P-3):')                                                          #印出內容

print()

pattern = '\w*'                                                          #標籤pattern為一字串，內容為正規表達式所要求格式 \w* = empty string 若要排除empty string→\w*\S

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-4) ====== #

print('(P-4):')                                                          #印出內容

print()

pattern = '[A-Za-z]+'                                                    #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-5) ====== #

print('(P-5):')                                                          #印出內容

print()

pattern = '^[A-Za-z]+'                                                   #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-6) ====== #

print('(P-6):')                                                          #印出內容

print()

pattern = '[A-Za-z]+$'                                                   #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-7) ====== #

print('(P-7):')                                                          #印出內容

print()

pattern = '^[A-Za-z]{2}|(?<=\s)..'                                       #標籤pattern為一字串，內容為正規表達式所要求格式
 
print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-8) ====== #

print('(P-8):')                                                          #印出內容

print()

pattern = '^[AEIOUaeiou][A-Za-z]+|^[AEIOUaeiou][A-Za-z]+|(?<=\s)[AEIOUaeiou][A-Za-z]+'                  #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-9) ====== #

print('(P-9):')                                                          #印出內容

print()

pattern = '(.).'                                                         #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()


"""
pattern = '[\s\S]{2}'                               #另一種寫法
                                                    #將原本的字串先分成兩個字元一組('Th')
List = re.findall(pattern, Str_1)                   #接著再去挑出前面那個

Str_1_1 = str(List)

pattern_1 = "(?<=['])[A-Za-z\s](?=[A-Za-z\s])"

print(re.findall(pattern_1, Str_1_1))
"""


# ====== (P-10) ====== #

print('(P-10):')                                                         #印出內容

print()

pattern = '.(.)'                                                         #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_1))                                        #找出Str_1中所有符合pattern格式的字串，回傳串列並印出

print()

"""
pattern_2 = "(?<=[A-Za-z\s])[A-Za-z\s](?=['])"      #承上去挑出後面那個

print(re.findall(pattern_2, Str_1_1))
"""


# ====== 輸入至少三個以上英文的email位址 ====== #

Str_2 = input('輸入任一英文字串(3個以上的email位址):')                   #標籤Str_2指向一個字串物件內容由使用者所輸入

Temp_2 = re.match('\S+[@]\S+\s\S+[@]\S+\s\S+[@]\S+', Str_2)              #標籤Temp_2指向一個物件，找出Srt_2字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件

print()

while(not Temp_2):                                                       #當標籤Temp_2為None時，執行while迴圈

    print('!!少於3個以上的email位址or輸入格式錯誤!!')                    #印出內容

    print()

    Str_2 = input('輸入任一英文字串(3個以上的email位址):')               #標籤Str_2指向一個字串物件內容由使用者所輸入

    Temp_2 = re.match('\S+[@]\S+\s\S+[@]\S+\s\S+[@]\S+', Str_2)          #標籤Temp_2指向一個物件，找出Srt_2字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件

    print()

    
# ====== (P-11) ====== #

print('(P-11):')                                                         #印出內容

print()

pattern = '[@][A-Za-z]+'                                                 #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_2))                                        #找出Str_2中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-12) ====== #

print('(P-12):')                                                         #印出內容

print()

pattern = '[@][A-Za-z]+[.][a-z]+'                                        #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_2))                                        #找出Str_2中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-13) ====== #

print('(P-13):')                                                         #印出內容

print()

pattern = '[a-z]{3}(?=\s)|[a-z]{3}$|(?<=[.])[a-z]{3}(?=[.])|[a-z]{3}(?=[,])'                    #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_2))                                        #找出Str_2中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-14) ====== #

print('(P-14):')                                                         #印出內容

print()

pattern = '[\w.]+(?=[@])'                                                #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_2))                                        #找出Str_2中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== 輸入至少三個以上以MM-DD-YYYY格式的日期資訊 ====== #

Str_3 = input('輸入任一英文字串(3個以上的MM-DD-YYYY格式):')              #標籤Str_3指向一個字串物件內容由使用者所輸入

Temp_3 = re.match('[\s\S]+\d{2}-\d{2}-\d{4}[,]\s[\s\S]+\d{2}-\d{2}-\d{4}[,]\s[\s\S]+\d{2}-\d{2}-\d{4}', Str_3)          #標籤Temp_3指向一個物件，找出Srt_3字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件

print()

while(not Temp_3):                                                       #當標籤Temp_3為None時，執行while迴圈

    print('!!少於3個以上的日期資訊or輸入格式錯誤!!')                                   #印出內容

    print()

    Str_3 = input('輸入任一英文字串(3個以上的MM-DD-YYYY格式):')          #標籤Str_3指向一個字串物件內容由使用者所輸入

    Temp_3 = re.match('[\s\S]+\d{2}-\d{2}-\d{4}[,]\s[\s\S]+\d{2}-\d{2}-\d{4}[,]\s[\s\S]+\d{2}-\d{2}-\d{4}', Str_3)      #標籤Temp_3指向一個物件，找出Srt_3字串的開頭是否符合正規表達式的pattern格式，若找不到回傳None，若找到則回傳match物件

    print()

    
# ====== (P-15) ====== #

print('(P-15):')                                                         #印出內容

print()

pattern = '(?<=\s)\d{2}-\d{2}-\d{4}'                                     #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_3))                                        #找出Str_3中所有符合pattern格式的字串，回傳串列並印出

print()


# ====== (P-16) ====== #

print('(P-16):')                                                         #印出內容

print()

pattern = '\d{4}(?=[,])|\d{4}$'                                          #標籤pattern為一字串，內容為正規表達式所要求格式

print(re.findall(pattern, Str_3))                                        #找出Str_3中所有符合pattern格式的字串，回傳串列並印出

print()

