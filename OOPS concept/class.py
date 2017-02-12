# Example 1 : Classes and Object

# class aircraft:
#     body = "aluminium"
#     size = 75.30
#
#     def work(self):
#         return "This aircraft is used in war"
#
#
#
# sukhoi = aircraft()
#
# print sukhoi.body
# print sukhoi.size
#
# print sukhoi.work()



#


# ****************************************************************************************************
# ****************************************************************************************************

# Example 2 : Subclasses and SuperClasses
#
# This is the first Class and it is the main class
#
#     class aircraft:
#         body = "aluminium"
#         size = 75.30
#
#         def aircraft_names(self, name):
#             self.name = name
#
#         def displayname_aircraft(self):
#             return self.name

### This is second class and  it is the sub class
# class small_aircraft(aircraft):
#     size = 85.80
#
#
# first_aircraft = aircraft()
# second_aircraft = aircraft()
#
# print first_aircraft.body
# print second_aircraft.body
#
# print "+++++++++++++++++++++++++++++++++"
#
# print first_aircraft.size
# print second_aircraft.size
#
# print "+++++++++++++++++++++++++++++++++"
#
# first_aircraft.aircraft_names("sukhoi")
# second_aircraft.aircraft_names("Blackbird")
#
#
# print first_aircraft.displayname_aircraft()
# print second_aircraft.displayname_aircraft()
# print "+++++++++++++++++++++++++++++++++"
#
# print first_aircraft.__dict__, second_aircraft.__dict__
#
# print "+++++++++++++++++++++++++++++++++"
#
#
# third_aircraft = small_aircraft()
# fourth_aircraft = small_aircraft()
#
# print '\n'
# print third_aircraft.size
# print fourth_aircraft.body
# #
# # print "+++++++++++++++++++++++++++++++++"
#
#
# third_aircraft.aircraft_names("Rafale")
# fourth_aircraft.aircraft_names("Horten Ho 229")
#
# print third_aircraft.displayname_aircraft()
#
# print fourth_aircraft.displayname_aircraft()
#
# print "+++++++++++++++++++++++++++++++++"


# **************************************************************************************************
# **************************************************************************************************

#
# class world:
#     country = "India"
#     population = 1293057000
#
#     def capital_Of_India(self,name):
#         self.name = name
#
#     def display_capital_of_India(self):
#         return self.name
#
#     def official_languages(self,language):
#         self.language = language
#
#     def display_official_languages(self):
#         return self.language
#
# tourist1 = world()
# tourist2 = world()
#
# print tourist1.country
# print tourist2.population
#
# tourist1.capital_Of_India("Delhi")
# tourist2.capital_Of_India("Delhi")
#
# print '\n'
#
# print tourist1.display_capital_of_India()
# print tourist2.display_capital_of_India()
#
# tourist1.official_languages("English")
# tourist2.official_languages("English")
#
# print '\n'
#
# print tourist1.display_official_languages()
# print tourist2.display_official_languages()

# ******************************************************************************
# ******************************************************************************


# class one:
#     color1 = "yellow"
#     color2 = "green"
#
#
# class two(one):
#     color2 = "red"
#
#
# pallete1 = one()
# pallete2 = two()
#
# print pallete1.color1
# print pallete1.color2
#
# print "******************"
#
# print pallete2.color1
# print pallete2.color2


# *********************************************************************************************
# ************************************************************************************************
#
# class Alpha:
#     alpha_quote = "I am head of the family !"
#
#
# class Beta:
#     beta_quote = "After Alpha Everyone should follow me!"
#
#
# class Charlie (Alpha,Beta):
#     charlie_quote = "I just follow the commands of Alpha and Beta !"
#
#
# tango = Charlie()
# print tango.alpha_quote
# print tango.beta_quote
# print tango.charlie_quote


# ***************************************************************************************************
# **************************************************************************************************
# What is Constructor in oops  ?
# #
# class rock:
#     def __init__(self):
#         print " Rock, Paper and Scissors!"
#
#
#
# object1 = rock()



####################################################################################################
#
# class parent:
#     mother = "Maria"
#     father = "Jacob"
#
#     def sister_name(self,name):
#         self.name = name
#
#     def display_sister_name(self):
#         return self.name
#
#
#
#
# son = parent()
# print son.mother
# print son.father
#
# son.sister_name("Melany")
#
# # print son.display_sister_name()
# #
# # print "''''''''''''''''''"
# #
# # print parent.display_sister_name(son) # name of sister can also be accessed trough class(parent)



#############################################################################################################
#
# class parent:
#     def __init__(self,mother,father,sister):
#         self.mother = mother
#         self.father = father
#         self.sister = sister
#
# son = parent("Maria", "Jacob", "melany")
#
# print son.mother
# print son.father
# print son.sister
#





#####################################################################################################################
#
# class python:
#     def __init__(self):
#         self.__pri = " I am private "
#         self._pro = " I am protected "
#         self.pub = " I am public "
#
#
# ob = python()
# print ob.pub
# print ob._pro
# # print ob.__pri

# class parent:
#     def __init__(self,name):
#         self.name = name
#         self.__mother = "Ruby"
#
#
# ob = parent("james")
# print ob.name
# print ob._parent__mother


# class man:
#     def name(self):
#         print "james"
#
#
# obj = man()
# man.name(obj)
# obj.name()
#
#
## static Method

# class parent:
#     @staticmethod
#     def static_method(attr):
#         print attr
#
# parent.static_method("This is the static method !")

#
















