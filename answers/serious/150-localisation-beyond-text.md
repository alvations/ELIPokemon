---
id: "150"
slug: localisation-beyond-text
style: serious
category: translation
difficulty: intermediate
question: "What does localisation involve beyond translating the words?"
tags: [localisation, i18n, formats, rtl, collation, transcreation, pluralisation]
---

# Localisation is not translation

Translation converts text. **Localisation** adapts a product to a locale, and most of it is not
text at all. A system that translates perfectly and localises badly is broken in ways no MT metric
can see.

```
   WHAT AN MT METRIC SEES              WHAT THE USER SEES
   ──────────────────────              ──────────────────
                                       ┌──────────────────────────────┐
   the translated strings ─► COMET     │  03/04/2025   ← wrong month  │
                              98.2     │  1,234.56     ← wrong marks  │
                                       │  [Zapisz w tym momenc…]      │  ← truncated
   everything below is invisible       │  ← back button on the wrong  │
   to every metric in question 129:    │    side for an RTL locale    │
     dates numbers currency units      │  ▯▯▯▯  ← font lacks the      │
     plurals name order sorting        │          script             │
     layout mirroring fonts            │  "1 items"  ← plural rule    │
     text baked into images            └──────────────────────────────┘
     colour and symbol meaning
                                       the translation was fine.
                                       the product is broken.
```

## The formats

| What | The trap |
| --- | --- |
| **Dates** | `03/04/2025` is March 4th or April 3rd depending on the reader. Never render dates as digits with separators; use the locale's format |
| **Numbers** | decimal comma vs point; digit grouping by 3, or by 2 then 3 (Indian lakh/crore); different digit glyphs entirely (Arabic-Indic) |
| **Currency** | symbol position, spacing, decimal places (some currencies have none), and **you cannot convert amounts** — a price is a business decision |
| **Units** | metric/imperial, but also paper sizes, clothing sizes, temperature |
| **Names** | given/family order, multiple surnames, patronymics, single-name people. A `firstName`/`lastName` schema is already a bug |
| **Addresses** | field order, postcode presence and format, states vs prefectures vs none |
| **Phone** | length, grouping, leading zeros that must not be stripped |
| **Calendars** | week start day, non-Gregorian calendars, which days are the weekend |

## Pluralisation is not two cases

English has singular and plural. Arabic has six plural categories; Russian and Polish have three or
four; Japanese and Chinese have one. Code written as `if (n == 1) ... else ...` cannot be localised
at all — it must be replaced, not translated. Use CLDR plural categories and let the locale decide
how many forms exist.

The same applies to **gender agreement in interpolated strings**: `"{name} liked your post"`
requires a gendered verb in many languages, and the data to choose it may not exist (question 142).

## Layout and script

* **RTL is a mirror, not a text direction.** Arabic and Hebrew interfaces flip the entire layout —
  navigation, icons with directional meaning, progress bars, back buttons. Bidirectional text
  (Arabic containing a Latin product name or a number) needs proper bidi handling, not string
  concatenation.
* **Expansion breaks layouts** (question 144). Design against the longest locale, not English.
* **Line breaking rules differ.** Thai, Japanese and Chinese do not use spaces (question 114);
  breaking mid-word is wrong in specific, language-defined ways.
* **Fonts.** A font without the target script renders as boxes. CJK needs different fonts for
  Japanese, Simplified and Traditional Chinese even where codepoints are shared — the same
  character has different correct shapes.
* **Sorting.** Alphabetical order is locale-defined: Swedish sorts `Ä` after `Z`, German does not;
  Chinese sorts by stroke or by pronunciation depending on convention. Never sort with a naive
  codepoint comparison and call it alphabetical.

## Content that must be recreated, not translated

* **Text baked into images.** It is invisible to your translation pipeline and will ship in English.
  Externalise it or accept a manual per-locale asset process.
* **Colour and symbol connotations.** White for mourning, red for luck or for danger, hand gestures
  that are obscene in some locales, animals with different associations.
* **Examples, names and scenarios** in documentation and onboarding.
* **Marketing copy** — transcreation, as in question 149.
* **Legal and regulatory text**, which is not a translation problem at all: the *requirements*
  differ per jurisdiction, so the content differs.

## Process notes

* **Externalise every string, with context.** A string catalogue where each entry carries a
  description, a screenshot and a character limit produces translations several grades better than
  a bare list (questions 133, 144).
* **Pseudo-localise early.** Replace strings with accented, expanded versions before you have any
  translations; it surfaces hardcoded strings, truncation and layout breakage in an afternoon.
* **Locale is not language.** `es-MX` and `es-ES`, `pt-BR` and `pt-PT`, `zh-Hans` and `zh-Hant`
  differ in vocabulary, formality and sometimes script. Ask which you are targeting before anyone
  translates anything.

## What an interviewer digs into next

* Why is `if (n == 1)` untranslatable rather than merely awkward?
* What does RTL support involve beyond text direction?
* Why can't currency amounts simply be converted?
* What is pseudo-localisation and what does it catch?
