function checkSolution() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var scramble = sheet.getRange("D1").getValues()[0][0];
  
  var solves = sheet.getDataRange().getValues();
  var i=1;
  solves.forEach(row => {
    var response = UrlFetchApp.fetch("https://solution-checker.guidodipietro.repl.co/"+scramble+"/"+row[0]);
    var parsed_res = JSON.parse(response.getContentText());
    
    Logger.log(parsed_res.result);
    
    sheet.getRange("B"+i).setValue(parsed_res.result);
    i++;
  });
}