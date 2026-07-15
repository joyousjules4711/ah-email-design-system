# Email Architecture

> **Applies to**
>
> * All transactional email templates
> * All reusable components
> * German and English versions

---

# Purpose

This document defines the standard architecture of an Akademikerhilfe transactional email.

The purpose of the architecture is to create a consistent structure across all templates, regardless of department, language or communication type.

A shared architecture improves

* usability
* readability
* accessibility
* maintainability
* development speed
* consistency across templates

The architecture describes the order and purpose of email sections.

It does not define the visual implementation of individual components.

---

# Core Principle

Every email should guide the recipient through a clear sequence.

The recipient should immediately understand

1. why the email was sent
2. what information is important
3. whether an action is required
4. what happens next
5. who to contact

The email structure should support this sequence.

---

# Standard Email Anatomy

The default Akademikerhilfe email follows this structure:

```text
Email Canvas
│
├── Preheader
├── Header
├── Hero
├── Metadata
├── Greeting
├── Introduction
├── Primary Content
├── Primary Action
├── Supporting Information
├── Closing
├── Signature
└── Footer
```

Not every template requires every section.

The order should remain consistent whenever possible.

---

# 1. Email Canvas

The Email Canvas is the outer background surrounding the main email container.

## Purpose

* separates the email from the email client interface
* creates visual consistency
* supports the Akademikerhilfe brand

## Recommended token

```text
surface-secondary
```

## Layout

The main email container should be centered within the canvas.

Recommended maximum width:

```text
660 px
```

---

# 2. Preheader

The preheader is the short text displayed next to or below the subject line in many email clients.

## Purpose

* provides additional context
* supports the subject line
* improves scanability in the inbox

## Example

```text
Please accept your housing offer by 15 June 2026.
```

## Guidelines

The preheader should

* complement the subject line
* remain concise
* avoid repeating the subject verbatim
* describe the main purpose or required action

The preheader may be visually hidden inside the email body if required.

---

# 3. Header

The Header establishes brand recognition.

## Typical content

* Akademikerhilfe logo
* optional department label
* optional visual accent

## Background

Recommended token:

```text
brand-primary
```

## Guidelines

The Header should

* remain visually consistent across all templates
* contain only approved brand assets
* avoid unnecessary navigation
* not compete with the email content

The logo should appear once per email.

---

# 4. Hero

The Hero communicates the primary purpose of the email.

## Typical content

* one H1
* optional short supporting line
* optional accent element

## Examples

```text
Your Housing Offer
```

```text
Welcome to Akademikerhilfe
```

```text
SEPA Pre-Notification
```

## Guidelines

Each email should contain only one Hero and one H1.

The H1 should use the defined display typography.

The Hero should remain concise.

---

# 5. Metadata

Metadata provides technical or administrative reference information.

## Examples

* AH-Code
* contract number
* object code
* booking reference
* invoice number

## Guidelines

Metadata should

* appear near the beginning of the email
* remain visually secondary
* use the standard body font
* not interrupt the primary message

Metadata should only be included when it provides value to the recipient or internal support teams.

---

# 6. Greeting

The greeting addresses the recipient directly.

## German

```text
{ANREDE},
```

## English

```text
{ANREDE_ENGL},
```

## Guidelines

Use the formal form of address for external communication.

The greeting should be followed by a clear introductory sentence.

---

# 7. Introduction

The Introduction explains why the email was sent.

## Purpose

The recipient should understand the email after reading the first paragraph.

## Example

```text
We are pleased to offer you a residence place at {HEIM_ADRESSE} starting from {DATE}.
```

## Guidelines

The Introduction should

* remain concise
* focus on the primary message
* avoid background information
* use active and service-oriented language

---

# 8. Primary Content

The Primary Content contains the information required to understand the message.

## Possible content

* offer details
* payment details
* reservation information
* contract information
* move-in instructions
* deadlines
* tables
* attachments

## Guidelines

Primary Content should be divided into clearly labeled sections.

Use section headings where they improve orientation.

Avoid large uninterrupted text blocks.

---

# 9. Primary Action

The Primary Action is the most important action the recipient should complete.

## Examples

* accept an offer
* open the online portal
* make a payment
* upload a document
* confirm an appointment

## Typical component

```text
AH Primary Button
```

## Guidelines

Each email should contain one clearly identifiable primary action.

The button text should describe the action directly.

Good:

```text
Accept Offer in Online Portal
```

Avoid:

```text
Click Here
```

If no action is required, the email should clearly state this.

---

# 10. Supporting Information

Supporting Information provides context that is useful but not part of the primary action.

## Examples

* waiting list information
* alternative payment options
* early move-in information
* legal information
* exceptions
* additional contacts

## Guidelines

Supporting Information should appear after the primary message and primary action.

It may use

* section headings
* dividers
* information cards
* tables
* feature panels

Supporting content should not compete with the primary action.

---

# 11. Closing

The Closing confirms the next step or offers support.

## Examples

```text
If you have any questions, we will be happy to help.
```

```text
We look forward to welcoming you soon.
```

## Guidelines

The Closing should

* remain brief
* provide reassurance
* avoid introducing new information
* clearly indicate whether the recipient needs to take further action

---

# 12. Signature

The Signature identifies the responsible team.

## Typical content

* team name
* department
* phone number
* email address
* organisation
* legal information where required

## Examples

```text
Team Studentservice
```

```text
Team Accounting
```

## Guidelines

The Signature should use an approved reusable component.

Personal names should only be included where the communication is sent by a specific employee.

