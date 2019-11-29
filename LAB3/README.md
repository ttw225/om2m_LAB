# LAB3_OM2M with Postman
## 目標:
    使用Postman分別建立以下Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
			6. Create a "Subscription" contact to localhost:1400/monitor

## 作法or步驟:
    1. Create "MY_SENSOR" Application through "POST application"
	2. Create "DESCRIPTOR" through "POST container"
	3. Create "DESCRIPTOR contentInsances" through "POST Descriptor contentInstances"
	4. Create "DATA" through "POST Data"
	5. Create "DATA contentInsances" through "POST Data contentInstances"
	6. Create "Subscription" through "POST subscribe data"


## Datas

+ [postman](/om2m.postman_collection.json)

+ postman data
![postman_data](/img/postman_data.png)

+ postman subscribe
![postman_subscribe](/img/postman_subscribe.png)


# LAB3_OM2M GA with Node-red
## 目標:
    使用 node-red 在GSCL分別建立以下 Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
	6. 在 GA(node-red) 開啟 /sensorData Server 負責轉傳 data 到 OM2M
	

## 作法or步驟:
    1. Add Application to add application
	2. Add Data-Container to add container
	3. Add Data-ContentInstance to add datas
	4. Add Descriptor-Container to add description container
	5. Add Descriptor-ContentInstance to add descriptor content instances
	6. Change Data-ContentInstance's Input from `timestamp` to `Post Sensor Data`, the node will listen to `/sensorData`

## Data

+ [Node-RED](/flows_GA.json)


# LAB3_OM2M  NA with Node-red
## 目標:

    使用 node-red 在 NSCL 分別建立以下 Entities
	1. Create a "MY_NETWORK_APPLICATION"
	2. Subscribe new contentInsatnace in the gscl/MYSENSOR/DATA 並儲存
	3. 開啟 /getxmlfile Server 負責讀取先前儲存的資料

## 作法or步驟:
    1. Add Application "MY_NETWORK_APPLICATION"
	2. Add Subscription to subscribe `gscl/MYSENSOR/DATA`
	3. Add an input listen to `/notification` and save data to `notification.xml`
	4. Add `/readSensorData` to show step 3's xml file

## Data

+ [Node-RED](/flows_NA.json)
