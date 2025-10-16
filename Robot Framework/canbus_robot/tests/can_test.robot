*** Settings ***
Library    ../keywords/CANLibrary.py

*** Test Cases ***
Send And Receive CAN Message
    Open CAN Channel    can0
    Send CAN Message    0x123    01,02,03,04
    ${msg}=    Read CAN Message    2.0
    Log    Received message: ${msg}
