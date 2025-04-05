from sys import argv
from requests import get

try:
    Number = argv[1]
except Exception:
    Number = str(input("Phone Number: "))

url = "http://apilayer.net/api/validate"
ACCESS_KEY = "" # https://numverify.com

params = {
    "access_key": ACCESS_KEY,
    "number": Number,
    "country_code": "",  
    "format": 1
}

if ACCESS_KEY == "":
    print("[-] MISSING API KEY!!")
    exit()

response = get(url, params=params)

def Print_Data(Data):
    Valid = "Yes" if Data['valid'] else "No"
    Number = Data['number']
    Local_Format = Data['local_format']
    International_Format = Data['international_format']
    Country_Code = Data['country_code']
    Country_Prefix = Data['country_prefix']
    Country_Name = Data['country_name']
    Location = Data['location']
    Carrier = Data['carrier']
    Line_Type = Data['line_type']

    print("\n[+] Phone Number Information")
    print("Phone Number         : {0}".format(Number))
    print("Valid Phone Number   : {0}".format(Valid))
    print("Local Format         : {0}".format(Local_Format))
    print("International Format : {0}".format(International_Format))
    print("Country Prefix       : {0}".format(Country_Prefix))
    
    print("\n[+] Phone Information")
    print("Line Type            : {0}".format(Line_Type))
    print("Carrier              : {0}".format(Carrier))
    
    print("\n[+] Geo Information")
    print("Country Name         : {0}".format(Country_Name))
    print("Country Code         : {0}".format(Country_Code))
    print("Location             : {0}".format(Location))

if response.status_code == 200:
    data = response.json()
    Print_Data(data)

else:
    print("[-] Request failed with status code:", response.status_code)
