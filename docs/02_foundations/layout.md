# Layout

> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - German and English versions

---

# Purpose

The layout system defines the overall structure of every Akademikerhilfe email.

A consistent layout improves readability, supports the Akademikerhilfe brand and creates a familiar user experience across all transactional communications.

---

# Design Principles

The layout should

- be clean
- be easy to scan
- work across all major email clients
- be responsive
- emphasize content over decoration

Whitespace is an intentional design element.

---

# Layout Structure

Every email follows the same structural hierarchy.

```
Email Canvas
    │
    ├── Header
    │
    ├── Hero
    │
    ├── Content Sections
    │
    ├── Call-to-Action
    │
    ├── Additional Information
    │
    ├── Signature
    │
    └── Footer
```

---

# Canvas

Maximum width

```
660 px
```

Background

`surface-secondary`

Content container

`surface-primary`

The email should be centered horizontally.

---

# Header

Purpose

Brand recognition.

Contains

- Logo
- Optional preheader

Background

`brand-primary`

---

# Hero

The Hero introduces the primary purpose of the email.

Contains

- H1
- Introductory paragraph

Only one Hero per email.

---

# Content Sections

Information is divided into clearly separated sections.

Each section may contain

- Heading
- Paragraph
- Table
- Information Card
- Button

Avoid overly long content blocks.

---

# Information Cards

Used to highlight supporting information.

Background

`surface-secondary`

Spacing should separate cards clearly from surrounding content.

---

# Tables

Tables should only be used for structured information.

Examples

- Payment plans
- Financial information
- Contract details

Avoid using tables for general page layout whenever possible.

---

# Buttons

Buttons represent the primary user action.

Each email should contain

- one primary button

Additional secondary buttons should be used only when necessary.

---

# Signature

Placed after the primary content.

Contains

- Team
- Contact information
- Organisation

---

# Footer

Contains

- Legal information
- Social media links
- Copyright
- Address

The footer should remain visually consistent across all templates.

---

# Responsive Behaviour

The layout should adapt to

- Desktop
- Tablet
- Mobile

Content should never require horizontal scrolling.

---

# White Space

Whitespace creates hierarchy.

Do not fill every available area.

Generous spacing improves readability.

---

# Component Hierarchy

The visual hierarchy should follow this order.

1. Hero
2. H2
3. Information Card
4. Body Text
5. Button
6. Footer

---

# Layout Tokens

| Token | Value |
|--------|-------|
| `layout-max-width` | 660 px |
| `layout-background` | `surface-secondary` |
| `layout-content` | `surface-primary` |
| `layout-alignment` | Center |
| `layout-radius` | 0 px |

Rounded corners are intentionally not used.

---

# Best Practices

✔ One clear Hero

✔ One primary action

✔ Clear visual hierarchy

✔ Consistent spacing

✔ Responsive layout

✔ White background for content

✔ Blue header

---

# Avoid

✘ Multiple Heroes

✘ Competing call-to-actions

✘ Decorative layout elements

✘ Large uninterrupted text blocks

✘ Fixed-width content exceeding 660 px

---

# Guiding Principle

Layout should organize communication—not decorate it.