# Markdown 

## Introduction

Markdown is a 'markup language' that is designed to format plain text with simple, easy syntax. It was created in 2004, and has become the defacto format for coders and use in their projects for instructions and project info. Markdown uses the `.md` file extension, and comes a few different 'flavors' or 'syntaxes'. This sheet is a reference for 'vanilla markdown', or markdown that will work most anywhere the format is used.

### Markdown Tools and Links

[Github](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) will display formatted marked when it finds special file names, such as `README.md` which will be displayed on project landings and `PULL_REQUEST_TEMPLATE.md` for markdown to be displayed before pull request are made.

[Hackmd](https://hackmd.io/) is a collaborative markdown site, that works similar to google docs but uses `md` instead.

[Vscode](https://code.visualstudio.com/Docs/languages/markdown) will display formatted markdown when the hotkey `cmd + shift + v`(pc `cntrl + shift + v`) is pressed.



## Paragraphs

Paragraphs are on the same line. This sentence is still in the same paragraph as the last.

Line breaks need a whole blank line in between paragraphs. Put a whole blank line between pretty much every new markdown thing (headers, code chunks, lists, ect). 

```markdown
Paragraphs are one the same line. This sentance is still in the same paragraph as the last.

Line breaks need a whole blank line inbetween paragraphs. Put a whole blank line between pretty much every new makrdown thing (headers, code chunks, lists, ect). 
```

## Headers

**Headers** are made with `#` hashes

```markdown
# H1

## H2

### H3

#### H4

##### H5

###### H6
```

# H1

## H2

### H3

#### H4

##### H5

###### H6


## Comments

Commented markdown uses HTML comments `<!--  -->` and isn't shown to the reader.

```markdown
<!-- I am a comment! you wouldn't see me! -->
```

# Dividers (Horizontal Rules)

there are three ways to make them. Three underscores `___`, three dashes `---` or three asterisks `***`:


```markdown
___

---

***
```

___

---

***


## Text Styles and Emphasis

**Bold** text is wrapped in two astericks `**bold**` or two underscores `__bold__` on either side. 

_Italic_ text is wrapped in one asterick `*italic*` or one underscore `_italalic_`.

`Inline code snippets`, or highlights, use backticks ``code``. 

~~Strike-through~~ uses two tildes on either side `~~strick-through~~``.

```markdown
**This text will be bold** 

__This will also be bold__ 

*This text will be italic* 

_This will also be italic_ 

`code snippet`

~~This text will be crossed out.~~ 

_You **can** `combine` ~~them~~_

### _And **they** ~~work~~ in `headers`!_
```

**This text will be bold** 

__This will also be bold__ 

*This text will be italic* 

_This will also be italic_ 

`code snippet`

~~This text will be crossed out.~~ 

_You **can** `combine` ~~them~~_

### _And **they** ~~work~~ in `headers`!_

## Lists

You can make unordered lists with asterisks `*` hyphens `-` and plus signs `+` (all interchangable!). You can also make ordered lists with the number followed by a period `1.`. If you find your lists are buggin out (one list followed by anteher), giving an extra blank line between them usually fixes it.

```markdown
* asterick
* asterick
- hyphen 
- hyphen
+ plus
+ plus

1. one
1. one
```

* asterick
* asterick
- hyphen 
- hyphen
+ plus
+ plus


1. one
1. one

Todo lists are started with sqaure brackets after `[]` the list symbol: `- []` and checked off with an `x`: `- [x]` (some markdown versions don't support making done lists look extra cool)

```markdown
- [ ] need to do
- [ ] need to do
- [x] nailed it so done
```

- [] need to do
- [] need to do
- [x] nailed it so done

You can indent lists to make sub lists, but ordered lists, but unordered list need to be on different indentation levels! (*i.e. you can't have an unordered list turn into an ordered list halfway thorugh)

```markdown
* asterick
* asterick
  - hyphen 
  - hyphen
  + plus
  + plus
1. one
1. one
  - [] need to do
  - [] need to do
  - [x] nailed it so done
```

* asterick
* asterick
  - hyphen 
  - hyphen
+ plus
+ plus
  1. one
  1. one
- [] need to do
- [] need to do
- [x] nailed it so done

## Block Quotes

**Block qoutes** start with a wokka `>`  (greater than? less than? what is this thing called...). Subsequent lines that start with a block qoute will be grouped together, even with a space between lines.

```markdown
> blockquote

> blockqoute
```

> blockquote

> blockqoute

This will break wtihout the empty line:

```markdown
> blockquote
> blockqoute
```

> blockquote
> blockqoute

If you want to combine lists and block qoutes, you can just use a wokka `>` on the first item in the list:

```markdown
> * blockqoute
* blockquote
* blockqoute
  1. ordered list
  2. ordered list
    * [] todos
    * [] todos
```

> * blockqoute
* blockquote
* blockqoute
  1. ordered list
  2. ordered list
    * [] todos
    * [] todos


```
let generic_demo = {
  code: block
}
```

## Code blocks

Open and close code blocks with three backticks **\`\`\`**. You can have a plaintext code block or specify the langauge for syntax highlighing after the opening backticks: **\`\`\`javascript**.

<div>
``` 
<br />
plain text
<br />
```
<br />

```python
<br />
def python_code_chunk():
<br />
  return 'syntax highlighting'
<br />
```
<br />

```javascript
<br />
function makeCodePretty() {
<br />
  return 'all the pretty colors'
<br />
}
<br />
```
<br />
</div>

```
plain text code
```

```python
def python_code_chunk():
  return 'syntax highlighting'
```

```javascript
function makeCodePretty() {
  return 'all the pretty colors'
}
```

## Links & Images

```markdown
[title](https://www.example.com)

![alt text](image.jpg)
```

[title](https://www.example.com)

![alt text](image.jpg)

## Tables


```markdwon
| Syntax | Description |
| ------ | ----------- |
| Header | Title |
| Paragraph | Text |
| **Bold** | *Italalic* | `code` |
```


| Syntax | Description |
| ------ | ----------- |
| Header | Title |
| Paragraph | Text |
| **Bold** | *Italalic* | `code` | 

## Escaping Characters:

You can escape markdown formattign with a forward slash before the character: `\`.

```makrdwon
hey look two backticks \`\` 
hello asterisks \*hello\*
```

hey look two backticks \`\`

hello asterisks \*hello\*

## HTML

Oh yea, you can do straight up HTML if you need to.

```markdown
<div>
 Markdown here will not be **parsed**
</div>
```

<div>
 Markdown here will not be **parsed**
</div>

 the details html is super useful for spoiler type things:

 ```markdown
<details>
  <summary>Exciting! What if I click on this?</summary>

    Hello there!

</details>
```


<details>
  <summary>Exciting! What if I click on this?</summary>

    Hello there!

</details>