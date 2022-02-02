# Markdown 

## Introduction

Markdown is a 'markup language' that is designed to format plain text with simple, easy syntax. It was created in 2004, and has become the defacto format for coders and use in their projects for instructions and project info. Markdown uses the `.md` file extension, and comes a few different 'flavors' or 'syntaxes'. This sheet is a reference for 'vanilla markdown', or markdown that will work most anywhere the format is used.

### Markdown Tools and Links

[Github](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) will display formatted marked when it finds special file names, such as `README.md` which will be displayed on project landings and `PULL_REQUEST_TEMPLATE.md` for markdown to be displayed before pull request are made.

[Hackmd](https://hackmd.io/) is a collaborative markdown site, that works similar to google docs but uses `md` instead.

[Vscode](https://code.visualstudio.com/Docs/languages/markdown) will display formatted markdown when the hotkey `cmd + shift + v`(pc `cntrl + shift + v`) is pressed.

Markdown has it's own syntax, but most valid html is also valid markdown.

## Paragraphs

Paragraphs are on the same line. This sentence is still in the same paragraph as the last.

Line breaks need a whole blank line in between paragraphs. Put a whole blank line between pretty much every new markdown thing (headers, code chunks, lists, etc). 

```markdown
Paragraphs are on the same line. This sentance is still in the same paragraph as the last.

Line breaks need a whole blank line inbetween paragraphs. Put a whole blank line between pretty much every new makrdown thing (headers, code chunks, lists, etc). 
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

**Bold** text is wrapped in two asterisks `**bold**` or two underscores `__bold__` on either side. 

_Italic_ text is wrapped in one asterisk `*italic*` or one underscore `_italalic_`.

`Inline code snippets`, or highlights, use back-ticks ``code``. 

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

You can make unordered lists with asterisks `*` hyphens `-` and plus signs `+` (all interchangeable!). You can also make ordered lists with the number followed by a period `1.`. If you find your lists are buggin out (one list followed by another), giving an extra blank line between them usually fixes it.

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

* asterisk
* asterisk
- hyphen 
- hyphen
+ plus
+ plus


1. one
1. one

Todo lists are started with square brackets after `[]` the list symbol: `- []` and checked off with an `x`: `- [x]` (some markdown versions don't support making done lists look extra cool)

```markdown
- [ ] need to do
- [ ] need to do
- [x] nailed it so done
```

- [ ] need to do
- [ ] need to do
- [x] nailed it so done

You can indent lists to make sub lists, but ordered lists, but unordered list need to be on different indentation levels! (*i.e. you can't have an unordered list turn into an ordered list halfway through)

```markdown
* asterick
* asterick
  - hyphen 
  - hyphen
  + plus
  + plus
1. one
1. one
  - [ ] need to do
  - [ ] need to do
  - [x] nailed it so done
```

* asterisk
* asterisk
  - hyphen 
  - hyphen
+ plus
+ plus
  1. one
  1. one
- [ ] need to do
- [ ] need to do
- [x] nailed it so done

## Block Quotes

**Block quotes** start with a wokka `>`  (greater than? less than? what is this thing called...). Subsequent lines that start with a block quote will be grouped together, even with a space between lines.

```markdown
> blockquote

> blockqoute
```

> blockquote

> blockqoute

This will break without the empty line:

```markdown
> blockquote
> blockqoute
```

> blockquote
> blockqoute

If you want to combine lists and block quotes, you can just use a wokka `>` on the first item in the list:

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

Open and close code blocks with three backpacks **\`\`\`**. You can have a plaintext code block or specify the langauge for syntax highlighing after the opening backticks: **\`\`\`javascript**.


``` 
plain text (no language specified)
```

```python
# like this: ```python
def python_code_chunk():
  return 'syntax highlighting'
```

```javascript
// like this: ```javascript
function makeCodePretty() {
  return 'all the pretty colors'
}
```

## Links & Images

Images and links are similar: a like is formatted like this:

```markdown
<!-- link to Google -->
[Google](https://www.google.com/)
```

and a image is a link with a `!` in front of it. Don't forget the file extension! (here it is `.jpg`)

```markdown
<!-- local image -->
![Cute Doggo](./images/cute-doggo.jpg)
<!-- image that lives on the internet -->
![Frosted Chonker](https://i.redd.it/y1s0l63llrf21.jpg)
```

These show as:

<!-- link to Google -->
[Google](https://www.google.com/)
<!-- local image -->
![Cute Doggo](./images/cute-doggo.jpg)
<!-- image that lives on the internet -->
![Frosted Chonker](https://i.redd.it/y1s0l63llrf21.jpg)

## Tables

Tables have the top section that creates columns, `| Syntax | Description |` and `| ------ | ----------- |`, followed but items that fill up the columns, `| Paragraph | Text |`
`| **Bold** | *Italalic* |  code |`

```markdown
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
| **Bold** | *Italic* | `code` | 

## Escaping Characters:

You can escape markdown formatting with a forward slash before the character: `\`.

```makrdown
hey look two backticks \`\` 
hello asterisks \*hello\*
```

hey look two backpacks \`\`

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