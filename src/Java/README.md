# Java-Docu
My own personal collection of Java Code. Good to knows and more.

<br>

4 Pillars of Object oriented programming: <br>
1. Encapsulation - Keyword: modifiers (protected/private) - Visibility of Data as low as needed <br>
2. Inheritance - Keyword: extends - Specialising smaller subgroups <br>
3. Abstraction - Keyword: abstract - shared properties but no actual Instance <br>
4. Polymorphism - Keyword: / - Different Things appear same outwards however are different internally <br>

# General

## Print
```java
System.out.println("Hello World");
```

## Input
```java
import java.util.Scanner;
Scanner sc = new Scanner(System.in);
String input = sc.nextline();
sc.close();
```

## Declaration of Variables
```java
// <type> <variable>
int count;
```

## Declaration & Initialization of Variables
```java
int count = 5;
```

## Operators
```java
int n = 17;
int o = n++; // o = 17; n = 18 first initialization then n+1
int p = ++n; // p = 19; n = 19 first n+1 then initialization
p += 3; // p = p + 3
```

## primitive Datatypes
```java
// Integers
byte // 8 Bit -128 to 127
short // 16 Bit -32.768 to 32.767
int // 32 Bit -2.147.483.648 to 2.147.483.647
long l = 13131564l;// 64 Bit

// Decimals
float f = 11.3f; // 32 Bit
double d = 103.0489d; // 64 Bit

// Booleans
boolean bt = true;
boolean bf = false;

// Characters
char c = 'c'; // only for single Characters
```

### **Type Casting**
```java
// (<Type>) to cast to a Datatype or even Class
float f = 12.5f;
int i = (int) f; // i = 12
// casting to int from floats/doubles just deletes the decimal places - no roundign of values
```

## Arrays
```java
// Declaration: <Type>[] variable
long[] zahlen;

// Declaration + Initialization: <Type>[] <variable> = new <Type>[<Array_length>]
long[] zahlen = new long[10];

// Arrays can also have Classes as Types. An Array contains only Elements of the same Type.
```

### **Array Indexing**
```java
long[] zahlen = new long[10];
zahlen[3] = 12l; // Assigning 12 to Index 3 (4th Position in the Array)
System.out.println(zahlen[3]); // Accessing Elements by [Index]
```

## Comparisons

### **Equality**
```java
// between primitive Datatypes
int i = 6;
int j = 7;
i == j // return false
// if used on objects tests if it is the exact same object (pointing to same storage cell)

// between objects for value comparison (eg. Strings)
String s1 = "test";
String s2 = "test";
s1.equals(s2); // return true
// Tip: If one of the two could be null, put it last, thus avoiding a null pointer exception
```

### **Greater, Smaller, Not**
```java
// greater than or equal
>=

// less than or equal
<=

// not
!=
```

### **Logical Comparisons**
```java
int i = 5;
boolean b = true;

// AND - requires 2 true's
(i > 4) && (b) // return true

// OR - requires at least 1 true
(i > 6) || (b) // return true
```

## Conditions
```java
int i = 5;
if (i < 5) {
    ;
} else if (i > 5) {
    ;
} else {
    ;
}

// () can also contain multiple conditions => ((i > 5) && (b == 6))
```

## Switch-Case
```java
// same as if, else if and else Conditions
Scanner sc = new Scanner(System.in);
System.out.println("How are you");
String input = sc.nextLine();
sc.close();

switch (input) {
    case "good":
        System.out.println("That's great!");
        break; // if break is not implemented it will test the other cases as well
    case "bad":
        System.out.println("Oh that's not good. Have you tried eating some ice cream?");
    // multiple case assignment to one block
    case "okay":
    case "not bad":
        System.out.println("Have a great day!");
    default:
        System.out.println("Good to know.");
}
```

## Loops
```java
// for-loops when the number of iterations is clear
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// while-loops to test conditions, when the number of iterations is unclear
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}

// do-while-loops for cases where you need to execute a loop at least once no matter what
int i = 0;
do {
    System.out.println(i);
} while (i < 10);
// returns 0, then breaks
```

### **Break**
```java
int i = 0;
while (i < 7) {
    System.out.println(i);
    i++;
    if (i == 3) {
        break;
    }
}
// return 0, 1, 2
// breaks out of most inner loop, also applicable to switch-case
```

