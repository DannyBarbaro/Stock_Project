#! /usr/bin/awk -f
BEGIN {
  query = ENVIRON["QUERY_STRING"] #grabbing the query string, its that easy lol
  print "Content-type: text/html \n" 
  print "<!DOCTYPE html><html><head>"
  print "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css' integrity='sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh' crossorigin='anonymous'>"
  print "<script src='https://cdn.anychart.com/releases/v8/js/anychart-base.min.js?hcode=c11e6e3cfefb406e8ce8d99fa8368d33'></script>"
  printFormValidation()
  print "<title>Investing Challenge</title></head><body style='text-align: center;'>"
  n = 0
  while("cat stock_names" | getline) {
    stocks[n] = $0
    symbols[n] = substr($1, 2, length($1) - 2)
    n++
  }

  print "<h2>Stock Investing Challange</h2>"
  print "<p>You have $100 to invest in tech stocks. Choose your 5 socks, amounts, and a date range to see how you would do!</p>"
  
  #example query: "stock1=ADBE&amount1=1&stock2=ADBE&amount2=2&stock3=ADBE&amount3=3&stock4=ADBE&amount4=4&stock5=ADBE&amount5=5&start=2000-01-04&end=2020-01-02"
  # Manually tested and verified that these work
  split(query,a,"&")
  stock[0] = substr(a[1], 8)
  amount[0] = substr(a[2], 9)
  stock[1] = substr(a[3], 8)
  amount[1] = substr(a[4], 9)
  stock[2] = substr(a[5], 8)
  amount[2] = substr(a[6], 9)
  stock[3] = substr(a[7], 8)
  amount[3] = substr(a[8], 9)
  stock[4] = substr(a[9], 8)
  amount[4] = substr(a[10], 9)

  startDate = substr(a[11], 7)
  endDate = substr(a[12], 5)
  startY = substr(startDate, 0, 4)
  startM = substr(startDate, 6, 2)
  startD = substr(startDate, 9, 2)
  endY = substr(endDate, 0, 4)
  endM = substr(endDate, 6, 2)
  endD = substr(endDate, 9, 2)
  
  print "<form name='myForm' action='' onsubmit='return validateForm()'>"
  print "<label>Choose Stock 1:</label>"
  print "<select id='stock1' name='stock1'>"
  for (i = 0; i < n; i++)
    if (symbols[i] == stock[0]) {
      print "<option value='"symbols[i]"' selected>"stocks[i]"</option>"
    } else {
      print "<option value='"symbols[i]"'>"stocks[i]"</option>"
    }
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='amount1' name='amount1'/>"
  print "<br>"

  print "<label>Choose Stock 2:</label>"
  print "<select id='stock2' name='stock2'>"
  for (i = 0; i < n; i++)
    if (symbols[i] == stock[1]) {
      print "<option value='"symbols[i]"' selected>"stocks[i]"</option>"
    } else {
      print "<option value='"symbols[i]"'>"stocks[i]"</option>"
    }  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='amount2' name='amount2'/>"
  print "<br>"

  print "<label>Choose Stock 3:</label>"
  print "<select id='stock3' name='stock3'>"
  for (i = 0; i < n; i++)
    if (symbols[i] == stock[2]) {
      print "<option value='"symbols[i]"' selected>"stocks[i]"</option>"
    } else {
      print "<option value='"symbols[i]"'>"stocks[i]"</option>"
    }
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='amount3' name='amount3'/>"
  print "<br>"

  print "<label>Choose Stock 4:</label>"
  print "<select id='stock4' name='stock4'>"
  for (i = 0; i < n; i++)
    if (symbols[i] == stock[3]) {
      print "<option value='"symbols[i]"' selected>"stocks[i]"</option>"
    } else {
      print "<option value='"symbols[i]"'>"stocks[i]"</option>"
    }
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='amount4' name='amount4'/>"
  print "<br>"

  print "<label>Choose Stock 5:</label>"
  print "<select id='stock5' name='stock5'>"
  for (i = 0; i < n; i++)
    if (symbols[i] == stock[4]) {
      print "<option value='"symbols[i]"' selected>"stocks[i]"</option>"
    } else {
      print "<option value='"symbols[i]"'>"stocks[i]"</option>"
    }
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='amount5' name='amount5'/>"
  print "<br>"

  print "<label>Start Date:</label>"
  print "<input type='date' id='start' name='start' value='"startDate"'>"
  print "<label>End Date:</label>"
  print "<input type='date' id='end' name='end' value='"endDate"'>"
  print "<br>"

  print "<input type='submit'>"
  print "</form>"  

  # loop for each stock, if stock names are not unique, subsequent calls will not work. 
  startPrice[0] = 0
  endPrice[0] = 0
  for (i = 0; i < 5; i++){
    api = "\"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="stock[i]"&apikey=DF70XN4LUOOLN6TN\""

    # get start date and end date stock values
    flag = 0 #idk why i couldn't get this to work without this stupid flag but wtv this works
    collectFlag = 0
    while("curl "api | getline) {
      if (flag == 1){
        #starting day opening price
        #NOTE, This is likely going to cause problems... grabing 7 digits of the stock.
        # so 64.4700 works, 1348.41 works, 2.1234 will grab an extra character, likely a double quote character
        startPrice[i] = substr($0, 25, 7) 
        flag = 0
        runningAmmount = substr($0, 25, 7)
        stockdata[i, runningDate] = runningAmmount
        collectFlag = 0
      }
      if (flag == 2){
        #ending day closing price
        if (index($1, "4") != 0) {
          endPrice[i] = substr($0, 26, 7)
          flag = 0
        }
      }
      if (index($0, startDate) != 0){
        flag = 1
      }
      if (index($0, endDate) != 0){
        flag = 2
        collectFlag = 1
      }
      if (collectFlag == 1 && index($0, "-") != 0) {
        runningDate = substr($1, 2, length($1) - 3)
      }
      if (collectFlag == 1 && index($0, "close") != 0) {
        runningAmmount = substr($0, 26, 7)
        stockdata[i, runningDate] = runningAmmount
      }
    }
  }

  # Calculate income and visualize it
  # startPrice[0-4] has the price of each stock on the starting day
  # endPrice[0-4] has the price of each stock on the ending day
  # amount[0-4] has the amount invested on the start day
  numStocksPurchased[0] = 0
  endingValue[0] = 0
  for (i = 0; i < 5; i++){
    print "<h3>"stock[i]"</h3>"
    percentChange = (endPrice[i] / startPrice[i] - 1) * 100
    print "<div class='row'>"
    print "<div class='col-md-9'>"
    print "    <div style='width:100%; height:300px;' id='graph"i"'></div>"
      print "<script>"
      print "anychart.onDocumentReady(function () {"
      print "var dataSet = anychart.data.set(["
      for(datapoint in stockdata) {
        split(datapoint, Q, SUBSEP)
        if (Q[1] == i) {
          split(Q[2], D, "-")
          print "[ Date.UTC("D[1]", "D[2]-1", "D[3]"), "stockdata[datapoint] "],"
        }
      }
      print "]);"
      print "var seriesData = dataSet.mapAs({'x': 0, 'value': 1});"
      print "var chart = anychart.line();"
      print "var dateScale = anychart.scales.dateTime();"
      print "chart.xScale(dateScale);"
      print "chart.animation(true);"
      print "chart.padding([10, 20, 5, 20]);"
      print "chart.crosshair().enabled(true).yLabel(false).yStroke(null);"
      print "chart.tooltip().positionMode('point');"
      print "chart.title('"stock[i]" Stock from "startDate" to "endDate"');"
      print "chart.yAxis().title('Price Per Share (USD)');"
      print "chart.xAxis().labels().padding(5);"
      print "var series = chart.line(seriesData);"
      print "series.name('"stock[i]"');"
      print "series.hovered().markers().enabled(true).type('circle').size(4);"
      print "series.tooltip().position('right').anchor('left-center').offsetX(5).offsetY(5);"
      if (percentChange > 0) {
        print "series.stroke('green')"
      } else if (percentChange < 0) {
        print "series.stroke('red')"
      }
      print "chart.container('graph"i"');"
      print "chart.draw();"
      print "}) </script>"
      print "</div>"
      print "<div class='col-md-3' style='position: relative;'>"
      print "<div style='margin: 0; position: absolute; top: 50%; -ms-transform: translateY(-50%); transform: translateY(-50%);'>"
      if (percentChange > 0) {
        print "<h4 style='color:green'>+"
      } else if (percentChange < 0) {
        print "<h4 style='color:red'>"
      } else {
        print "<h4 style='color:grey'>"
      }
      printf "%.2f", percentChange
      print "%</h4>"
      numStocksPurchased[i] = amount[i] / startPrice[i]
      endingValue[i] = numStocksPurchased[i] * endPrice[i]
      sum += endingValue[i]
      amountChange = (endingValue[i] - amount[i])
      if (amountChange > 0) {
        print "<h4 style='color:green'>+ $"
      } else if (amountChange < 0) {
        print "<h4 style='color:red'>- $"
        amountChange = amountChange*(-1)
      } else {
        print "<h4 style='color:grey'>+ $"
      }
      printf "%.2f", amountChange
      print "</h4>"
      print "<h4 style='color: grey'>"
      printf "Starting Value: $%.2f", amount[i]
      print "</h4>"
      print "<h4 style='color: grey'>"
      printf "Final Value: $%.2f", endingValue[i]
      print "</h4>"
      print "</div>"
      print "</div>"
      print "</div>"

  }
  print "<h3> You turned your $100 into: "
  printf "$%.2f", sum
  print "</h3>"
  print "</body></html>"

}

