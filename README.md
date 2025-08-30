# Python Learning Journey - Udemy Course

This repository contains my Python learning journey through a comprehensive Udemy course. The project is organized into 11 main sections, each focusing on different Python concepts and programming fundamentals.

## 📚 Course Structure

### 01. Basic Python (`01_basic/`)
- **`01.py`** - Introduction to Python system information
  - Exploring `sys.version` and `sys.copyright`
  - Basic Python environment setup
- **`02_virtual/`** - Virtual Environment Setup
  - **`requirements.txt`** - Project dependencies (requests, flask)

### 02. Data Types (`02_datatypes/`)
Comprehensive coverage of Python data types through 11 chapters:
- **`chapter_1.py`** - Variables and memory management
  - Variable assignment and reassignment
  - Understanding object IDs and memory allocation
- **`chapter_2.py` to `chapter_11.py`** - Advanced data type concepts
  - Strings, numbers, lists, dictionaries, sets, tuples
  - Type conversion and manipulation

### 03. Conditionals (`03_conditionals/`)
Real-world conditional logic examples:
- **`chai_price_calculator.py`** - Price calculator based on cup size
  - Small (₹10), Medium (₹15), Large (₹20)
- **`delivery_fees_waiver.py`** - Delivery fee logic
- **`mini_story_1.py`** - Interactive story with conditions
- **`smart_thermostat.py`** - Temperature control logic
- **`snak_suggestion.py`** - Snack recommendation system
- **`train_seat.py`** - Train seat booking logic

### 04. Loops (`04_loops/`)
Various looping concepts and applications:
- **`01_token_dispenser.py`** - Token dispensing system (1-10)
- **`02_batch_chai.py`** - Batch processing for chai orders
- **`03_tea_orders.py`** - Processing multiple tea orders
- **`04_tea_menu.py`** - Menu display and selection
- **`05_order_summary.py`** - Order summarization
- **`06_tea-temperature.py`** - Temperature monitoring
- **`07_put_of_order.py`** - Out of order handling
- **`08_for_else.py`** - For-else loop constructs
- **`09_walrus.py`** - Walrus operator (:=) usage
- **`10_dictionary_case.py`** - Dictionary iteration patterns

### 05. Functions (`05_functions/`)
Function concepts from basic to advanced:
- **`01_duplication.py`** - Function basics to avoid code duplication
  - Example: `print_order(name, chai_type)` function
- **`02_complex.py`** - Complex function structures
- **`03_hiding.py`** - Information hiding principles
- **`04_readability.py`** - Code readability improvements
- **`05_trace.py`** - Function execution tracing
- **`06_scopes.py`** - Variable scope concepts
- **`07_nonlocal.py`** - Nonlocal keyword usage
- **`08_global_scope.py`** - Global scope management
- **`09_input_params.py`** - Parameter handling
- **`10_return.py`** - Return statement usage
- **`11_types_of_functions.py`** - Different function types
- **`12_built_in.py`** - Built-in function exploration
- **`13_invoice_generator.py`** - Practical invoice generation

### 06. Chai Business (`06_chai_business/`)
Modular programming with a chai business theme:
- **`main.py`** - Main application entry point
- **`recipes/`** - Recipe module
  - **`__init__.py`** - Package initialization
  - **`flavors.py`** - Chai flavor functions (elaichi_chai, ginger_chai)
- **`utils/`** - Utility functions
  - **`discounts.py`** - Discount calculation logic

### 07. Comprehensions (`07_comprehensions/`)
Python comprehension techniques:
- **`01_list_compre.py`** - List comprehensions
  - Example: Filtering iced teas from menu
- **`02_set_compre.py`** - Set comprehensions
- **`03_dict_compre.py`** - Dictionary comprehensions
- **`04_genrator_compre.py`** - Generator comprehensions

### 08. Generators (`08_generators/`)
Generator functions and advanced iteration:
- **`01_basics.py`** - Generator fundamentals
  - `serve_chai()` generator yielding different chai types
  - Comparison between regular functions and generators
