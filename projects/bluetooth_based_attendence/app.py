import asyncio
import csv
from datetime import datetime
from bleak import BleakScanner


STUDENT_DATABASE = {
    "AA:BB:CC:DD:EE:01": "Riham",
    "AA:BB:CC:DD:EE:02": "Casper",
    "AA:BB:CC:DD:EE:03": "Danial",
    "AA:BB:CC:DD:EE:04": "Alvia"
}

ATTENDANCE_FILE = "attendance.csv"
SCAN_DURATION_SECONDS = 10.0



def initialize_csv():
    """Initializes the CSV file with headers if it does not exist."""
    try:
        with open(ATTENDANCE_FILE, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Student ID / MAC", "Student Name", "Status"])
    except FileExistsError:
        pass  


def mark_attendance(mac_address: str, student_name: str):
    """Logs the student's attendance into the CSV file."""
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    
    try:
        with open(ATTENDANCE_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[0] == current_date and row[2] == mac_address:
                    print(f"⚠️  {student_name} ({mac_address}) already marked present today.")
                    return
    except FileNotFoundError:
        initialize_csv()

    
    with open(ATTENDANCE_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([current_date, current_time, mac_address, student_name, "Present"])
        print(f"✅ Marked Present: {student_name} ({mac_address}) at {current_time}")


async def scan_and_mark_attendance():
    """Scans for active BLE devices and correlates with registered database."""
    initialize_csv()
    print(f"🔍 Scanning for BLE Bluetooth devices ({SCAN_DURATION_SECONDS}s window)...")

    # Perform asynchronous BLE discovery
    devices = await BleakScanner.discover(timeout=SCAN_DURATION_SECONDS, return_adv=True)

    if not devices:
        print("❌ No Bluetooth devices detected in range.")
        return

    print(f"📡 Found {len(devices)} active Bluetooth device(s). Processing attendance...\n")

    present_count = 0
    for mac_or_uuid, (device, adv) in devices.items():
        mac_upper = mac_or_uuid.upper()
        
        # Match against registered database
        if mac_upper in STUDENT_DATABASE:
            student_name = STUDENT_DATABASE[mac_upper]
            mark_attendance(mac_upper, student_name)
            present_count += 1

    print(f"\n📊 Attendance Session Complete. Total Present: {present_count}")



if __name__ == "__main__":
    asyncio.run(scan_and_mark_attendance())