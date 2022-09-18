from time import sleep
from unicodedata import name
import requests
from tqdm import tqdm
import sys

# number = input("Enter the number: ")
# number = "9618658826"

try:
      n = sys.argv[1].split('=')[1]
      upi = sys.argv[1].split('=')[1]
      if("n" in sys.argv[1]):
        print("Searching with Number: " + n)
        num_lines = sum(1 for line in open('mobile.txt','r'))
        with open('mobile.txt','r') as f:
          for line in tqdm(f, total=num_lines):
                      # print(n + '@' + line)
              upi = n + '@' + line.split('\n')[0]
              uri = 'https://upibankvalidator.com/api/upiValidation?upi='+upi
              response = requests.post(uri)
              if "true" in response.text:
                json = response.json()
                name = json['name']
                vpa = upi

                print("\n")
                print("Found")
                print("-------------------------------------")
                print("Name: " + name)
                print("VPA: " + vpa)
                print("\n")
                print("Searching For Other if Any")
                print("-------------------------------------")
                print("\n")
      elif("upi" in sys.argv[1]):
        print("Searchin with UPI: " + upi)
        uri = 'https://upibankvalidator.com/api/upiValidation?upi='+upi
        response = requests.post(uri)
        if "true" in response.text:
                json = response.json()
                name = json['name']
                vpa = upi

                print("\n")
                print("Found")
                print("-------------------------------------")
                print("Name: " + name)
                print("VPA: " + vpa)
                print("-------------------------------------")
                print("\n")
      else:
        print("Something went wrong..!")
        print("Usage: python trace.py upi=0000000000@upi")
        print("python trace.py n=0000000000")

except IndexError:
     print("Usage: python trace.py upi=0000000000@upi")
     print("python trace.py n=0000000000")


print("Finished....")

