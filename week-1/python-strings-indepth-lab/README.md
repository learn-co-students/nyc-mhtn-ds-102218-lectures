
# Python Strings - Reloaded

Strings (otherwise known as text) is a very important datatype in programming. Because strings are such a big part of programming and Python, there are a lot of ways to use them and many built-in methods that Python provides for us to use with them.

## Formatting Strings

First thing we should talk about is the ways we can format strings. After all, we are programmers and we will usually need to make our strings programmatic. There are two main forms of combining and formatting strings called concatenation and interpolation. 

**Concatenation** is the operation of joining strings end-to-end. When we concatenate two strings, we are basically adding them together. So, if I have one string, `"Hello, my name is"`, and a second string, `"Terrance!"`, I can concatenate them together and make one longer string.

**Interpolation** is the insertion of string variables into parts of an existing string. When we interpolate, we mark where we would like to insert values into a string (like placeholders), and then pass the values to the string, resulting in a string where the placeholders are replaced with their corresponding string values. In Python it would look something like this: `"Hi, my name is {}".format("Terrance!")` which would yield "Hello, my name is Terrance!"


```python
name = "Terrance!"
print("Hello, my name is %s" % (name)) # interpolation
print("Hello, my name is " + name) # concatenation
print("Hello, my name is {name}".format(name=name)) # interpolation
print(f"Hello, my name is {name}") # interpolation with f-strings - newest method as of Python 3.6
```

As we can see there are 4 different was to format strings in python! That can be pretty confusing. So, in general we should choose one method and stick to it. 

If we're simply combining a few strings end to end, concatenating them is the way to go (the one with the `+` signs).

However, if we are interpolating we have three options. As with everything in Python and programming, it is important to have a reason behind every decision. A reason to not use the `%s` method would be that it can quickly become confusing if we have more than one element to interpolate since our markers for interpolation are just a non-descript symbol (`%s`). So, if we eliminate the first method of interpolation, we are left with the last two. There are benefits to both. 

`f-strings` or `string literals` allow you to directly interpolate strings and functions. You can more easily separate the things you want to interpolate so that it is not all bunched together, and maybe more significantly f-strings are much faster than other forms of string interpolation. However, the f-string is new to python as of version 3.6. So, they may not be supported on all applications. 

the `.format` method is also a good way of interpolating with strings. We simply choose where you would like to have a value interpolated and mark it with the double curly braces `{}`. Optionally, we can define a variable name inside the curly braces, `{name}`. Then, we give the `.format` method the arguments necessary. If we do not define a variable name (i.e. "hello my name is {}".format("Terrance")), then we just give the value we want to be interpolated. If we do decide to define a variable, (i.e. "hello my name is {name}".format(name="Terrance")), then we will need to tell our `.format` method what value to assign to each variable.


```python
# f-string interpolation
name = "Terrance"
language = "Python"
home_state = "New York"
def borough_name():
    return "Brooklyn"

f"Hi, my name is {name}! I love coding, especially in {language}. I live in {borough_name()}, {home_state}"
# here we can see that we don't need to worry about passing arguments or defining variables inside our string
# we can also call functions and perform any normal python operations inside the curly braces
```


```python
# .format() interpolation
name = "Terrance"
language = "Python"
home_state = "New York"
"Hi, my name is {name}! I love coding, especially in {lang}. I live in {location}, {location}".format(lang=language, location=home_state, name=name)
# here we can see that we need to name our arguments in the .format function what we call our variables
# in the string itself. Order does not matter here, and we can use the same variable multiple times.
```


```python
# .format() interpolation
name = "Terrance"
language = "Python"
home_state = "New York"
"Hi, my name is {} I love coding, especially in {}. I live in {}, {}".format(name, language, "New York City", home_state)
# here we can see that the order of arguments matters and that we need the exact number of arguments as we have {}
```

Now that we know how to interpolate and concatenate strings, let's talk about the different kinds of string methods we have available to us. 

There are many methods that are built-in to python for strings. Some of the most common string methods are below:

* [format()]('https://www.programiz.com/python-programming/methods/string/format') - (we already used this one above!)
* [split()]('https://www.programiz.com/python-programming/methods/string/split')
* [join()]('https://www.programiz.com/python-programming/methods/string/join')
* [find()]('https://www.programiz.com/python-programming/methods/string/find')
* [count()]('https://www.programiz.com/python-programming/methods/string/count')
* [startswith()]('https://www.programiz.com/python-programming/methods/string/endswith')
* [endswith()]('https://www.programiz.com/python-programming/methods/string/startswith')
* [replace()]('https://www.programiz.com/python-programming/methods/string/replace')
* [strip()]('https://www.programiz.com/python-programming/methods/string/strip')
* [upper()]('https://www.programiz.com/python-programming/methods/string/upper')
* [lower()]('https://www.programiz.com/python-programming/methods/string/lower')
* [title()]('https://www.programiz.com/python-programming/methods/string/title')
* [casefold()]('https://www.programiz.com/python-programming/methods/string/casefold')

Many of the names can be used to infer what functionality they provide, but click on the links and peruse the documentation if you want to learn more and see the full functionality of these methods. 

## Practicing With Strings

Now that we have a more of an understanding of how string formating works and what built in methods we can use, let's practice our skills by writing some functions.

Open up the string_functions.py file and follow along with the comments which detail the functionality each should have. Run the tests to make sure your functions will work with any example.

## Summary

In this lab we introduced the basics of how strings work and what methods we have available to us when we are working with strings in Python. Then we put those skills to the test by defining functions that used some of these methods to alter and format strings for our own uses. This is a common need of any good programmer to make sure that their application only accepts information in a uniform format, as well as guard against information coming into the program that might be malicious.
