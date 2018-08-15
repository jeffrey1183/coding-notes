# MATLAB



之前的筆記：[https://legacy.gitbook.com/book/jeffrey1183/pm-matlab/edit\#/edit/master/README.md?\_k=f77zli](https://legacy.gitbook.com/book/jeffrey1183/pm-matlab/edit#/edit/master/README.md?_k=f77zli)



## Record and Play Audio

[document](https://www.mathworks.com/help/matlab/import_export/record-and-play-audio.html)document 就可以學很多東西

看到 

```text
y = getaudiodata(recObj);
```

步驟

* 創建一個 object
* 印出文字，開始錄音
  * [display method](https://www.mathworks.com/help/matlab/ref/disp.html)
  * [Record audio](https://www.mathworks.com/help/matlab/ref/audiorecorder.recordblocking.html)

重要知識

* [numeric types, double-precision array ](https://www.mathworks.com/help/matlab/numeric-types.html)



## Signal Processing with MATLAB

[Signal Processing with MATLAB](https://www.mathworks.com/videos/signal-processing-with-matlab-88866.html)

* 這個才是我要的，上次看到這個
* [Medium 編輯](https://medium.com/@jeffreywang1183/%E7%94%A8-matlab-%E5%81%9A%E9%9F%B3%E8%A8%8A%E8%99%95%E7%90%86-%E9%9F%B3%E6%A8%82%E7%A7%91%E6%8A%80%E7%B6%B2-6aa5b07129df)

[Signal Processing and Machine Learning Techniques for Sensor Data Analytics](https://www.mathworks.com/videos/signal-processing-and-machine-learning-techniques-for-sensor-data-analytics-107549.html)

下面就有很多很棒的音訊處理內容 **Related Videos and Webinars**

## Onramp

Adding a semicolon to the end of a command will suppress the output, though the command will still be executed, as you can see in the **Workspace**. When you enter a command without a semicolon at the end, When you enter a command without a semicolon at the end, MATLAB displays the result in the command window.

[使用分號的時機](https://www.quora.com/When-and-why-do-we-use-semicolons-in-matlab)

按上可以叫出之前的 command

When you enter just a variable name at the command prompt, MATLAB returns the current value of that variable.

## Deep Learning Matlab Onramp

使用 pretrained network 去辨識圖片

在 add-on 裡找 pretrained network 會找到 alexnet ，但他要先裝 [Neural Network Toolbox](https://www.mathworks.com/products/neural-network.html) 這個 Matlab Toolbox，價值 29 美金，可以先在 alexnet 的畫面找到 neutral network toolbox，然後再試用

我還沒裝 

看到 2-2 的 [obtaining pretrained network](https://matlabacademy.mathworks.com/R2018a/portal.html?course=deeplearning#chapter=2&lesson=2&section=2)



## File Exchange

[開源平台](https://www.mathworks.com/matlabcentral/fileexchange/)



[Python 與 Matlab](https://www.zhihu.com/question/21404521)



[鼓手的故事](https://www.mathworks.com/company/mathworks-stories/prosthetics-for-drummer.html.html?s_eid=PSM_brj.html)

\[週五放輕鬆\] 一個天生的鼓手必須截肢，如何再次回到音樂路上? 義肢多加一支鼓棒~人工智慧創造與音樂家互動新時代!內有影片&gt;&gt;[https://goo.gl/Mz41TV](https://goo.gl/Mz41TV)

Jason Barnes因意外失去了鼓手必須的靈活手腕，最初他自製了彈簧義肢 以獲得亞特蘭大音樂媒體學院（AIMM）的入學資格，之後在學校幫助下與喬治亞科技大學音樂科技中心\(GTCMT\)進行新的義肢研發專案。新的義肢被設計成擁有兩支鼓棒， 一支可依照Jason的意志進行演奏，另一支則是靠人工智慧自由的配合音樂家演奏。

利用MATLAB&Simulink打造機械構造並不難，短短半年，新的義肢便已完成~透過在他的二頭肌上使用肌電圖（EMG）感測器進行電子控制，並具備超越人類的每秒20下擊鼓速度 ，但如何讓另一支鼓棒可以透過人工智慧（AI）來檢測他的擊鼓中的節拍，節奏和頻率並以一種與其“聽到”相匹配的節拍作出回應，便是一大挑戰了! 研發團隊利用MATLAB 的機器學習以及深度學習演算法， 離線組合非常豐富和結構化的音樂。

這樣的手臂還有很多需要改進的地方，但可以幫助因意外失去手臂的Jason持續追尋夢想，很多的努力是值得的  
看全文&gt;&gt;[https://goo.gl/Mz41TV](https://l.facebook.com/l.php?u=https%3A%2F%2Fgoo.gl%2FMz41TV&h=AT3_ri3AiNQNKQ1KUpcoH627StV8S45t8YnOSRNTXskkazx_m4dFm17oeP-a9JaVoPqRG6Q_guxjM9TfUrU0w1_pYsQWoqfjGPqm-2F1gdp3SxubQaZQi8hbC85jhwBL-FlyJoIkO7XZiGgWSukB84snITChEg)

台灣區 [\#MATLAB](https://www.facebook.com/hashtag/matlab?source=feed_text) [\#Simulink](https://www.facebook.com/hashtag/simulink?source=feed_text) 活動最新消息盡在 [\#鈦思科技](https://www.facebook.com/hashtag/%E9%88%A6%E6%80%9D%E7%A7%91%E6%8A%80?source=feed_text):[www.terasoft.com.tw](https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.terasoft.com.tw%2F&h=AT15K4CWYm5X7lXydJkUTkdbQmFVyamEphgYgiWcOI1wTbs_ARBchsIQnOUGYQtqxA2hoRYZtTq756sGnB2jVkXWOzeF1oslNL99I1KCDeroBR_AqewglCPN-tBM6c4g9h1fmB5QPjuPk-yoytCLvjTRRs5Xjw)