# Classes
```java
public class Person {

    public String prename;
    public String surname;
    private int calls = 0;

    public String getName() {
        String name = prename + " " + surname;
        raiseCalls()
        return name;
    }

    private void raiseCalls() {
        calls++;
    }
}
```

## Constructor
```java
// address Object attributes with "this.", to differentiate between passed parameters
public class Person {

    public String prename; // Declaration
    public String surname;
    private int calls = 0; // Initialization to standard value

    // empty Constructor, overrides Default Construcotr
    public Person () {
        this.prename = "John";
        this.surname = "Smith";
        this.calls = 0;
    }

    // Constructor with Parameters
    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
    }
}
```

## Creating an Object
```java
import package_name.Person;
Person p1 = new Person(); // empty Constructor is called
Person p2 = new Person("Frank", "Schmitt", 8); // Constructor with the corresponding Attribute count (+ Datatype matches) is called
```

## Methods
```java
// <modifier> <Datatype or void for no return> <method_name>
public class Person {

    public String prename;
    public String surname;
    private int calls = 0;

    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
    }

    // Method with no return value
    public void raiseCalls () {
        this.calls++;
    }
}
```

### **Getter/Setter**
```java
// central way of assigning / changing attributes of an Object
public class Person {

    public String prename;
    public String surname;
    private int calls = 0;

    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
    }

    // obtain current object's surname
    public String getSurname () {
        return this.surname;
    }

    // set current object's surname
    public void setSurname (String surname) {
        this.surname = surname;
    }
}
```

### **to-String**
```java
public class Person {

    public String prename;
    public String surname;
    private int calls = 0;

    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
    }

    @Override // Tag to overwrite the Default to String Method
    public String toString() {
        return "Person{" +
                "prename='" + this.prename + '\'' +
                ", surname='" + this.surname + '\'' +
                ", calls=" + this.calls +
                '}';
    }

}
```

### **Using a Method**
```java
import package_name.Person;
Person p = new Person("Frank", "Schmitt", 8);
Sytsem.out.println(p.getName());
```

## Static

### **Attributes**
```java
// Static Attributes count for the Class as a whole, so they are only accessible once instead of per Object
public class Person {

    // static indicates a Class Attribute
    public static int persons_created = 0;
    public String prename;
    public String surname;
    private int calls = 0;

    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
        Person.persons_created++; 
    }

}
// to access Class Attributes: classname.static_attribute_name
```

### **Constants**
```java
// static final creates a Constant
// Constants can be used to differentiate between different states with if/else or switch-case
public class Person {
    public static final int STUDENT = 0;
    public static final int GRADUATE = 1;

    public Person (int person_type, String prename, String surname, int age, int student_id, int gpa) {
        this.person_type = person_type;
        this.prename = prename;
        this.surname = surname;

        if (person_type == STUDENT) {       // same as person_type == 0
            this.student_id = student_id;
        }
        if (person_type == GRADUATE) {      // same as person_type == 1
            this.gpa = gpa;
        }
    }
}


```

### **Methods**
```java
// Static Methods are available once for the Class, not every Object
public class Person {

    public static int persons_created = 0;
    public String prename;
    public String surname;
    private int calls = 0;

    public Person (String prename, String surname, int calls) {
        this.prename = prename;
        this.surname = surname;
        this.calls = calls;
        Person.persons_created++;
    }

    // static indicates a Class Method
    public static int getPersonsCreated () {
        return Person.persons_created;
    }

}
// to access Class Methods: classname.static_method_name(parameters)
```

# Encapsulation

## Modifier
```java
public class Person {
    
    public String prename;
    protected String hair_color;
    String surname;                     // friendly
    private int age;
}
```
| visibility\modifier                          | public | protected | friendly | private |
|----------------------------------------------|--------|-----------|----------|---------|
| own Class A                                  | Yes    | Yes       | Yes      | Yes     |
| Class B same package                         | Yes    | Yes       | Yes      | No      |
| Subclass to A different package              | Yes    | Yes       | No       | No      |
| Class B different package & no Subclass to A | Yes    | No        | No       | No      |


# Inheritance

