# HTML

---

## The basis

### **Tags**

> Tags (```<>```) are used to start new blocks <br>
> those blocks are closed like this ```</>``` <br>
> if you have blocks that don't contain any text you should write them like this: ```<meta charset="UTF-8" />```

### **Starter Layout**
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link href="style.css" type="text/css" rel="stylesheet"> 
        <script type="text/javascript">
            console.log("hello");
        </script>
    </head>

    <body>
        <p>This is a paragraph</p>
    </body>
</html>
```

> The ```<head>``` contains Information like the character set that is used by the Website <br>
> additionally the ```<title>``` of the Tab can be set <br>
> external CSS can be imported for some styling <br>
> Logic can be achieved via the usage of Javascript

> The ```<body>``` contains the elements which are displayed on the screen.

> Information within the tag, e.g. ```type="text/javascript"``` are considered Attributes.

---

## Key Elements

### **Headings**

> There are 6 Heading Tags starting with ```h1``` up to ```h6``` <br>
> The font size decreases with increasing the number of the heading <br>
> All headings have a default fixed margin

### **Paragraph**

> Created via the ```<p>``` tag. <br>
> Paragraphs are used to format text passages. <br>
> Text written across multiple lines in a ```<p>``` tag is displayed without line breaks. <br>
> They have a default fixed margin for the top and bottom of the element. <br>
> Any text written appears in a new line after the ```<p>``` tag.

### **Links**

Full URL
```html
<a href="https://www.google.com">
```

relative path based on current URL
```html
<a href="/faq">
```

> The new URL would be: old URL + /faq

### **Buttons**
```html
<button type="button">

<!--Buttons for form tags-->
<button type="submit">
<button type="reset">
```

> The first button is a plain Button. Logic needs to be added via Javascript. This can be done by using the ```onclick="functionName()"``` attribute. <br>
> The other buttons are used to either submit a form (extract entered information and process it) or to reset a form back to it's original state.

### **input & label**

```html
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname"><br><br>
<label for="lname">Last name:</label>
<input type="text" id="lname" name="lname"><br><br>
```

> the user can enter data in the input tag while the label reveals which information should be entered to the respective input Element <br>
> there are various types for the input tag. Here are some of the most important ones: text, button, checkbox, radio, submit, reset, email, file, password <br>
> The label tag should be used together with following input types: text, checkbox, radio, file, password

> multi line input fields for text can use the ```<textarea>``` tag work as a replacement

### **form**

```html
<form action="http://localhost:8080/faq" method="POST">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>

    <input type="submit" value="confirm selection">
</form>
```

> forms are a powerful tool to receive user input and perform HTTP Methods (GET/POST/...) on URLs
> the input tags can be extracted and processed

### **Nav**
### **ul**
### **ol**
### **li**
always wrapped in either ol or ul
```css
li {
    list-style-type: none;
}
```

> Displays no sort of bullets points in front of each list Element.

### **select & option**

```html
<select>
    <option>Option 1</option>
    <option>Option 2</option>
    <option>Option 3</option>
</select>
```

> select is the dropdown wrapper and option is the single option displayed within the dropdown

### **table**

```html
<table border="1">
    <tr>
        <th>Column 1</th>
        <th>Column 2</th>
    </tr>
    <tr>
        <td>Row 1</td>
        <td>Row 2</td>
    </tr>
</table>
```

> tr tags highlight a row <br>
> th is for table headers <br>
> td is for row entries

### **hr and br**

```html
Hello
<br>
World
<hr>
How are you?
```

> \<br> starts a new line
> \<hr> places a horizontal line

### **div**

> div is like a wrapper for smaller components within this Element to enable styling modularised

---

## Key attributes

### **name**

> is used to specify a name for an element in order to use it as an identifier
> supported by those tags: button, meta, select, form, img, a, input, frame, iframe, object, map, param, textarea

### **value**

Usage with
> buttons: value that can be retrieved to know which button was clicked
> option: value that can be retrieved to know which option was selected
> input: defining default values, displayed as innerHTML
> li: initilization for first list element, following elements are incremented based on preceding element's value
