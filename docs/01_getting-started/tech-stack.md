# Technology Stack

This document describes the technologies, tools and development environment used for the Akademikerhilfe Email Design System.

The objective is to keep the technology stack simple, maintainable and compatible with common email clients.

---

# Philosophy

The Email Design System prioritizes compatibility over complexity.

Transactional emails must render reliably across a wide range of desktop, web and mobile email clients.

Whenever possible, proven technologies should be preferred over modern features with limited email client support.

---

# Current Technology Stack

## Version Control

Git

Used for version control and change tracking.

---

## Repository Hosting

GitHub

The project repository, documentation and release history are maintained on GitHub.

---

## Development Environment

Visual Studio Code

Visual Studio Code is the primary development environment.

Recommended extensions are documented separately.

---

## Markup Language

HTML5

Email templates are written in HTML.

Modern HTML should be used where supported while maintaining compatibility with email clients.

---

## Styling

Inline CSS

Because many email clients have limited CSS support, styles should primarily be written as inline CSS.

Reusable styles should be documented but not relied upon unless supported by target clients.

---

## Images

PNG

Preferred format for

- logos
- icons
- illustrations

SVG may be used internally but should not be embedded directly in production emails due to limited client support.

---

## Fonts

Primary fonts

- Erstoria
- Brandon Text

Fallback fonts

- Cormorant Garamond
- Lato
- Arial
- Georgia
- sans-serif
- serif

---

# Email Client Support

Templates should be tested for compatibility with

## Desktop

- Microsoft Outlook (Windows)
- Apple Mail

---

## Web

- Outlook Web
- Gmail
- Microsoft 365
- Yahoo Mail

---

## Mobile

- Apple Mail (iOS)
- Gmail (Android)
- Outlook Mobile

---

# Responsive Design

Templates follow a mobile-first approach where technically feasible.

Recommended maximum width

660 px

Media queries should be used carefully to maintain compatibility.

---

# Development Workflow

Typical workflow

```
GitHub

↓

Visual Studio Code

↓

HTML Development

↓

Testing

↓

Review

↓

Production
```

---

# Documentation

Documentation is written in Markdown.

Markdown files are stored inside the `/docs` directory.

---

# File Naming

Documentation

English

Example

```
colors.md

typography.md

layout.md
```

---

Templates

German template names

Example

```
angebot_de.html

angebot_en.html

sepa-vorabinformation_de.html
```

---

# Future Technologies

The following technologies may be evaluated in future versions.

## MJML

Evaluation planned.

MJML could simplify responsive email development while maintaining compatibility.

---

## Automated Email Testing

Potential tools

- Litmus
- Email on Acid

---

## HTML Validation

Automated HTML validation may be introduced as part of the build process.

---

## CI/CD

Future versions may include automated

- validation
- testing
- deployment

using GitHub Actions.

---

# Not in Scope

The Email Design System currently does not include

- marketing newsletters
- CRM campaigns
- landing pages
- website components

The focus remains on transactional email communication.

---

# Guiding Principle

Choose the simplest technology that reliably works across supported email clients.

Compatibility is always more important than technical elegance.