<p> 
extends - Subclass extends Superclass - Inherit Class Attributes & Methods <br>
final - public final class - can't act as a Superclass, Inheritance disabled <br>
protected - Modifier to enable Subclasses accessing Superclass values <br>
</p>

## Constructor
```java
// <Subclass> extends <Superclass>
// all Methods + Attributes are inherited from the Superclass as long as the modifier matches the required access for that
// In the case of private Attributes they can still be accessed with Getter/Setter Methods if they have the required modifier for the visibility
public class Student extends Person {

    protected int student_id; // additional Student Attribute (Person Attributes are inherited)

    public Student (String prename, String surname, int age, int student_id) {
        super(prename, surname, age); // call Superclass Constructor
        this.student_id = student_id; // additional Attributes exclusive to Subclass need to be declared seperately
    }
}
// Constructors are never inherited
// If you call a Super-Constructor in a Block it has to be in the first line
// You can only call the Super-Constructor once in the Sub-Constructor
```

## Overwriting Methods
```java
// Subclasses can overwrite Methods inherited from Superclasses
// While they can be overwritten, the Superclass' Method can still be called and used to add something to the existing Method without redundant Code
@Override
public String toString() {
    return super.toString() + " student_id=" + this.student_id + "}"; 
}
```

# Abstraction

## Abstract Classes
```java
// Use case: Summarize shared properties
// No Objects can be created
public abstract class Person {}
```

## Abstract Methods
```java
// Define that Subclasses need to implement a Method, Superclass only defines signature
public abstract class Person {

    public abstract String say_hello (String name);
}

public class Student extends Person {
    // ...

    // required Implementation
    public String say_hello (String name) {
        System.out.println("Howdy " + name + ", how are ya?")
    }
}
```

# Polymorphism

## Arrays and Classes
```java
// Arrays with multiple Subclasses can be realized if an Array of the Superclass is created
Person[] people = new Person[10];
String prename = "John";
String surname = "Smith";
int age = 20;
int student_id = 516540;
people[0] = new Person(prename, surname, age);
people[1] = new Student(prename, surname, age, student_id);
```

### **Accessing Subclass Objects in a Superclass Array - instanceof**
```java
// instanceof tests if something is an Object of the provided Subclass (or Subclasses of the provided Subclass)
if (people[1] instanceof Student) {
    // cast only works if the Object is an instance of the Subclass
    Student s = (Student) people[1];
    System.out.println(s.getStudent_ID);
}
// Objects in the Array can be accessed as their resoective Class, however not edited
```

# Interfaces
```java
// Use case: Two different Classes which aren't related to each other
// and Inheritance from a Superclass wouldn't make sense
// can use an Interface to implement Methods fit for the requirements
// but the Functionality can be assumed through the Interface
public interface Control_Panel {
    public void calculate();
    public void calculate_complex(int n);
}
```

```java
public class A implements Control_Panel {
    // ...

    public void calculate() {
        System.out.println("A implements Control_Panel's method calculate().");
    }
    public void calculate_complex (int n) {
        System.out.println(n + 1);
    }
}
```

```java
public class B implements Control_Panel {
    // ...

    public void calculate() {
        System.out.println("B implements Control_Panel's method calculate() better than A.");
    }
    public void calculate_complex (int n) {
        System.out.println(n + 10);
    }
}
```

## Using Interfaces
```java
Control_Panel cp1 = new A();
Control_Panel cp2 = new B();

cp1.calculate();                // "A implements Control_Panel's method ..."
cp2.calculate_complex(10);      // 20
```

# String

## String Initialization & Declaration
```java
String s = "Hello World";
String s = new String();                // s = ""
String s = new String("Hello World")
String s;                               // String variable not initialized
s = "";
s = null;                               // String variable not initialized
```

## Comparisons

### **Comparisons Equality**
```java
String s = "Hello";
String t = "Hello";

s == t;         // return false - testing for same Object Identity
s.equals(t);    // return true - testing for same Value
```

### **Comparisons Inequality**
```java
String s = "Hello";
String t = "Hello";

!s.equals(t);   // return false
```

### **Comparisons non-case-sensitive**
```java
String s = "Hello";
String t = "HELLO";

s.equals(t);            // return false
s.equalsIgnoreCase(t);  // return true
```

