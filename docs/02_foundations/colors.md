> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - German and English versions

# Color System

This document defines the color system used throughout the Akademikerhilfe Email Design System.

The color system is based on semantic design tokens rather than hardcoded color values. This approach improves consistency, simplifies maintenance and allows future updates without changing component implementations.

The values defined here are derived from the official Akademikerhilfe Brand Guide.

---

# Design Philosophy

Colors should support communication.

They establish hierarchy, strengthen the Akademikerhilfe brand and guide the recipient's attention.

Colors should never be used for decoration alone.

---

# Color Tokens

| Token | Color | Hex | Usage |
|--------|-------|-----|-------|
| `brand-primary` | Elite Blue | `#033655` | Primary brand colour |
| `brand-accent` | Mint | `#7DC097` | Accent colour |
| `surface-primary` | White | `#FFFFFF` | Main content background |
| `surface-secondary` | Thassos Marble | `#EFF3F5` | Secondary background |
| `text-primary` | Elite Blue | `#033655` | Primary text |
| `text-inverse` | White | `#FFFFFF` | Text on dark backgrounds |
| `button-primary` | Elite Blue | `#033655` | Primary button background |
| `button-primary-text` | White | `#FFFFFF` | Primary button text |
| `button-secondary` | White | `#FFFFFF` | Secondary button background |
| `button-secondary-text` | Elite Blue | `#033655` | Secondary button text |
| `link` | Mint | `#7DC097` | Hyperlinks |
| `icon-primary` | Elite Blue | `#033655` | Standard icons |
| `icon-accent` | Mint | `#7DC097` | Accent icons |
| `border-light` | Thassos Marble | `#EFF3F5` | Dividers and subtle borders |

---

# Token Usage

## brand-primary

The primary Akademikerhilfe colour.

### Used for

- Header
- Headlines
- Primary Buttons
- Footer
- Brand Elements

---

## brand-accent

Used to create emphasis.

### Used for

- Icons
- Links
- Highlights
- Small decorative accents

Avoid using the accent colour for large surfaces.

---

## surface-primary

Main reading surface.

Used for

- Email body
- Tables
- Cards
- Content containers

---

## surface-secondary

Secondary background.

Used for

- Information cards
- Highlight sections
- Email canvas background

---

## text-primary

Primary text colour.

Used for

- Headings
- Body text
- Tables
- Signatures

Pure black should never be used.

---

## text-inverse

Used only on dark backgrounds.

Examples

- Header
- Primary buttons
- Dark feature panels

---

## button-primary

Primary call-to-action.

Background

`brand-primary`

Text

`text-inverse`

---

## button-secondary

Secondary actions.

Background

`surface-primary`

Text

`brand-primary`

Border

`brand-primary`

---

# Component Mapping

| Component | Token |
|-----------|-------|
| Header | `brand-primary` |
| Footer | `brand-primary` |
| Hero | `brand-primary` |
| Primary Button | `button-primary` |
| Secondary Button | `button-secondary` |
| Information Card | `surface-secondary` |
| Payment Table | `surface-primary` |
| Body Background | `surface-primary` |
| Email Background | `surface-secondary` |
| Icons | `icon-primary` / `icon-accent` |

---

# Accessibility

Colours must never communicate information on their own.

Always combine colours with

- headings
- icons
- descriptive text

All text should meet WCAG AA contrast recommendations whenever technically possible.

---

# Email Client Considerations

Email clients may modify colours automatically, especially in

- Dark Mode
- High Contrast Mode

Templates should remain readable when colours are adjusted.

---

# Future Semantic Tokens

Additional semantic tokens may be introduced in future releases.

Examples

| Token | Purpose |
|--------|---------|
| `status-success` | Positive confirmations |
| `status-warning` | Warnings |
| `status-error` | Errors |
| `status-info` | Informational messages |

These tokens should always map to approved brand colours.

---

# Best Practices

✔ Use semantic tokens instead of hexadecimal values.

✔ Keep the number of colours intentionally small.

✔ Use colour to create hierarchy.

✔ Prioritize readability over decoration.

✔ Reuse existing tokens before introducing new ones.

---

# Guiding Principle

Every colour has a purpose.

If a new colour is introduced, its purpose must be documented before it is used.