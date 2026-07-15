# Button

> **Applies to**
>
> - All transactional email templates
> - German and English versions
> - Desktop and mobile layouts
> - Outlook-compatible implementations

---

## Status

**Stable** ✅

Version: 1.0

Owner: Email Design System

---

# Purpose

The Button component represents the primary interactive element within the Akademikerhilfe Email Design System.

Buttons guide recipients towards a specific action and should always represent the next logical step in the user journey.

Every button should communicate one clear action.

---

# Design Principles

Buttons should

- encourage action
- remain highly visible
- be easy to understand
- work across all supported email clients
- remain accessible on desktop and mobile devices

Buttons should never compete with one another.

---

# Variants

The Email Design System defines two button variants.

| Variant | Purpose |
|----------|---------|
| **Primary Button** | Main action |
| **Secondary Button** | Optional or alternative action |

---

# Primary Button

## Purpose

The Primary Button represents the most important action within the email.

Whenever possible, each email should contain only one Primary Button.

### Typical Actions

- Accept Offer
- Open Online Portal
- Upload Documents
- Pay Invoice
- View Contract

---

## Appearance

Background

`button-primary`

Text

`button-primary-text`

Border

None

Typography

Brandon Text / Arial

---

# Secondary Button

## Purpose

The Secondary Button is used for optional actions.

It should never visually compete with the Primary Button.

### Typical Actions

- Contact Studentservice
- Learn More
- Download Information
- View FAQ

---

## Appearance

Background

`button-secondary`

Text

`button-secondary-text`

Border

`brand-primary`

Typography

Brandon Text / Arial

---

# Usage Rules

✔ One Primary Button per email whenever possible.

✔ Secondary Buttons are optional.

✔ Secondary Buttons should always appear after the Primary Button.

✔ Do not place multiple Primary Buttons within the same section.

---

# Button Labels

Button labels should

- begin with a verb
- remain concise
- describe the destination

Good examples

```
Accept Offer
```

```
Open Online Portal
```

```
Upload Documents
```

Avoid

```
Click Here
```

```
Continue
```

```
More
```

---

# Typography

Font

Brandon Text

Fallback

Arial

Production Stack

```css
font-family:"Brandon Text",Arial,sans-serif;
```

Weight

Bold

Corporate Size

10 pt

Recommended HTML Implementation

14 px

Alignment

Center

Sentence case should always be used.

---

# Dimensions

Minimum height

44 px

Recommended horizontal padding

`space-lg`

Recommended vertical padding

`space-md`

Buttons should remain comfortable to tap on mobile devices.

---

# Alignment

Preferred alignment

Left

Centered buttons may be used inside centered layouts.

Avoid placing buttons next to each other.

---

# Spacing

| Element | Token |
|----------|-------|
| Content → Button | `space-lg` |
| Button → Next Section | `space-xl` |

Buttons should always have sufficient surrounding whitespace.

---

# Responsive Behaviour

On mobile devices

- buttons may expand to full width
- minimum height remains 44 px
- labels should remain on a single line whenever possible

---

# Accessibility

Buttons must

- have descriptive labels
- maintain sufficient contrast
- be understandable without surrounding text
- avoid ALL CAPS

---

# Outlook Compatibility

Buttons should use

- table-based HTML
- inline CSS

VML support may be introduced in future versions.

Avoid

- gradients
- shadows
- CSS animations

---

# Recommended HTML Structure

## Primary Button

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
<tr>
<td>

<a
href="{URL}"
style="
display:inline-block;
padding:14px 28px;
background:#033655;
color:#ffffff;
font-family:'Brandon Text',Arial,sans-serif;
font-size:14px;
font-weight:bold;
text-decoration:none;
">

Open Online Portal

</a>

</td>
</tr>
</table>
```

---

## Secondary Button

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
<tr>
<td>

<a
href="{URL}"
style="
display:inline-block;
padding:14px 28px;
background:#ffffff;
border:2px solid #033655;
color:#033655;
font-family:'Brandon Text',Arial,sans-serif;
font-size:14px;
font-weight:bold;
text-decoration:none;
">

Contact Studentservice

</a>

</td>
</tr>
</table>
```

---

# Design Tokens

| Property | Token |
|----------|-------|
| Primary Background | `button-primary` |
| Primary Text | `button-primary-text` |
| Secondary Background | `button-secondary` |
| Secondary Text | `button-secondary-text` |
| Font | `font-body` |
| Font Size | `font-size-body` |
| Horizontal Padding | `space-lg` |
| Vertical Padding | `space-md` |

---

# Best Practices

✔ Use one Primary Button whenever possible.

✔ Use Secondary Buttons only for optional actions.

✔ Use action-oriented labels.

✔ Keep labels concise.

✔ Maintain consistent spacing.

✔ Ensure touch-friendly sizing.

---

# Avoid

✘ "Click Here"

✘ More than one Primary Button

✘ Buttons without context

✘ Long button labels

✘ Decorative button styles

✘ Small tap targets

---

# Definition of Done

The Button component is complete when

- the correct variant is selected
- the label is action-oriented
- spacing follows the design system
- typography follows the design system
- the button is accessible
- Outlook compatibility is verified
- responsive behaviour is verified

---

# Guiding Principle

Every button should answer one simple question:

> **What should the recipient do next?**

If that answer is immediately obvious, the component has fulfilled its purpose.

---

## Related Documentation

- Email Architecture
- Colors
- Typography
- Spacing
- Accessibility
- Outlook Compatibility
- Section