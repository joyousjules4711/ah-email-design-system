# Placeholder Reference

> **Applies to**
>
> * All transactional email templates
> * German and English versions
> * Residence-specific variants
> * Template development and review

---

# Purpose

This document defines the placeholders available within the Akademikerhilfe email template system.

Placeholders are provided by the source system and replaced with live data when an email is generated.

Placeholder names must not be changed unless the source system configuration is updated accordingly.

---

# General Rules

* Always use the exact placeholder name.
* Placeholder names are case-sensitive unless explicitly confirmed otherwise.
* Do not translate placeholder names.
* Do not invent new placeholders inside production templates.
* German and English aliases may point to the same underlying property.
* Placeholders must be tested with real or representative data before release.
* Personal and financial data must be handled according to applicable data protection requirements.

---

# Placeholder Syntax

Placeholders are inserted using curly brackets.

Example:

```text
{STUDENT_EMAIL}
```

The corresponding XML definition uses the placeholder name without curly brackets:

```xml
<placeholder
  Name="STUDENT_EMAIL"
  Type="Person"
  Property="Email"
/>
```

---

# Data Categories

The available placeholders are grouped by data source.

---

# Multilanguage and Shared Placeholders

| Placeholder       | Type            | Property               | Description                |
| ----------------- | --------------- | ---------------------- | -------------------------- |
| `{STUDENT_EMAIL}` | `Person`        | `Email`                | Student email address      |
| `{ROOM_CATEGORY}` | `RoomsCategory` | `Code`                 | Room category code         |
| `{ITEM_CATEGORY}` | `RoomsCategory` | `Code`                 | Item or room category code |
| `{KUNDENDATEN}`   | `Person`        | `PersonCustomerNumber` | Customer number            |
| `{PERSON_ID}`     | `Person`        | `ID`                   | Internal person ID         |

---

# Student Data — English

| Placeholder               | Type     | Property                | Description                              |
| ------------------------- | -------- | ----------------------- | ---------------------------------------- |
| `{STUDENT_FULL_NAME}`     | `Person` | `FullName`              | Full student name                        |
| `{STUDENT_FIRST_NAME}`    | `Person` | `FirstName`             | Student first name                       |
| `{StudentFirstName}`      | `Person` | `FirstName`             | Alternate student first name placeholder |
| `{StudentLastName}`       | `Person` | `LastName`              | Alternate student last name placeholder  |
| `{STUDENT_LAST_NAME}`     | `Person` | `LastName`              | Student last name                        |
| `{FIRSTCANCELLATIONDATE}` | `Person` | `FirstCancellationDate` | First possible cancellation date         |

---

# Person Login Data

| Placeholder           | Type          | Property      | Description                    |
| --------------------- | ------------- | ------------- | ------------------------------ |
| `{PERSON_LOGIN}`      | `PersonLogin` | `Login`       | Person login name              |
| `{PERSON_FULL_NAME}`  | `PersonLogin` | `FullName`    | Full name of logged-in person  |
| `{PERSON_FIRST_NAME}` | `PersonLogin` | `FirstName`   | First name of logged-in person |
| `{PERSON_LAST_NAME}`  | `PersonLogin` | `LastName`    | Last name of logged-in person  |
| `{PERSON_PHONE}`      | `PersonLogin` | `PhoneNumber` | Phone number                   |
| `{PERSON_EMAIL}`      | `PersonLogin` | `Email`       | Email address                  |

---

# Security User Data

| Placeholder         | Type           | Property    | Description               |
| ------------------- | -------------- | ----------- | ------------------------- |
| `{USER_LOGIN}`      | `SecurityUser` | `Login`     | System user login         |
| `{USER_FULL_NAME}`  | `SecurityUser` | `FullName`  | Full name of system user  |
| `{USER_FIRST_NAME}` | `SecurityUser` | `FirstName` | First name of system user |
| `{USER_LAST_NAME}`  | `SecurityUser` | `LastName`  | Last name of system user  |
| `{USER_PHONE}`      | `SecurityUser` | `Phone`     | System user phone number  |
| `{USER_EMAIL}`      | `SecurityUser` | `Email`     | System user email address |

---

# Debt Data — English

| Placeholder        | Type   | Property    | Description     |
| ------------------ | ------ | ----------- | --------------- |
| `{DEBT_NAME}`      | `Debt` | `Name`      | Debt name       |
| `{DEBT_NUMBER}`    | `Debt` | `Number`    | Debt number     |
| `{DEBT_ISSUEDATE}` | `Debt` | `IssueDate` | Debt issue date |
| `{DEBT_COST}`      | `Debt` | `Cost`      | Debt amount     |

---

# Contract Data — English

