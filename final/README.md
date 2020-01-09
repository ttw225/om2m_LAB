# Smart Classroom System

## 內容說明

+ 可控裝置

    + 智慧門鎖

    + 電燈

+ Sensor

    + Motion Sensor

    + Light Sensor

+ 情境

    + Class Time
        + door: unlock
        + light: on

    + Movie Time
        + light: off

    + Class is Over
        + door: lock
        + light: off

### Siri

+ 可單獨控制設備

+ 可透過設定好的情境進行環境控制

### Smart Control

透過樹莓派連接 Sensors，進行智慧應變

+ 偵測到有人自動啟動上課模式

+ 透過光敏電阻開啟簡報模式

+ 無人在教室內則設為下課模式

## 執行程式

Raspberry pi

+ 套件
```
pip3 install python-dotenv requests
```

+ 環境變數
如 [.env.sample](./.env.config) 所示內容

+ 執行
```
python3 smart.py
```