### **Comparisons contain Strings**
```java
// case-sensitive
String s = "Hello";

s.startsWith("He");     // return true
s.endsWith("lo");       // return true
s.contains("l");        // return true
```

### **Comparisons lexically**
```java
String s = "Hello";
String t = "Hi";

// case-sensitive
s.compareTo(t);     // return -4

// non-case-sensitive
s.compareToIgnoreCase(t);

// cases
// return value < 0     => s is lexically speaking ahead of t
// return value > 0     => s is lexically speaking behind of t
// return value == 0    => s and t are identical
```

## Conversion

### **Convert Strings to other Datatypes (Wrapper.parseDT)**
```java
String s = "true";
Boolean.parseBoolean(s);    // return true
Byte.parseByte();
Short.parseShort();
Integer.parseInt();
Long.parseLong();
Float.parseFloat();
Double.parseDouble();
```

### **Convert Datatypes to Strings (String.valueOf(DT))**
```java
int i = 17;
String s = String.valueOf(i);   // s = "17"
```

## Concatenation
```java
// Implicit Datatype Conversion for primitive Datatypes when concatenated with +
int i = 30;

System.out.println("Happy " + i + "th Birthday!")
```

## Substrings
```java
String s = "Hello there";
// start until end of String
s.substring(6);             // return "there"

// start, stop (exclusive)
s.substring(0,5);           // return "Hello"
```

## String Length
```java
String s = "Hello there.";
s.length()              // return 12
```

## Indexing for Strings
```java
// first appearance within the String
String s = "Hello";
s.indexOf("l");         // return 2

// searching for a Index of a String in reverse
s.lastIndexOf("l");     // return 3
```

## String Shaping

### Convert Case
```java
// creates a copy
String s = "Hello";
s.toLowerCase();        // return "hello"   however s = "Hello"
s.toUpperCase();        // return "HELLO"   however s = "Hello"

// if current String should be changed it needs to be reassigned
s = s.toLowerCase();    // s = "hello"
```

### Deleting Whitespaces & Replacing
```java
String s = " Hello ";
s.trim();               // removes trailing whitespaces at the Start & End

s.replace("ll", "yy")   // <String to be replaced>, <String replacing old one>
```

# StringBuffer (Dynamic String extension)

## Constructor
```java
// Default 16 Characters
Stringbuffer b1 = new StringBuffer();
// Length of the provided String
Stringbuffer b2 = new StringBuffer("Hello World");
// Define length - great if length is clear
Stringbuffer b3 = new StringBuffer(1000);
```

## Add Strings
```java
Stringbuffer sb = new StringBuffer("Hello");
// add String at the end
sb.append(" John");         // sb = "Hello John"

// add String at provided Index
sb.insert(5, " Mister");    // sb = "Hello Mister John"
```

## Remove Strings
```java
StringBuffer sb = new StringBuffer("Hello there");
sb.deleteCharAt(5);     // sb = "Hellothere"

// <start>,<stop exclusive>
sb.delete(5,10);         // sb = "Hello"
```

## toString
```java
StringBuffer sb = new StringBuffer("Hello World");
String s = sb.toString();           // s = "Hello World"
```

# StringTokenizer (Splitting Strings)

## Usage
```java
// <String to be split up>, <Deliminator>
String s = "Germany, Swiss, Austria";
StringTokenizer st = new StringTokenizer(s, ",");
while (st.hasMoreTokens()) {                        // Iteration for each Part
    System.out.println(st.nextToken());             // obtain single Part
}
```

## Layout Deliminators
```java
" ";    // Whitespace (Default)
"\t";   // Tab
"\n";   // New Line
"\r";   // Carriage Return (Same Line)
"\f";   // Formfeed (Indicates Page Break)
```

# Files

## Reading Files
```java
import java.io.BufferedReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;

try {
    Path my_file = Paths.get("cwd/path/to/file.txt");

    // Create File if it doesn't exist yet
    if (!Files.exists(my_file)) {
        Files.createFile(my_file);
    }

    // Reading
    BufferedReader my_reader = Files.newBufferedReader(my_file);
    
    String current_line = my_reader.readLine();     // reading first line

    while (current_line != null) {                  // readLine() returns null ath the end of a file
        System.out.println(current_line);
        current_line = my_reader.readLine();        // reading following lines
    }

    my_reader.close();                              // required to prevent passive system resource occupation

} except (Exception e) {
    e.printStackTrace();
}
```

