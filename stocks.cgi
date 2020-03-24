#! /usr/bin/awk -f
BEGIN {
  print "Content-type: text/html \n" 
  print "<!DOCTYPE html><html><head>"
  printFormValidation()
  print "<title>Investing Challenge</title></head><body>"
  n = 0
  while("cat stock_names" | getline) {
    stocks[n] = $0
    symbols[n] = substr($1, 2, length($1) - 2)
    n++
  }

  print "<h2>Stock Investing Challange</h2>"
  print "<form name='myForm' action='' onsubmit='return validateForm()'>"
  print "<label>Choose Stock 1:</label>"
  print "<select id='stock1' name='stock1'>"
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>"
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='ammount1' name='ammount1'/>"
  print "<br>"

  print "<label>Choose Stock 2:</label>"
  print "<select id='stock2' name='stock2'>"
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>"
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='ammount2' name='ammount2'/>"
  print "<br>"

  print "<label>Choose Stock 3:</label>"
  print "<select id='stock3' name='stock3'>"
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>"
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='ammount3' name='ammount3'/>"
  print "<br>"

  print "<label>Choose Stock 4:</label>"
  print "<select id='stock4' name='stock4'>"
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>"
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='ammount4' name='ammount4'/>"
  print "<br>"

  print "<label>Choose Stock 5:</label>"
  print "<select id='stock5' name='stock5'>"
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>"
  print "</select>"
  print "<input type='number' min='0' max='100' step='0.01' id='ammount5' name='ammount5'/>"
  print "<br>"

  print "<label>Start Date:</label>"
  print "<input type='date' id='start' name='start'>"
  print "<label>End Date:</label>"
  print "<input type='date' id='end' name='end'>"
  print "<br>"

  print "<input type='submit'>"
  print "</form>"

  print "</body></html>"
}

function printFormValidation() {
	print "<script>"

	print "  function validateForm() {"
  	print "    var stock1 = document.forms['myForm']['ammount1'].value;"
  	print "    var stock2 = document.forms['myForm']['ammount2'].value;"
  	print "    var stock3 = document.forms['myForm']['ammount3'].value;"
  	print "    var stock4 = document.forms['myForm']['ammount4'].value;"
  	print "    var stock5 = document.forms['myForm']['ammount5'].value;"

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
  	print "    if (startDate.getTime() < 788918400000){"
    print "      alert('Too far in the past! try something after 1995!');"
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