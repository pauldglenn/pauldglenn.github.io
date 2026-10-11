Title: Household Agent Privacy Policy
Date: 2026-10-10
Slug: household-agent-privacy
URL: household-agent/privacy/
Save_as: household-agent/privacy/index.html
Status: hidden

Effective date: October 10, 2026.

This policy describes the private Household Agent application operated by Paul Glenn. It applies to the assistant's Google account integration, not to unrelated projects or articles on pdglenn.com. [About Household Agent](/household-agent/).

## Information accessed

With the account owner's authorization, Household Agent accesses basic Google account identity, including email address, and Gmail data needed for searching, reading, and summarizing messages. This may include message identifiers, senders, recipients, subjects, timestamps, labels, snippets, and message bodies. The current connector exposes message search and reading, not attachment downloads.

The application requests `gmail.readonly` and basic email/OpenID identity permissions. It does not request permission to send email, delete messages, change labels or read status, modify mailbox settings, or access Google Calendar or Drive.

Google provides OAuth credentials so the application can maintain authorized access. The application does not request or store your Google password.

## Purpose and processing

Gmail data is used to provide the authorized user's requested personal-assistant features, such as finding messages and answering questions or producing summaries. Email contents are treated as untrusted input, not authorization to perform actions.

When you request an AI response using Gmail, relevant email information and conversation context may be sent to OpenAI, the application's AI service provider, to generate that response. Google provides the mailbox API; DigitalOcean hosts the private application; Tailscale provides private network access. These providers process information under their applicable service terms and privacy policies. This application does not promise that data remains exclusively on its server.

Household Agent does not sell Gmail data, use it for advertising, or distribute it to data brokers. The operator does not use Gmail data to build or train generalized AI models. Provider-side handling is governed by the applicable provider settings and terms; no separate guarantee about provider retention or training is made here.

Human access to another authorized user's Gmail data is limited to that user's affirmative permission for specific data, necessary security investigation, or legal obligations. The application is currently for the operator's personal use; adding another user requires separate authorization.

## Storage and security

OAuth credentials are stored in an encrypted connector keyring on the private application server. Gmail content, tool results, and generated summaries may remain in conversation history, application state, diagnostic logs, or backups. There is currently no automatic retention or deletion schedule; retained application data remains until the operator removes it.

The dashboard and administration are restricted to the private network and authenticated access. Credentials are kept outside the assistant's permitted file workspace. The current connector is restricted to read-only Gmail tools, and general shell execution is disabled. These safeguards reduce risk but do not guarantee absolute security.

This public information website does not receive Gmail contents or OAuth tokens. Its hosting and embedded theme resources may receive ordinary website request information, such as IP addresses, independently of the private assistant.

## Revocation and deletion

You can stop future Gmail access by removing Household Agent's connection in [Google Account third-party connections](https://myaccount.google.com/connections). Revocation does not delete your Gmail messages and does not automatically erase information already retained in assistant history or backups.

To request removal of stored connector credentials, Gmail-derived conversations, summaries, logs, or operator-controlled backups, contact [paul.glenn@gmail.com](mailto:paul.glenn@gmail.com). The operator will identify and remove the requested data from systems under their control, subject to necessary legal or security retention. Copies retained independently by service providers are subject to those providers' policies and deletion procedures.

## Google API data commitments

Household Agent's use and transfer of information received from Google APIs will adhere to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including its Limited Use requirements. Data use is limited to the disclosed user-facing assistant features; transfers require the user's consent or another exception permitted by that policy.

## Changes and contact

This policy will be updated if data handling changes. New uses of Google data or additional permissions require notice and renewed consent before those uses begin.

Operator: Paul Glenn. Questions or requests: [paul.glenn@gmail.com](mailto:paul.glenn@gmail.com).
