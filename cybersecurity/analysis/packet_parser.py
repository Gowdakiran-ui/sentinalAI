# analysis/packet_parser.py

from scapy.all import rdpcap
import pandas as pd

def parse_pcap(file_path):
    packets = rdpcap(file_path)
    rows = []

    for pkt in packets:
        if pkt.haslayer("IP"):
            row = {
                "src": pkt["IP"].src,
                "dst": pkt["IP"].dst,
                "proto": pkt["IP"].proto,
                "summary": pkt.summary()
            }
            rows.append(row)

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = parse_pcap(r"C:\Users\Kiran gowda.A\OneDrive\Documents\vs code\cybersecurity\analysis\packets.pcap")
    print(df.head())
