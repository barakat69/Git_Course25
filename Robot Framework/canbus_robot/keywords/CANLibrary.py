# keywords/CANLibrary.py

import can
from robot.api.deco import keyword

class CANLibrary:
    def __init__(self):
        self.bus = None

    @keyword("Open CAN Channel")
    def open_can_channel(self, channel="can0", bustype="socketcan"):
        """Opens CAN interface using python-can"""
        self.bus = can.interface.Bus(bustype='virtual')
        print(f"Connected to CAN channel: {channel}")

    @keyword("Send CAN Message")
    def send_can_message(self, arbitration_id, data):
        """Sends a CAN message"""
        if self.bus is None:
            raise Exception("CAN bus not initialized. Use 'Open CAN Channel' first.")

        if isinstance(data, str):
            # Expecting comma-separated string like "01,02,03"
            data = [int(byte.strip(), 16) for byte in data.split(",")]

        msg = can.Message(arbitration_id=int(arbitration_id, 16), data=data, is_extended_id=False)
        self.bus.send(msg)
        print(f"Sent CAN msg: ID={arbitration_id}, Data={data}")

    @keyword("Read CAN Message")
    def read_can_message(self, timeout=1.0):
        """Reads a message from CAN bus"""
        if self.bus is None:
            raise Exception("CAN bus not initialized.")

        msg = self.bus.recv(timeout)
        if msg:
            print(f"Received: ID={hex(msg.arbitration_id)}, Data={list(msg.data)}")
            return f"{hex(msg.arbitration_id)}:{','.join(format(b, '02X') for b in msg.data)}"
        else:
            return "No message received"
