# Network Scanner

This Python script scans a local network using ARP requests to identify active devices. It gathers details like IP addresses, MAC addresses, and hostnames of connected devices.

## Setup and Running the Script

### Setup Steps:

0. **Install Python 3.x**  
   Make sure you have Python installed on your system.

1. **Install Required Libraries**  
   Install the `scapy` library by running the following command:
   ```bash
   pip install scapy
   ```

2. **Clone or Download the Script**  
   Clone this repository or download the `network_scanner.py` file directly.

3. **Edit the Script**  
   Open the script file and update the `network_prefix` variable to match your network.

4. **Run the Script**  
   Execute the script using Python:
   ```bash
   python network_scanner.py
   ```

## Usage Instructions

### 1. Scanning the Network

To scan the network for devices, run the script as described above. It will automatically identify active devices within the specified range.

### 2. Customizing Parameters

To customize scanning behavior, modify the following parameters in the script:
- **`network_prefix`**: Specify the network range (e.g., `192.168.1`).
- **`timeout`**: Adjust the timeout period for ARP responses.
- **`retries`**: Set the number of retries to improve detection accuracy.

### 3. Example Output

The script will output the discovered devices in the following format:
```plaintext
IP: 192.168.1.2, MAC: AA:BB:CC:DD:EE:FF, Hostname: printer.local
IP: 192.168.1.3, MAC: FF:EE:DD:CC:BB:AA, Hostname: Unknown
```

## Donations

If you appreciate this project and want to support its development, feel free to send a donation to the following wallet addresses:

### TON Address  
```
UQA59lyLjF8TXbvAXXyLk9U1f-LN03jyJyit3pXqonZGXZGO
```
### BTC Address  
```
bc1q3ltptp54pe587axj5ye26pcqqg3sqrlu9fcam0
```

Your contributions are greatly appreciated!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy scanning! :rocket:

