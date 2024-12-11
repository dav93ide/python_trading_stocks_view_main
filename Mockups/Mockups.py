from random import *
import uuid
from Resources.Constants import *
from Classes.PlatformData import PlatformData

class Mockups:

    MOCKUP_USER_CAPITAL = 10000

    MOCKUP_USERNAMES = ["AA", "TiA", "Mo", "Puzzi", "unSacco93", "penegrande69", "kita", "bellissimo"]
    MOCKUP_PLATFORM_NAMES = ["Platform1", "platform2", "platform3", "platform4"]
    MOCKUP_PASSWORDS = ["password1", "password", "password3"]
    MOCKUP_EMAILS = ["aa@gmail.com", "ds@gmail.com", "bellissima@gmail.com"]
    MOCKUP_TOT_CAPITAL = [5000, 1000, 2000, 3000, 4000]
    MOCKUP_TOT_PL = [+10, -20, +25, -30]

    @staticmethod
    def get_mockup_platform_data(num):
        datas = []
        for i in range(0, num):
            id = uuid.uuid4()
            mod = randint(0, len(Mockups.MOCKUP_PLATFORM_NAMES) - 1)
            name =  Mockups.MOCKUP_PLATFORM_NAMES[mod]
            mod = randint(0, len(PlatformType) - 1)
            tt = PlatformType.ETORO
            ttt = PlatformType(1)
            typ = PlatformType(mod)
            mod = randint(0, len(Mockups.MOCKUP_USERNAMES) - 1)
            username = Mockups.MOCKUP_USERNAMES[mod]
            mod = randint(0, len(Mockups.MOCKUP_PASSWORDS) - 1)
            password = Mockups.MOCKUP_PASSWORDS[mod]
            mod = randint(0, len(Mockups.MOCKUP_TOT_CAPITAL) - 1)
            capital = Mockups.MOCKUP_TOT_CAPITAL[mod]
            mod = randint(0, len(Mockups.MOCKUP_EMAILS) - 1)
            email = Mockups.MOCKUP_EMAILS[mod]
            openPositions = randint(0, 10)
            numBots = randint(0, 10)
            mod = randint(0, len(Mockups.MOCKUP_TOT_PL) - 1)
            totPl = Mockups.MOCKUP_TOT_PL[mod]
            pdata = PlatformData(id, name, typ)
            pdata.set_username(username)
            pdata.set_password(password)
            pdata.set_tot_capital_value(capital)
            pdata.set_email(email)
            pdata.set_num_open_positions(openPositions)
            pdata.set_num_bots_running(numBots)
            pdata.set_tot_pl(totPl)
            datas.append(pdata)
        return datas

