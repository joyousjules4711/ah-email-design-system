> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - German and English versions

# Typography

> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - German and English versions

---

# Purpose

Typography is one of the core building blocks of the Akademikerhilfe Email Design System.

It creates hierarchy, improves readability and supports a consistent brand experience across all email templates.

Because email clients provide only limited font support, the typography system prioritizes compatibility and reliability over visual complexity.

---

# Typography Philosophy

The Akademikerhilfe Brand Guide defines the preferred typefaces.

However, HTML emails must remain fully functional across all supported email clients.

For this reason, every font definition includes a production-ready fallback using standard operating system fonts.

No web fonts are loaded.

---

# Font Strategy

## Brand Display Font

Preferred

```
Erstoria
```

Production Font Stack

```css
font-family: "Erstoria", Georgia, serif;
```

Usage

- H1 only

---

## Brand Text Font

Preferred

```
Brandon Text
```

Production Font Stack

```css
font-family: "Brandon Text", Arial, sans-serif;
```

Usage

- Body text
- Headings (H2–H6)
- Buttons
- Tables
- Lists
- Signature
- Footer

---

# Typography Scale

## H1

Purpose

Primary email headline

Font

Erstoria

Fallback

Georgia

Size

Desktop

40 px

Mobile

32 px

Weight

Regular

Line Height

120%

Colour

`text-primary`

Maximum

One H1 per email

---

## H2

Purpose

Section heading

Font

Brandon Text

Fallback

Arial

Size

Desktop

26 px

Mobile

22 px

Weight

Bold

Line Height

130%

Colour

`text-primary`

---

## H3

Purpose

Subsection heading

Font

Brandon Text

Fallback

Arial

Size

Desktop

22 px

Mobile

20 px

Weight

Bold

Line Height

135%

Colour

`text-primary`

---

## Body Text

Purpose

General communication

Font

Brandon Text

Fallback

Arial

Size

10 pt

HTML equivalent

13.33 px

Recommended implementation

14 px

Weight

Regular

Line Height

160%

Colour

`text-primary`

---

## Small Text

Purpose

Secondary information

Examples

- Footer
- Legal Information
- References

Font

Brandon Text

Fallback

Arial

Size

9 pt

HTML equivalent

12px

Line Height

150%

Colour

`text-primary`

---

## Buttons

Font

Brandon Text

Fallback

Arial

Weight

Bold

Size

16 px

Line Height

100%

Colour

`text-inverse`

Buttons should always use sentence case.

---

## Tables

Font

Brandon Text

Fallback

Arial

Header

Bold

Body

Regular

Size

16 px

Colour

`text-primary`

---

## Signature

Font

Brandon Text

Fallback

Arial

Size

16 px

Weight

Regular

Colour

`text-primary`

---

# Text Alignment

Default alignment

Left

Centered text should only be used for

- Hero headline
- Hero introduction

Body text should always remain left-aligned.

---

# Text Colour

The Email Design System intentionally limits text colours.

| Token | Usage |
|--------|-------|
| `text-primary` | Standard text |
| `text-inverse` | Text on dark backgrounds |

Pure black should never be used.

---

# Font Loading

No web fonts are loaded.

Custom fonts are displayed only when they are available on the recipient's device.

Fallback fonts are standard operating system fonts to maximize compatibility across

- Microsoft Outlook
- Gmail
- Apple Mail
- Outlook Web
- Outlook Mobile

---

# Responsive Behaviour

Typography should remain readable on all screen sizes.

Body text should never be smaller than

16 px

Small text should never be smaller than

14 px

Headlines scale proportionally on mobile devices.

---

# Accessibility

Typography should

- maintain sufficient colour contrast
- use generous line spacing
- avoid justified text
- avoid excessive bold formatting

Typography should comply with the accessibility guidelines defined in

`accessibility.md`

---

# Typography Tokens

| Token | Value |
|--------|-------|
| `font-display` | Erstoria |
| `font-display-fallback` | Georgia |
| `font-body` | Brandon Text |
| `font-body-fallback` | Arial |
| `font-size-h1` | 40 px |
| `font-size-h2` | 26 px |
| `font-size-h3` | 22 px |
| `font-size-body` | 16 px |
| `font-size-small` | 14 px |
| `line-height-heading` | 120% |
| `line-height-body` | 160% |

---

# Best Practices

✔ Use only one H1 per email.

✔ Use Erstoria exclusively for H1.

✔ Use Brandon Text for all remaining text.

✔ Always include the defined fallback fonts.

✔ Maintain generous whitespace.

✔ Prefer readability over decoration.

---

# Avoid

✘ Using Erstoria outside H1.

✘ Mixing additional font families.

✘ Using pure black text.

✘ Using body text smaller than 16 px.

✘ Center-aligning long paragraphs.

---

# Guiding Principle

Typography should never draw attention to itself.

The recipient should notice the message—not the typeface.