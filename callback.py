def set_device(google_sheet, env_param):
    sheet_ai = google_sheet.worksheet("AI")
    sheet_ai.update("C2", "1")
    sheet_ai.update("D2", "1")

    return True
