var SHEETNAME="temp"

function doGet(e) {
  let sheet;
  if (this.sheet == null) {
      this.sheet = SpreadsheetApp.getActiveSpreadsheet();
  }

  let SHEET = this.sheet.getSheetByName(SHEETNAME);
  lastLog=SHEET.getRange("C1").getValue();
  SHEET.getRange("C1").setValue(lastLog+1);
  ContentService.createTextOutput(SHEET.getRange("B"+lastLog).setValue(e.parameter.temp.split(",")[1]));
  ContentService.createTextOutput(SHEET.getRange("A"+lastLog).setValue(e.parameter.temp.split(",")[0]));
  return "ok"
}