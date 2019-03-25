# How to run
step 0. (如已有*novel_data.csv*可跳過)用*spyder* Editer運行或是直接將*solr_import.py*跟*solr_retrieve.py*放進與*python.exe*同位置資料夾後，以此資料夾為路徑開啟cmd視窗後輸入以下指令，以獲取*novel_data.csv*資料：
<pre><code>python solr_scraping.py
</code></pre>
step 1. 執行*solr-7.7.0/bin*資料夾內的*start.bat*，確實等待"Happy search!"字樣跑出來

step 2. 用瀏覽器進入 *http://127.0.0.1:8983/solr/#/* ，在Core Admin新增一個Core名為*Assignment1*，並在Schema分別新增*question*和*answer* Field，field type皆為text_general。

step 3. 於0.步驟開啟的cmd視窗輸入以下指令(此步驟後可能需要關掉所有視窗後重新執行1.步驟)：
<pre><code>python solr_import.py
</code></pre>

step 4. 重新用瀏覽器進入 *http://127.0.0.1:8983/solr/#/* 後，確認Query欄位點選Execute Query按鈕後有沒有顯示確實導入了*solr_import.py*內的*QA_Pair_list*，並於3.步驟開啟的cmd視窗輸入以下指令：
<pre><code>python solr_retrieve.py
</code></pre>
step 5. 輸入paper內第四點Experiment下提供的十點測試input。

