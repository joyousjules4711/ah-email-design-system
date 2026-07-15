# AH Hero

> **Applies to**
>
> * All transactional email templates
> * German and English versions
> * Desktop and mobile layouts
> * Outlook-compatible implementations

---

# Purpose

The AH Hero introduces the primary purpose of an Akademikerhilfe email.

It creates immediate brand recognition, establishes the visual hierarchy and helps recipients understand the message before reading the main content.

The Hero should be concise, recognizable and consistent across all transactional email templates.

---

# Role in the Email Architecture

The AH Hero appears directly after the Header or may be visually combined with the Header.

Recommended position:

```text
Email Canvas
│
├── Header
├── AH Hero
├── Metadata
├── Greeting
└── Main Content
```

In the current Akademikerhilfe email design, the Header and Hero may be implemented as one continuous Elite Blue section.

---

# Anatomy

The AH Hero may contain:

1. Akademikerhilfe logo
2. Department label
3. H1
4. Mint accent line
5. Optional short supporting line

Example:

```text
[Akademikerhilfe Logo]

AKADEMIKERHILFE STUDENTSERVICE

Your Housing Offer

────────────
```

---

# Required Elements

## H1

Every Hero must contain exactly one H1.

The H1 communicates the main purpose of the email.

Examples:

```text
Welcome to Akademikerhilfe
```

```text
Your Housing Offer
```

```text
SEPA Pre-Notification
```

```text
Payment Agreement
```

The H1 must remain concise and should generally fit within two lines on mobile devices.

---

# Optional Elements

## Logo

The official Akademikerhilfe logo may appear once inside the Hero.

The approved logo version must be selected according to the background.

For Elite Blue backgrounds, use the approved light or white logo version.

Do not place the dark logo directly on an Elite Blue background.

---

## Department Label

A small uppercase department label may appear above the H1.

Examples:

```text
AKADEMIKERHILFE STUDENTSERVICE
```

```text
AKADEMIKERHILFE ACCOUNTING
```

The department label is optional.

It should remain visually secondary.

---

## Accent Line

A Mint accent line may appear below the H1.

Purpose:

* reinforce the brand
* create visual closure
* separate the Hero from the following content

The accent line should remain short and decorative.

It must not be used as the only visual separator for important information.

---

## Supporting Line

A short supporting sentence may appear below the H1 where required.

Example:

```text
Please accept your offer by 15 June 2026.
```

The supporting line should not duplicate the introduction in the content area.

---

# Visual Style

## Background

Recommended token:

```text
brand-primary
```

Current value:

```text
#033655
```

---

## H1 Colour

Recommended token:

```text
text-inverse
```

Current value:

```text
#FFFFFF
```

---

## Accent Colour

Recommended token:

```text
brand-accent
```

Current value:

```text
#7DC097
```

---

## Department Label Colour

Recommended token:

```text
brand-accent
```

---

# Typography

## H1

Font:

```text
Erstoria
```

Fallback:

```text
Georgia
```

Production font stack:

```css
font-family: "Erstoria", Georgia, serif;
```

Desktop size:

```text
40 px
```

Mobile size:

```text
32 px
```

Weight:

```text
Regular
```

Line height:

```text
120%
```

---

## Department Label

Font:

```text
Brandon Text
```

Fallback:

```text
Arial
```

Production font stack:

```css
font-family: "Brandon Text", Arial, sans-serif;
```

Recommended size:

```text
12 px
```

Recommended styling:

```text
Uppercase
Letter spacing: 1.5–2 px
Bold or Medium
```

---

# Spacing

Recommended desktop values:

| Element                  |     Spacing |
| ------------------------ | ----------: |
| Hero outer padding       | `space-2xl` |
| Logo to department label |  `space-xl` |
| Department label to H1   |  `space-sm` |
| H1 to accent line        |  `space-lg` |
| Hero to content          | `space-2xl` |

Recommended mobile values:

| Element                  |    Spacing |
| ------------------------ | ---------: |
| Hero outer padding       | `space-lg` |
| Logo to department label | `space-lg` |
| Department label to H1   | `space-sm` |
| H1 to accent line        | `space-lg` |

---

# Logo Usage

The logo should:

* appear once per email
* remain proportionally scaled
* use an approved brand asset
* include descriptive alternative text
* remain readable when images are blocked

Recommended alternative text:

```text
Akademikerhilfe
```

The Hero must remain understandable if the logo does not load.

---

# Alignment

Default alignment:

```text
Left
```

Left alignment supports readability and matches the Akademikerhilfe presentation and email design direction.

Centered Hero layouts should only be introduced as a documented variant.

Long supporting text must never be centered.

---

# Variants

## Standard Hero

Contains:

* logo
* department label
* H1
* accent line

Recommended for most transactional emails.

---

## Compact Hero

Contains:

* department label
* H1
* accent line

Used where the logo is already displayed in a separate Header component.

---

## Minimal Hero

Contains:

