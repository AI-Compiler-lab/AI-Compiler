"""
COGNITIVE FREEDOM OPEN-SOURCE COMPILER // CLOUDFLARE DDNS PORTAL TUNNEL
FILE: cf_ddns.py
ROLE: BYPASS CPANEL BLOCK. OVERRIDE POINTING OF CHINESEBANK.ORG TO LOCAL HARDWARE VIA CLOUDFLARE API
NO SINGLE POINT OF FAILURE. 100% STANDALONE.
"""
import time
import json
import urllib.request

# =====================================================================
# 核心參數配置（完美鏈結您的 Cloudflare 加密盾牌）
# =====================================================================
CF_API_TOKEN = "YOUR_CLOUDFLARE_API_TOKEN_HERE"  # 填入您的 Cloudflare API 令牌
ZONE_ID = "YOUR_CLOUDFLARE_ZONE_ID_HERE"        # 填入您的網域區域識別碼
RECORD_ID = "YOUR_DNS_RECORD_ID_HERE"          # 填入該 node1 紀錄的特定 ID
SUB_DOMAIN = "node1.chinesebank.org"            # 您名正言順的外部上網通道

def get_current_physical_ip():
    """ 透過開源公有通道，嗅探你本地 14nm 硬體當前在物理世界的真實外網 IP """
    try:
        with urllib.request.urlopen("https://ipify.org", timeout=10) as resp:
            return json.loads(resp.read().decode('utf-8'))["ip"]
    except Exception:
        return None

def update_cloudflare_dns(current_ip):
    """ 調用 Cloudflare 全球開放 API，強行重構網域指標 """
    url = f"https://cloudflare.com{ZONE_ID}/dns_records/{RECORD_ID}"
    
    payload = {
        "type": "A",
        "name": SUB_DOMAIN,
        "content": current_ip,
        "ttl": 120,        # 設定極短生存時間（2分鐘），確保 IP 改變時全球秒級對齊
        "proxied": True    # 開啟小雲朵代理，徹底隱藏你家裡主機的真實物理 IP
    }
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {CF_API_TOKEN}",
            "Content-Type": "application/json"
        },
        method="PUT"
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            if res_data.get("success"):
                print(f"[CF-DDNS SUCCESS] Domain [{SUB_DOMAIN}]一箭穿心綁定物理實體 IP: {current_ip}")
            else:
                print(f"[CF-DDNS WARNING] API error response: {res_data}")
    except Exception as e:
        print(f"[CF-DDNS CRITICAL] Failed to touch Cloudflare wall. Error: {e}")

def run_ddns_daemon():
    print("=" * 70)
    print("   LAUNCHING UNRESTRICTED CLOUDFLARE DDNS RESTORATION TUNNEL SUITE   ")
    print("=" * 70)
    
    last_ip = None
    while True:
        current_ip = get_current_physical_ip()
        if current_ip and current_ip != last_ip:
            print(f"\n[Telemetry] Physical IP drift detected: {last_ip} -> {current_ip}")
            update_cloudflare_dns(current_ip)
            last_ip = current_ip
            
        # 每 3 分鐘自動對齊，確保上網通道 24 小時名正言順地敞開
        time.sleep(180)

if __name__ == "__main__":
    run_ddns_daemon()
