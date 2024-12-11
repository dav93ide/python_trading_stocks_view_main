from multipledispatch import dispatch
from Classes.BaseClasses.BaseClass import BaseClass
from Classes.Portfolio import Portfolio

class Investor(BaseClass):
	
	__mName = None
	__mSurname = None
	__mUsername = None
	__mPortfolio = None
	__mNumOfCopiers = None
	__mNumOfFollowers = None
	__mCopiers = []
	__mTotCapital = None
	__mTotPL = None
	__mPercPL = None
	
	def __init__(self, id):
		super().__init__(id)
		self.__mCopiers = []
		
#region - Getter Methods
	def get_name(self):
		return self.__mName

	def get_surname(self):
		return self.__mSurname

	def get_username(self):
		return self.__mUsername

	def get_portfolio(self):
		return self.__mPortfolio

	def get_num_of_copiers(self):
		return self.__mNumOfCopiers

	def get_num_of_followers(self):
		return self.__mNumOfFollowers

	def get_copiers(self):
		return self.__mCopiers

	def get_tot_capital(self):
		return self.__mTotCapital

	def get_tot_pl(self):
		return self.__mTotPL

	def get_perc_pl(self):
		return self.__mPercPL
#endregion
	
#region - Setter Methods
	def set_name(self, name):
		self.__mName = name

	def set_surname(self, surname):
		self.__mSurname = surname

	def set_username(self, username):
		self.__mUsername = username

	def set_portfolio(self, portfolio):
		self.__mPortfolio = portfolio

	def set_num_of_copiers(self, num):
		self.__mNumOfCopiers = num

	def set_num_of_followers(self, num):
		self.__mNumOfFollowers = num

	def set_copiers(self, copiers):
		self.__mCopiers = copiers

	def set_tot_capital(self, tot):
		self.__mTotCapital = tot

	def set_tot_pl(self, pl):
		self.__mTotPL = pl

	def set_perc_pl(self, perc):
		self.__mPercPL = perc
#endregion
		
#region - Public Methods
	@dispatch()
	def store_data(self):
		super().store_data(DataFilenames.FILENAME_INVESTOR_DATA_LIST)

	@staticmethod
	@dispatch()
	def get_stored_data():
		return super().get_stored_data(DataFilenames.FILENAME_INVESTOR_DATA_LIST)
#endregion

	# To String
	def __str__(self):
		return 	"####################\n"\
				f"# {Investor.__name__}\n"\
				"####################\n"\
				f"{super().__str__()} \n"\
				f"#- __mName: {self.__mName} \n"\
				f"#- __mSurname: {self.__mSurname} \n"\
				f"#- __mUsername: {self.__mUsername} \n"\
				f"#- __mPortfolio: {str(self.__mPortfolio)} \n"\
				f"#- __mNumOfCopiers: {self.__mNumOfCopiers} \n"\
				f"#- __mNumOfFollowers: {self.__mNumOfFollowers} \n"\
				f"#- __mCopiers: {str(self.__mCopiers)} \n"\
				f"#- __mTotCapital: {self.__mTotCapital} \n"\
				f"#- __mTotPL: {self.__mTotPL} \n"\
				f"#- __mPercPL: {self.__mPercPL} \n"\
				"####################"
