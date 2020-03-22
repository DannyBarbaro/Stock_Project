BEGIN {
  ofile = "testing.html"
  print "<!DOCTYPE html><html><head><title>Investing Challenge</title></head><body>" > ofile
  n = 0
  while("cat stock_names" | getline) {
    stocks[n] = $0
    symbols[n] = substr($2, 2, length($2) - 2)
    n++
  }

  print "<h2>Stock Investing Challange</h2>" > ofile
  print "<form action=''>" > ofile
  print "<label>Choose Stock 1:</label>" > ofile
  print "<select id='stock1' name='stock1'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 2:</label>" > ofile
  print "<select id='stock2' name='stock2'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 3:</label>" > ofile
  print "<select id='stock3' name='stock3'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 4:</label>" > ofile
  print "<select id='stock4' name='stock4'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<br>" > ofile

  print "<label>Choose Stock 5:</label>" > ofile
  print "<select id='stock5' name='stock5'>" > ofile
  for (i = 1; i < n; i++)
    print "<option value='"symbols[i]"'>"stocks[i]"</option>" > ofile
  print "</select>" > ofile
  print "<br>" > ofile
  print "<input type='submit'>" > ofile
  print "</form>" > ofile

  print "</body></html>" > ofile
}