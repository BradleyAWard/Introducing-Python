## 5) Text Strings

Unlike other languages, strings in Python are immutable. You cannot change a string in place, but you can copy parts of strings to another string to get the same effect. Python has a variety of types of strings, indicated by the letter before the first quote. `f` or `F` starts and f-string which is used for formatting. `r` or `R` starts a raw string and is used to prevent escape sequences in the string. The combination `fr` or `FR` starts a raw f-string, and a u-string starts a unicode string, which is the same as a plain string.

Python lets us escape the meaning of some characters within strings to achieve something that would otherwise be difficult to express. For example, the most common escape sequence is `\n` which begins a new line. Similarly, `\t` is used as a tab for aligning text. Note, however, that a raw string negates escape sequences, so will be printed exactly as written.

---

### Slicing, splitting and joining

We can extract part of a string using a slice. We define a slice using square brackets, a start value, an end value and an optional step count between them. Some of these values can be omitted as follows:

