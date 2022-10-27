# Object-Oriented Programming (OOP) in Python

### Terminology
- OOP: programming pattern where properties and methods are aggregated into objects
- Class: blueprint for an object
- Object: instance of a class
- Inheritance: a child class takes the attributes and methods of a parent class

### Class Structure
- Initializer: called when an object is created
   - Attributes
- Getters, setters, other methods

### Class Example: Person
_Attributes_
- Name
- Age
- Occupation

_Methods_
- getName
- setAge
- changeOccupation

### Inheritance Example: Student
- Inherits attributes and methods from the Person class
- Can override specific attributes and methods

### Adding a new element to the GUI
1. Create a new class for the element (probably make it a subclass of `QWidget`)
2. Implement the initializer and at least one other method to setup the element
3. Update the `widgets/__init__.py` file accordingly
4. In the `utils` folder, add this new element to `header.py` or `body.py`
5. Run the GUI to view the widget and update the class as needed
