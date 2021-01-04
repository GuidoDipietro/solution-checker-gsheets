function checkSolutions() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var scramble = sheet.getRange("D1").getValues()[0][0];
  
  var solves = sheet.getDataRange().getValues();
  var i=2;
  solves.forEach(row => {
    if (i>2) {
      var response = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/"+scramble+"/"+row[1]);
      var parsed_res = JSON.parse(response.getContentText());
    
      Logger.log(parsed_res.result);
    
      sheet.getRange("C"+(i-1)).setValue(parsed_res.result);
    }
    i++;
  });
}
