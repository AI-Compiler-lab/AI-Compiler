# AI-Compiler: Cognitive Freedom Architecture

> 「這是一場以架構靈活性對抗製程暴力與資本壟斷的聖戰。」

## ✦ 專案願景 // Project Vision
在科技巨頭壟斷先進製程（2nm/1nm）與封閉生態（CUDA）的時代，人類的思惟自由正面臨前所未有的審查與控制。本專案致力於打破這種算力極權。

我們透過**「軟體定義晶片 / 空間計算（Spatial Computing）」**的邏輯，將大模型的矩陣演算法直接編譯為物理晶片內部的電路通路。不依賴先進製程，讓全球的自由主義者利用過時、廉價或成熟製程的 14nm 硬體，亦能榨乾最後一滴物理潛能，獨立運行不受審查的大模型。

## ✦ 核心模組 // Core Framework
* **VM Layer**: 將物理晶圓與邏輯應用解耦，實施動態資源按需分配。
* **Hardware Compiler**: 將代碼直接實體化為電子開關的走線與通斷。
* **NTU (Network Transport Unit)**: 物理層動態加密變形，防範國家級 DPI 審查，建立思惟地下鐵路。
* **NPU (Neural Processing Unit)**: 免指令集、純資料流架構，空間換時間硬啃大模型矩陣。
* **Recovery Agent (MoltBot/ClawdBot)**: 全時遙測硬體溫度與網路狀態，實施毫秒級動態避障與操控恢復。

---

## ✦ 本地端快速測試與指令說明 // Quick Test Guide

不論您使用的是 Linux, macOS 或 Windows 系統，只要您的環境裝有 **Python 3.8+** 或 **Docker**，即可依據以下指令在本地端沙盒快速啟動全棧編譯與雙機器人監控流：

### 方案 A：使用原生 Python 啟動（適合本機快速調試）

**1. 複製並進入專案目錄**
```bash
git clone https://github.com
cd AI-Compiler
```

**2. 安裝 WebSocket 通訊依賴套件**
```bash
pip install -r requirements.txt
```

**3. 一鍵啟動全系統總指揮程式**
```bash
python main.py
```
*執行後，您將在終端機看見 `MoltBot` 開始高頻巡檢晶片溫度，並自動在 `localhost:8084` 拉起串流廣播通道。*

---

### 方案 B：使用 Docker 容器啟動（適合 24/7 背景全時落地測試）

若您不希望污染本機 Python 環境，且需要測試它在背景無限次自動重啟的「無單點故障」防禦力，請使用本方案：

**1. 一鍵建置並常駐啟動背景容器**
```bash
docker-compose up -d --build
```

**2. 即時監聽監控日誌與 MoltBot 遙測報告**
```bash
docker logs -f cognitive_node_core
```

**3. 關閉測試容器環境**
```bash
docker-compose down
```

---

## ✦ 節點對齊 // Node Alignment
* **Web Portal**: [https://www.chinesebank.org/AI-Compiler/](https://www.chinesebank.org/AI-Compiler/)
* **IPFS Hash**: QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco
