import urllib.request as urllib

def main(url):
        print("Checking Connectivity ")

        response = urllib.urlopen(url)
        print("Connected to", url, "succesfully")
        print("The response code was:", response.getcode()) 


print("This is a Site connectivity checker program")
input_url = input("input the url of the site you want to check: ")

main(input_url)


        
