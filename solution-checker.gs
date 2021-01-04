function checkSolutions() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var scramble = sheet.getRange("C2").getValues()[0][0];
  
  var solves = sheet.getDataRange().getValues();
  var i=2;
  solves.forEach(row => {
    if (row[0]!="Solution") {
      var response = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/"+scramble+"/"+row[0]);
      var parsed_res = JSON.parse(response.getContentText());
    
      Logger.log(parsed_res.result);
    
      sheet.getRange("B"+i).setValue(parsed_res.result);
      i++;
    }
  });
}
