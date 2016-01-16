import logging
import requests
import sys

format = '[%(asctime)s] {%(pathname)s:%(lineno)d}' + \
    ' [%(levelname)s] - %(message)s'
logging.basicConfig(
    format=format,
    level=logging.DEBUG,
    datefmt='%H:%M:%S'
)
logger = logging.getLogger()


class Nigeria(object):
    states_and_capitals = {
        "Abia": "Umuahia",
        "Adamawa": "Yola",
        "Akwa Ibom": "Uyo",
        "Anambra": "Awka",
        "Bauchi": "Bauchi",
        "Bayelsa": "Yenagoa",
        "Benue": "Makurdi",
        "Borno": "Maiduguri",
        "Cross River": "Calabar",
        "Delta": "Asaba",
        "Ebonyi": "Abakaliki",
        "Edo": "Benin City",
        "Ekiti": "Ado-Ekiti",
        "Enugu": "Enugu",
        "FCT": "Abuja",
        "Gombe": "Gombe",
        "Imo": "Owerri",
        "Jigawa": "Dutse",
        "Kaduna": "Kaduna",
        "Kano": "Kano",
        "Katsina": "Katsina",
        "Kebbi": "Birnin Kebbi",
        "Kogi": "Lokoja",
        "Kwara": "Ilorin",
        "Lagos": "Ikeja",
        "Nasarawa": "Lafia",
        "Niger": "Minna",
        "Ogun": "Abeokuta",
        "Ondo": "Akure",
        "Osun": "Oshogbo",
        "Oyo": "Ibadan",
        "Plateau": "Jos",
        "Rivers": "Port Harcourt",
        "Sokoto": "Sokoto",
        "Taraba": "Jalingo",
        "Yobe": "Damaturu",
        "Zamfara": "Gusau"
    }

    def __init__(self):
        logger.info("Creating a new instance of Nigeria")

    def states(self):
        self.states = self.states_and_capitals.keys()
        self.states.sort()
        return self.states

    def capitals(self):
        self.capitals = self.states_and_capitals.values()
        self.capitals.sort()
        return self.capitals

    def states_and_capital(self):
        return list(
            {key: value} for key,
            value in self.states_and_capitals.iteritems()
        )

    def retrieve_current_country_president(self):
        url = 'http://google.com'
        return requests.get(url)


def main():
    print "You wouldn't be needing this if you had paid attention in class."

if __name__ == "__main__":
    sys.exit(main())
