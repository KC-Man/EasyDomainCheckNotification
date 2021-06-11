#!/usr/bin/env python3

# Add this file to Crontab

import sys
import config

from edcn import domain_checker

dClass = domain_checker.DomainChecker(config.recipientMail, config.domains, config.apiData, config.smtpData)
dClass.check_status()

sys.exit()
