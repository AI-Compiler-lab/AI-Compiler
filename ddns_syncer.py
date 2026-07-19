"""
COGNITIVE FREEDOM OPEN-SOURCE COMPILER // DDNS PORTAL TUNNEL SYNCER
FILE: ddns_syncer.py
ROLE: AUTOMATICALLY UPDATE CHINESEBANK.ORG DDNS POINTER TO LOCAL PHYSICAL NODE
NO SINGLE POINT OF FAILURE. 100% STANDALONE.
"""
import time
import urllib.request
import urllib.parse

# 完美鏈結你的專屬網域權柄
DDNS_TOKEN = "YOUR_CPANEL_DDNS_TOKEN_HERE"
DDNS_DOMAIN = "node1.chinesebank.org"

def sync_physical_node_to_domain():
    print(f"[DDNS PORTAL] Initiating Dynamic Domain Sync Sequence for [{DDNS_DOMAIN}]...")
    
    # 網域商（cPanel）提供的動態更新網址 (此處模擬標準 cPanel DDNS API)
    cpanel_ddns_url = f"https://chinesebank.org{DDNS_TOKEN}"
    
    while True:
        try:
            # 遠端握手，告知伺服器：我這台 14nm 實體晶片目前的真實物理 IP 是多少
            req = urllib.request.Request(cpanel_ddns_url, headers={'User-Agent': 'Cognitive-NTU-Agent/1.0'})
            with urllib.request.urlopen(req) as response:
                result = response.read().decode('utf-8')
                print(f"[DDNS SUCCESS] Node mapped successfully to domain. Server Response: {result}")
        except Exception as e:
            print(f"[DDNS WARNING] Link temporarily blocked or timeout. Retry scheduled. Error: {e}")
            
        # 每 5 分鐘自動對齊一次，確保上網通道 24 小時名正言順地敞開
        time.sleep(300)

if __name__ == "__main__":
    sync_physical_node_to_domain()
