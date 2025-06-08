function simulateAnalysis() {
  const tableBody = document.querySelector("#resultsTable tbody");
  tableBody.innerHTML = "";

  // Simulated packet data and classification
  const dummyData = [
    { packet: "TCP Packet from 192.168.1.5:443 to 10.0.0.9:3389", result: "❌ Malicious - Potential RDP brute force" },
    { packet: "UDP Packet from 10.0.0.5:53 to 192.168.1.2:1045", result: "✅ Benign - DNS request" },
    { packet: "ICMP Echo Request from 172.16.0.3", result: "✅ Benign - Regular ping" },
    { packet: "HTTP POST from 198.51.100.20 to 10.0.0.1", result: "❌ Malicious - Data exfiltration suspected" }
  ];

  dummyData.forEach(entry => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${entry.packet}</td><td>${entry.result}</td>`;
    tableBody.appendChild(row);
  });
}
