fileVer='201907041350'
print('main ver ' + fileVer)
from main.ota_updater import OTAUpdater
#from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/TribulusTechOTA/yfidot.git')
    ota_updater.download_and_install_update_if_available('Tribulus', 'Redhat@345')

def start():
    #import smartplug
    #smartplug.listen()
    print("Hello 1")

def boot():
    download_and_install_update_if_available()
    start()

#boot()
