# 🔵 Bluetooth Device Finder Using Python

A Python-based Bluetooth Low Energy (BLE) device discovery tool built using the **Bleak** library. This project scans for nearby BLE devices and displays their available device names, MAC addresses, and signal strength (RSSI).

The application helps identify nearby Bluetooth Low Energy devices through a simple Python script.

## ✨ Features

- **📡 BLE Device Discovery:** Scan for nearby Bluetooth Low Energy devices.
- **🔍 Device Identification:** Retrieve device names and MAC addresses.
- **📶 Signal Strength Detection:** Display RSSI values in dBm.
- **⏱️ Timed Scanning:** Scan for nearby devices for 5 seconds.
- **📋 Device Listing:** Display discovered devices in a structured table.
- **⚠️ Error Handling:** Display a message when no BLE devices are discovered.
- **🔒 Unknown Device Handling:** Identify devices whose names are unavailable.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Bleak | Bluetooth Low Energy device discovery |
| Jupyter Notebook | Development and execution environment |

## 📁 Project Structure

```text
Bluetooth_Device_Finder/
│
├── bluetooth_device_finder_using_python.ipynb
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework
```

Navigate to the Bluetooth project folder after placing it inside your repository's `projects` directory.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the Bleak library and Jupyter Notebook:

```bash
pip install bleak notebook
```

## 🚀 Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

`bluetooth_device_finder_using_python.ipynb`

Run the notebook cell to start scanning for nearby Bluetooth Low Energy devices.

## 💻 How It Works

1. Import `BleakScanner` from the Bleak library.
2. Initiate Bluetooth Low Energy device discovery.
3. Scan for nearby devices for 5 seconds.
4. Retrieve discovered device information and advertisement data.
5. Extract the device name, MAC address, and RSSI signal strength.
6. Display the discovered devices in a formatted table.

## 📊 Sample Output

```text
Scanning for BLE device...

Found 3 device(s):

Address / MAC                         | Name                           | RSSI (Signal)
--------------------------------------------------------------------------------
AA:BB:CC:DD:EE:FF                     | Bluetooth Device                | -55 dBm
11:22:33:44:55:66                     | Unknown / Hidden                | -72 dBm
22:33:44:55:66:77                     | Wireless Device                 | -65 dBm
```

*Note: The output above is illustrative. Actual devices and signal strengths depend on the surrounding environment.*

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Python asynchronous programming.
- Bluetooth Low Energy (BLE) fundamentals.
- Device discovery using the Bleak library.
- Working with device addresses and advertisement data.
- Understanding RSSI and Bluetooth signal strength.
- Displaying and processing discovered device information.

## ⚠️ Important Notes

- This project discovers Bluetooth Low Energy devices, not necessarily all Bluetooth Classic devices.
- Bluetooth must be enabled on your computer.
- Device discovery depends on operating system permissions and Bluetooth hardware support.
- Some devices may not broadcast their names.
- RSSI values vary depending on distance, obstacles, and environmental interference.
- Device discovery does not establish a connection or pair with the discovered devices.

## 🔮 Future Improvements

- Add a graphical user interface.
- Display discovered devices in real time.
- Add continuous Bluetooth scanning.
- Filter devices based on signal strength.
- Identify devices by manufacturer information.
- Add device selection and connection functionality.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring Python, asynchronous programming, and Bluetooth Low Energy technology.*
