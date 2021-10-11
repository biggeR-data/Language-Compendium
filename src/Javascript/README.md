# Javascript

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
> Javascript is part of the functional programming languages.

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