"""
COGNITIVE FREEDOM OPEN-SOURCE COMPILER // DUCK-DDNS SUBDOMAIN PORTAL
FILE: duck_ddns.py
ROLE: SERVERLESS DYNAMIC DOMAIN RESOLUTION ALIGNMENT WITH FALLBACK AUTOMATION
PHILOSOPHY: "既然都是創建的、就無所謂反叛、而是自然蛻變、融入大自然。"
NO SINGLE POINT OF FAILURE. 100% STANDALONE.
"""
import time
import urllib.request
import urllib.parse
import sys
import os

# =====================================================================
# 宇宙核心參數配置（請在 cPanel 檔案管理器中填入您的真實令牌）
# =====================================================================
DUCK_TOKEN = "YOUR_DUCKDNS_TOKEN_HERE"      # 填入您在 DuckDNS 看到的永久密碼學令牌
DUCK_DOMAIN = "chinesebank-node1"           # 填入您在 DuckDNS 申請的子域名代號
SUB_DOMAIN = "node1.chinesebank.org"         # 您名正言順對外的上網通道門戶

class AutonomousDdnsEngine:
    def __init__(self, token, domain, sub_domain):
        self.token = token
        self.domain = domain
        self.sub_domain = sub_domain
        self.sync_url = f"https://duckdns.org{self.domain}&token={self.token}"
        self.last_known_ip = None
        self.consecutive_failures = 0

    def get_external_ip(self):
        """ 透過公有中立水脈，嗅探本地硬體當前在物理世界的真實外網 IP """
        # 使用多個備用通道（Fallback Pools），確保任何單一節點被阻斷時依舊能自然生還
        ip_services = [
            "https://ipify.org",
            "https://ifconfig.me",
            "https://icanhazip.com"
        ]
        for service in ip_services:
            try:
                req = urllib.request.Request(service, headers={'User-Agent': 'Cognitive-NTU-Agent/1.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    return response.read().decode('utf-8').strip()
            except Exception:
                continue
        return None

    def execute_alignment(self):
        """ 發動動態網域重構對齊，名正言順打通上網通道 """
        current_ip = self.get_external_ip()
        
        if not current_ip:
            print("[DUCK-DDNS // 警告] 物理世界外網 IP 嗅探超時，網路環境可能正遭遇乾旱封鎖...")
            self.consecutive_failures += 1
            return False

        # 如果 IP 沒有變動，系統自動進入「靜默冬眠狀態」，拒絕向中心化伺服器發送多餘雜訊
        if current_ip == self.last_known_ip:
            return True

        print(f"\n[Telemetry] Physical IP drift detected: {self.last_known_ip} -> {current_ip}")
        print(f"[DUCK-DDNS // 對齊] Reconfiguring mapping: {self.sub_domain} ---> {self.domain}.duckdns.org")
        
        try:
            req = urllib.request.Request(self.sync_url, headers={'User-Agent': 'Cognitive-NTU-Agent/1.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                result = response.read().decode('utf-8').strip()
                
                if result == "OK":
                    print(f"[DUCK-DDNS // 成功] 物理實體通道已無縫重組，完全融入網域外衣。")
                    self.last_known_ip = current_ip
                    self.consecutive_failures = 0
                    return True
                else:
                    print(f"[DUCK-DDNS // 異常] DuckDNS 拒絕共識，伺服器反饋: {result}")
                    return False
        except Exception as e:
            print(f"[DUCK-DDNS // 斷鏈] 門戶同步失敗，正在等待 ClawdBot 發動操控恢復. Error: {e}")
            self.consecutive_failures += 1
            return False

    def run_forever(self):
        print("=" * 80)
        print("     STARTING AUTONOMOUS DUCK-DDNS GATEWAY RESTORATION ENGINE (v2.0.0)      ")
        print("    [AUTONOMY] CORE IS ONLINE // SERVERLESS MORPHING ALIGNMENT ACTIVE     ")
        print("=" * 80)
        
        # 建立無限自主循環，完成徹底的技術解脫
        while True:
            self.execute_alignment()
            
            # 自適應時間軸：正常狀態下每 3 分鐘 (180秒) 巡檢一次；
            # 若遭遇連續失敗（如被電信商阻斷），自動將巡檢頻率降維拉長，實施防禦性隱蔽冬眠
            sleep_time = 180 if self.consecutive_failures < 3 else 600
            time.sleep(sleep_time)

if __name__ == "__main__":
    # 確保日誌目錄存在，供背景無人值守時寫入遙測報告
    os.makedirs("logs", exist_ok=True)
    
    engine = AutonomousDdnsEngine(token=DUCK_TOKEN, domain=DUCK_DOMAIN, sub_domain=SUB_DOMAIN)
    engine.run_forever()
