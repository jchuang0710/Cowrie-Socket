# Wazuh agent
1. 將 wazuh.py 放入 wazuh agent 執行，他會監聽 9999 port，並執行收到的指令
2. 將 cowrie.py 放入 cowrie 目錄底下執行，他會監控 ./var/log/cowrie/cowrie.json 的內容，如果有更動，會讀取新的部分，判斷 event 是不是 cowrie.command.input，如果是就會傳遞 input 給 wazuh.py
3. 有些很長但不是 input 的 json 讀取會有錯誤產生，所以我用 try 來忽略它

# Wazuh api
1. wazuh api 會透過 9200 去跟 wazuh indexer 要 data
2. data 要求的類型我設為取得特定 ip 最新的 data
3. 如需更改要求只需修改 data 的部分

# 還原 VM 狀態
1. 使用指令 <code> virt-install --name CentOS_8_Server --memory 2048 --vcpus 1 --disk snapshot-name.qcow2,bus=sata --import --os-variant centos8 --network default </code>
2. 記得選 deny ，不然會點不到 host 虛擬機
## 參考資料
* https://ostechnix.com/create-a-kvm-virtual-machine-using-qcow2-image-in-linux/
