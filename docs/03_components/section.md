# AH Section

> **Applies to**
>
> - All transactional email templates
> - German and English versions
> - Desktop and mobile layouts
> - Outlook-compatible implementations

---

# Purpose

The AH Section is the primary content component of the Akademikerhilfe Email Design System.

It groups related information into clearly structured and visually separated content blocks.

Every transactional email consists of one or more AH Sections.

---

# Role in the Email Architecture

The AH Section follows the Hero and contains the main communication of the email.

Typical structure

```
Hero

↓

AH Section

↓

AH Section

↓

AH Section

↓

Signature

↓

Footer
```

Each section communicates exactly one topic.

---

# Anatomy

A section may contain

- Section Icon (optional)
- Section Heading
- Introductory paragraph
- Body content
- Lists
- Tables
- Information Cards
- Buttons

Typical structure

```
[AH Icon]

Section Heading

Short introduction

Content

Primary Action (optional)
```

---

# Content Principle

One section = One topic

Do not combine unrelated information inside the same section.

Examples

✔ Payment Options

✔ Your Online Portal

✔ Before Your Move-In

✔ Early Move-In

Avoid

✘ Payment + Move-In + Parking + Laundry

---

# Section Heading

Every section should contain one heading.

The heading should clearly describe the content.

Good examples

Payment Options

Your Online Portal

Before Your Move-In

Early Move-In

Avoid

Information

Details

Important

---

# Section Icon

The Akademikerhilfe Brand Icon should be used to identify major content sections.

The icon should

- appear left of the heading
- use the documented size
- align vertically with the heading
- remain visually secondary

The icon should never replace the heading.

---

# Introductory Text

The first paragraph should explain the purpose of the section.

Keep introductions concise.

Recommended length

1–3 sentences

---

# Body Content

The body may contain

- paragraphs
- lists
- tables
- information cards
- links
- buttons

Content should remain logically grouped.

---

# Primary Action

A section may contain one primary action.

Examples

Open Online Portal

Accept Offer

Upload Documents

Pay Invoice

Buttons should always appear after the explanatory text.

---

# Visual Style

Background

```text
surface-primary
```

Heading

```text
text-primary
```

Body

```text
text-primary
```

Icon

```text
icon-primary
```

---

# Typography

## Heading

Token

```
font-body
```

Weight

Bold

Size

26 px

---

## Body

Token

```
font-body
```

Size

10 pt

Recommended HTML implementation

14 px

---

# Layout

Content alignment

Left

Maximum width

Container width

Sections should never extend beyond the content container.

---

# Spacing

Recommended values

| Element | Token |
|----------|-------|
| Section top | `space-2xl` |
| Icon to heading | `space-sm` |
| Heading to paragraph | `space-md` |
| Paragraph spacing | `space-md` |
| Content to button | `space-lg` |
| Section bottom | `space-2xl` |

---

# Variants

## Standard Section

Heading

Paragraph

Content

---

## Action Section

Heading

Paragraph

Primary Button

---

## Information Section

Heading

Information Card

---

## Table Section

Heading

Table

Optional Button

---

# Responsive Behaviour

On mobile devices

- maintain left alignment
- stack all content vertically
- reduce horizontal padding
- preserve spacing hierarchy
- avoid horizontal scrolling

The order of content must never change.

---

# Accessibility

Every section should

- contain one meaningful heading
- remain understandable without icons
- maintain sufficient colour contrast
- use descriptive links
- support screen readers

Icons should never communicate information on their own.

---

# Outlook Compatibility

The section should use

- table-based layout
- inline CSS
- PNG icons

Avoid

- Flexbox
- CSS Grid
- SVG icons
- background images

Spacing should rely on table cells and padding.

---

# Recommended HTML Structure

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding:48px 44px;">

      <table role="presentation" cellpadding="0" cellspacing="0" border="0">
        <tr>

          <td width="24" valign="top">
            <img
              src="{AH_ICON}"
              width="24"
              alt=""
              style="display:block;border:0;">
          </td>

          <td width="12"></td>

          <td valign="top">

            <h2>Payment Options</h2>

            <p>
              Choose the payment method that works best for you.
            </p>

          </td>

        </tr>
      </table>

    </td>
  </tr>
</table>
```

---

# Design Tokens

| Property | Token |
|----------|-------|
| Background | `surface-primary` |
| Heading | `text-primary` |
| Body | `text-primary` |
| Icon | `icon-primary` |
| Heading Font | `font-body` |
| Body Font | `font-body` |
| Top Padding | `space-2xl` |
| Bottom Padding | `space-2xl` |

---

# Best Practices

✔ One topic per section.

✔ One clear heading.

✔ Keep paragraphs short.

✔ Use icons consistently.

✔ Place buttons after explanatory text.

✔ Maintain consistent spacing.

✔ Reuse existing components.

---

# Avoid

✘ Multiple unrelated topics.

✘ Missing headings.

✘ Long text blocks.

✘ Decorative icons.

✘ Multiple competing buttons.

✘ Inconsistent spacing.

✘ Nested sections.

---

# Definition of Done

An AH Section is complete when

- the topic is immediately understandable
- one clear heading is present
- spacing follows the design system
- typography follows the design system
- icons are used correctly
- Outlook renders the section correctly
- the section is responsive
- accessibility requirements are fulfilled

---

# Guiding Principle

An AH Section should communicate one topic clearly and independently.

If the recipient can understand the purpose of the section within a few seconds, the component has achieved its goal.

---

## Related Documentation

- Email Architecture
- Layout
- Spacing
- Typography
- Color System
- Icon System
- Accessibility
- AH Hero