| Placeholder                       | Type        | Property        | Description                         |
| --------------------------------- | ----------- | --------------- | ----------------------------------- |
| `{CONTRACT_START_DATE}`           | `Contract`  | `StartDate`     | Contract start date                 |
| `{CONTRACT_END_DATE}`             | `Contract`  | `EndDate`       | Contract end date                   |
| `{CONTRACT_NAME}`                 | `Contract`  | `Name`          | Contract name                       |
| `{ContractName}`                  | `Contract`  | `Name`          | Alternate contract name placeholder |
| `{ContractStartDate}`             | `Residence` | `ContractStart` | Residence contract start            |
| `{ContractEndDate}`               | `Residence` | `ContractEnd`   | Residence contract end              |
| `{RESIDENCE_CONTRACT_START_DATE}` | `Residence` | `ContractStart` | Residence contract start date       |
| `{RESIDENCE_CONTRACT_END_DATE}`   | `Residence` | `ContractEnd`   | Residence contract end date         |

---

# Student Bank Account

| Placeholder                               | Type                   | Property              | Description                          |
| ----------------------------------------- | ---------------------- | --------------------- | ------------------------------------ |
| `{BANKACCOUNT_BANK_ROUTING_NUMBER}`       | `Account`              | `BankRoutingNumber`   | Bank routing number                  |
| `{BANKKONTO_BANKLEITZAHL}`                | `Account`              | `BankRoutingNumber`   | German alias                         |
| `{BANKACCOUNT_IBAN}`                      | `Account`              | `BankSwiftIban`       | Full IBAN                            |
| `{BANKKONTO_IBAN}`                        | `Account`              | `BankSwiftIban`       | German alias                         |
| `{BANKACCOUNT_IBAN_MASKED}`               | `Account`              | `BankSwiftIbanMasked` | Masked IBAN                          |
| `{BANKKONTO_IBAN_MASKED}`                 | `Account`              | `BankSwiftIbanMasked` | German alias                         |
| `{BANKACCOUNT_BIC}`                       | `Account`              | `BankSwiftBic`        | BIC                                  |
| `{BANKKONTO_BIC}`                         | `Account`              | `BankSwiftBic`        | German alias                         |
| `{BANKACCOUNT_BIC_MASKED}`                | `Account`              | `BankSwiftBicMasked`  | Masked BIC                           |
| `{BANKKONTO_BIC_MASKED}`                  | `Account`              | `BankSwiftBic`        | German alias as currently configured |
| `{BANKACCOUNT_NUMBER}`                    | `Account`              | `AccountNumber`       | Account number                       |
| `{BANKKONTO_KONTONUMMER}`                 | `Account`              | `AccountNumber`       | German alias                         |
| `{BANKACCOUNT_BANKNAME}`                  | `Account`              | `BankName`            | Bank name                            |
| `{BANKKONTO_BANKNAME}`                    | `Account`              | `BankName`            | German alias                         |
| `{BANKACCOUNT_ACCOUNT_HOLDER}`            | `Account`              | `FullName`            | Account holder full name             |
| `{BANKKONTO_KONTOINHABER}`                | `Account`              | `AccountHolder`       | German account holder                |
| `{BANKACCOUNT_ACCOUNT_HOLDER_FIRSTNAME}`  | `Account`              | `FirstName`           | Account holder first name            |
| `{BANKKONTO_KONTOINHABER_VORNAME}`        | `Account`              | `FirstName`           | German alias                         |
| `{BANKACCOUNT_ACCOUNT_HOLDER_LASTNAME}`   | `Account`              | `LastName`            | Account holder last name             |
| `{BANKKONTO_KONTOINHABER_NACHNAME}`       | `Account`              | `LastName`            | German alias                         |
| `{BANKACCOUNT_ACCOUNT_HOLDER_PHONE}`      | `Account`              | `Phone`               | Account holder phone                 |
| `{BANKKONTO_KONTOINHABER_TELEFON}`        | `Account`              | `Phone`               | German alias                         |
| `{BANKACCOUNT_ACCOUNT_HOLDER_EMAIL}`      | `Account`              | `Email`               | Account holder email                 |
| `{BANKKONTO_KONTOINHABER_EMAIL}`          | `Account`              | `Email`               | German alias                         |
| `{BANKACCOUNT_MANDATE_REFERENCE}`         | `AccountAuthorization` | `MandateReference`    | SEPA mandate reference               |
| `{BANKKONTO_MANDATSREFERENZ}`             | `AccountAuthorization` | `MandateReference`    | German alias                         |
| `{BANKACCOUNT_MANDATE_AUTHORIZATIONDATE}` | `AccountAuthorization` | `AuthorizationDate`   | Mandate authorization date           |
| `{BANKKONTO_MANDATDATUM}`                 | `AccountAuthorization` | `AuthorizationDate`   | German alias                         |

