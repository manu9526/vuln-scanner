import requests
from bs4 import BeautifulSoup
 # colored text
class bcolors:
    RED = '\033[31m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'     
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fetch_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            print("Page fetched Successfully")
            return response.text
        else:
            print(f"Failed to Fetch Page/ Status code: {response.status_code}")
            return None
    except Exception as e:
            print (f"An error occurrd: {e}")
            return None

def find_forms(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    forms = soup.find_all('form')
    print(f"{bcolors.RED} Found {len(forms)} form(s) on the page.{bcolors.ENDC}")

    for i, form in enumerate(forms, 1):
        print(f"\nForm {i}:")

        # check for http or https
        action = form.get('action')
        if action and action.startswith('http:'):
            print(f"{bcolors.WARNING} Warning: Form uses HTTP instead of HTTPS! Action: {action}{bcolors.ENDC}")
        elif action and action.startswith('https:'):
            print(f"{bcolors.OKGREEN}Form action is secure (HTTPS). Action: {action}{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Form action not specified or relative. Be cautious!{bcolors.ENDC}")

        inputs = form.find_all('input')
        print(f" - {bcolors.RED} Found {len(inputs)} inputs(s) in this form. {bcolors.ENDC}")
        for inp in inputs:
            print(f"{bcolors.BOLD}{bcolors.WARNING}  * Input name: {bcolors.ENDC}{bcolors.OKCYAN}{inp.get('name')}{bcolors.ENDC} {bcolors.WARNING} * Type: {bcolors.ENDC} {bcolors.OKCYAN}{inp.get('type')} {bcolors.ENDC}")

# main 

if __name__ == "__main__":

    url = input("Enter the URL to scan: ")
    html_content=fetch_page(url)

    if html_content:
       find_forms(html_content, url)



      