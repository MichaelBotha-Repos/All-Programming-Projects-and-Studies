"""
FACETED DATA:

Read Schmitz et al (2016) article about faceted data.

Questions:
1.) Do you think this is a good approach to protect systems from data leakage?
2.) What are the pros and cons?
3.) Create a basic outline design of how you would create such a system in Python.

Answers:
1.) Yes I do, because it applies the principle of authorisation to data specifically,
    ensuring that the data carries a form of metadata and thereby ownership. 
2.) Pros:
    > Allocates ownership to data. 
    > Does not require multiple systems for different levels of data secrecy.

    Cons:
    > May decrease code performance due to additional checking requried.
    > Increases data size due to the additional metadata appended to each value.

3.) Please refer to the below program, where a class is created to represent data
    in a system. The class inherits a standard Python data type and adds the features
    inherent in faceted data viz. owners and views. This meta data will be checked
    whenever a user wants to access or alter data.
    

"""
# Class creation
class FacetedString(str):
    """
        This class extends the native string class
        by adding faceted metadata
    """
    
    def __init__(self, string):
        """ An object is initialised by adding the faceted data
            elements to it"""

        super().__init__()
        #self.string = string + "<<>>" + user + view

# Example use

test_data = "Bank: FNB ID: 85467834"
faceted_test_data = FacetedString(test_data)
#print(faceted_test_data.string)



