---

# Akademikerhilfe Recipient Account

| Placeholder              | Type             | Property             | Description                    |
| ------------------------ | ---------------- | -------------------- | ------------------------------ |
| `{RECIPIENT_IBAN}`       | `BookingAccount` | `BankSWIFTIBAN`      | Akademikerhilfe recipient IBAN |
| `{EMPFÄNGER_IBAN}`       | `BookingAccount` | `BankSWIFTIBAN`      | German alias                   |
| `{RECIPIENT_BIC}`        | `BookingAccount` | `BankSWIFTBIC`       | Akademikerhilfe recipient BIC  |
| `{EMPFÄNGER_BIC}`        | `BookingAccount` | `BankSWIFTBIC`       | German alias                   |
| `{RECIPIENT_BANK}`       | `BookingAccount` | `AccountHoldingBank` | Recipient bank                 |
| `{EMPFÄNGER_BANK}`       | `BookingAccount` | `AccountHoldingBank` | German alias                   |
| `{RECIPIENT_CREDITORID}` | `LegalEntity`    | `CreditorID`         | Creditor ID                    |
| `{EMPFÄNGER_CREDITORID}` | `LegalEntity`    | `CreditorID`         | German alias                   |
| `{RECIPIENT_NAME}`       | `LegalEntity`    | `Name`               | Legal entity name              |
| `{EMPFÄNGER_NAME}`       | `LegalEntity`    | `Name`               | German alias                   |
| `{RECIPIENT_ADDRESS}`    | `LegalEntity`    | `Address`            | Legal entity address           |
| `{EMPFÄNGER_ADRESSE}`    | `LegalEntity`    | `Address`            | German alias                   |

---

# Student Data — German

| Placeholder                    | Type     | Property                | Description             |
| ------------------------------ | -------- | ----------------------- | ----------------------- |
| `{STUDENT_VOLLSTÄNDIGER_NAME}` | `Person` | `FullName`              | Full student name       |
| `{STUDENT_VORNAME}`            | `Person` | `FirstName`             | Student first name      |
| `{STUDENT_NACHNAME}`           | `Person` | `LastName`              | Student last name       |
| `{KÜNDIGUNGSTERMIN}`           | `Person` | `FirstCancellationDate` | First cancellation date |

---

# Security User Data — German

| Placeholder                     | Type           | Property    | Description            |
| ------------------------------- | -------------- | ----------- | ---------------------- |
| `{BENUTZER_LOGIN}`              | `SecurityUser` | `Login`     | System user login      |
| `{BENUTZER_VOLLSTÄNDIGER_NAME}` | `SecurityUser` | `FullName`  | Full system user name  |
| `{BENUTZER_VORNAME}`            | `SecurityUser` | `FirstName` | System user first name |
| `{BENUTZER_NACHNAME}`           | `SecurityUser` | `LastName`  | System user last name  |
| `{BENUTZER_TELEFON}`            | `SecurityUser` | `Phone`     | System user phone      |
| `{BENUTZER_EMAIL}`              | `SecurityUser` | `Email`     | System user email      |

---

# Debt Data — German

| Placeholder                     | Type   | Property    | Description     |
| ------------------------------- | ------ | ----------- | --------------- |
| `{FORDERUNGSNAME}`              | `Debt` | `Name`      | Debt name       |
| `{FORDERUNGSNUMMER}`            | `Debt` | `Number`    | Debt number     |
| `{DATUM_FORDERUNGSAUSSTELLUNG}` | `Debt` | `IssueDate` | Debt issue date |
| `{FORDERUNGSBETRAG}`            | `Debt` | `Cost`      | Debt amount     |

---

# Contract Data — German

| Placeholder                         | Type        | Property        | Description                   |
| ----------------------------------- | ----------- | --------------- | ----------------------------- |
| `{DATUM_VERTRAGSBEGINN}`            | `Contract`  | `StartDate`     | Contract start date           |
| `{DATUM_VERTRAGSENDE}`              | `Contract`  | `EndDate`       | Contract end date             |
| `{VERTRAGSBEZEICHNUNG}`             | `Contract`  | `Name`          | Contract name                 |
| `{AUFENTHALT_DATUM_VERTRAGSBEGINN}` | `Residence` | `ContractStart` | Residence contract start date |
| `{AUFENTHALT_DATUM_VERTRAGSENDE}`   | `Residence` | `ContractEnd`   | Residence contract end date   |

---

# Deficiency Data

