"""
FACETED DATA:

Read Schmitz et al (2016) article about faceted data.

Questions:
1.) Do you think this is a good approach to protect systems from data leakage?
2.) What are the pros and cons?
3.) Create a basic outline design of how you would create such a system in Python.

Answers:
1.) Yes I do, because it applies the principle of authorisation to data specifically,
    ensuring that the data carries a form of metadata. 
2.) Pros:
    > Does not require multiple systems for ..

    Cons:
    > May decrease code performance due to additional checking
    > Increases data size due to the additional metadata appended to each value

3.) Please refer to the below program, where a class is created to represent data
    in a system. The class inherits standard Python data types and adds the features
    inher in faceted data. 
    

"""
# Class creation
class FacetedString(str):
    """
        This class extends the native string class
        by addng faceted data metadata
    """
    
    def __init__(self, string, user, view):
        """ An object is initialised by adding the faceted data
            elements to it"""
        
        self.string = string
        self.string = string + "<<>>" + str(user) + str(view)

# Example use





























