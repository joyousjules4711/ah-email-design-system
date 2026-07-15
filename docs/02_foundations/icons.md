> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - German and English versions

# Icon System

This document defines the icon strategy for the Akademikerhilfe Email Design System.

Icons support orientation, reinforce the Akademikerhilfe brand and improve the readability of transactional emails.

They should always support communication and never replace meaningful text.

---

# Purpose

Icons provide visual anchors throughout an email.

They help recipients quickly identify important sections and improve the overall reading experience without creating unnecessary visual complexity.

Icons should always have a clear functional purpose.

---

# Design Principles

The icon system follows five principles.

## Brand Recognition

Icons should strengthen the Akademikerhilfe identity.

---

## Simplicity

Icons should be visually simple and immediately recognizable.

---

## Consistency

Only one icon style should be used throughout the entire design system.

---

## Meaning

Every icon should communicate a purpose.

Icons without a clear purpose should be removed.

---

## Accessibility

Icons should support information—not replace it.

Every important message must remain understandable without relying on icons alone.

---

# Icon Categories

The Email Design System currently defines three icon categories.

---

## 1. Brand Icon

The official Akademikerhilfe icon is the primary icon of the design system.

It serves as a visual identifier for major content sections.

### Typical usage

- Payment Options
- Your Online Portal
- Before Your Move-In
- Early Move-In
- Important Information

The Brand Icon should always appear together with a section heading.

---

## 2. Social Media Icons

Social media icons are only used in the footer.

Supported platforms

- Instagram
- Facebook

Requirements

- consistent style
- equal size
- official Akademikerhilfe profiles only

---

## 3. Functional Icons

Functional icons are reserved for future use.

Examples include

- Documents
- Downloads
- Notifications
- Payments
- Warnings

New functional icons should only be introduced when they improve usability.

---

# Placement

Icons should always be aligned with their corresponding heading.

Recommended layout

```
[AH Icon]  Payment Options
```

Recommended spacing

- 12–16 px between icon and heading
- consistent spacing throughout the email

Icons should never appear without a related heading.

---

# Icon Size

Recommended sizes

Desktop

24 × 24 px

Mobile

20 × 20 px

All icons should remain optically balanced.

Do not stretch or distort icons.

---

# Colour

Icons use semantic color tokens.

| Token | Usage |
|--------|-------|
| `icon-primary` | Standard icons |
| `icon-accent` | Highlighted sections |

Additional colours should only be introduced through approved design tokens.

---

# Component Mapping

| Component | Icon Category |
|-----------|---------------|
| Section Heading | Brand Icon |
| Hero | None |
| Information Card | Optional Brand Icon |
| Feature Panel | Optional Brand Icon |
| Footer | Social Media Icons |
| Primary Button | No icon |
| Secondary Button | No icon |

---

# Accessibility

Icons should never communicate information on their own.

Always combine icons with

- headings
- descriptive text
- labels

Meaningful icons should include alternative text where appropriate.

Decorative icons should use empty alternative text.

Example

```
alt=""
```

---

# Email Client Considerations

Icons should be embedded as images.

Preferred production format

PNG

SVG may be stored inside the project repository but should not be embedded directly into production emails due to inconsistent email client support.

---

# Best Practices

✔ Use the Akademikerhilfe Brand Icon as the primary section marker.

✔ Maintain consistent icon sizes.

✔ Keep spacing consistent.

✔ Align icons with headings.

✔ Prefer fewer icons over many.

✔ Use icons only when they improve understanding.

---

# Avoid

✘ Mixing multiple icon libraries.

✘ Using icons as bullet points.

✘ Decorating paragraphs with icons.

✘ Using icons without descriptive text.

✘ Stretching or distorting icons.

✘ Introducing new icon styles without documentation.

---

# Future Development

Additional functional icons may be introduced in future releases.

Any new icon must

- follow the Akademikerhilfe visual language
- use the existing design tokens
- improve usability
- be documented before implementation

The introduction of new icon families requires approval as part of the Email Design System.

---

# Guiding Principle

Icons should improve orientation.

The best icon is the one that helps recipients find information faster while remaining almost invisible as a design element.