| Placeholder                  | Type         | Property      | Description                           |
| ---------------------------- | ------------ | ------------- | ------------------------------------- |
| `{DEFICIENCY_SUBJECT}`       | `Deficiency` | `Title`       | Deficiency subject                    |
| `{DEFICIENCY_DESCRIPTION}`   | `Deficiency` | `Description` | Deficiency description                |
| `{DEFICIENCY_STATUS}`        | `Deficiency` | `Status`      | Internal deficiency status            |
| `{DEFICIENCY_PORTAL_STATUS}` | `Deficiency` | `PotalStatus` | Portal status as currently configured |
| `{DEFICIENCY_HOSTEL}`        | `Deficiency` | `Hostel`      | Residence                             |
| `{DEFICIENCY_ROOM}`          | `Deficiency` | `Room`        | Room                                  |
| `{DEFICIENCY_CHAMBER}`       | `Deficiency` | `Chamber`     | Chamber or unit                       |

---

# Appointment Data

| Placeholder              | Type          | Property   | Description          |
| ------------------------ | ------------- | ---------- | -------------------- |
| `{APPOINTMENT_TYPE}`     | `Appointment` | `Type`     | Appointment type     |
| `{APPOINTMENT_DATE}`     | `Appointment` | `Date`     | Appointment date     |
| `{APPOINTMENT_Time}`     | `Appointment` | `Time`     | Appointment time     |
| `{APPOINTMENT_LOCATION}` | `Appointment` | `Location` | Appointment location |
| `{APPOINTMENT_LINK}`     | `Appointment` | `Link`     | Appointment link     |

---

# Known Aliases

Some placeholders refer to the same source property.

Examples:

| Preferred Context          | Placeholder                       | Alias                 |
| -------------------------- | --------------------------------- | --------------------- |
| English student first name | `{STUDENT_FIRST_NAME}`            | `{StudentFirstName}`  |
| English student last name  | `{STUDENT_LAST_NAME}`             | `{StudentLastName}`   |
| English contract name      | `{CONTRACT_NAME}`                 | `{ContractName}`      |
| Residence contract start   | `{RESIDENCE_CONTRACT_START_DATE}` | `{ContractStartDate}` |
| Residence contract end     | `{RESIDENCE_CONTRACT_END_DATE}`   | `{ContractEndDate}`   |

Do not replace existing aliases automatically.

Use the placeholder already supported by the relevant source template unless a migration decision has been documented.

---

# Data Sensitivity

The following categories contain personal or financial data:

* person names
* email addresses
* phone numbers
* login data
* customer numbers
* person IDs
* account details
* mandate details
* contract data
* debt data

These placeholders must not be used in public examples or screenshots without anonymization.

---

# Formatting Responsibilities

The source system may provide raw values.

Templates must define the required display format where necessary.

Examples include:

* date format
* currency format
* line breaks
* masked account details
* translated labels

The placeholder itself must not contain additional formatting instructions unless supported by the source system.

---

# HTML Escaping

Dynamic content must be safely escaped by the source system.

Special attention is required for:

* names
* addresses
* descriptions
* deficiency text
* appointment locations
* user-generated content

Templates must not assume that placeholder content is safe HTML.

---

# Known Configuration Questions

The following entries should be verified with the source system owner:

1. `{BANKKONTO_BIC_MASKED}` currently maps to `BankSwiftBic` rather than `BankSwiftBicMasked`.
2. `{DEFICIENCY_PORTAL_STATUS}` maps to `PotalStatus`, which may be a source-system spelling.
3. `{APPOINTMENT_Time}` uses mixed capitalization.
4. `{BANKACCOUNT_ACCOUNT_HOLDER}` and `{BANKKONTO_KONTOINHABER}` map to different properties.
5. Multiple English aliases exist for student and contract names.

Do not correct these names inside templates without confirming system behavior.

---

# Best Practices

✔ Use exact placeholder names.

✔ Use placeholders only in the appropriate context.

✔ Preserve existing aliases until migration is approved.

✔ Anonymize placeholders in documentation screenshots.

✔ Document new placeholders before use.

✔ Verify date and currency formatting.

✔ Test optional values and empty states.

---

# Avoid

✘ Renaming placeholders inside HTML.

✘ Translating placeholder names.

✘ Inventing undocumented placeholders.

✘ Exposing personal data in examples.

✘ Assuming optional values are always populated.

✘ Embedding placeholder values directly inside image URLs without validation.

---

# Guiding Principle

Placeholders are an interface contract between the source system and the email template.

Treat every placeholder name, type and property as production data infrastructure.

---

## Related Documentation

* [Technology Stack](../01_getting-started/tech-stack.md)
* [Email Architecture](../02_foundations/email-architecture.md)
* [Writing Guidelines](../02_foundations/writing-guidelines.md)
* [Outlook Compatibility](../02_foundations/outlook-compatibility.md)
* [Coding Guidelines](coding-guidelines.md)
