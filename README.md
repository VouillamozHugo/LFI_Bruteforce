# LFI_Bruteforce
Python script to brute force LFI exploit with a given wordlist of file to test. 
The script will replace the LFI part of the url with all line present in the wordlist. 
The output can be displayed in the console or inside an output file using the -o options 

Required arguments : 
  -w LIST, --wordlist LIST     Wordlist containing files to test with LFI (example: /etc/passwd)
  -u URL, --url URL            The path to the LFI exploit example: http://localhost?file=LFI
  
Example 

python LFI_Bruteforce.py -w /usr/share/wordlist/LFI_List -u http://localhost/page?file=LFI 


options:

 -h, --help                   show this help message and exit
 -w LIST, --wordlist LIST     Wordlist containing files to test with LFI (example: /etc/passwd)
 -u URL, --url URL            The path to the LFI exploit example: http://localhost?file=LFI
 -o DEST, --outfile DEST      Output file to write all informations found
