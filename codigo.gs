function checkSolutions(sheetname, scramble_cell, solutions_col, results_col) { 
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetname);
  var scramble = sheet.getRange(scramble_cell).getValue();
  
  var i=2;
  var solution;
  while ((solution = sheet.getRange(solutions_col+i).getValue())) {
    if (!sheet.getRange(results_col+i).getValue()){
      var response = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/"+scramble+"/"+solution);
      var parsed_res = JSON.parse(response.getContentText());    
      sheet.getRange(results_col+i).setValue(parsed_res.result);
    }
    i++;
  }
}

// args: sheet, scramble_cell, solutions_col, results_col
function checkA1() {
  checkSolutions("a1","D1","B","C");
}
function checkA2() {
  checkSolutions("a2","D1","B","C");
}
function checkA3() {
  checkSolutions("a3","D1","B","C");
}

function genCode() {
  ////// EDIT VALUES HERE //////
  var sheet = "codes";
  var name_col = "B";
  var code_col = "H";
  //////////////////////////////
  
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheet);
  var i=2;
  var val;
  while ((val = sheet.getRange(name_col+i).getValue())) {
    if (!sheet.getRange(code_col+i).getValue()) {
      var code = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/code");
      var parsed_code = JSON.parse(code.getContentText()).code;
      sheet.getRange(code_col+i).setValue(parsed_code);
    }
    i++;
  }
}