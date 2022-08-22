---
marp: true
theme: gaia
class: gaia
color: black
---

<!--
_class:
  - gaia
  - lead
-->

# AI Programming with Python

![bg right](https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/2dmDLmWvCncVHcQ6lz9u5v/9ebc8c914fcf0e8b546bce78133b2a4a/OpenGraph_Udacity_Logo_Update__1_.png)

## Session 3

[attendance](../README.md)

---

![bg](https://www.brainyquote.com/photos_tr/en/a/alanperlis/126631/alanperlis3-2x.jpg)

---

# Agenda

- Q&A
- Review & Practice
  - Scripting
  - Intro to OOP
- Q&A _(encore)_

---

# Scripting

- `input` function
- `eval` function (generally avoided)
- errors vs exceptions (in short)
- `try/except` statement
- `finally` statement

---

```py
response = input("prompt") # displays the prompt and receives a response
print(type(response)) # response from input is a string
# it could be cast using `int`, `float` or other conversion methods
```

```py
import math
result = eval("- math.sqrt(9)") # eval `evaluates` the expression inside
# a string and returns the result
```

```py
try:
  pass # some code that might break
except Exception1 as e1:
  pass # some logic for specified exception
except Exception as e:
  pass # some logic for undefined exceptions
finally:
  pass # code here is executed whether try fails or not
```

---

```cpp
#include <iostream>

int main(void)
{
  int input{0};
  std::cin >> input;
  std::cout << "double of " << input << " is " << 2 * input << std::endl;
  return 0;
}
```

```py
if __name__ == "__main__":
  var = int(input())
  print(f"double of {var} is {2 * var}")
```

---

# Object-Oriented Programming **OOP**

## I-PEA

- Inheritance: code reusability, passing of properties & behaviours of an object to another
- Polymorphism: the same logic performs differently based on the type of the object involved
- Encapsulation: keeping together data and logic operating on it
- Abstraction: hiding unnecessary information from users

---

# OOP Terminology

- `class` vs object
- attribute (property) & method (behaviour)
- function vs method, the `self` keyword
- setters & getters
- magic methods (`__init__`, `__repr__`, `__str__`, etc&#8230;)

---

|               |         |
| :-----------: | :-----: |
| ![width:16em height:9.5em](https://video.udacity-data.com/topher/2018/July/5b511ad5_screen-shot-2018-07-19-at-4.06.55-pm/screen-shot-2018-07-19-at-4.06.55-pm.png) | ![width:14em](https://miro.medium.com/max/1400/1*iP78XqAbkntOuzbHCoiubg.png) |

---

# From classroom

![bg width:90%](../data/cls-diag-1.png)

---

![bg height:48em](../data/big-1.png)

---

# Notes from Statistics

Almost all distributions share the property of having moments

## Moments

1. First **raw** moment _mean(&mu;)_
2. Second **centred** moment _variance($\sigma^2$)_
3. Third **standardised** moment _skewness(&gamma;)_
4. Fourth **standardised** moment _kurtosis(&kappa;)_

---

<!--
_class:
  - gaia
  - lead
-->

# Q&A _(encore)_ <!-- fit -->

---

<!--
_class:
  - gaia
  - lead
 -->

# Thank You

## Good Luck

## Have Fun
