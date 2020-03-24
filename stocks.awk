BEGIN {
  ofile = "testing.html"
  print "<!DOCTYPE html><html><head>" > ofile
  printFormValidation()
  print "<title>Investing Challenge</title></head><body>" > ofile
  n = 0
  while("cat stock_names" | getline) {
    stocks[n] = $0
    symbols[n] = substr($1, 2, length($1) - 2)
    n++
  }

  print "<h2>Stock Investing Challange</h2>" > ofile
  print "<form name='myForm' action='' onsubmit='return validateForm()'>" > ofile
  print "<label>Choose Stock 1:</label>" > ofile
  print "<select id='stock1' name='stock1'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<input type='number' min='0' max='100' step='0.01' id='ammount1' name='ammount1'/>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 2:</label>" > ofile
  print "<select id='stock2' name='stock2'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<input type='number' min='0' max='100' step='0.01' id='ammount2' name='ammount2'/>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 3:</label>" > ofile
  print "<select id='stock3' name='stock3'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<input type='number' min='0' max='100' step='0.01' id='ammount3' name='ammount3'/>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 4:</label>" > ofile
  print "<select id='stock4' name='stock4'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<input type='number' min='0' max='100' step='0.01' id='ammount4' name='ammount4'/>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 5:</label>" > ofile
  print "<select id='stock5' name='stock5'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<input type='number' min='0' max='100' step='0.01' id='ammount5' name='ammount5'/>" > ofile
  print "<br>" > ofile

  print "<label>Start Date:</label>" > ofile
  print "<input type='date' id='start' name='start'>" > ofile
  print "<label>End Date:</label>" > ofile
  print "<input type='date' id='end' name='end'>" > ofile
  print "<br>" > ofile

  print "<input type='submit'>" > ofile
  print "</form>" > ofile

  print "</body></html>" > ofile
}

function printFormValidation() {
	print "<script>" > ofile

	print "  function validateForm() {" > ofile
  	print "    var stock1 = document.forms['myForm']['ammount1'].value;" > ofile
  	print "    var stock2 = document.forms['myForm']['ammount2'].value;" > ofile
  	print "    var stock3 = document.forms['myForm']['ammount3'].value;" > ofile
  	print "    var stock4 = document.forms['myForm']['ammount4'].value;" > ofile
  	print "    var stock5 = document.forms['myForm']['ammount5'].value;" > ofile

  	print "    var sum = +stock1 + +stock2 + +stock3 + +stock4 + +stock5;" > ofile
  	print "    if (sum < 0 || sum > 100) {" > ofile
    print "      alert('sum must be less than $100');" > ofile
    print "      return false;" > ofile
  	print "    }" > ofile

  	print "    var startDate = myStringToDate(document.forms['myForm']['start'].value);" > ofile
  	print "    var endDate = myStringToDate(document.forms['myForm']['end'].value);" > ofile
  	print "    if (isNaN(endDate.getTime()) || isNaN(startDate.getTime())) {" > ofile
    print "      alert('Missing date');" > ofile
    print "      return false;" > ofile
  	print "    }" > ofile
  	print "    if (endDate.getTime() <= startDate.getTime()) {" > ofile
    print "      alert('Time cant go backwards!');" > ofile
    print "      return false;" > ofile
  	print "    }" > ofile
  	print "    if (endDate.getTime() > (new Date()).getTime()){" > ofile
    print "      alert('cant predict the future!');" > ofile
    print "      return false;" > ofile
  	print "    }" > ofile
  	print "    if (startDate.getTime() < 788918400000){" > ofile
    print "      alert('too far in the past! try something after 1995!');" > ofile
    print "      return false;" > ofile
  	print "    }" > ofile

	print "  }" > ofile


	print "  function myStringToDate(str) {" > ofile
  	print "    var arr  = str.split('-');" > ofile
  	print "    var yyyy = arr[0] - 0;" > ofile
  	print "    var jsmm = arr[1] - 1;" > ofile
  	print "    var dd   = arr[2] - 0;" > ofile
  	print "    return new Date(yyyy, jsmm, dd);" > ofile
	print "  }" > ofile

	print "</script>" > ofile
}