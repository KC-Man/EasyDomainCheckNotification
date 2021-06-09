##EASY Domain Check Notification

This is a simple python script for monitoring occupied domains in the market.
When a domain becomes available, an email will be sent to the recipient email (SMTP).
I am using the whoisxmlapi API to retrieve the domain status. 
If you use a different API feel free to modify the script.

**How to use** 
1. Rename the file "default.config.py" to "config.py"
2. Add your settings and domains to the config file
3. Add file checkDomain.py to the crontab 
   
   For Example: 0 9 * * 1-7 root python3 /PATH/TO/SCRIPT/checkDomain.py >/dev/null 2>&1


**The MIT License**

Copyright 2021 Ka Chun Man <https://kachunman.de>



   
