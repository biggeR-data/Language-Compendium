# CSS

---

## CSS Integration

### **Inline**
in a HTML file
```html
<p style="background-color:black;color:white;padding:20px;">
```

### **Internal**
in a HTML file
```html
<head>
    body {
        background-color: black;
    }

    h1 {
        color: red;
    }
</head>
```

### **External**
in a HTML file
```html
<head>
    <link href="style.css" type="text/css" rel="stylesheet">
</head>
```

in the same directory, in a CSS file named ```style.css```
```css
body {
    background-color: black;
}

h1 {
    color: red;
}
```

> The external integration is the standard nowadays.
> It is also possible to reference stylesheets from the Internet via a URL.

---

## Identifiers

> Identifiers are used to target specific Elements for styling

### **Tag**
```css
h1 {
    background-color: blue;
    color: white;
}
```

> every Element with the ```<h1>``` tag will receive those styles

### **Classes**
```html
<h1 class="blue">This is blue</h1>
<h2 class="blue">This is also blue</h2>
```

```css
.blue {
    color: blue;
    background: black;
}
```

> Classes can be applied to varying Tags.
> Classes are useful to make universal changes across multiple Elements.

### **ID**
```html
<p id="left_abstract">To the right you see an image of the Berlin Wall.</p>
```

```css
#left_abstract {
    float: left;
}
```

> IDs are usually used for single Element styling. If an Element is unique it is a candidate for ID styling. <br>
> If an Element has noticeable overlap with another Element the Overlap can be aggregated to a Class and used as a centralized way of styling. This also reduces redundant code.

### **Dynamic pseudoclasses**
```html
<a href="https://www.google.com">
```

```css
a :hover {
    color: red;
}
```

> This identifier builds up on other identifiers and provides dynamic utility. <br>
> In this case we are adjusting the font color when we hover over the link.
---

## Inheritance

### **inherit from parent tag**
```html
<div id="right_content">
    <h1>Heading</h1>
    <p>First paragraph</p>
    <p>Second Paragraph</p>
</div>
```

```css
#right_content {
    float: right;
}
```

> ```h1``` and ```p``` are also floating to the right because they are nested inside the ```div``` tag where they inherited the styles from.

### **overwriting parent tag styles**
```html
<div id="right_content">
    <h1 id="introduction">Heading</h1>
    <p>First paragraph</p>
    <p>Second Paragraph</p>
</div>
```

```css
#right_content {
    float: right;
    color: blue;
}

#introduction {
    color: red;
}
```

> ```h1``` inherits the float and color from the ```div``` tag, however since there is also styling specified for the id of the ```h1``` Element the color is overwritten.

---

## Responsive Web Design

```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/faq">FAQ</a></li>
    </ul>
</nav>
```

```css
nav {
    float: left;
}

li {
    width: 100px;
    margin: 20px;
}

@media(max-width:600px) {
    li {
        float: none;
        width: 300px;
    }
}

```

> The ```@media``` annotation specifies an action that is applied once the **width** of the **browser window** is at **600 pixels or below** that.

---

## Nested styling
```html
<div id="left_content">
    <h1 id="heading_intro">Heading</h1>
    <p>First paragraph</p>
    <p>Second Paragraph</p>
</div>
```

```css
#left_content {
    float: left;
}

#left_content #heading_intro {
    font-size: 70px;
}
```
---

## Margin versus Padding

> Padding is the white space within the element <br>
> Margin is the white space outside of the element to other elements

---

## Border

> in order to achieve a border the border-style parameter has to be set <br>
> possible options: solid, dotted, dashed <br>
> can also be applied like this:

```css
p {
    border-style: dotted dashed solid dotted;
}
```

---

## Influencing top, right, bottom, left

> values are received clock-wise
> top right bottom left