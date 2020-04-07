## -- USE AT YOUR OWN RISK --
## -- USE AT YOUR OWN RISK --
## -- USE AT YOUR OWN RISK --

# amz_mobi
This script can automatically "buy" e-books that are free on amazon.com.

--Initially this will only work on Linux.

### The start script is a bash command that have:

  pwd
  
  wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
  
  unzip chromedriver_linux64.zip \n
  
  rm chromedriver_linux64.zip \n
  
  sudo mv chromedriver /usr/bin \n
  
### Using the Python Script

You can run the "start" script, or make this manually. For windows you have to figure out how to install the chromedriver, and maybe the script work.

Then you can use "python main.py" to start buying the books.

The starter point is:

https://www.amazon.com.br/s?i=digital-text&bbn=5308307011&rh=n%3A5308307011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A6406077011%7C6406078011&s=popularity-rank&dc&page=1&language=en_US&_encoding=UTF8&fst=as%3Aoff&linkCode=sl2&linkId=02321018ed113bd4621621a252c9f986&qid=1586219653&rnid=19553430011&ref=sr_pg_2

#### CURRENTLY THEY BUY PORTUGUESES AND ENGLISH BOOKS, CHANGE IF YOU WANT.

but you can use your own filters, but remember to change the link little part of the link "&page=1&" to "&page={}&" and set the initial pages on GLOBAL VARIABLES.

Just warning you that the script use the "One-click buy" so, just for sure, remove your credit card before using...

You can help me improve this!

## DISCLAIMER
I RECOMEND TO ACCESS THE LINK AND SEE WHAT IT SHOWS, MAKE SURE WHAT ARE YOU SEEING. 

I CANOOT BE RESPONSIBLE IF YOU CHANGE THE PROGRAM AND BUY REAL STUFFS USING THIS.
THE SCRIPT USE A LINK FOR ONLY $0,0 PRICES ITENS, 
SO IF YOU USE A DIFERENT LINK, WITH A CREDIT CARD, MAYBE YOU WILL ACTUALY BUY A LOT OF THINGS...

## -- USE AT YOUR OWN RISK --
## -- USE AT YOUR OWN RISK --
## -- USE AT YOUR OWN RISK --
