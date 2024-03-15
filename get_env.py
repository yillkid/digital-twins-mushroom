def get_environment_params(google_sheet, env_param):
    # Get data
    sheet_air_box = google_sheet.worksheet("空氣盒子")
    
    env_param["temperature"] = sheet_air_box.acell("B2").value
    env_param["humidity"] = sheet_air_box.acell("C2").value
    
    return True
