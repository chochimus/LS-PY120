# You can determine the Pythons look order by using the class.mro() method
# It will first check the objects own class instance, then from left to right on 
# The inheritance chain check everyobject, ending with the Object superclass.
# In the case of the my_obj we would call it like so my_obj.__class__.mro()