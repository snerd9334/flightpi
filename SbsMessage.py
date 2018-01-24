"""
SbsMessage.py
Parses SBS-1 ADS-B messages into a workable Python object

Inspiration from https://github.com/kanflo/ADS-B-funhouse/blob/master/sbs1.py

Matt Dyson
24/01/18

Part of FlightPi - http://github.com/mattdy/flightpi
"""
class SbsMessageType:
    ES_IDENT_AND_CATEGORY = 1
    ES_SURFACE_POS = 2
    ES_AIRBORNE_POS = 3
    ES_AIRBORNE_VEL = 4
    SURVEILLANCE_ALT = 5
    SURVEILLANCE_ID = 6
    AIR_TO_AIR = 7
    ALL_CALL_REPLY = 8

class SbsMessage:
    def __init__(self, input):
        self.parts = input.split(",")

        if self.parts[0] != "MSG":
           raise ValueError("Invalid message")

        self.transmissionType = self.parts[1]
        self.sessionID = self.parts[2]
        self.aircraftID = self.parts[3]
        self.icao24 = self.parts[4]
        self.flightID = self.parts[5]
        self.callsign = self.parts[10]
        self.altitude = self.parts[11]
        self.groundSpeed = self.parts[12]
        self.track = self.parts[13]
        self.verticalRate = self.parts[16]
        self.squawk = self.parts[17]
