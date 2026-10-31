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

## Revision 3: contextual evidence and reading layout

29 answers across all eight subjects now contain additional Arabic evidence or a classical definition, an original Urdu translation, a source citation and an explanation of its relevance. Quotations are identified as excerpts where applicable. The selected Qur'anic passages were checked against Quran.com, the hadith against their cited Bukhari/Muslim records on Sunnah.com, and the fiqh definition against the cited passage of al-Ibhaj on Shamela. These checks concern the new passages, rather than certifying every interpretation or bibliographic item in the entire collection.

12 further answers received worked examples. Hypothetical hadith transmission examples are explicitly identified as such, rather than presented as historical reports. The question-level revision list is in CONTENT_ENRICHMENT.json.

The reader header and metadata are more compact. Previous/next navigation appears immediately after the final answer paragraph, before references and study controls. Arabic quotations retain Amiri Bold and their distinct colour; Urdu remains Jameel Noori Nastaleeq. Highlighting respects complete Unicode words and combining marks, preventing inserted tags from splitting Urdu ligatures. Whole-word wrapping replaces arbitrary character wrapping in reading text.

Regression checks exercise the actual text renderer, word-boundary cases, Arabic annotation and answer-end navigation. All 470 IDs and original question identities are retained. Responsive CSS includes narrow-phone layouts; browser-based visual verification was unavailable during this revision, so device-wide rendering is not certified.
