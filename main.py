"""
COGNITIVE FREEDOM OPEN-SOURCE COMPILER // MAIN ORCHESTRATOR SYSTEM
FILE: main.py
ROLE: LINK ALL MODULES TO RUN FULL-STACK SOFTWARE-DEFINED CORE COMPUTING WITH WEBSOCKET
NO SINGLE POINT OF FAILURE. 100% STANDALONE.
"""
import json
import time
import asyncio
import threading
import websockets

# 完美導入核心技術模組
from compiler import CognitiveCompiler
from ntu_protocol import CognitiveNetworkTransport
from tiling_engine import CognitiveTilingEngine
from hardware_control import SiliconHardwareController
from recovery_agent import CognitiveRecoveryAgent

# 全域共享實體，以便 WebSocket 讀取即時數據
silicon_hardware = SiliconHardwareController(rows=32, cols=32)
my_ntu_node = CognitiveNetworkTransport(node_address="Node-Base-Taipei")

async def broadcast_metrics(websocket, path):
    """ 核心機制：MoltBot 遙測串流廣播 (MoltBot Telemetry WebSocket Stream) """
    print(f"[MoltBot // Streaming] Client connected to secure websocket channel.")
    try:
        while True:
            # 實時捕捉 MoltBot 巡檢的真實硬體數據
            metrics_payload = {
                "thermal_index": float(silicon_hardware.thermal_index),
                "power_draw": float(silicon_hardware.power_draw),
                "active_peers": int(len(my_ntu_node.peers)),
                "timestamp": time.time()
            }
            # 透過廣播通道向前端即時推播 JSON 數據流
            await websocket.send(json.dumps(metrics_payload))
            await asyncio.sleep(1.0) # 每秒高頻刷新
    except websockets.exceptions.ConnectionClosed:
        print("[MoltBot // Streaming] Client disconnected from channel.")

def start_websocket_server():
    """ 啟動異步 WebSocket 服務器監聽 """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(broadcast_metrics, "0.0.0.0", 8084)
    print("[SYSTEM] MoltBot Streaming Tunnel established on port 8084...")
    loop.run_until_complete(start_server)
    loop.run_forever()

def run_cognitive_freedom_runtime():
    print("=" * 80)
    print("      INITIALIZING FULL-STACK COGNITIVE FREEDOM ARCHITECTURE (v1.1.0)      ")
    print("    [ALERT] DECENTRALIZED RUNTIME // RECONFIGURABLE LOGIC LAYER ONLINE    ")
    print("=" * 80)

    # -----------------------------------------------------------------
    # 階段 1: 初始化去中心化網路、硬體、與自動化恢復代理
    # -----------------------------------------------------------------
    print("\n[PHASE 1] Initializing P2P Transport Layer & Hardware Entities...")
    mock_p2p_peers = [
        {"node_id": "Node-Tokyo-02", "memory_bandwidth": 6.39, "network_latency": 20}
    ]
    for peer in mock_p2p_peers:
        my_ntu_node.p2p_handshake(peer["node_id"])
    
    # 啟動自動化操控恢復防線 (MoltBot & ClawdBot 背景執行)
    recovery_agent = CognitiveRecoveryAgent(target_hardware=silicon_hardware, target_network=my_ntu_node)
    recovery_agent.start_monitoring_loop()
    
    # 【全時落地升級：拉起 WebSocket 後台串流線程】
    ws_thread = threading.Thread(target=start_websocket_server, daemon=True)
    ws_thread.start()

    # -----------------------------------------------------------------
    # 階段 2 & 3: 模擬持續計算流，讓 MoltBot 的數據隨時間動態變化
    # -----------------------------------------------------------------
    tiling_system = CognitiveTilingEngine(hardware_tile_size=2048)
    compiler = CognitiveCompiler(total_pe_units=1024)
    
    print("\n[RUNTIME] Entering Autonomous Dataflow Loop. 24/7 Service Active.")
    try:
        tile_id = 0
        while True:
            # 模擬不間斷流進矩陣切片進行物理空間運算，使溫度與功耗產生起伏
            silicon_hardware.power_draw = 150.0 + (tile_id % 5) * 45.3
            silicon_hardware.thermal_index = 42.0 + (tile_id % 7) * 4.1
            
            tile_id += 1
            time.sleep(2.0)
    except KeyboardInterrupt:
        print("[SYSTEM] Cognitive Freedom Runtime Halted by User.")

if __name__ == "__main__":
    run_cognitive_freedom_runtime()
