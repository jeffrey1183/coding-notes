

The version of JavaScript that we're going to be using in this class is one of the more popular, more recent versions of JavaScript known as ES6.

# Concepts
* [Why we might want code running on the client instead of on the server?](https://youtu.be/xMs4ER1rcLg?t=73)
* 

# Example 1: [hello0.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/hello0.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=286)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/hello0.html)

## I've Learned:
* Displaying an alert window shwoing "Hello!"
* Using script tag to insert JavaScript code.


# Example 2: [events.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/events.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=382)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/events.html)

## I've Learned:
* JavaScript code only run or execute after certain things happen or when certain events happen.
* When I click a button, the pop-up window shows "Hello!".
* Define a function to say hello.

## Advanced Practice: [events0.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/events0.html)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/events.html)
* [Common HTML events like onmouseover, onkeydown, onkeyup, onload](https://www.w3schools.com/js/js_events.asp) and [onblur](https://www.w3schools.com/jsref/event_onblur.asp).


# Example 3: [query.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/query.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=777)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/query.html)

## I've Learned:
* Create a function to change the heading to say goodbye.
* `Document` is just a variable in JavaScript that refers to the web document, the web page that we're currently displaying.
* `querySelector` is a special function will allow us to search through the contents of the web page for a particular CSS selector. So if I querySelect for the H1, that will select this H1 element.
    * What would happen if there were multiple H1 tags is the question? The querySelector will select the first thing that `querySelector` finds.
* The `innerHTML` refers to the content in between the opening and closing tags of html element. The innerHTML of the HTML content in this case is word "Welcome!"
* [We can use document.querySelector to select a html tag, id and class.](https://youtu.be/xMs4ER1rcLg?t=1083)
* We can make a button called multiple functions, but not in this case.

## Advanced Practice: [getElement.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/getElement.html)
* [Source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/getElement.html)
* The [getElementById() method](https://www.w3schools.com/jsref/met_document_getelementbyid.asp) returns the element that has the ID attribute with the specified value.

# Example 4: [counter0.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/counter0.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=1146)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/counter0.html)

## I've Learned:
* When I click a button, the count function gets called. The function makes 0 increasing by one every time.

# Example 5: [counter1.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/counter1.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=1299)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/counter1.html)

## I've Learned:
* Every 10 times we click the button, it should pop up with an alert. 
* Dynamically generate a string with some contents of variables that exist inside of my JavaScript code. And we start to use the if condition.
* Triple equal sign is JavaScript's way of comparing things for exact.


# Example 6: [counter2.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/counter2.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=1542)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/counter2.html)

## I've Learned:
* An attempt at trying to take all this JavaScript logic and code factoring it out of the HTML. So I don't need to have JavaScript code inside the body of the HTML contents. But instead, I can put it all inside of these script tags.
 * [Why is this better than just putting the onclick inside of the button?](https://youtu.be/xMs4ER1rcLg?t=1827)
* When the content of the DOM is loaded, then JavaScript is going to call the function we code.


# Example 7: [counter3.html](https://jeffrey1183.github.io/coding-notes/My%20Practice/JavaScript/counter3.html)
* [Youtube tutorial](https://youtu.be/xMs4ER1rcLg?t=1973)
* [My source code](https://github.com/jeffrey1183/coding-notes/blob/master/My%20Practice/JavaScript/counter3.html)

## I've Learned:
* Put the JavaScript code not just at the top of the HTML file, but in a second file altogether. It makes the JavaScript file reusable. If I had multiple HTML files that wanted to use the same JavaScript, I could just reference them all to the same JavaScript.