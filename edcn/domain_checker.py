#!/usr/bin/env python3

import urllib.request
import urllib.error
import json
import time
import smtplib

from email.message import EmailMessage


class DomainChecker:
    def __init__(self, email, domains, api_data, smtp_data, mail_debug_mode=0):
        self.email = email
        self.domains = domains
        self.api_data = api_data
        self.smtp_data = smtp_data
        self.mail_debug_mode = mail_debug_mode

    def check_status(self):
        available_domains = []
        if not self.domains:
            print('No domains added to the config')
            return False
        for dname in self.domains:
            status = self.request_domain_status(dname)
            if status:
                available_domains.append(status)
            # Convert ms to s
            time.sleep(self.api_data['timeout_ms'] / 100)
        if available_domains:
            print(available_domains)
            self.mail_service(available_domains)
        else:
            print('All domains are occupied')

    def request_domain_status(self, dname):
        url = self.build_api_uri(dname)
        url = self.api_data['url'] + url
        urllib.request.urlcleanup()
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as responseObj:
                response = responseObj.read()
                if response != '':
                    res = json.loads(response)
                    if res['DomainInfo']['domainAvailability'] == 'AVAILABLE':
                        return dname
                    else:
                        return False
                else:
                    print('Error: return empty response')
                    return False

        except urllib.error.URLError as error:
            print('Failed to fetch API for Domain: ' + dname)
            print(error.reason)
            return False

    def build_api_uri(self, dname):
        req_api_querystring = '?apiKey=' + self.api_data['key']
        req_api_querystring += '&domainName=' + dname
        req_api_querystring += '&mode=' + self.api_data['mode']
        req_api_querystring += '&credits=' + self.api_data['credits']
        req_api_querystring += '&outputFormat=' + self.api_data['outputFormat']
        return req_api_querystring

    def mail_service(self, domain_list):
        sender = self.smtp_data['sender']
        pw = self.smtp_data['pw']
        host = self.smtp_data['host']
        port = int(self.smtp_data['port'])
        recipient = self.email
        msg = EmailMessage()
        msg.add_header("From", sender)
        msg.add_header("To", recipient)
        msg.add_header("Subject", 'Easy Domain Check Notification Service')
        body = """Following domains are available to buy:"""
        for dl in domain_list:
            body += '\r\n' + '-' + dl + '\r\n'
        msg.set_content(body)
        try:
            smtp_obj = smtplib.SMTP_SSL(host, port, None, None, None, 45)
            smtp_obj.set_debuglevel(self.mail_debug_mode)
            smtp_obj.login(sender, pw)
            smtp_obj.sendmail(sender, recipient, msg.as_string())
            smtp_obj.quit()
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")
