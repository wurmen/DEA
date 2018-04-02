# Data-Envelopment-Analysis
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)<br>

在此主要透過一些範例來說明如何利用Python-Gurobi來建構資料包絡分析模組(Data-Envelopment-Analysis, DEA)

### § Requirements

- python 3.6

- gurobipy 6.5.2 以上版本

### § DEA Models
此區文章主要針對以下DEA模型進行簡介，並說明Python-Gurobi的建模流程：

- CRS(constant return to scale; input-oriented) ：固定規模報酬投入導向模型

- VRS(variable return to scale; input-oriented) ：變東規模報酬投入導向模型

- Relational network DEA Model ：關聯網絡DEA模型

|更新時間|文章|
|---|---|
|2018-01-29|[CRS Model](https://github.com/wurmen/DEA/blob/master/CRS_Model/CRS%20model.md)|
|2018-02-05|[VRS Model](https://github.com/wurmen/DEA/blob/master/VAS_Model/VRS%20model.md)|
|2018-01-30|[Relational network DEA Model](https://github.com/wurmen/DEA/blob/master/Network_DEA/network_dea.md)|

### § DEA Models Functions
針對上述DEA模型建構幾個簡單的DEA擴充函數，讓使用者能夠更輕鬆的利用這些DEA函數來進行效率分析，或者可由這些已建好的函數去做延伸。<br>

以下連結分別對應到每個主題的說明文章、範例文章、程式碼以及檔案資料夾(內部包含該主題的所有資源)，可根據說明文章自行下載操作學習。

|更新時間|文章|連結|
|---|---|---|
|2018-03-23|DEA Functions Instructions|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/user's%20guide.md)|
|2018-03-23|Read data functions for basic DEA models|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/read_data_example.ipynb) / [Code](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/DEA.py) / [Folder](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Basic DEA functions|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/basic_dea_functions.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/basic_DEA_function.ipynb) / [Code](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/DEA.py) / [Folder](https://github.com/wurmen/DEA/tree/master/Functions/basic_DEA_data%26code)|
|2018-03-23|Read data function for network DEA|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/read_data_for_networkDEA.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Read_data_for_network_DEA_function%20example.ipynb) / [Code](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/network_function.py) / [Folder](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|
|2018-03-23|Relational network DEA function|[Documentation](https://github.com/wurmen/DEA/blob/master/Functions/network_DEA_function.md) / [Example](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/Network_DEA_function_example.ipynb) / [Code](https://github.com/wurmen/DEA/blob/master/Functions/network_data%26code/network_function.py) / [Folder](https://github.com/wurmen/DEA/tree/master/Functions/network_data%26code)|
--------
### 參考資源(Python-Gurobi)
若對python-gurobi的建模較不熟悉，可參考下面資源~
- [環境安裝教學](https://github.com/wurmen/Gurobi-Python/blob/master/Installation/%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8.md)
- [Python+Gurobi基本架構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%9F%BA%E6%9C%AC%E6%9E%B6%E6%A7%8B.md)<br>
- [Python+Gurobi建模](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%BB%BA%E6%A8%A1.md)<br>
- [Python+Gurobi特殊資料結構](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python%2BGurobi%E7%89%B9%E6%AE%8A%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B.ipynb)

