"""
- 適宜溫度: 25
- 適宜濕度: 80
- 滴灌每次噴霧，濕度增加 10%
"""

def set_device(google_sheet, env_param):
    sheet_ai = google_sheet.worksheet("AI")
    
    # 濕度 - 滴灌
    if (int(env_param["humidity"]) < 80):
        value = int((80 - int(env_param["humidity"]))/10)
        env_param["drip"] = str(value)
        sheet_ai.update("C2", str(value))
    else:
        env_param["drip"] = "0"
        sheet_ai.update("C2", "0")

    # 溫度 - 風扇
    if (int(env_param["temperature"]) > 25):
        env_param["fan"] = "1"
        sheet_ai.update("D2", "1")
    else:
        env_param["fan"] = "0"
        sheet_ai.update("D2", "0")

    return True
