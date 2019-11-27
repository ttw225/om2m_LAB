# LAB2_Get_Sensor_Value(get_sensor_value.aia)
## 目標:

    按下按鈕時，抓取手機上的三種sensor，Accelerometer、OrientationSensor、LocationSensor

## 作法or步驟:

    1. 加入三種 Sensor
    2. 依序顯示內容

# LAB2_Show_Location_on_Google.aia(map.aia)

## 目標:

    實現五個功能:
        1. 抓取LocationSensor(GPS)
        2. 將1中的值傳到node-red顯示
        3. 讀取server存放的location資料
        4. (5)將1(3)中的資料用google map定位

## 作法or步驟:

    1. Sensor 端皆直接抓取
    2. Server 端需要 parsing 取得的字串
    3. 透過 Android Action 啟動 Google Map 並帶入經緯度

# LAB2_flow.json(flow.json))

## 目標:

    1. 接受來自app的訊息，並回復response
    2. 回傳在server儲存的location data

## 作法or步驟:

    1. 從 APP POST 經緯度資料
    2. 從 APP GET 經緯度資料