# OO Book

### The object Model

- Classes are blueprints from which we create objects of a given type
- Objects are individual things created by classes
  e.g that value of a given type.
- Instantiation is the process of creating a new
  object
- hiding data and functionality from the code base is
  known as encapsulation, it prevents uneccesary
  manipulation of data. it is done through interfaces
  (methods) that interact with the objects
- polymorphism is the ability for different types to
  respond to the same interface (e.g move on multiple
  types of objects that share the method)
- classes can inherit behaviors and properties
  through inheritance allowing reusable classes and
  specific classes for fine-grained behaviors
- the data in an object defines its state (instance
  variables)
- instance methods (behaviors) operate on instances
  of the class and shared by all class instances
- `__init__` is a magic or dunder method, known as the
  initializer,instance constructor or just constructor
- attributes can be names, or names and values
  attributed to object (includes methods and instance
  variables)
- difference between class Constructor and instance constructor, class orchestrates the instantiation
  of an instance object, calling **new** which creates
  an instance object of the class, the uninitialized
  object is passed to init where it gets initialized
- typical nomenclateur is Constructor for class
  constructor initialized for init

### Classes and Objects

- we focuse on state and behavior when defining a class where state refers
  to data associated with an individual class instance and behavior is what
  class instance objects can do.
- object scope has two main components, methods in the class (including those inherited)
  and instance variables associated with an object
- instance methods belong to the class, instance variables belong to objects
- leading underscore is the simplest convention of marking a variable for internal use
  it doesn't prevent access, but it's a clear indicator.
- two leading underscores causes name mangling, internally the name is stored with a
  prepended underscore and classname followed by the unmangled name
- class methods provide general servicces for the class as a whole rather than the
  individual objects.
- static methods belong to the class but don't need access to class/instance attributes
  typically they provide utitility services to the instance/class methods or users of the class
  (printing rules for a game)

### Magic Methods

- double underscore methods are known as magic methods or dunder methods
- `__str__` defines how object is represented as a string where `__repr__` is a representation
  that could be used to create an instance, hence when defined we should do it like so:
  `return f'Cat({repr(self.name)})'` so that we keep any quotes around strings, etc
- `__str__` will fall back to `__repr__` if no str function exists (not the other way around)
- by default `==` and `!=` only check if the object is the same object, if we want custom
  behavior to compare sepearate objects with similar values we need to define `__eq__` and
  `__ne__` functions
- similar for `__lt__`, `__le__`, `__gt__`, `__ge__` but there will be an error if used without
  defining as there is no default comparison for < <= => >
- all of the functions above should return NotImplemented if the other object isn't an instance
  of the comparing class (unless defined for another class)
- also `__add__`, `__iadd__`, `__sub__`, `__isub__` and mul, truediv, floordiv, mod...
  i versions should return self plain versions should return a new object
- dunder variables exist `__main__` current program being run, `__name__` name of current
  module, `__file__` full path of current running program, `__dict__` dictionary of all instances
  of variables defined by an object

### Inheritance

- lets classes acquire of subclass attributes from another class
- 'is-a' relationship
- mixins are a good way to acieve polymorphism in python, they provide behaviors to other
  classes. They're interface only (standard set of methods to be used wherever needed)
  typically called interface inheritance
- mixins have a 'has-a' realtionship
- collaboration: collaborators are objects a class interacts with to perform its
  responsibilities and functionality (at least one of the class's instance
  methods must use that object to aid the containing class behavior)
- class has a mro() method to find the method resolution order or the lookup path
  it uses when a method is called (where to find it)
- typically when inheriting mixins and superclasses we should put the mixins first
  so that the mro behaves in a way that is expected -> check class -> check mixins ->
  move to superclass

###

- property in python is a combination of a getter
  method and optional setter method (prodive controlled
  access to instance variables and can be dynamic)
