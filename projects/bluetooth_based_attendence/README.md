# 📡 Bluetooth-Based Student Attendance Management System

An automated student attendance management system built using **Python, Bluetooth Low Energy (BLE), and the Bleak library**.

The project scans for nearby Bluetooth devices, identifies registered students using their device addresses, and automatically records attendance in a CSV file with the current date and time.

## ✨ Features

- **📡 Bluetooth Device Scanning:** Detect nearby Bluetooth Low Energy devices.
- **👨‍🎓 Student Identification:** Match detected device addresses against a predefined student database.
- **✅ Automatic Attendance:** Mark registered students as present when their devices are detected.
- **⏱️ Timed Scanning:** Scan for nearby BLE devices within a 10-second window.
- **📅 Date and Time Tracking:** Automatically record the attendance date and timestamp.
- **📁 CSV Attendance Records:** Store attendance details in a structured CSV file.
- **🚫 Duplicate Prevention:** Prevent the same student from being marked present more than once per day.
- **📊 Attendance Summary:** Display the total number of detected registered students after each scanning session.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Bleak | Bluetooth Low Energy device discovery |
| Asyncio | Asynchronous Bluetooth scanning |
| CSV | Attendance data storage |
| Datetime | Date and time tracking |

## 📁 Project Structure

```text
Bluetooth_Attendance_System/
│
├── app.py
├── attendance.csv
└── README.md
```

**Note:** The `attendance.csv` file is automatically initialized with column headers if it does not already exist. Attendance records are appended to this file.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
cd TopMentor_Coursework
```

Navigate to the Bluetooth attendance project folder inside `projects`.

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

Install the Bleak library:

```bash
pip install bleak
```

## 🔧 Configuration

The application uses a predefined student database containing Bluetooth device addresses and student names.

Example:

```python
STUDENT_DATABASE = {
    "AA:BB:CC:DD:EE:01": "Riham",
    "AA:BB:CC:DD:EE:02": "Casper",
    "AA:BB:CC:DD:EE:03": "Danial",
    "AA:BB:CC:DD:EE:04": "Alvia"
}
```

Replace the sample addresses with the actual Bluetooth identifiers associated with registered devices.

The scanning duration is configured as:

```python
SCAN_DURATION_SECONDS = 10.0
```

## 🚀 Running the Application

Run the Python application:

```bash
python app.py
```

The application will scan for nearby Bluetooth Low Energy devices and check whether their addresses match registered students.

## 💻 How It Works

1. **Initialize Attendance File:** Create `attendance.csv` with the required headers if the file does not exist.
2. **Start Bluetooth Scanning:** Use `BleakScanner.discover()` to detect nearby BLE devices for 10 seconds.
3. **Identify Devices:** Retrieve the Bluetooth addresses or identifiers of discovered devices.
4. **Match Students:** Compare detected identifiers against the predefined student database.
5. **Check Existing Records:** Verify whether the student has already been marked present on the current date.
6. **Mark Attendance:** Record the date, time, device identifier, student name, and attendance status.
7. **Display Summary:** Show the total number of matched registered devices for the scanning session.

## 📊 Attendance CSV Format

Attendance records are stored in `attendance.csv`.

| Column | Description |
|---|---|
| Date | Attendance date (YYYY-MM-DD) |
| Time | Attendance time (HH:MM:SS) |
| Student ID / MAC | Registered Bluetooth device identifier |
| Student Name | Student's registered name |
| Status | Attendance status (Present) |

### Sample Output

```text
Date,Time,Student ID / MAC,Student Name,Status
2026-09-11,21:27:08,CB4AC209-893F-77D8-B5CB-45D9B2B2E0C4,Danial,Present
2026-09-11,21:27:08,0C4AB969-B868-88A7-115D-1F71878568DE,Alvia,Present
2026-09-11,21:27:08,41114D16-BC3F-93A1-799F-17D8E3D328C9,Casper,Present
2026-09-11,21:27:08,4A6527A2-3D4D-A0AF-FBB1-3CB37945B3E1,Riham,Present
```

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Bluetooth Low Energy (BLE) technology.
- Bluetooth device discovery using Python.
- Asynchronous programming with Asyncio.
- Working with the Bleak library.
- File handling and CSV operations.
- Date and time management.
- Dictionary-based student identification.
- Implementing duplicate attendance prevention.
- Automating real-world attendance workflows.

## ⚠️ Important Considerations

- Bluetooth must be enabled on the scanning computer.
- The system requires appropriate Bluetooth permissions and BLE hardware support.
- Only registered device identifiers are recognized.
- Devices must be discoverable through BLE scanning.
- Bluetooth identifiers may differ across operating systems and devices.
- Device presence alone does not prove that the registered student is physically present.
- Device identifiers can potentially be spoofed, so this implementation should be treated as a learning prototype rather than a secure attendance system.

## 🔮 Future Improvements

- Develop a Streamlit-based attendance dashboard.
- Add student registration functionality.
- Generate daily and monthly attendance reports.
- Export attendance summaries to Excel.
- Add attendance percentage calculations.
- Implement real-time device monitoring.
- Introduce stronger student and device verification.

## 👩‍💻 Author

**Riham**

GitHub: [@Riham203](https://github.com/Riham203)

---

*Built as a hands-on project exploring Python, Bluetooth Low Energy, asynchronous programming, and automation.*
