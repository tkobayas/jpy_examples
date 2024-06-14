import jpy

# Configure jpy
jpy.create_jvm(["-Djava.class.path=."])

# Import the Java class
HelloWorld = jpy.get_type('HelloWorld')

# Create an instance of the Java class
hello_world = HelloWorld()

# Call the method
result = hello_world.sayHello("World")
print(result)  # Output: Hello, World!
