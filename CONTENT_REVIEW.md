# Editorial and reading revision — 2.0

The eight-subject structure remains intact. The library now contains **470 questions**, including two added discussions on **Mu'tah** and **the incident of Ifk**. All 468 previous learning IDs still identify the same question, so existing study records remain meaningful.

## Content improvements

52 existing answers received focused explanatory or language edits. This is a targeted revision, not a claim that every existing answer was rewritten or every referenced book read in full.

- Replaced abstract explanations with concrete examples where useful: salam sales, textual implications, qualifications of hadith narrations and thematic tafsir.
- Completed the eight recognized methods of receiving hadith, and supplied representative examples of hadith collection types.
- Named representative authors and works when the answer previously referred only generally to a school or method.
- Explained technical expressions in ordinary academic Urdu, including the logical use of “natiq,” acquisition of an act, and the four levels of irtifaqat.
- Split the long presentation of the five legal maxims into manageable sentences and attached practical examples.
- Clarified wording in the comparison of Christian atonement models and the historical identification of South Asian Muslim schools.
- Added specific examples to tafsir, Qur'anic recitation and Seerah discussions without turning disputed reports into certain claims.
- Replaced several instructions about “a good interview answer” with direct explanation of the subject itself.
- Retained distinctions between established evidence, scholarly interpretation and contemporary application.

## Typography

- Bundled **Jameel Noori Nastaleeq** is the default for Urdu prose and interface text.
- Arabic quotations are explicitly annotated with exact spans, rendered in **Amiri Bold**, and given a distinct high-contrast colour and light background.
- Arabic passages are dark navy in light mode and pale blue in dark mode; Urdu reading text is white in dark mode.
- Type sizes and line spacing have been adjusted for Jameel rather than reusing the previous Noto metrics.
- All fonts load locally. Font attribution and notices are in `dist/assets/fonts/`.

## Usability

- The chapter list can be opened in a labelled dialog on smaller screens, without scrolling past the full answer.
- Added a return-to-top button for long reading pages.
- Kept bookmarks, notes, review records and progress attached to stable learning IDs.
- Keyboard navigation, search, settings and the interview practice flow remain available.

## Verification

The validation script checks all 470 question IDs, the correspondence between source JSON and browser content, Arabic span matching, and required assets. Browser checks cover font rendering, quotation styling and primary reading controls. The two newly added Seerah discussions include direct references to relevant authentic hadith reports; the educational content remains an academic study aid rather than an independently issued fatwa.
