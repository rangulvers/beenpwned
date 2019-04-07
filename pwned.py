import hashlib, requests, json, sys, argparse

def check_pwned_pwd(pw_in):    
    for pw in pw_in:
        try:
            sh1hash = hashlib.sha1(pw.encode('utf-8')).hexdigest().upper()
            head, tail = sh1hash[:5], sh1hash[5:]
            r = requests.get('https://api.pwnedpasswords.com/range/{0}'.format(head))
            
            hashes = (line.split(':') for line in r.text.splitlines())
            count = next((int(count) for t, count in hashes if t == tail),0)
            if count:
                print('Password : "{0}" found {1} times [{2}]'.format(pw, count, sh1hash))
            else:
                print('Your password has not been pwned...yet! Keep Safe')
        except Exception:
            print('Something went wrong : {0}'.format(sys.exc_info()[0]))

def check_pwned_account(accounts):
    for account in accounts:
        r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{0}'.format(account[0]))
        if r.text:
            for breach in r.json():
                print('{0} -> Account breached at : {1} - {2}'.format(account,breach['Name'], breach['BreachDate']))
        else:
            print("No breach as been found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Report Tool to gather Information from the DCGY API.')
    parser.add_argument('-p','--p', nargs='+')
    parser.add_argument('-u','--u', nargs='+')
    
    args = parser.parse_args()

    if args.p:
        check_pwned_pwd(args.p)
    if args.u:
        check_pwned_account(args.u)