import asyncio
import sys
import platform
import codecs
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
# 8C:F6:81:D5:1D:A2: XMWSDJ04MMC

ADDRESS = (
    "8C:F6:81:D5:1D:A2"
    if platform.system() != "Darwin"
    else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
)
TEMP_UUID = "ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6"
client = BleakClient(ADDRESS)


def notification_handler(characteristic: BleakGATTCharacteristic, sensor_data: bytearray):
    """Simple notification handler which prints the data received."""
    #print(f"{characteristic.description}: {data}")
    
    temperature = int.from_bytes(sensor_data[:2],byteorder='little',signed=True) / 10
    humidity = int.from_bytes(sensor_data[2:4],byteorder='little',signed=True) / 10
    voltage = int.from_bytes(sensor_data[4:],byteorder='little',signed=True) / 1000
        
    print(str(temperature) + "℃")
    print(str(humidity) + "%")
    print(str(voltage) + "V")

    f = codecs.open("test.txt","w","utf-8")
    text = str(temperature) + "℃"
    f.write(text)
    f.close()


async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(50000.0)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else TEMP_UUID,
        )
    )