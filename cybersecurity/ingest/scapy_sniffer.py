from scapy.all import sniff, wrpcap
import time

def capture_packets(duration=30, output_file="data/packet_dumps/packets.pcap"):
    print(f"[+] Capturing packets for {duration} seconds...")
    packets = sniff(timeout=duration)
    wrpcap(output_file, packets)
    print(f"[+] Saved {len(packets)} packets to {output_file}")

if __name__ == "__main__":
    capture_packets()