* H1
* accent line

Used for short system notifications where vertical space should be reduced.

---

# Content Guidelines

The H1 should describe the message, not the department.

Good:

```text
Your Housing Offer
```

```text
Welcome to Akademikerhilfe
```

```text
Upcoming SEPA Debit
```

Avoid:

```text
Important Information
```

```text
Studentservice
```

```text
Notification
```

---

# Responsive Behaviour

On screens below 600 px:

* horizontal padding is reduced
* H1 size decreases from 40 px to 32 px
* logo width may be reduced
* text remains left-aligned
* the Hero must not cause horizontal scrolling
* the H1 should remain readable without manual zooming

The content order must remain unchanged.

---

# Accessibility

The Hero must:

* contain one meaningful H1
* maintain sufficient colour contrast
* remain understandable without images
* avoid text embedded inside images
* use descriptive logo alternative text
* preserve logical reading order

Decorative images must use:

```html
alt=""
```

The logo is not decorative and should use:

```html
alt="Akademikerhilfe"
```

---

# Outlook Compatibility

The Hero should use table-based layout.

Critical styles must be inline.

Avoid:

* Flexbox
* CSS Grid
* background images
* SVG logos in production
* CSS positioning
* border radius as a required visual feature

Use solid background colours.

The Hero must remain functional if custom fonts are unavailable.

---

# Recommended HTML Structure

```html
<table
  role="presentation"
  width="100%"
  cellpadding="0"
  cellspacing="0"
  border="0"
  style="width:100%; background-color:#033655;"
>
  <tr>
    <td
      class="ah-hero"
      style="
        padding:42px 44px 46px 44px;
        background-color:#033655;
        text-align:left;
      "
    >

      <img
        src="{LOGO_URL}"
        width="300"
        alt="Akademikerhilfe"
        style="
          display:block;
          width:300px;
          max-width:100%;
          height:auto;
          margin:0 0 32px 0;
          border:0;
        "
      >

      <p
        style="
          margin:0 0 12px 0;
          font-family:'Brandon Text',Arial,sans-serif;
          font-size:12px;
          line-height:1.4;
          font-weight:bold;
          letter-spacing:2px;
          text-transform:uppercase;
          color:#7dc097;
        "
      >
        Akademikerhilfe Studentservice
      </p>

      <h1
        style="
          margin:0;
          font-family:'Erstoria',Georgia,serif;
          font-size:40px;
          line-height:1.2;
          font-weight:normal;
          color:#ffffff;
        "
      >
        Your Housing Offer
      </h1>

      <div
        style="
          width:150px;
          height:2px;
          margin-top:24px;
          background-color:#7dc097;
        "
      ></div>

    </td>
  </tr>
</table>
```

---

# Design Tokens

| Property             | Token                 |
| -------------------- | --------------------- |
| Background           | `brand-primary`       |
| H1 text              | `text-inverse`        |
| Department label     | `brand-accent`        |
| Accent line          | `brand-accent`        |
| H1 font              | `font-display`        |
| Supporting text font | `font-body`           |
| Desktop padding      | `space-2xl`           |
| Mobile padding       | `space-lg`            |
| H1 desktop size      | `font-size-h1`        |
| H1 mobile size       | `font-size-h1-mobile` |

---

# Best Practices

✔ Use one Hero per email.

✔ Use one H1 per email.

✔ Keep the H1 short and descriptive.

✔ Use the approved Akademikerhilfe logo.

✔ Use the correct logo version for the background.

✔ Keep supporting information concise.

✔ Use the Mint accent sparingly.

✔ Maintain the same structure across German and English templates.

✔ Ensure the Hero remains readable without custom fonts.

---

# Avoid

✘ Multiple H1 elements.

✘ Generic titles such as “Information”.

✘ Large paragraphs inside the Hero.

✘ Multiple logos.

✘ Unsupported SVG logos in production emails.

✘ Background photography in transactional emails without a documented use case.

✘ Center-aligned long text.

✘ Buttons inside the Hero by default.

✘ Decorative elements that compete with the message.

---

# Definition of Done

The AH Hero is complete when:

* the H1 clearly communicates the purpose of the email
* the correct logo version is used
* the department label is accurate
* the Hero follows the documented typography
* the layout is responsive
* the component works without custom fonts
* the component works when images are disabled
* the component renders correctly in Outlook
* the German and English versions use the same structure

---

# Guiding Principle

The Hero should make the purpose of the email immediately clear while establishing Akademikerhilfe as the sender.

Brand recognition and message clarity are equally important.

---

## Related Documentation

* [Email Architecture](../02_foundations/email-architecture.md)
* [Color System](../02_foundations/colors.md)
* [Typography](../02_foundations/typography.md)
* [Spacing](../02_foundations/spacing.md)
* [Icon System](../02_foundations/icons.md)
* [Outlook Compatibility](../02_foundations/outlook-compatibility.md)
* [Accessibility](../02_foundations/accessibility.md)
