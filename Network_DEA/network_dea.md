# Network DEA 

*POLab*
<br>
*2017/01/30*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)
<br>
#### ※*Reference*
*本篇主要參考於[高強教授](http://www.iim.ncku.edu.tw/files/11-1407-20368.php?Lang=zh-tw)在2007發表的Paper：[Efficiency decomposition in network data envelopment analysis: A relational model](https://www.sciencedirect.com/science/article/pii/S0377221707010077)*


## (一)前言

常見的DEA再進行效率衡量時，一般會將整個系統(System)視為一整體，並不探討內部各製程(Process)的狀況，但往往會忽略系統內部製程間的效率，就如在建置[CRS Model](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS%20model.md)所提出的範例般，而高強教授在本篇研究中建構了一個**關聯網絡DEA模型**(Relational network DEA model)，藉由該模型來探討系統內部各製程間的相互關係，並同時衡量系統效率及各製程的效率，通過引入虛擬製程(Dummy processes)，將原始網絡系統轉換為串聯系統，並使串聯中的每個階段都是並行結構，以達到效率分解的目的，透過效率分解，找出導致系統低效運行的製程，以便將來進行改進；**因此在此篇文章中主要是利用paper中的範例及所提出的數學模式來進行說明及建模**

## (二)範例說明
#### ※在此利用paper中第三節所提出的範例進行說明

### § 範例系統架構

- 下圖是一個由三個製程所形成的系統，該系統最初有兩項投入，最終會有三項產出，而系統內部各製程的投入與產出情形，如下圖所示：<br>
1. 系統最初的兩項投入會分成三個部份分別給製程1、製程2、製程3當成他們各自的投入項。<br>
2. 製程1和製程2的產出會被分成兩個部份，一部份為最終系統產出，另一部份則當成製程3的部份投入項

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/network%20system.PNG" width="550" height="350">
</div>
<br>

- 為了能夠達到效率分解，使各製程的效率能夠被衡量，本研究透過加入虛擬製程來將上述系統轉換成一個具有兩個階段(stage)，並且每個階段都是並行結構的系統，如下圖所示：<br>

※ 圖中各個符號表示一併於下面的數學模型進行詳細解釋

<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/network%20system1.png" width="750" height="350">
</div>

##### ※在第三節前本篇研究有提出兩個論點(推論過程可詳閱[原文](https://www.sciencedirect.com/science/article/pii/S0377221707010077))
###### 1. 在一個由串聯結構的製程所形成的系統中，各製程的效率乘積等於整體的效率值
###### 2. 在一個由並形結構的製程所成的系統中，各製程的低效率鬆弛(inefficiency slack)總和等於整體效率的低效率鬆弛
###### 因此在此系統中，整體系統效率值為串聯結構中每個階段效率的乘積，也就是階段1及階段2的效率乘積，而每個階段的低效率鬆弛為並聯結構中，各製程的低效率鬆弛總和，也就是階段1的低效率鬆弛為製程1及製程2都總和，階段2的低效率鬆弛則等於製程3的低效率鬆弛

### § 決策單位各項產出項與投入項數據

- 共有五個決策單位要進行比較，其系統及各製程的產出與投入情形如下表所示：
<div align=center>
<img src="https://github.com/wurmen/DEA/blob/master/Network_DEA/pictures/example-data.PNG" width="800" height="370">
</div>

## (三)數學模型
上述的系統可形成如下所示的數學模型

### § 符號說明

- E<sub>k</sup></sub>： 決策單位k的效率值
- n： 決策單位(DMU)個數 (在此例中n=5)<br>
- ε： 極小的正值稱之為非阿基米德數(non-Archimedean constant)，通常設為10<sup>-4</sup></sub>或10<sup>-6</sup></sub>(目的為了使任一投入或產出項皆不會被忽略)

### § 參數說明

- X<sub>ij</sup></sub>： 決策單位j (j=1,...,n)的整體系統中，最初的第i (i=1,...,m)個投入項 (在此例中m=2)

- X<sup>(t)</sup></sub><sub>ij</sup></sub>： 決策單位j (j=1,...,n)在製程t的第i個投入項 (在此例中t=1,2,3、i=1,2)

- Y<sup>(O)</sup></sub><sub>1j</sup></sub>、Y<sup>(I)</sup></sub><sub>1j</sup></sub>： 決策單位j (j=1,...,n)製程1的產出項，Y<sup>(O)</sup></sub><sub>1j</sup></sub>為最終的系統產出，Y<sup>(I)</sup></sub><sub>1j</sup></sub>會成為製程3的部份投入項

- Y<sup>(O)</sup></sub><sub>2j</sup></sub>、Y<sup>(I)</sup></sub><sub>2j</sup></sub>： 決策單位j (j=1,...,n)製程1的產出項，Y<sup>(O)</sup></sub><sub>2j</sup></sub>為最終的系統產出，Y<sup>(I)</sup></sub><sub>2j</sup></sub>會成為製程3的部份投入項

- Y<sub>ij</sup></sub>： 決策單位j (j=1,...,n)在製程i的總產出

### § 決策變數
- u<sub>r</sup></sub>： 第r個產出項之權重 (在此例中r=1,2,3)
- v<sub>i</sup></sub>： 第i個投入項之權重 (在此例中i=1,2)













