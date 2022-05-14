import requests

from Helpers.MailSender import MailSender

class PrizebondChecker:
    url = "https://www.bb.org.bd/en/index.php/investfacility/prizebond"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic e3tjbGllbnQtaWR9fTp7e2NsaWVudC1zZWNyZXR9fQ==',
    'Cookie': 'TS01de1f8a=01e82ae0e4ed8a5b09d1e3b9188d97f50325732790243f8b7d4b74b75447a39fdfa1d3d88c380c90776654ac1094559f8d39bd7af0; ci_session=0cljtg5lhkklkr4u61jb4db870tk5jee'
    }

    def check():
        payload = 'gsearch=0084301~0084400,0874326~0874340,0905173,0905174,0905179,0591322,0847421,0859879,0885018,0885014'
        response = requests.request("POST", PrizebondChecker.url, headers=PrizebondChecker.headers, data=payload)

        if response.text.find('Congratulations') == -1:
            return
        else:
            sender = MailSender()
            sender.send([sender.receiverEmail], 'Congratulations. You won a prizebond', 'Please check govt. website to see which prizebond won.')