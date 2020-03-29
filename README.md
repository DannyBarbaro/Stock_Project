# Stock_Project
A basic stock simulator written in awk. You have $100 dollars to invest in 5 companies over any date range from 2005 to now. Good luck!

## Super simple way to run locally
- git clone
- mkdir cgi-bin
- cp stocks.cgi cgi-bin/
- do all the permissions stuff here
- python -m CGIHTTPServer
- in browser, go to localhost:8000/cgi-bin/stocks.cgi


## Screenshots
#### Home Page
![alt text](https://raw.githubusercontent.com/DannyBarbaro/Stock_Project/master/Screenshots/1.PNG)
#### Filled out form
![alt text](https://raw.githubusercontent.com/DannyBarbaro/Stock_Project/master/Screenshots/2.PNG)

#### Result
![alt text](https://raw.githubusercontent.com/DannyBarbaro/Stock_Project/master/Screenshots/3.PNG)
![alt text](https://raw.githubusercontent.com/DannyBarbaro/Stock_Project/master/Screenshots/4.PNG)
![alt text](https://raw.githubusercontent.com/DannyBarbaro/Stock_Project/master/Screenshots/5.PNG)

## Known bugs
- Setting a date before the company existed. A division by 0 error occurs and the screen is not rendered. Try a different stock or a later date!
- Choosing a date that is a holiday. Similar division by 0 error occurs. Our validator will screen for weekends but holidays are a little tougher to implement
- Basically if the screen doesn't load, try different dates and different stocks to debug!
