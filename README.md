# WebTimer

This script takes input a time, and --openrandom argument (to randomly open a URL), or --openbyurl argument (to open a specified URL) and a URL with --url argument to open at given time.

--help argument can be used to see all arguments and there description.

'links.txt' file contains the URLs used to be selected randomly with --openrandom argument. Links can be added randomly to this file.

## Handling "WebDriverException":

If you get this exception saying geckodriver or chromedriver needs to be in path, you need to download geckodriver or chromedriver and copy it to /usr/local/bin and you will not need to change code for specifying the path ([Link to solution](https://stackoverflow.com/a/40931903)).
