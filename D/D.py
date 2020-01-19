# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
N = int(input())
print(N)
order = len(str(N))

if order == 1:
    print(N)
elif order == 2:
    cnt = 9

    temp_comb = [[int(str(i) + str(j)), int(str(j) + str(i))] for i in range(1,10) for j in range(1,10)]
    
    for i, j in temp_comb:
        if i <= N and j <=N:
            cnt += 1
            print(i,j)
    
    temp_comb_2 = [[int(str(i)), int(str(i) + str(i))] for i in range(1,10)]
    temp_comb_3 = [[int(str(i) + str(i)), int(str(i))] for i in range(1,10)]
    temp_comb_4 = temp_comb_2 + temp_comb_3

    for i, j in temp_comb_4:
        if i <= N and j <=N:
            cnt += 1
            print(i,j)

else:
    cnt_1_2 = 108
    cnt_3 = 1098 - 108
    cnt_4 = cnt_3*(8**2)
    cnt_5 = cnt_4*(7**2)

    if order == 3:
        cnt = cnt_1_2

        temp_comb = [[int(str(i) + str(k) + str(j)), int(str(j) + str(k) + str(i))] for i in range(1,10) for j in range(1,10) for k in range(0,10)]
        
        for i, j in temp_comb:
            if i <= N and j <=N:
                cnt += 1
                print(i,j)
        
        temp_comb_2 = [[int(str(i)), int(str(i) + str(k) + str(i))] for i in range(1,10) for k in range(0,10)]
        temp_comb_3 = [[int(str(i) + str(k) + str(i)), int(str(i))] for i in range(1,10) for k in range(0,10)]
        temp_comb_4 = temp_comb_2 + temp_comb_3

        for i, j in temp_comb_4:
            if i <= N and j <=N:
                cnt += 1
                print(i,j)


    elif order == 4:

        cnt = cnt_1_2 + cnt_3

        temp_comb = [[int(str(i) + str(k) + str(l) + str(j)), int(str(j) + str(k) + str(l) + str(i))]
        for i in range(1,10) for j in range(1,10)
        for k in range(0,10)
        for l in range(0,10)]
        
        for i, j in temp_comb:
            if i <= N and j <=N:
                cnt += 1
                print(i,j)
        
        temp_comb_2 = [[int(str(i)), int(str(i) + str(k) + str(l) + str(i))] 
        for i in range(1,10)
        for k in range(0,10)
        for l in range(0,10)]
        temp_comb_3 = [[int(str(i) + str(k)  + str(l) + str(i)), int(str(i))] 
        for i in range(1,10) 
        for k in range(0,10)
        for l in range(0,10)]
        temp_comb_4 = temp_comb_2 + temp_comb_3

        for i, j in temp_comb_4:
            if i <= N and j <=N:
                cnt += 1
                print(i,j)

    elif order ==5:
        pass
    else:
        pass



print('cnt', cnt)

