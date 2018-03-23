# Basic DEA functions

*POLab*
<br>
*2018/03/22*
<br>
[【回到首頁】](https://github.com/wurmen/DEA)

本文主要針對所建立的基本DEA模型函式進行說明: <br>
(※函式執行範例可參考[這裡](https://github.com/wurmen/DEA/blob/master/Functions/basic_DEA_data%26code/basic_DEA_function.ipynb))
* [CRS()](#CRS) <br>
DEA固定規模報酬模型函式
* [VRS()](#VRS) <br>
DEA變動規模報酬模型函式

## <h2 id="CRS">CRS()</h2>
### § Description
- 固定規模報酬DEA模型函式，包含產出導向、投入導向，以及它們的對偶模式

### § Usage
- CRS(DMU, X, Y, orientation, dual)
- 回傳各DMU的效率值

### § Arguments
- **DMU**：list, 記錄所有要被衡量效率值的DMU名稱列表，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(DMU)
- **X**：dict, 記錄每個DMU所對應的投入資料，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(X)
- **Y**：dict, 記錄每個DMU所對應的產出資料，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(Y)
- **orientation**： string, DEA模型定位，用來設定是屬於產出導向output，還是投入導向input
- **dual**： boolean, 決定是(True)否(False)要為對偶模式

## <h2 id="VRS">VRS()</h2>
### § Description
- 變動規模報酬DEA模型函式，包含產出導向、投入導向，以及它們的對偶模式

### § Usage
- VRS(DMU, X, Y, orientation, dual)
- 回傳各DMU的效率值

### § Arguments
- **DMU**：list, 記錄所有要被衡量效率值的DMU名稱列表，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(DMU)
- **X**：dict, 記錄每個DMU所對應的投入資料，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(X)
- **Y**：dict, 記錄每個DMU所對應的產出資料，可放入經由csv2dict()或csv2dict_sep()轉換後的回傳值(Y)
- **orientation**： string, DEA模型定位，用來設定屬於產出導向output，還是投入導向input
- **dual**： boolean, 決定是(True)否(False)要為對偶模式
