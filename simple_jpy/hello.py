import jpyutil

# Initialize the JVM using jpyutil
jpyutil.init_jvm(jvm_classpath=['./simple-pojo-1.0.0-SNAPSHOT.jar'])

# import jpy after jpyutil.init_jvm. If not, you would need to set LD_LIBRARY_PATH for libjvm.so
import jpy

# Import the Java class
Person = jpy.get_type("org.example.Person")

# Create an instance of the Java class
person = Person("John", 30)

# Call the method
result = person.getName()
print("Hello!", result)  # Output: Hello! John