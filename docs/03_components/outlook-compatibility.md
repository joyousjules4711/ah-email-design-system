# Outlook Compatibility

## Purpose

Microsoft Outlook uses the Microsoft Word rendering engine instead of a modern
web browser. As a result, many HTML and CSS features behave differently or are
not supported.

This design system follows a conservative approach to maximise compatibility
across Outlook, Gmail, Apple Mail and other major email clients.

---

# General Principles

The following rules apply to every component and every template.

- Use table-based layouts.
- Use inline CSS whenever possible.
- Avoid complex CSS selectors.
- Avoid external stylesheets.
- Avoid JavaScript.
- Avoid HTML forms.
- Use fixed-width email containers.
- Test every template in Outlook before production.

---

# Tables

Always use presentation tables for layout.

```html
<table
  role="presentation"
  cellpadding="0"
  cellspacing="0"
  border="0"
>
```

Never use CSS Grid or Flexbox for email layouts.

---

# Microsoft Office (MSO) CSS

Several CSS properties are recognised only by Microsoft Outlook.

Examples:

```css
mso-table-lspace: 0;
mso-table-rspace: 0;
mso-line-height-rule: exactly;
```

These properties are expected and should never be removed.

---

# Conditional Comments

Use MSO conditional comments whenever Outlook-specific markup is required.

Example:

```html
<!--[if mso]>
...
<![endif]-->
```

VML buttons are implemented using conditional comments.

---

# Buttons

Primary buttons use:

- HTML for modern email clients
- VML for Microsoft Outlook

Both versions must always be kept in sync.

---

# Images

Always use:

```html
display:block;
border:0;
outline:none;
text-decoration:none;
-ms-interpolation-mode:bicubic;
```

Always define:

- width
- alt
- height:auto

Never rely on CSS background images for important content.

---

# Typography

Supported fonts:

- Arial
- Helvetica
- sans-serif

Do not use web fonts.

---

# Border Radius

Rounded corners are supported by most email clients.

Microsoft Outlook does not fully support CSS border-radius.

Where rounded buttons are required, use VML.

---

# Spacing

Prefer:

- table padding
- cell padding

Avoid:

- margin-based layouts

Outlook renders padding more consistently than margins.

---

# Responsive Design

Responsive behaviour is implemented using:

```css
@media only screen and (max-width:600px)
```

Desktop Outlook ignores media queries.

Templates must therefore remain readable without responsive behaviour.

---

# VS Code Warnings

The standard CSS validator reports several Outlook-specific CSS properties
as unknown.

Examples:

```css
mso-table-lspace
mso-table-rspace
mso-line-height-rule
```

These warnings are expected.

Do not remove these properties.

---

# Testing Checklist

Before releasing a template, verify:

- Layout in Outlook Desktop
- Layout in Outlook Web
- Gmail
- Apple Mail
- Mobile Gmail
- Mobile Outlook
- Images
- Buttons
- Links
- Placeholders
- Responsive layout

---

# References

- outlook rendering
- VML buttons
- MSO conditional comments