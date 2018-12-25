# WebTimer

This script takes input a time, and openrandom argument (to randomly open a url), or openbyurl argument (to open a specified url) and a url to open at given time.

--help argument can be used to see all arguments and there description.

## Handling "WebDriverException":

If you get this exception saying geckodriver or chromedriver needs to be in path, you need to download geckodriver or chromedriver and copy it to /usr/local/bin and you will not need to change code for specifying the path ([Link to solution](https://stackoverflow.com/a/40931903)).