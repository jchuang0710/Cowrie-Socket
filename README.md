1. 將 wazuh.py 放入 wazuh agent 執行，他會監聽 9999 port，並執行收到的指令
2. 將 cowrie.py 放入 cowrie 目錄底下執行，他會監控 ./var/log/cowrie/cowrie.log 的內容，如果有更動，會讀取新的部分，判斷 event 是不是 input，如果是就會傳遞 input 給 wazuh.py
