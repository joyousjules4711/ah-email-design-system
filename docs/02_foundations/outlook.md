# Outlook Compatibility

> **Applies to**
>
> - All transactional email templates
> - All reusable components
> - Microsoft Outlook (Windows)
> - Outlook Web
> - Outlook Mobile

---

# Purpose

Microsoft Outlook remains one of the most challenging email clients for HTML email development.

This document defines the compatibility guidelines required to ensure reliable rendering across supported Outlook versions.

The Email Design System follows a compatibility-first approach.

Reliable rendering is always preferred over modern HTML or CSS features with limited support.

---

# Supported Outlook Clients

The Email Design System supports

- Outlook for Windows
- Outlook for Microsoft 365
- Outlook on the Web
- Outlook Mobile

Special attention should be given to Outlook for Windows, which uses the Microsoft Word rendering engine.

---

# Development Philosophy

Always build for Outlook first.

If a feature is not supported by Outlook, evaluate whether it is essential before using it.

Compatibility takes precedence over visual enhancements.

---

# HTML Structure

Emails should use a simple and predictable HTML structure.

Preferred

- nested tables
- inline styles
- fixed-width content container

Avoid unnecessary nesting.

---

# Layout

Preferred layout method

HTML tables

Avoid

- CSS Grid
- Flexbox
- Floating elements
- Absolute positioning

These techniques are inconsistently supported by Outlook.

---

# CSS

Use inline CSS wherever possible.

Avoid relying on

- external stylesheets
- embedded CSS for essential layout
- advanced selectors

Critical styling should always be inline.

---

# Width

Recommended maximum content width

660 px

Always define widths explicitly.

---

# Images

Preferred format

PNG

Avoid

SVG

SVG support remains inconsistent across Outlook versions.

---

# Logos

Logos should preferably be embedded as inline attachments (CID images).

Alternative methods

- HTTPS hosted images
- Base64 (not recommended)

---

# Buttons

Primary buttons should be created using table-based HTML.

For maximum Outlook compatibility, VML buttons may be introduced in future versions.

Avoid relying solely on

- border-radius
- padding
- CSS background effects

---

# Background Images

Avoid background images.

If background images are required, VML must be used for Outlook compatibility.

Solid background colours are preferred.

---

# Fonts

Use the defined font stacks.

Outlook may ignore custom fonts.

Fallback fonts should always remain readable.

Example

```css
font-family: "Brandon Text", Arial, sans-serif;
```

---

# Spacing

Prefer

- padding
- table cell spacing

Avoid excessive use of CSS margins.

Margins behave inconsistently in Outlook.

---

# Borders

Simple borders are preferred.

Avoid

- complex shadows
- blur effects
- advanced gradients

---

# Border Radius

Small border radii are generally acceptable.

Critical design elements should remain functional if rounded corners are ignored.

---

# Shadows

Avoid box shadows.

Support is inconsistent across Outlook versions.

---

# Transparency

Avoid transparent PNGs where possible.

Test transparency carefully against both light and dark backgrounds.

---

# Icons

Icons should be embedded as PNG images.

Maintain consistent sizing.

Avoid SVG icons.

---

# Animated Content

Avoid animated GIFs when essential information is involved.

Outlook displays only the first frame.

Animations should always be optional.

---

# Forms

HTML forms are not supported.

Never embed forms inside transactional emails.

Always link to the Online Portal instead.

---

# Video

Do not embed videos.

Use

- preview image
- play icon
- external link

---

# Media Queries

Media queries are supported inconsistently.

Layouts should remain usable even if media queries are ignored.

Responsive behaviour should degrade gracefully.

---

# Dark Mode

Outlook may automatically modify

- background colours
- text colours
- images

Templates should remain readable when colour inversion occurs.

Dark Mode behaviour is documented separately.

---

# Accessibility

Ensure

- sufficient contrast
- descriptive links
- alternative text
- logical reading order

Outlook users should receive the same information as users of other email clients.

---

# Testing

Every template should be tested in

- Outlook for Windows
- Outlook Web
- Outlook Mobile

Testing should verify

- layout
- typography
- buttons
- tables
- spacing
- images
- responsive behaviour

---

# Development Checklist

Before releasing a template, verify

- tables render correctly
- images display correctly
- buttons remain clickable
- fallback fonts work
- spacing is consistent
- no horizontal scrolling occurs
- links function correctly

---

# Recommended Practices

✔ Use tables for layout.

✔ Use inline CSS.

✔ Use PNG images.

✔ Use explicit widths.

✔ Use simple HTML.

✔ Test frequently.

---

# Avoid

✘ CSS Grid

✘ Flexbox

✘ SVG

✘ Position absolute

✘ JavaScript

✘ HTML forms

✘ Embedded video

✘ External CSS

✘ Complex animations

---

# Future Improvements

Future versions of the Email Design System may introduce

- VML button components
- Outlook-specific conditional comments
- automated Outlook rendering tests
- Litmus integration
- Email on Acid integration

---

# Guiding Principle

If Outlook renders the email correctly, most other email clients will render it correctly as well.

Build for compatibility first, then enhance where supported.

---

## Related Documentation

- Technology Stack
- Layout
- Typography
- Accessibility
- Components