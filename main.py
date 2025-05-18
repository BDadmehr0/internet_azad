import requests
import json
import base64
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

console = Console()

# اینجا فایل sub.json رو می‌خونیم
with open("sub.json", "r", encoding="utf-8") as f:
    subs = json.load(f)

# دوتا لیست رو از فایل بیرون میکشیم
encoded_urls = subs.get("encoded_subs", [])
urls = subs.get("normal_subs", [])

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

        except (requests.exceptions.RequestException, base64.binascii.Error) as e:
            console.print(f"[red]Error in {url}: {e}[/red]")

all_protocols = []

# اول آدرس‌هایی که Base64 هستن رو می‌خونیم
fetch_encoded_content(encoded_urls, all_protocols)

# حالا آدرس‌های معمولی رو می‌خونیم
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

# ذخیره همه‌ی پروتکل‌ها در فایل
with open("all_protocols.json", "w", encoding="utf-8") as f:
    json.dump(all_protocols, f, indent=4, ensure_ascii=False)

# نمایش نتایج
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