- **`02_infinite_generators.py`** - Infinite sequence generation
- **`03_send_generators.py`** - Generator communication with send()
- **`04_close_generator.py`** - Generator cleanup and closing
- **`05_smart_token_dispenser.py`** - Advanced token dispensing system

### 09. Decorators (`09_decorators/`)
Function decoration and enhancement:
- **`01_basics.py`** - Decorator fundamentals
  - `@my_decorator` implementation with `@wraps`
  - Before/after function execution logging
- **`02_logging_decorator.py`** - Logging functionality
- **`03_auth_decorator.py`** - Authentication decorators

### 10. Object-Oriented Programming (`10_oop/`)
Comprehensive OOP concepts:
- **`01_simple_class.py`** - Basic class creation
  - `Chai` and `ChaiTime` class examples
  - Type checking and instance creation
- **`02_namespace.py`** - Namespace management
- **`03_attribute_shadowing.py`** - Attribute shadowing concepts
- **`04_self_args.py`** - Self parameter usage
- **`05_init_objects.py`** - Object initialization
- **`06_inheritance_composition.py`** - Inheritance vs composition
- **`07_base_class.py`** - Base class design
- **`09_static_methods.py`** - Static method implementation
- **`10_classmethod.py`** - Class method usage
- **`11_propert_decorators.py`** - Property decorators
- **`12_vehicle_rental.py`** - Practical vehicle rental system

### 11. Files and Exception Handling (`11_files_and_exception/`)
File operations and error management:
- **`01_basic.py`** - Basic exception handling
  - IndexError demonstration with orders list
- **`02_try_except.py`** - Try-except blocks
- **`03_complex_try.py`** - Complex exception handling
- **`04_multiple_exception.py`** - Multiple exception types
- **`05_custom_exceptions.py`** - Custom exception classes
- **`06_custom_except_two.py`** - Advanced custom exceptions
- **`07_complete_order.py`** - Complete order processing with exceptions
- **`08_file_handling.py`** - File I/O operations

## 🎯 Learning Objectives

This course covers:
- **Python Fundamentals**: Variables, data types, operators
- **Control Flow**: Conditionals, loops, exception handling
- **Functions**: Definition, parameters, scope, decorators
- **Object-Oriented Programming**: Classes, inheritance, polymorphism
- **Advanced Concepts**: Generators, comprehensions, file handling
- **Modular Programming**: Packages, modules, imports
- **Best Practices**: Code organization, error handling, documentation

## 🚀 Getting Started

1. **Setup Virtual Environment**:
   ```bash
   cd 01_basic/02_virtual
   pip install -r requirements.txt
   ```

2. **Run Examples**:
   ```bash
   # Basic Python info
   python 01_basic/01.py
   
   # Chai price calculator
   python 03_conditionals/chai_price_calculator.py
   
   # Token dispenser
   python 04_loops/01_token_dispenser.py
   ```

3. **Explore Modules**:
   ```bash
   # Run chai business application
   python 06_chai_business/main.py
   ```

## 📝 Key Concepts Demonstrated

### Variables and Memory Management
```python
sugar_amount = 2
print(f"ID of 2: {id(2)}")  # Understanding object identity
```

### Function Definition
```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")
```

### List Comprehensions
```python
iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]
```

### Generator Functions
```python
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"
```

### Decorators
```python
@my_decorator
def greet():
    print("Hello from decorators class")
```

### Class Definition
```python
class Chai:
    pass

ginger_tea = Chai()
print(type(ginger_tea) is Chai)  # True
```

## 🛠️ Dependencies

- **Python 3.x**
- **requests==2.32.3** - HTTP library
- **flask==3.1.0** - Web framework

## 📖 Course Theme

The course uses a **chai (tea) business theme** throughout, making learning engaging with real-world examples like:
- Chai price calculations
- Order processing systems
- Token dispensers for chai stalls
- Recipe management
- Customer service scenarios

## 🎓 Progress Tracking

Each folder represents a completed module with practical exercises and real-world applications. The progression from basic concepts to advanced OOP and file handling demonstrates a comprehensive Python learning path.

---

*This repository serves as both a learning record and a reference for Python programming concepts learned through the Udemy course.*