Team-based transactional communication should use the responsible team name.

---

# 13. Footer

The Footer contains global information shared across templates.

## Typical content

* Akademikerhilfe address
* website
* legal registration information
* social media links
* object or template reference

## Guidelines

The Footer should

* remain consistent across templates
* use approved links
* remain visually secondary
* avoid repeating content already included in the Signature

Social icons should only appear in the Footer.

---

# Optional Sections

Some templates may require additional sections.

---

## Language Separator

Bilingual emails may contain both German and English versions.

Recommended structure:

```text
German Version
│
├── German Content
├── German Signature
│
└── Language Separator

English Version
│
├── English Content
└── English Signature
```

The English section should be clearly labeled.

A visual divider should separate both language versions.

---

## Attachment Information

When attachments are included, the email should explain

* what is attached
* why it is attached
* what the recipient should do with it

Attachment information should appear near the Introduction or Primary Action.

---

## Legal Notice

Legal notices should be placed after the primary content.

They should not interrupt the main user journey unless legally required.

---

## House-Specific Information

Residence-specific content should be inserted through dedicated placeholders or data fields.

House-specific content should not require duplication of the full email structure.

Preferred approach:

```text
Master Template
+
House-Specific Content
+
Language Variant
```

This principle is essential because many Akademikerhilfe templates contain multiple residence-specific variants.

---

# Content Priority

Information should be ordered by importance.

Recommended priority:

1. Primary message
2. Required action
3. Deadline
4. Important details
5. Supporting information
6. Exceptions
7. Legal information
8. Contact information

Do not place legal or technical information before the primary message unless required.

---

# Primary and Secondary Actions

## Primary Action

The main action required from the recipient.

Examples:

* Accept offer
* Complete payment
* Open portal

## Secondary Action

An optional alternative.

Examples:

* Contact Studentservice
* Join waiting list
* Download information

Secondary actions should be visually less prominent than the primary action.

---

# Bilingual Architecture

Where German and English are included in one email, both versions should follow the same information hierarchy.

The English version should not be a structurally different email.

Recommended order:

```text
German Header and Content
English Version Separator
English Content
Shared Footer
```

Alternatively, separate templates may be used if supported by the sending system.

Separate language templates are preferred where technically possible.

---

# Template Variants

The architecture supports three levels of variation.

## Master Template

Defines

* layout
* shared components
* content order
* responsive behavior

## Language Variant

Defines

* German or English content
* localized dates
* localized currency formats
* localized call-to-action labels

## Residence Variant

Defines

* residence-specific contact details
* house-specific information
* house-specific attachments
* local instructions

Residence variants should not duplicate shared HTML unnecessarily.

---

# Responsive Architecture

On smaller screens

* content must remain in the same logical order
* tables may stack where required
* primary actions should remain easy to tap
* padding may be reduced
* headings may scale down
* no content should require horizontal scrolling

The desktop and mobile versions should communicate the same hierarchy.

---

# Accessibility Requirements

The architecture should support

* one logical H1
* meaningful section headings
* descriptive links
* readable content order
* screen-reader-friendly navigation
* clear calls to action

The email should remain understandable when images are disabled.

---

# Component Mapping

| Architecture Section   | Recommended Component |
| ---------------------- | --------------------- |
| Header                 | `AH Header`           |
| Hero                   | `AH Hero`             |
| Metadata               | `AH Metadata`         |
| Section Heading        | `AH Section Heading`  |
| Primary Action         | `AH Primary Button`   |
| Supporting Information | `AH Info Card`        |
| Important Information  | `AH Feature Panel`    |
| Structured Data        | `AH Data Table`       |
| Signature              | `AH Signature`        |
| Footer                 | `AH Footer`           |

---

# Architecture Tokens

| Token                         | Value               |
| ----------------------------- | ------------------- |
| `architecture-canvas`         | `surface-secondary` |
| `architecture-container`      | `surface-primary`   |
| `architecture-max-width`      | `660 px`            |
| `architecture-header`         | `brand-primary`     |
| `architecture-primary-action` | One per email       |
| `architecture-h1-count`       | One per email       |
| `architecture-alignment`      | Left                |
| `architecture-content-order`  | Logical and linear  |

---

# Best Practices

✔ Communicate the primary message immediately.

✔ Place the primary action near the relevant information.

✔ Use one clear H1.

✔ Use section headings for long emails.

✔ Keep optional information visually secondary.

✔ Reuse shared components.

✔ Separate house-specific content from the master structure.

✔ Keep German and English versions structurally consistent.

---

# Avoid

✘ Starting with legal or technical information.

✘ Using multiple primary actions.

✘ Repeating the same information in several sections.

✘ Creating separate HTML structures for every residence.

✘ Placing essential information only inside images.

✘ Using different architectures for similar communication types.

✘ Adding sections without a clear communication purpose.

---

# Definition of a Complete Email

A transactional email is structurally complete when the recipient can clearly answer:

> Why did I receive this email?

> What do I need to know?

> What do I need to do?

> When do I need to do it?

> What happens next?

> Who can help me?

---

# Guiding Principle

Email architecture should guide the recipient from information to action without unnecessary friction.

The structure should feel predictable, even when the content changes.

---

## Related Documentation

* [Design Philosophy](../01_getting-started/philosophy.md)
* [Writing Guidelines](writing-guidelines.md)
* [Layout](layout.md)
* [Spacing](spacing.md)
* [Accessibility](accessibility.md)
* [Typography](typography.md)
