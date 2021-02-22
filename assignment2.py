import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
    """Downloads the data"""
    response = urllib.request.urlopen(url)
    file_content = response.read().decode('utf-8')
    data  = file_content.split("\n")
    return data
    pass

def processData(file_content):
    dataDic = {}
    file = file_content
    for i in range (len(file)-1):
        row = file[i].split(",")
        num = row[0]
        name = row[1]
        bdate = row[2]
        try:
           bdate = datetime.datetime.strptime(bdate,"%d/%m/%Y")
           dataDic [num] = (name,bdate)
           #“Person  # <id> is <name> with a birthday of<date>”,
        except:
            logging.error("Error processing line #" + str(i) + "for ID "+ num+" value "+bdate)
    return dataDic
    pass


def displayPerson(id, personData):

    try:
        id = id.strip()
        tup = personData[id]
        nm = tup[0]
        bd = tup[1].date()
        out = 'Person {} is {} with a birthday of {}'.format(id,nm,bd)


        return out

    except Exception as e:
        print("No user found with that id")


def main(url):
    print (f"Running main with URL = {url}...")

    info = downloadData(url)
    processed = processData(info)
    id= input("Enter an id: " )
    dp = displayPerson(id,processed)
    print(dp)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    logger = logging.getLogger("assignment2")
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    main(args.url)

