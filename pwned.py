import hashlib, requests, json, sys

def check_pwned_pwd(pw_in):
    sh1hash = hashlib.sha1(pw_in.encode('utf-8')).hexdigest().upper()
    head, tail = sh1hash[:5], sh1hash[5:]
    r = requests.get('https://api.pwnedpasswords.com/range/{0}'.format(head))
    
    hashes = (line.split(':') for line in r.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail),0)
    return sh1hash ,count


def main(args):
    pwd_in = args[0]
    for pwd_in in args:
        try:
            sh1hash, count = check_pwned_pwd(pwd_in)  
            if count:
                print('Password : "{0}" found {1} times [{2}]'.format(pwd_in, count, sh1hash))
            else:
                print('Your password has not bin pwned...yet! Keep Safe')
        except Exception:
            print('Something went wrong : {0}'.format(sys.exc_info()[0]))

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) 