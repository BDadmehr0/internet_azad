import requests
import json
import base64
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from datetime import date

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
    "https://raw.githubusercontent.com/Mohammadgb0078/IRV2ray/refs/heads/main/vmess.txt",
    "https://raw.githubusercontent.com/Mohammadgb0078/IRV2ray/refs/heads/main/vless.txt",
    "https://raw.githubusercontent.com/freefq/free/refs/heads/master/v2",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/mixed",
    "https://nodefree.githubrowcontent.com/2024/07/20240705.txt",
    "https://raw.githubusercontent.com/wrfree/free/refs/heads/main/v2",
    "https://raw.githubusercontent.com/wrfree/free/refs/heads/main/ssr",
    "https://raw.githubusercontent.com/codingbox/Free-Node-Merge/refs/heads/main/node.txt",
    "https://raw.githubusercontent.com/Lewis-1217/FreeNodes/refs/heads/main/bpjzx1",
    "https://raw.githubusercontent.com/Lewis-1217/FreeNodes/refs/heads/main/bpjzx2",
    "https://shadowmere.xyz/api/b64sub/",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/refs/heads/main/splitted/hysteria2",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/shadowsocks",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/refs/heads/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/shadowsocks",
    "https://raw.githubusercontent.com/AzadNetCH/Clash/refs/heads/main/AzadNet_iOS.txt",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/tuic",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/hysteria",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/juicity",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/reality",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/trojan",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/vless",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/protocols/vmess",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/trojan",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/ss",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/tuic",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/hysteria",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/juicity",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/reality",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/trojan",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/vless",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/refs/heads/main/channels/protocols/vmess",
    # "",
    # "",
    # "",
    # "",
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
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/United%20States/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Turkey/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/United%20Arab%20Emirates/config.txt",
    "https://raw.githubusercontent.com/Epodonios/bulk-xray-v2ray-vless-vmess-...-configs/main/sub/Hong%20Kong/config.txt",
    "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_RAW.txt",
    "https://raw.githubusercontent.com/vxiaov/free_proxies/refs/heads/main/links.txt",
    "https://raw.githubusercontent.com/HakurouKen/free-node/main/public",
    "https://github.com/halfaaa/Free/blob/main/1.30.2023.txt",
    "https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/SSTime",
    "https://robin.nscl.ir/",
    "https://raw.githubusercontent.com/Proxydaemitelegram/Proxydaemi44/refs/heads/main/Proxydaemi44",
    "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/speed.txt",
    "https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Vless",
    "https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Reality",
    "https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/SS",
    "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/refs/heads/main/server.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/refs/heads/main/Sub1.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/refs/heads/main/Sub2.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/refs/heads/main/Sub3.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Splitted-By-Protocol/vmess.txt",
    # "",
    # "",
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

protocol_counts = {"vmess": 0, "vless": 0, "ss": 0, "trojan": 0}

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


def save_protocols(protocol_type, all_protocols):
    file_name = f"{protocol_type}_protocols_{date.today()}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        for protocol in all_protocols:
            if protocol.startswith(f"{protocol_type}://"):
                file.write(protocol + "\n")
    print(f"{protocol_type.capitalize()} protocols saved to {file_name}")


def save_all_protocols(all_protocols):
    file_name = f"all_protocols_{date.today()}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        for protocol in all_protocols:
            file.write(protocol + "\n")
    print(f"All protocols saved to {file_name}")


# Update the display_menu function to include saving logic
def display_menu():
    print("Please select an option to save:")
    print("1. ss")
    print("2. vless")
    print("3. vmess")
    print("4. trojan")
    print("5. all protocols")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You selected: ss")
        save_protocols("ss", all_protocols)
    elif choice == "2":
        print("You selected: vless")
        save_protocols("vless", all_protocols)
    elif choice == "3":
        print("You selected: vmess")
        save_protocols("vmess", all_protocols)
    elif choice == "4":
        print("You selected: trojan")
        save_protocols("trojan", all_protocols)
    elif choice == "5":
        print("You selected: all protocols")
        save_all_protocols(all_protocols)
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display_menu()
