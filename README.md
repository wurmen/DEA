# Data-Envelopment-Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

* 最清楚完整的資料包絡分析(Data Envelopment Analysis, DEA)建模流程介紹 [:door:](#DEA_model)
 

* 使用 [Gurobi Python interface](http://www.gurobi.com/resources/seminars-and-videos/modeling-with-the-gurobi-python-interface) 進行線性規劃(Linear Programming)的求解

* 開發擴充函式，方便針對問題進行 DEA 的迅速建模 [:door:](#DEA_function)
(Development of functions for easy and quick DEA modeling)
--------

## Requirements

* Python 3.6

* gurobipy 6.5.2 ([Gurobi Python interface 安裝](https://github.com/wurmen/Gurobi-Python/blob/master/Installation/%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8.md))

* itertools

--------

<h2 id='DEA_model'>DEA 建模流程介紹 </h2>

撰寫 DEA 各種模型的算法與建模流程的文章，目前包含以下模型：

* CRS(constant return to scale; input-oriented) ：固定規模報酬的模型

* VRS(variable return to scale; input-oriented) ：變動規模報酬的模型

* Network DEA：探討系統內部各階段的效率值

完整文章內容請參考以下連結(持續更新中)：

|更新時間|文章|
|---|--|
|2018-01-29|[CRS Model](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS%20model.md)|
|2018-02-05|[VRS Model](https://github.com/wurmen/DEA/blob/master/VAS_Model/VRS%20model.md)|
|2018-01-30|[Network DEA Model](https://github.com/wurmen/DEA/blob/master/Network_DEA/network_dea.md)|


--------

<h2 id='DEA_function'>DEA 擴充函式 </h2>

將 DEA 複雜的建模流程包裝成擴充函式，方便迅速針對問題進行建模與分析。

下載對應的 Repo ，裡面包含擴充函式原始碼、資料(.csv)、以及範例(Jupyter Notebook Example)，再根據說明文件(Documentation)來操作。

完整資源請參考以下連結(持續更新中)：

|更新時間|主題|連結|
|---|---|---|
|2018-03-23|DEA Functions Instructions|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/user's%20guide.md) / Example / Repo|
|2018-03-23|Read data functions for basic DEA models(CRS, VRS)|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Basic DEA models(CRS, VRS)|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/basic_dea_functions.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/basic_DEA_function.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Read data functions for network DEA|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_for_networkDEA.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Read_data_for_network_DEA_function%20example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|
|2018-03-23|Network DEA model|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/network_DEA_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Network_DEA_function_example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|


--------


## 額外資源 (Python-Gurobi Tutorial)
若對 [Gurobi Python interface](http://www.gurobi.com/resources/seminars-and-videos/modeling-with-the-gurobi-python-interface) 的建模較不熟悉，可以參考先前寫的教學資源([Gurobi-Python Repo](https://github.com/wurmen/Gurobi-Python))：

- [環境安裝教學](https://github.com/wurmen/Gurobi-Python/blob/master/Installation/%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8.md)
- [Python+Gurobi基本架構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%9F%BA%E6%9C%AC%E6%9E%B6%E6%A7%8B.md)<br>
- [Python+Gurobi建模](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%BB%BA%E6%A8%A1.md)<br>
- [Python+Gurobi特殊資料結構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python%2BGurobi%E7%89%B9%E6%AE%8A%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B.ipynb)



--------

# Data-Envelopment-Analysis 

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

* The most complete and clear description for DEA algorithms and modeling [:door:](#DEA_model)

* Solve DEA problems with linear programming techniques by [Gurobi Python interface](http://www.gurobi.com/resources/seminars-and-videos/modeling-with-the-gurobi-python-interface)

* Develop functions for easy and quick DEA modeling [:door:](#DEA_function)

* All documentation is written in Chinese.

--------

## Requirements

* Python 3.6

* gurobipy 6.5.2 ([Gurobi Python interface Installation](https://github.com/wurmen/Gurobi-Python/blob/master/Installation/%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8.md))

* itertools

--------

<h2 id='DEA_model'>DEA 建模流程介紹 </h2>

The articles are about DEA models' algorithms and modeling process, including：

* CRS(constant return to scale; input-oriented) ：固定規模報酬的模型

* VRS(variable return to scale; input-oriented) ：變動規模報酬的模型

* Network DEA：探討系統內部各階段的效率值

Please refer to the links below for full contents(updating)：

|更新時間|文章|
|---|--|
|2018-01-29|[CRS Model](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS%20model.md)|
|2018-02-05|[VRS Model](https://github.com/wurmen/DEA/blob/master/VAS_Model/VRS%20model.md)|
|2018-01-30|[Network DEA Model](https://github.com/wurmen/DEA/blob/master/Network_DEA/network_dea.md)|


--------

<h2 id='DEA_function'>DEA 擴充函式 </h2>

將 DEA 複雜的建模流程包裝成擴充函式，方便迅速針對問題進行建模與分析。

下載對應的 Repo ，裡面包含擴充函式原始碼、資料(.csv)、以及範例(Jupyter Notebook Example)，再根據說明文件(Documentation)來操作。

完整資源請參考以下連結(持續更新中)：

|更新時間|主題|連結|
|---|---|---|
|2018-03-23|DEA Functions Instructions|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/user's%20guide.md) / Example / Repo|
|2018-03-23|Read data functions for basic DEA models(CRS, VRS)|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Basic DEA models(CRS, VRS)|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/basic_dea_functions.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/basic_DEA_function.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Read data functions for network DEA|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_for_networkDEA.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Read_data_for_network_DEA_function%20example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|
|2018-03-23|Network DEA model|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/network_DEA_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Network_DEA_function_example.ipynb) / [Repo](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|


--------


## 額外資源 (Python-Gurobi Tutorial)
若對 [Gurobi Python interface](http://www.gurobi.com/resources/seminars-and-videos/modeling-with-the-gurobi-python-interface) 的建模較不熟悉，可以參考先前寫的教學資源([Gurobi-Python Repo](https://github.com/wurmen/Gurobi-Python))：

- [環境安裝教學](https://github.com/wurmen/Gurobi-Python/blob/master/Installation/%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8.md)
- [Python+Gurobi基本架構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%9F%BA%E6%9C%AC%E6%9E%B6%E6%A7%8B.md)<br>
- [Python+Gurobi建模](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%BB%BA%E6%A8%A1.md)<br>
- [Python+Gurobi特殊資料結構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python%2BGurobi%E7%89%B9%E6%AE%8A%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B.ipynb)


Solve DEA problems with linear programming by Gurobi Python interface)
