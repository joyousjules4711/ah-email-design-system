# MSO Conditional Comments

> **Applies to**
>
> - Microsoft Outlook (Windows)
> - HTML email templates
> - Reusable components

---

# Purpose

Microsoft Outlook for Windows uses the Microsoft Word rendering engine instead of a web browser to display HTML emails.

Because of this limitation, certain HTML structures and CSS properties require Outlook-specific code.

MSO Conditional Comments allow developers to provide alternative HTML that is rendered only by Microsoft Outlook.

---

# When to Use

Use MSO Conditional Comments only when Outlook requires a different implementation.

Typical use cases include

- VML buttons
- background images
- layout fixes
- spacing adjustments
- Outlook-specific tables

Avoid using conditional comments unnecessarily.

---

# Basic Syntax

```html
<!--[if mso]>
    Outlook-specific HTML
<![endif]-->
```

Only Microsoft Outlook (Windows) renders the enclosed HTML.

Other email clients ignore it.

---

# Outlook Version Targeting

All Outlook versions

```html
<!--[if mso]>
...
<![endif]-->
```

Outlook 2007 and later

```html
<!--[if gte mso 9]>
...
<![endif]-->
```

Older Outlook versions can also be targeted when required.

---

# Typical Use Cases

## Outlook Wrapper Table

```html
<!--[if mso]>
<table role="presentation" width="660" cellpadding="0" cellspacing="0" border="0">
<tr>
<td>
<![endif]-->

<!-- Standard HTML -->

<!--[if mso]>
</td>
</tr>
</table>
<![endif]-->
```

Purpose

Provides a stable layout for Outlook.

---

## Fixed Width Container

Outlook sometimes ignores responsive container widths.

A fixed wrapper table ensures predictable rendering.

---

## VML Buttons

Microsoft Outlook does not reliably support modern CSS buttons.

VML should be used for

- primary buttons
- important call-to-actions

Future versions of the Email Design System will provide a reusable VML button component.

---

## Background Images

Background images require VML.

Preferred approach

Use solid background colours whenever possible.

---

## Spacing Fixes

Margins behave inconsistently in Outlook.

Conditional comments may introduce Outlook-specific table rows or padding.

---

# Design Principles

Conditional comments should

- solve Outlook-specific problems
- remain isolated
- not duplicate large HTML sections
- remain easy to maintain

Whenever possible, the standard HTML should remain identical across email clients.

---

# Best Practices

✔ Use conditional comments only when necessary.

✔ Keep Outlook-specific code separate.

✔ Comment Outlook workarounds.

✔ Test every Outlook modification.

✔ Prefer reusable solutions.

---

# Avoid

✘ Wrapping the entire email in conditional comments.

✘ Duplicating complete layouts.

✘ Creating different email structures.

✘ Mixing Outlook fixes with standard HTML.

---

# Code Documentation

Every Outlook-specific implementation should include a short explanation.

Example

```html
<!-- Outlook wrapper table -->

<!--[if mso]>
...
<![endif]-->
```

This improves maintainability.

---

# Testing

Every Outlook-specific implementation should be tested in

- Outlook for Windows
- Outlook for Microsoft 365

Visual appearance should be compared with

- Apple Mail
- Gmail
- Outlook Web

---

# Future Components

The following reusable Outlook components are planned

- AH VML Primary Button
- AH Outlook Wrapper
- AH Outlook Background
- AH Outlook Divider

These components will minimize duplicated Outlook-specific code.

---

# Related Documentation

- Outlook Compatibility
- Components
- Layout
- Buttons
- Hero

---

# Guiding Principle

Use MSO Conditional Comments only to improve compatibility.

The standard HTML should always remain the primary implementation.