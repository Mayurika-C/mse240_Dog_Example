# Dog.py
#
# Author: Oliver Schneider 
# Email: oliver.schneider@uwaterloo.ca
# Student ID: 1234567890 
# 
# Source code for the Dog class.

class Dog:
    """ Dog
        A class representing an individual dog.
    """

    def __init__(self, name : str, breed : str, gender : str, initial_weight : float, 
                 colour: str, potential_health_issues : list[str], birth_year: int):
        """ Dog constructor

            name    the dog's given name
            breed   the dog's breed
            gender  the dog's gender
            initial_weight  the dog's initial weight (lbs)
            colour  a description of the dog's colour
            potential_health_issues a list of known potential health issues (each a string)
            birth_year  the year the dog was born
        """
        self._name = name
        self._breed = breed
        self._gender = gender
        self._weight = initial_weight
        self._colour = colour
        self._potential_health_issues = potential_health_issues
        self._birth_year = birth_year


    #############
    # Accessors #
    #############

    
    def get_name(self) -> str:
        """ get_name

            returns the dog's name as a string
        """
        #stub
        return self._name
    

    def get_breed(self) -> str:
        """ get_breed

            returns the dog's breed as a string
        """
        #stub
        return self._breed
    
    def get_gender(self) -> str:
        """ get_gender

            returns the dog's gender as a string
        """
        #stub
        return self._gender
    
    def get_weight(self) -> float:
        """ get_weight

            return the dog's weight in lbs
        """
        #stub
        return self._weight

    def get_colour(self) -> str:
        """ get_colour

            return the dog's colour as a description
        """
        #stub
        return self._colour
    
    def get_potential_health_issues(self) -> list[str]:
        """ get_potential_health_issues

            return the dog's known potential_health_issues as a list
        """
        #stub
        return self._potential_health_issues
    
    def get_age(self) -> int:
        """ get_age

            return the dog's age
        """
        #stub
        return self._birth_year



    ############
    # Mutators #
    ############


    def set_name(self, new_name : str):
        """ set_name

            new_name    the dog's new name
        """
        #stub
        pass
    
    def set_weight(self, new_weight):
        """ set_weight

            new_weight  the new measured weight of the dog (in lbs)
        """
        #stub
        pass
    
    def add_potential_health_issue(self, health_issue : str):
        """ add_potential_health_issues

            add a health issue to the potential health issues
        """
        #stub
        pass

