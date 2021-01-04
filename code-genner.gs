function checkSolutions() {
  var sheet = SpreadsheetApp.getActiveSheet();
  
  var inscris = sheet.getDataRange().getValues();
  var i=2;
  inscris.forEach(row => {
    if (i>2) {
      var response = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/code");
      var parsed_res = JSON.parse(response.getContentText());    
      sheet.getRange("C"+(i-1)).setValue(parsed_res.code);
    }
    i++;
  });
}