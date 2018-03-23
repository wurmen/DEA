# Read data function

*POLab*
<br>
*2018/03/20*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
<br>
在使用DEA functions時，必須先將要衡量的資料讀取成主函式所要使用的資料格式，以利後續建模使用，因此在此建構兩種讀檔的函式，詳細的說明如下所示：(※函式執行示範可參考[這裡](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb))
* [csv2dict()](#csv2dict()) <br>
主要用於投入與產出資料都放在同一個檔案(.csv )時使用。
* [csv2dict_sep()](#csv2dict_sep()) <br>
當產出與投入資料放於不同檔案(.csv )時使用。

※函式執行結果可參考[這裡](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb)

## <h2 id="csv2dict()">csv2dict()</h2>
### § Description
- 用來讀取各決策單位投入與產出資料的csv檔，將資料轉換成字典格式(dictionary type)，以利後續建模使用，此函式**主要用於投入與產出資料都放在同一個檔案時使用**。

### § Usage
- csv2dict(dea_data, in_range, out_range, assign=False)
- 回傳三個值，分別是DMU(list), Input(dict), Output(dict)

### § Arguments
- **dea_data**：string, 資料所在的路徑位置(path)，必須是csv檔案
- **in_range**：list, 投入資料(input)的行範圍
- **out_range**：list, 產出資料(output)的行範圍
- **assign**：boolean, 是否要指定行數 (default = False) <br>
  - **True**：表示in_range, out_range的值是指定行數。例如，in_range=[2,4]，代表csv檔案中第二行跟第四行的資料要做為input，轉換成字典形式
  - **False**：表示in_range, out_range的值是一個範圍。例如，in_range=[2,4]，代表csv檔案中從第二行至第四行的資料要做為input，轉換成字典形式

### § Notice
- 檔案必須為csv格式，**資料從第一行的第二列開始讀起**，並且首行必須為DMU名稱，首列可為各產出投入資料的名稱，如Example圖所示
- 檔案內數值不能包含逗號
### § Example(以下圖為例)
#### 不指定形式
- 若2-3行為投入，4-6行為產出，則給定資料範圍，並回傳DMU名稱列表(list)及投入項(X)與產出項(Y)資料的字典格式(dict)
```python
DMU, X, Y = csv2dict(“data.csv”, in_range=[2,3], out_range=[4,6],assign=False)
```
#### 指定形式
- 若指定第2、4行為投入，第5、6行為產出，則指定行數，並回傳DMU名稱列表(list)及投入項(X)與產出項(Y)資料的字典格式(dict)
```python
DMU, X, Y = csv2dict(“data.csv”, in_range =[2,4], out_range=[5,6],assign=True)
```
<br>

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/csv2dict_data_example.gif" width="430" height="160">
</div>



##  <h2 id="csv2dict_sep()">csv2dict_sep()</h2>
### § Description
- 用來讀取各決策單位投入與產出資料的csv檔，將資料轉換成字典格式(dictionary type)，以利後續建模使用，與csv2dict()不同的是，此函式主要用於投入與產出資料放於兩個不同檔案時使用。

### § Usage
- csv2dict_sep(dea_data, vrange =[0,0], assign=False)
- 回傳二個值，分別是DMU(list)跟Input/Output(dict)

### § Arguments
- **dea_data**： string, 資料所在的路徑位置(path)，必須是csv檔案
- **vrange**：list, 資料的行範圍 (default=[0,0]，代表全範圍的值皆用於後續建模)
- **assign**：boolean, 是否要指定行範圍 (default = False)<br>
  - **True**：表示vrange的值是指定行數。例如， vrange =[2,4]，代表csv檔案中第二行跟第四行的資料會轉換成字典形式，用於後續建模<br>
  - **False**：表示vrange的值是一個範圍。例如， vrange =[2,4]，代表csv檔案中從第二行至第四行的資料會轉換成字典形式，用於後續建模<br>

### § Notice
- 檔案必須為csv格式，資料從第一行的第二列開始，首行必須為DMU的名稱，首列可為各產出投入資料的名稱，接著緊鄰著投入或產出資料。若無指定特定行做為產出或投入資料，函式會直接從第二行開始讀取，如Example圖所示
- 檔案內數值不能包含逗號
### § Example(以下圖為例)
#### 不指定形式
- 讀取資料，資料名稱為“data_input.csv”，並回傳DMU名稱列表(list)及投入項資料的字典格式(dict)  (在此視讀取資料為投入項，固用X表示)
```python
DMU, X = csv2dict_sep(“data_input.csv”)
```
#### 指定形式
- 假設要讀取資料2跟4行當作產出項，資料名稱為“data_output.csv”，最後回傳DMU名稱列表(list)及產出項字典格式(dict)
```python
DMU, Y = csv2dict_sep(“data_output.csv”, vrange =[2,4], assign=True)
```
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/csv2dictsep_inoutputdata_example.gif" width="500" height="230">
</div>
