# Network DEA function

*POLab*
<br>
*2018/03/23*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)

本文主要針對所建立的Network DEA模型函式進行說明: <br>
(※函式執行範例可參考[這裡](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Network_DEA_function_example.ipynb))


## network()

### § Description
- 本函式是將[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)在2007發表的
[paper](https://www.sciencedirect.com/science/article/pii/S0377221707010077)中所提出的關聯網絡DEA模型(Relational network DEA model)，建立成函式，以利使用

### § Usage
- network(DMU, X, Y, Z_input, Z_output, p_n, var_lb)
- 回傳各DMU的效率值，以及各製程的效率值與無效率值



### § Arguments 
#### (※請務必閱讀過讀檔程式[csv2dict_for_network_dea()](https://github.com/wurmen/DEA/blob/master/Functions/read_data_for_networkDEA.md)的內容)
- **DMU**：list, 記錄所有要被衡量效率值的DMU名稱列表，可放入經由csv2dict_for_network_dea()轉換後的回傳值(DMU)
- **X**：dict, 記錄每個DMU及每個製程所對應來自系統外部的投入，可放入經由csv2dict_for_network_dea()轉換後的回傳值(X)
- **Y**：dict, 記錄每個DMU及每個製程所對應會成為系統最終產出的產出項，可放入經由csv2dict_for_network_dea()轉換後的回傳值(Y)
- **Z_input**：dict, 紀錄每個DMU及每個製程的投入來自某內部製程的產出項資料，在此被視為中間產物投入項，可放入經由
csv2dict_for_network_dea()轉換後的回傳值(Z_input)
- **Z_output**：dict, 紀錄每個DMU及每個製程的產出會成為某內部製程的投入項資料，在此被視為中間產物投入項，可放入經由
csv2dict_for_network_dea()轉換後的回傳值(Z_output)
- **p_n**： integer, 紀錄系統中共有幾個製程，可放入經由csv2dict_for_network_dea()轉換後的回傳值(p_n)
- **var_lb**： float, 決定權重的下限值