## Writing to Files
```java
import java.io.BufferedWriter;
import java.nio.file.*;

try {
    Path my_file = Paths.get("cwd/path/to/file.txt");

    // Writing
    BufferedWriter my_writer = Files.newBufferedWriter(my_file, StandardOpenOption.APPEND);
    my_writer.write("This is written in the last line of the File.");
    my_writer.write("\nThis is extends the file by one line and writes this String in the new last line.");

    my_writer.close();          // required to prevent passive system resource occupation

} catch (Exception e) {
    e.printStackTrace();
}
```

# Exceptions

> **Throwable** is the **Superclass** to all *Exceptions* and *Errors*. <br>
> **Error** is a Subclass of Throwable. Critical failures which **shouldn't be caught** (eg. OutOfMemoryError, StackOverFlowError). <br>
> **Exception** is a Subclass of Throwable. Failures which **should be caught**. <br>
> **RuntimeException** is a Subclass of Exception (eg. NullPointerException). Don't have to be caught. [unchecked exceptions] <br>
> Other Exceptions have to be caught. [checked exceptions] 2 Options:<br>
> try-catch or throws.

```java
Exception.toString();           // Exception Description
Exception.getMessage();         // Failure Message
Exception.printStackTrace();    // prints calling history
```

## try-catch
```java
try {
    // Input by user
    String s = JOptionPane.showInputDialog("Enter a number");
    int i = Integer.parseInt(s);
    System.out.println(2 * i);
} catch (java.lang.NumberFormatException e) {       // first case
    e.printStackTrace();
} catch (Exception e) {                             // second case
    System.out.println("An Exception occured");
} finally {
    // always executed
}
```

## throws
```java
// throws are not inherited and need to be specified for each Method (including Constructors) that could have the Exception

public static void main(String[] args) {
    String date = javax.swing.JOptionPane.showInputDialog("Date:");
    try {
        if (dateInFuture(date))
            System.out.println("The date is in the future.");
        else
            System.out.println("The date is not in the future.");
    } catch (ParseException e) {
        System.out.println("Invalid date.");
    }
}

// throws passes the Exception to the Caller-Method where the Exception has to be handled 
public static boolean dateInFuture(String s) throws ParseException {
    SimpleDateFormat sdf = new SimpleDateFormat("dd.MM.yyyy");
    Date d = sdf.parse(s);
    return d.after(new Date());
}
```

## throw
```java
// throw the Error in the corresponding block

int time;
// ...

if (time < 0) {
    throw new IllegalArgumentException("There is no negative time.")
}
```

## own Exception Classes
```java
public class My_Exception extends Exception () {
    public My_Exception() {
        super();
    }

    public My_Exception(String exception) {
        super(exception);
    }
}
```

### **Implementing own Exception Classes**
```java
throw new My_Exception("This is my own Exception");

try {
    // ...
} catch (My_Exception e) {
    System.out.println(e.getMessage());
}
```

### **Expansion for Implementation of own Exception Classes (IDs)**
```java
class My_Exception extends Exception {
    public int exceptionID;

    public My_Exception() {
        super();
    }

    public My_Exception(String fehler, int exceptionID) {
        super(fehler);
        setexceptionID(exceptionID);
    }

    protected void setExceptionID(int exceptionID) {
        this.exceptionID = exceptionID;
    }

    public int getExceptionID() {
        return this.exceptionID;
    }

    public String getExceptionMessage() {
        return getExceptionID() + " " + getMessage();
    }
}
```

```java
try {
    boolean exception_condition;
    // ...
    if (exception_condition) {
        throw new My_Exception("New Exception", 17);
    }
    // ...
} catch (My_Exception e) {
    System.out.println(e.getExceptionMessage() );
}
```

# Math

## random
```java
// Math.random() returns a value x -> 0<=x<1
// Math.random() * <multiple of 10 according to decimals required> + <minimum value>
int i;
i = (int) (Math.random() * 10 + 1)
```

# Package

## Class1
```java

```

### **Class1 Functionality 1**
```java

```