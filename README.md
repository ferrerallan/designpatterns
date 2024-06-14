
# Design Patterns Example

## Description

This repository provides examples of various design patterns implemented in Python. It demonstrates how to implement and use common design patterns such as Singleton, Factory, Observer, and more in a Python application. This is useful for developers looking to understand and apply design patterns to improve code structure and maintainability.

## Requirements

- Python
- pip for package management

## Mode of Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/designpatterns.git
   ```
2. Navigate to the project directory:
   ```bash
   cd designpatterns
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Implementation Details

- **patterns/**: Contains the implementation of various design patterns.
- **main.py**: The main entry point of the application that demonstrates the use of design patterns.
- **requirements.txt**: Configuration file for the project dependencies.

### Example of Use

Here is an example of the Singleton pattern implemented in Python:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def do_something(self):
        print("Singleton instance method called.")


if __name__ == "__main__":
    singleton = Singleton()
    singleton.do_something()
```

This code defines a Singleton class with a method that can be called through the Singleton instance, demonstrating the Singleton design pattern.

## License

This project is licensed under the MIT License.

You can access the repository [here](https://github.com/ferrerallan/designpatterns).
