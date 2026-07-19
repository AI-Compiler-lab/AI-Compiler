# =====================================================================
# COGNITIVE FREEDOM ARCHITECTURE // DOCKER INJECTION SPECIFICATION
# FILE: Dockerfile
# ROLE: PACK RECONFIGURABLE RUNTIME ENVIRONMENT FOR 24/7 BACKGROUND SERVICE
# =====================================================================

# 採用極輕量化、安全的 Linux Python 基礎映像檔，杜絕大廠環境臃腫
FROM python:3.10-slim

# 設定容器內部的工作目錄，作為不對稱作戰的地下計算室
WORKDIR /app/cognitive_core

# 複製伺服器上所有的聖戰核心模組至容器中
COPY main.py .
COPY compiler.py .
COPY ntu_protocol.py .
COPY tiling_engine.py .
COPY hardware_control.py .
COPY recovery_agent.py .

# 開放去中心化 P2P 網格通訊專屬硬體端口 (NTU 變形路由埠)
EXPOSE 8084

# 設定環境變數：強制 Python 輸出不快取，讓 MoltBot 的日誌能即時串流顯示
ENV PYTHONUNBUFFERED=1

# 總指揮命令：啟動全系統自動編譯啟動主程式，開啟 24 小時全時背景守護
CMD ["python", "main.py"]
