from Classes.Investment import Investment
from Classes.BaseClasses.BaseClass import BaseClass

class Portfolio(BaseClass):
	
	__id = None
	mInvestments = []
	
	def __init__(self, id):
		super().__init__(id)
		self.__mInvestments = []

	# Getter Methods
	def get_investments(self):
		return self.__mInvestments

	# Setter Methods
	def set_investments(self, investments: [Investment]):
		self.__mInvestments = investments

	# To String
	def __str__(self):
		return 	"####################\n"\
				f"# {Portfolio.__name__}\n"\
				"####################\n"\
				f"{super().__str__()} \n"\
				f"#- __mInvestments: {self.mInvestments.__str__()} \n"\
				"####################"
