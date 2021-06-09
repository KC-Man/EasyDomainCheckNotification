#!/usr/bin/env python3

# Add this file to Crontab

import sys
import config

from Classes import EDCN

dClass = EDCN.EasyDomainCheckNotification(config.recipientMail, config.domains, config.apiData, config.smtpData)
dClass.check_status()

sys.exit()
