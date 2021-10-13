# Javascript

---

## ToC

1. [Integration](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#Integration)
2. [Basic Language concepts](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#basic-language-concepts)
3. [Variables](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#variables)
4. [Access to HTML](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#access-to-html)
5. [JSON](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#json)
6. [Ajax](https://github.com/Big-P/Language-Compendium/tree/main/src/Javascript#ajax)

---

## Integration

### **internal**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Document</title>
        <script type="text/javascript">
        def hello_world () {
            console.log("hello");
            }
        </script>
    </head>

    <body onload="hello_world()">
        <p>This is a paragraph</p>
        <script type="text/javascript">
            console.log("hello world");
        </script>
    </body>
</html>
```

> As you can see Javascript can be injected in the ```head``` or ```body``` tag


### **external**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Document</title>
        <link href="style.css" type="text/css" rel="stylesheet"> 
        <script src="myJavascriptFile.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    </head>

    <body>
        <!---->
    </body>
</html>
```

> As shown here you can include a local Javascript file in your HTML file.
> Alternatively you can reference an online Javascript file by providing a URL.

---

## Basic Language concepts

> Javascript is syntactically close to Java. <br>
> Javascript is dynamically typed, not statically. This means when we create a variable there is no requirement to enforce a type on it. <br>
> Javascript is part of the functional programming languages. <br>
> Javascript is single-threaded and event-based.

### **Console output**
```javascript
console.log("This is printed to the console which can be reached via F12 in your browser.");
```

### **Conditions**
```javascript
if (value != 13) {
    // This is a comment
    /*
        This is a multiline comment
     */
} else {
    throw new Error("You chose the forbidden number!");
}
```

### **Equality**

> = assignment <br>
> == equality with type conversion <br>
> === equality without type conversion

### **Loops**
```javascript
while (index < 10) {
    //
}

for (i=0; i<10; i++) {
    //
}
```

### **Object Literals**
```javascript
let person = {
    prename:"Tony",
    surname:"Stark",
    address: {
        street:"Malibu Point 10880",
        postalCode:"90265"
    } 
};

console.log(person.address.postalCode); // 90265
```

> This direct declaration of an object from the Person class with the Address class as an attribute is much quicker than in Java for example.

### **Functional Programming - functions as parameters**
```javascript
function whisper (text) {
    return text.toLowerCase();
}

function printer (str, modifier) {
    console.log(modifier(str));
}

printer("HELLO", whisper); // hello
```

> As you can see when we just use the function name without parantheses the actual function is passed around which can be called in another function.

### **Arrow functions**
```javascript
function writer(text) {
    console.log(text);
}

button.onclick(function(text) {
    writer(text);
});
```

> can be shortened to

```javascript
button.onclick((text) => writer(text));
```

---

## Variables

### **var**
```javascript
// declaration
var index;

// assignment
index = 1;

// var - global scope
/* ... */ {
    console.log(index); // 1
}

console.log(index); // 1
```

> redeclarable <br>
> global scope

### **let**
```javascript
// let - block scope
let call = "hello";

/* ... */ {
    let call = "world";
    console.log(call); // world
}

console.log(call); // hello
```

> not redeclarable <br>
> block scope

### **const**
```javascript
const PI = 3.141;

// Elements in arrays and properties in objects can be changed, however they cannot be reassigned as a whole
const chores = ["cleaning", "take out trash", "washing dishes"];
chores[0] = "buying groceries";
```

> not redeclarable <br>
> not reassignable <br>
> block scope <br>
> value needs to be assigned together with declaration

---

## Access to HTML

### ***DOM**

> The document object model refers to a tree structure of Elements within a HTML file. <br>

![Document Object Model displaying the tree structure of the elements](https://raw.githubusercontent.com/Big-P/Language-Compendium/main/res/DOM.png)
[Credits](https://en.wikipedia.org/wiki/Document_Object_Model)

> Let's suppose we have the following as our HTML base:

```html
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    </head>
    <body>
        <p id="special_p">Number One</p>
        <div class="container">
            <p class="item">Number Two</p>
            <p class="item">Number Three</p>
        </div>
    </body>
</html>
```

### **Plain Javascript Document accessing**
```javascript
// Access the displayed text associated with an Element
let displayed_text = document.getElementById("special_p").innerHTML
console.log(displayed_text); // Number One

// Access via CSS selectors for classes
displayed text = document.querySelectorAll(".container .item").item(0);
console.log(displayed_text); // Number Two

// appending 
var paragraph = document.createElement("p");
paragraph.innerHTML = "Number Four";
document.querySelector(".container").appendChild(paragraph);
// <p>Number Four</p> appended after Number Three
```

### **jQuery**
```javascript
// Access the displayed text associated with an Element via CSS selector
let displayed_text = $("#special").text();
console.log(displayed_text); // Number One

// Access via CSS selectors for classes
displayed text = $(".container .item").get(0);
console.log(displayed_text); // Number Two

// appending
$(".container").append('<p class="item">Number Four</p>')
// <p class="item">Number Four</p> appended after Number Three
```

---

## JSON

### **parse - String to JSON**
```javascript
const json = '{"fistName":"Tony", "lastName":"Stark"}';
const actor = JSON.parse(json);
console.log(author)
```

> The string with a dictionnary type notation is shaped into a Javascript object which is closer to a JSON notation.

### **serialize - JSON to String**
```javascript
// builds up on the parse script
const stringAgain = JSON.stringify(actor);
console.log(stringAgain);
// {"fistName":"Tony", "lastName":"Stark"} plain string
```

---

## Ajax

### **XHR**
```javascript
// 1
const request = new XMLHttpRequest();

// 2
request.onload = () => {
    // 5
    console.log(request.responseText);
};

// 3
request.open("GET", "https://wwww.example.org/example.txt");
// 4
request.send();
```
> Performs a GET Call on the provided URL. After finishing this process the results are logged to the console.

### **Fetch API - modern alternative to XHR**
```javascript
fetch("https://www.example.org/example.txt")
  .then(response => response.text())
  .then(text => console.log(text))
  .catch(error => console.log("An error occured."));

// api with JSON response
fetch("https://swapi.dev/api/people/3")
  .then((response) => response.json())
  .then((person) => {
      console.log(person.name);
      return fetch(person.homeworld); // person.homeworld contains a URL
      })
  .then((response) => response.json())
  .then((homeworld) => console.log(homeworld.name))
```

---
