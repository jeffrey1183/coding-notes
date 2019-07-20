A variable is a fundamental unit of programming. Variables allow us to store information.

#Float vs. Double
Now what about these Float and Double types? They seem to represent pretty similar values, they're floating point numbers, but why would you use one over the other? Well that comes down to an issue of precision and being able to most accurately represent a floating point number.

Truth be told, computers actually have a pretty difficult time doing this. Usually computers even have special hardware dedicated just to floating-point numbers. Typically, you will want to use Double instead of Float because it can handle floating-point numbers at a higher-precision. But, Double isn’t always better — in cases where speed is more important than accuracy, you might want to choose Float instead.

#Constants

Constants are defined using the keyword let, and variables are defined using the keyword var.


#String
In Swift, strings include a host of useful properties. Properties are like values that are associated with a particular type.


#I've Learned
* .syntax gives us the ability to access properties and functions for a type. And here the .syntax is used to access the characters property
for the animal string, type animal, followed by a dot.
And then let Xcode's auto completion show you all the possible properties and functions.
* The `.characters` property itself has a [property called `.count`](https://developer.apple.com/documentation/swift/string/3003522-count), which allows us to count the number of characters in a string:


[characters-is-deprecated](https://stackoverflow.com/questions/46467284/warning-characters-is-deprecated-please-use-string-or-substring-directly)

* Through .characters we gain access to functions that are only available to collections, like the function, reversed()



[document](https://developer.apple.com/documentation/swift/string#//apple_ref/doc/uid/TP40015181-CH1-DontLinkElementID_31)

