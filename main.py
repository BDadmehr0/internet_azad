import requests
import json
import base64
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

console = Console()

def fetch_encoded_content(url_list, all_protocols):
    for url in tqdm(url_list, desc="Fetching encoded URLs", unit="URL"):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            content = response.text
            decoded_content = base64.urlsafe_b64decode(content).decode("utf-8")
            
            for line in decoded_content.splitlines():
                line = line.strip()
                if (
                    line.startswith("vmess://")
                    or line.startswith("vless://")
                    or line.startswith("ss://")
                    or line.startswith("trojan://")
                ):
                    all_protocols.append(line)

        except requests.exceptions.RequestException as e:
            console.print(f"[red]Error in {url}: {e}[/red]")

encoded_urls = [
    "https://github.com/Mohammadgb0078/IRV2ray/raw/refs/heads/main/vmess.txt",
]

urls = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes",
    "https://raw.githubusercontent.com/245237866/v2rayn/main/everydaynode",
    "https://raw.githubusercontent.com/Creativveb/v2configs/main/updated",
    "https://raw.githubusercontent.com/imohammadkhalili/V2RAY/main/Mkhalili",
    "https://raw.githubusercontent.com/Jia-Pingwa/free-v2ray-merge/main/output.txt",
    "https://raw.githubusercontent.com/jikelonglie/meskell/main/meskell",
    "https://raw.githubusercontent.com/budamu/clashconfig/main/v2ray.txt",
    "https://raw.githubusercontent.com/budamu/clashconfig/main/v2ray2.txt",
    "https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt",
    "https://raw.githubusercontent.com/mfuu/v2ray/master/merge/merge.txt",
    "https://raw.githubusercontent.com/resasanian/Mirza/main/mirza-all.txt",
    "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub.txt",
    "https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt",
    "https://raw.githubusercontent.com/SamanValipour1/My-v2ray-configs/main/MySub.txt",
    "https://raw.githubusercontent.com/YasserDivaR/pr0xy/main/ShadowSocks2021.txt",
    "https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/all.txt",
    "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/main/config.txt",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub1.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub2.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub3.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub4.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub5.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub6.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub7.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub8.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Realm",
    "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Iran/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/United%20Kingdom/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/France/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Ireland/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Germany/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Sweden/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Finland/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Czech%20Republic/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Poland/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Netherlands/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Italy/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Costa%20Rica/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Austria/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Switzerland/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Singapore/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Bahrain/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Slovak%20Republic/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/China/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/United%20States/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Turkey/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/United%20Arab%20Emirates/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Hong%20Kong/config.txt",
]

all_protocols = []

fetch_encoded_content(encoded_urls, all_protocols)

for url in tqdm(urls, desc="Fetching URLs", unit="URL"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        for line in response.text.splitlines():
            line = line.strip()
            if (
                line.startswith("vmess://")
                or line.startswith("vless://")
                or line.startswith("ss://")
                or line.startswith("trojan://")
            ):
                all_protocols.append(line)

    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error in {url}: {e}[/red]")

with open("all_protocols.json", "w", encoding="utf-8") as f:
    json.dump(all_protocols, f, indent=4, ensure_ascii=False)

# Display the results in a table
table = Table(title="Collected Protocols")
table.add_column("Protocol", justify="right", style="cyan", no_wrap=True)
table.add_column("Count", style="magenta")

protocol_counts = {
    "vmess": 0,
    "vless": 0,
    "ss": 0,
    "trojan": 0
}

for protocol in all_protocols:
    if protocol.startswith("vmess://"):
        protocol_counts["vmess"] += 1
    elif protocol.startswith("vless://"):
        protocol_counts["vless"] += 1
    elif protocol.startswith("ss://"):
        protocol_counts["ss"] += 1
    elif protocol.startswith("trojan://"):
        protocol_counts["trojan"] += 1

for protocol, count in protocol_counts.items():
    table.add_row(protocol, str(count))

console.print(table)
console.print(f"[green]Collected {len(all_protocols)} protocol lines.[/green]")