import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        logger.info(f"Add operation: {self.a} + {self.b} = {result}")
        return result

    def __repr__(self):
        return f"Add {self.a} and {self.b} = {self.execute()}"

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        logger.info(f"Subtract operation: {self.a} - {self.b} = {result}")
        return result

    def __repr__(self):
        return f"Subtract {self.a} and {self.b} = {self.execute()}"

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        logger.info(f"Multiply operation: {self.a} * {self.b} = {result}")
        return result

    def __repr__(self):
        return f"Multiply {self.a} and {self.b} = {self.execute()}"

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            logger.error("Divide operation: Division by zero attempted.")
            raise ValueError("Cannot divide by zero.")
        result = self.a / self.b
        logger.info(f"Divide operation: {self.a} / {self.b} = {result}")
        return result

    def __repr__(self):
        return f"Divide {self.a} by {self.b} = {self.execute()}"