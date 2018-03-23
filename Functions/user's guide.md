# DEA Functions使用說明

*POLab*
<br>
*2018/03/19*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br><br>
在此針對基本DEA model建構幾個簡單的DEA Functions，使大家能夠更輕鬆的利用這些DEA函數來求解效率值，或者可由這些已建好的函數去做延伸。
<br>


## (一)使用前注意事項
1. 必須具備gurobi package(Gurobi 6.5.2)、python3.6
2. 需將存放DEA Functions的py檔與所要使用的程式碼檔及數據放在同一資料夾中，這裡採用呼叫的方式進行函式的使用
3. 產出與投入資料須符合所需格式

## (二)使用步驟
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/1.PNG">
</div>

1. 先載入存放DEA函式的py檔(在此檔名為"DEA.py")
```python
import DEA
```
2. 讀取資料，並取得DMU列表，以及產出(Y)投入(X)資料
```python
DMU,X,Y=DEA.csv2dict("data.csv",in_range=[2,4],out_range=[5,8],assign=True)
```
3. 選取所要使用的DEA model
```python
DEA.CRS_input(DMU,X,Y) 
```
## (三)函式說明
- [Read data function for basic DEA models](https://github.com/wurmen/DEA/blob/master/Functions/read_data_function.md)
- [Basic DEA functions](https://github.com/wurmen/DEA/blob/master/Functions/basic_dea_functions.md)
- [Read data function for network DEA model](https://github.com/wurmen/DEA/blob/master/Functions/read_data_for_networkDEA.md)
- [Network DEA function](https://github.com/wurmen/DEA/blob/master/Functions/network_DEA_function.md)

## (四)範例
- [Read data function examples for basic DEA models](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb)
- [Basic DEA functions examples](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/basic_DEA_function.ipynb)
- [Read data function example for network DEA model](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Read_data_for_network_DEA_function%20example.ipynb)
- [Network DEA function example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Network_DEA_function_example.ipynb)