function printFormValidation() {
	print "<script>"

	print "  function validateForm() {"
  	print "    var stock1 = document.forms['myForm']['amount1'].value;"
  	print "    var stock2 = document.forms['myForm']['amount2'].value;"
  	print "    var stock3 = document.forms['myForm']['amount3'].value;"
  	print "    var stock4 = document.forms['myForm']['amount4'].value;"
  	print "    var stock5 = document.forms['myForm']['amount5'].value;"

  	print "    var sum = +stock1 + +stock2 + +stock3 + +stock4 + +stock5;"
  	print "    if (sum < 0 || sum > 100) {"
    print "      alert('sum must be less than $100');"
    print "      return false;"
  	print "    }"

  	print "    var startDate = myStringToDate(document.forms['myForm']['start'].value);"
  	print "    var endDate = myStringToDate(document.forms['myForm']['end'].value);"
  	print "    if (isNaN(endDate.getTime()) || isNaN(startDate.getTime())) {"
    print "      alert('Missing date');"
    print "      return false;"
  	print "    }"
    print "    if([6,0].includes(startDate.getUTCDay()) || [6,0].includes(endDate.getUTCDay())){"
    print "      alert('No trading data on weekends');"
    print "      return false;"
    print "    }"
  	print "    if (endDate.getTime() <= startDate.getTime()) {"
    print "      alert('Time cant go backwards!');"
    print "      return false;"
  	print "    }"
  	print "    if (endDate.getTime() > (new Date()).getTime()){"
    print "      alert('Cant predict the future!');"
    print "      return false;"
  	print "    }"
  	print "    if (startDate.getTime() < 1104537600000){"
    print "      alert('Too far in the past! try something after 2004!');"
    print "      return false;"
  	print "    }"

	print "  }"


	print "  function myStringToDate(str) {"
  	print "    var arr  = str.split('-');"
  	print "    var yyyy = arr[0] - 0;"
  	print "    var jsmm = arr[1] - 1;"
  	print "    var dd   = arr[2] - 0;"
  	print "    return new Date(yyyy, jsmm, dd);"
	print "  }"

	print "</script>"
}