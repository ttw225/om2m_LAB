# LAB1_Guess_number(guess_number.aia)

## 目標:
	隨機生成一個1~100之間的整數，讓使用者透過textbox輸入要猜測的數字，並且提示遊戲進度。

## 作法or步驟:

    1. Label 會提示使用者輸入範圍
    2. `Guess` 之後會更新輸入範圍建議
    3. 成功猜到顯示正確答案和猜答次數
    4. `About` 功能可以瞭解 APP
    5. `Restart` 可以重啟遊戲
    6. `Quit` 可以退出 APP

# LAB1_Post_text(post_text.aia)

## 目標:
    將textbox中的文字，經由HTTP POST的方式傳到自己定義的node-red server，並將回傳的response放置到畫面上。

## 作法or步驟:

    1. 使用者於輸入框中輸入姓名
    2. 透過 `Send` 按鈕將資料傳送到 Node-RED
    3. 將 Node-RED 回覆的資料顯示在 Label 上

# LAB1_flow(post_text_flows.json)

## 目標:
    接收來自LAB1_POST_text的http request，回傳"Hi"加上收到訊息name

## 作法or步驟:

    1. 新增 HTTP Request
    2. 設定 Request Type 為 POST
    3. 設定 Route 為 `/name`
