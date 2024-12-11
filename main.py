import wx, logging
import faulthandler
from Environment import Environment
from MainApplication import MainApplication

def main():
    faulthandler.enable()
    Environment().init()
    application = MainApplication(False)
    application.MainLoop()

if __name__ == "__main__":
    main()