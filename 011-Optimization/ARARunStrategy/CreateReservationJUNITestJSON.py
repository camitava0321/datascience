# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:56:18 2024

@author: AMITAVA
"""

import csv
import json

with open('reservations.csv') as f:
    reader = csv.DictReader(f)

    result = []

    for row in reader:
        obj = {
            #booleanVal": bool(int(row["booleanVal"])),
            #"stringVal": row["stringVal"],
            
            "compositeRoomReqInd": bool(int(row["compositeRoomReqInd"])),
            "connectingRoomReqInd": bool(int(row["connectingRoomReqInd"])),
            "crsConfirmationId": row["crsConfirmationId"],
            "crsContStayLinkId": row["crsContStayLinkId"],
            "crsShareLinkId": row["crsShareLinkId"],
            "groupId": row["groupId"],
            "pmsConfirmationId": row["pmsConfirmationId"],
            "resUpgradeScore": row["resUpgradeScore"],
            "roomAssignedByAraInd": bool(int(row["roomAssignedByAraInd"])),
            "roomUpgradedByAraInd": bool(int(row["roomUpgradedByAraInd"])),
            "araProcessedTs": row["araProcessedTs"],
            
            "segments": [
                {
                    #"subStringVal": row["seg.subStringVal"],
                    #"subBooleanVal": bool(int(row["seg.subBooleanVal"])),
                    #"subIntVal": int(row["seg.subIntVal"])
                    "arrivalDate": row["@arrivalDate"], #2024-08-22T15:00:00.000Z
                    "arrivalTime": row["@arrivalDate"]+"T"+row["@arrivalTime"]+":00.000Z",
                    "complimentaryUpgraded": bool(int(row["@complimentaryUpgraded"])),
                    "dateSearchString": row["@dateSearchString"],
                    "departureDate": row["@departureDate"],
                    "departureTime": row["@departureDate"]+"T"+"12:00:00.000Z",
                    "doNotMoveInd": bool(int(row["@doNotMoveInd"])),
                    "dtArrivalDate": row["@dtArrivalDate"],
                    "dtDepartureDate": row["@dtDepartureDate"],
                    "finalInventoryTypeCode": row["@finalInventoryTypeCode"],
                    "id": row["@id"],
                    "inventoryTypeCode": row["@inventoryTypeCode"],
                    "miosUpgraded": bool(int(row["@miosUpgraded"])),
                    "roomId": row["@roomId"],
                    "sNAUpgraded": bool(int(row["@sNAUpgraded"])),
                    "upgradedInventoryTypeCode": row["@upgradedInventoryTypeCode"],
                    "upgradeScore": row["@upgradeScore"]            
                }
            ]
        }

        result.append(obj)

    json_result = json.dumps(result)
    with open('result.json', 'w') as outfile:
        json.dump(result, outfile)

    print("JSON saved to result.json")    