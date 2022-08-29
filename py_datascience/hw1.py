#**********************************************************************
#*
#*  	Name :	shou
#*
#*  	Class :	資管三
#*
#*	SID :	S06490001
#*
#*      Program Name : hw1.py
#*
#*  	Functions : 檔案與檔案目錄的處理
#*               
#*	Homework : No.1
#*
#*      Limitations : 依題意
#*                      
#*	Last Modified Date :	2020/3/20
#*
#**********************************************************************


import os;              #引入os模組

import glob;            #引入glob模組

import datetime;        #引入datetime模組

import time;            #引入time模組

import sys;             #引入sys模組





# ====== 標頭的螢幕顯示 ====== #



#***********************************************************************
#*                                                                     *
#*                             資料處理區                              *
#*                                                                     *
#***********************************************************************


# ====== 使用程式區塊「try…except…else…」攔截例外 ====== #

try:                                              #在try區塊中撰寫可能發生錯誤的程式
    
    path = input('請輸入指定工作目錄:')           #path指標指向一個字串物件由User輸入       
    
    print()
    
    os.chdir(path)                                #改變到path所指定的資料夾下
    
except Exception as e:                            #若發生錯誤會跳到except區塊進行後續的處理
    
    print()
    
    print('指定工作目錄錯誤')                     #印出內容
    
    sys.exit()                                    #停止程式的執行
    
else:                                             #若沒有發生錯誤則執行此區塊
    
    print()
    
    print('使用者指定工作目錄存在，系統現行工作區已轉至該目錄！')     #印出內容
    
    #print(os.getcwd())                          #回傳目前所在的資料夾(多Check一次現在位址)

    print()
    
    file_type = input('請輸入指定檔案型式:')     #標籤file_type指向一個字串物件由User輸入
    
    print()
    
    print('    =======================================', end = '\n')    #印出內容
    
    print()
    
    print('        符合的檔案名稱:', end = '\n') #印出內容
    
    print()


# ====== 設定使用者輸入的檔案型式與輸出結果 ====== #

    star = '*'                                   #標籤star指向一個字串物件
    
    finalFT = star + file_type                   #標籤finalFT指向一個字串物件由另外兩個字串物件所合起來的
    
    Num = int(len(glob.glob(finalFT)))           #標籤Num指向一個整數物件由list物件的長度轉變而來
    
    Str_To_List = glob.glob(finalFT)             #標籤Str_To_List指向一個List物件為用glob模組收集指定路徑中副檔名符合FinalFT的檔案
    
    for i in range(Num):
        
        print('        ',i+1,'.',Str_To_List[i]) #從順序1.開始Str_To_List中的內容印出
        
    print()
    
    total_num = os.listdir(path)                 #標籤total_num指向一個List物件為當下路徑中有什麼檔案
    
    print('       ','本目錄中共有',len(total_num),'個檔案')                          #將List物件(total_num)的長度印出，表示總共有幾個檔案
    
    print('       ','其中',len(glob.glob(finalFT)),'個是',file_type,'的檔案型態')    #將List物件(glob.glob(finalFT))的長度印出，表示有多少檔案的副檔名符合finalFT
    
    print('    =======================================', end = '\n')                 #印出內容
    
    print()
    
    print()
    
    print()


# ====== 顯示完成時當下的年月日時分秒 ====== #

    t =  time.time()                                                            #標籤t指向一個浮點數函式，其內容為取得現在的時間並以秒為單位

    dt = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")       #標籤dt指向一個物件，其內容為t並轉為年-月-日 時-分-秒的形式

    print('程式結束',dt,'***************************************************')  #印出結束程式字樣與完成當下的時間

    print()

    print()

    print()

    input('Please enter any key to exit...')

