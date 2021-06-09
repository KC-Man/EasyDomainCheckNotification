#!/usr/bin/env python3

debug = 0
domains = ['domain.tld', 'example.tld']
recipientMail = '--YOUR_EMAIL--'
smtpData = {
    'sender': '--SMTP_EMAIL--',
    'host': '--SMTP_HOST--',
    'port': '--SMTP_PORT--',
    'pw': '--SMTP_PW--',
}
apiData = {
    'url': 'https://domain-availability.whoisxmlapi.com/api/v1',
    'key': '--API_KEX--',
    'mode': 'DNS_AND_WHOIS',
    'credits': 'WHOIS',
    'outputFormat': 'JSON',
    'timeout_ms': 300,
}
