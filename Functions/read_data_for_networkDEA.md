# Read data function for network DEA 
*POLab*
<br>
*2018/03/20*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇範例資料取自[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)於2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*

------------

由於Network DEA涉及了決策單位的內部製程(processes)，整體系統以及每個製程都有各自的投入與產出，加上有些製程的產出會成為部分製程的投入，因此，有別於[基本DEA function的讀檔函式](https://github.com/wurmen/DEA/blob/master/Functions/readdata_function.md)，在此對程式的部份內容進行了修改，以利Network DEA function的使用。<br>
在本文中，會對讀檔的函式進行參數及使用說明，並於最後舉兩個例子解說資料要如何給定，對於使用Network DEA function，資料的給定相當重要，因此可能要多花點時間閱讀最後的兩個[範例說明](#Example)。

## csv2dict_for_network_dea()

### § Description
- 用來讀取各決策單位整體系統及各製程投入與產出資料的csv檔，將資料轉換成字典格式(dictionary type)，以利後續建模使用。
### § Usage
- csv2dict_for_network_dea(dea_data, v1_range, v2_range, p_n=0)
- 回傳四個值，分別是DMU(list), V1(dict), V2(dict),p_n(interger)

### § Arguments
- **dea_data**：string, 資料所在的路徑位置(path)，必須是csv檔案
- **v1_range**：list, 整體系統及各製程中，來自外部的投入資料 **(X)** 的行範圍(或者整體系統及各製程中，為系統最終產出 **(Y)** 的行範圍)，內含兩個值-起始行數及結束行數
- **v2_range**：list, 整體系統及各製程中，該投入為來自某內部製程產出資料 **(Z_input)** 的行範圍 (或者整體系統及各製程中，該產出將成為某內部製程投入資料 **(Z_output)** 的行範圍)，內含兩個值-起始行數及結束行數
- **p_n**：interger, 內部製程的數量

### § Notice
- 檔案必須為csv格式，**資料從第一行的第二列開始讀起**，並且首行必須為DMU及各製程的名稱，首列可為各產出投入資料的名稱，如Example所示
- 檔案內數值不能包含逗號

### <h2 id="Example">§ Example </h2>
(※範例執行結果可點擊[這裡](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Read_data_for_network_DEA_function%20example.ipynb))
#### 1.說明
為了簡化Network DEA function的複雜度，在此偏向給定較完整的整體資料來對主函式做使用，首先，必須先釐清整體系統及各製程投入與產出的角色，在Network DEA function中，主要將投入項分為X、Z_input兩個角色，產出項分為Y、Z_output兩個角色，各角色說明如下：<br>
- **X**：來自系統外部的投入
- **Z_input**：該投入是來自某內部製程的產出，在此被視為中間產物的投入項
- **Y**：會成為系統最終產出的產出項
- **Z_output**：只要該產出有部分會成為某內部製程的投入，即被視為中間產物的產出項

#### 2.資料給定建議
建議將X與Z_input兩項資料放置同一csv檔內，形成投入資料，Y與Z_output放在同一csv檔，形成產出資料，再各自透過函式csv2dict_for_network_dea()讀取，回傳X、Z_input及Y、Z_output的字典格式

#### 3.範例
#### ◎ Example1

**題目描述**
- 下圖是一個由三個製程所形成的系統，該系統最初有兩項投入，最終會有三項產出，而系統內部各製程的投入與產出情形，如下圖所示：<br>
1. 系統最初的兩項投入會被分成三個部份分別給製程1、製程2及製程3當成他們各自的投入項。<br>
2. 製程1和製程2的產出會被分成兩個部份，一部份為最終系統產出，另一部份則當成製程3的部份投入項

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/network%20system.PNG" width="550" height="350">
</div>
<br>

**角色釐清**
- **X**：X</sub><sub>1</sup></sub>、X</sub><sub>2</sup></sub>
- **Z_input**：Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub> (對製程3而言)
- **Y**：Y</sub><sub>3</sup></sub>
- **Z_output**：Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub> (對製程1及製程2而言)

**原始產出與投入項數據**
- 共有五個決策單位要進行比較，其系統及各製程的產出與投入情形如下表所示：<br>

##### ※ Y<sup>(O)</sup></sub><sub>1</sup></sub>、Y<sup>(I)</sup></sub><sub>1</sup></sub>：Y<sup>(O)</sup></sub><sub>1</sup></sub>為製程1最終的系統產出，Y<sup>(I)</sup></sub><sub>1</sup></sub>為製程1會成為製程3的部份投入項<br>

##### ※ Y<sup>(O)</sup></sub><sub>2</sup></sub>、Y<sup>(I)</sup></sub><sub>2</sup></sub>： Y<sup>(O)</sup></sub><sub>2</sup></sub>為製程2最終的系統產出，Y<sup>(I)</sup></sub><sub>2</sup></sub>為製程2會成為製程3的部份投入項

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/example-data.PNG" width="800" height="370">
</div>
<br>

**給定資料型式**<br>

- 投入資料(Input data)<br>
1. 第一行為每個決策單位的名稱及各製程的名稱(對於每個決策單位，先寫決策單位名稱接著才是製程名稱)，讀檔程式會自動抓取每個決策單位的名稱，以方便結果的呈現<br>
2. 第一列為各投入資料名稱，讀檔程式會重第一行的第二列開始讀起<br>
3. 整體系統投入共有兩項X</sub><sub>1</sup></sub>、X</sub><sub>2</sup></sub> (X)，投入項是來自某內部製程的產出共有兩項Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub> (Z_input)，將同角色的資料放一起，以利讀檔，另外，雖然Z_input只跟製程三有關，但為了程式給定權重的方便，其他皆補0值。
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example1_inputdata.gif" >
</div>
<br>

- 產出資料(Output data) <br>

最終成為系統產出的產出項有一項Y</sub><sub>3</sup></sub> (Y)，雖然Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub>部分也會成為系統最終產出，但由於它們會有部分給製程3當作製程3的投入，因此，在此將此兩項視為Z_output，如投入資料所述，相同角色的資料放在一起，以利讀檔，且雖然Z_output只跟製程1、2有關，但為了程式給定權重的方便，其他皆補0值。

##### **※注意：基本上，Z_input與Z_output在題目中是相同的，都是Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub>，他們各自擁有相同的權重，只是再給定資料時，對於不同製程所扮演的角色不同，給定的資料也會不同，才會將其分為Z_input與Z_output，因此在投入資料Z_input與產出資料Z_output的順序要相同，才不會使程式再給定權重時發生錯誤。**

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example1_outputdata.gif" >
</div>
<br>

**讀檔方式**<br>
- 投入資料(Input data)<br>

第2-3行為X，第4-5行為Z_input，共有三個製程
```python
 DMU, X, Z_input, p_n=csv2dict_for_network_dea("Input data.csv", v1_range=[2,3], v2_range=[4,5], p_n=3)
```

- 產出資料(Output data)<br>

第2行為Y，第3-4行為Z_output，共有三個製程
```python
 DMU, Y, Z_output, p_n=csv2dict_for_network_dea("Output data.csv", v1_range=[2,2], v2_range=[3,4], p_n=3)
```

#### ◎ Example2
**題目描述**
- 下圖是一個由兩個製程所形成的系統，該系統最初有兩項投入，最終會有兩項產出，而系統內部各製程的投入與產出情形，如下圖所示：<br>
1. 系統最初的兩項投入(X</sub><sub>1</sup></sub>、X</sub><sub>2</sup></sub>)分別被分給製程1、製程2當成他們各自的投入項。<br>
2. 製程1會產生三項產出(Y</sub><sub>1</sup></sub>、Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub>)，其中兩項(Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub>)將成為製程2的投入，剩餘那項(Y</sub><sub>1</sup></sub>)成為系統產出，製程2會產生一項產出(Y</sub><sub>2</sup></sub>)，並會成為系統的產出項

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example2.gif" >
</div>
<br>


**角色釐清**
- **X**：X</sub><sub>1</sup></sub>、X</sub><sub>2</sup></sub>
- **Z_input**：Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub> (對製程2而言)
- **Y**：Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub>
- **Z_output**：Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub> (對製程1而言)

**原始產出與投入項數據**
- 共有七個決策單位要進行比較，其系統及各製程的產出與投入情形如下表所示：<br>
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example2_data.GIF">
</div>
<br>

**給定資料型式**<br>

- 投入資料(Input data)<br>

1.如Example1給定資料格式1、2點所述
2. 整體系統投入共有兩項X</sub><sub>1</sup></sub>、X</sub><sub>2</sup></sub> (X)，投入項是來自某內部製程的產出共有兩項Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub> (Z_input)，將同角色的資料放一起，以利讀檔，另外，雖然Z_input只跟製程2有關，但為了程式給定權重的方便，其他皆補0值。
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example2_inputdata.gif" >
</div>
<br>

- 產出資料(Output data) <br>

最終成為系統產出的產出項有兩項Y</sub><sub>1</sup></sub>、Y</sub><sub>2</sup></sub>(Y)，產出項是會成為某內部製程的投入共有兩項Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub>，如投入資料所述，相同角色的資料放在一起，以利讀檔，且雖然Z_output只跟製程1有關，但為了程式給定權重的方便，其他皆補0值。

##### **※注意：基本上，Z_input與Z_output在題目中是相同的，都是Z</sub><sub>1</sup></sub>、Z</sub><sub>2</sup></sub>，他們各自擁有相同的權重，只是再給定資料時，對於不同製程所扮演的角色不同，給定的資料也會不同，才會將其分為Z_input與Z_output，因此在投入資料Z_input與產出資料Z_output的順序要相同，才不會使程式再給定權重時發生錯誤。**

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Functions/picture/example2_outputdata.gif" >
</div>
<br>

**讀檔方式**<br>
- 投入資料(Input data)<br>

第2-3行為X，第4-5行為Z_input，共有兩個製程
```python
 DMU, X, Z_input, p_n=csv2dict_for_network_dea("Input data.csv", v1_range=[2,3], v2_range=[4,5], p_n=2)
```

- 產出資料(Output data)<br>

第2-3行為Y，第4-5行為Z_output，共有兩個製程
```python
 DMU, Y, Z_output, p_n=csv2dict_for_network_dea("Output data.csv", v1_range=[2,3], v2_range=[4,5], p_n=2)
```
