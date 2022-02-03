"""
FACETED DATA:

Read Schmitz et al (2016) article about faceted data.

Questions:
1.) Do you think this is a good approach to protect systems from data leakage?
2.) What are the pros and cons?
3.) Create a basic outline design of how you would create such a system in Python.

Answers:
1.) Yes I do, because it applies the principle of authorisation specifically to data,
    ensuring that the data carries a form of metadata and thereby ownership
    (Schmitz et al., 2016). 
2.) Pros:
    > Allocates ownership to data (Schmitz et al., 2016). 
    > Does not require multiple systems for different
      levels of data secrecy (Schmitz et al., 2016).

    Cons:
    > May decrease code performance due to additional
      checking required (Schmitz et al., 2016).
    > Increases data size due to the additional metadata appended to each value.

3.) Please refer to the below program, where a class is created to represent data
    in a system. The class inherits a standard Python data type and adds the features
    inherent in faceted data viz. owners and views. This meta data will be checked
    whenever a user wants to access or alter data.

    Another method is to simply create a list with the first element being the
    original data and the second,third and so on the meta data.

References:

Schmitz, T., Rhodes, D., Austin, T.H., Knowles, K., Flanagan, C. (2016)
Faceted Dynamic Information Flow via Control and Data Monads. In: Piessens F., Viganò L.
(eds) Principles of Security and Trust. POST 2016.
Lecture Notes in Computer Science, vol 9635. Springer, Berlin, Heidelberg


"""


# Class creation.
class FacetedList(list):
    """
        This class extends the native string class
        by adding faceted metadata
    """
    
    def __init__(self, data, owner, view):
        """ An object is initialised by adding the faceted data
            elements to it"""

        list.__init__(self, data)
        self.owner = owner
        self.view = view
        

# Example use:

test_data = [1234, 987, 100, 5231]
faceted_test_data = FacetedList(test_data, "Michael", 1000)

# The faceted list behaves the same as a normal list
# however has meta values.
for elem in faceted_test_data:
    print(elem)

print(faceted_test_data.owner)
print(faceted_test_data.view)



























