# الحیات — علومِ اسلامیہ

An Urdu learning website for thoughtful study and university interview preparation.

**Prepared by Dr. Imran Hayat**  
Lecturer in Islamic Studies, University of Education, Lahore  
[drimranhayat.com](https://drimranhayat.com)

## Included content

All **470 questions and answers** from the eight supplied JSON files are included. The content has been editorially refined, with examples and source details added where useful. Existing learning IDs are preserved so earlier bookmarks, notes and progress still identify the same questions.

| Subject | Questions |
|---|---:|
| عقیدہ و ایمانیات | 42 |
| علومِ قرآن | 58 |
| تفسیر و اصولِ تفسیر | 64 |
| حدیث و علومِ حدیث | 50 |
| فقہ و اصولِ فقہ | 50 |
| سیرت و تاریخِ اسلام | 67 |
| اسلامی فکر و فلسفہ | 67 |
| ادیان و مکاتبِ فکر | 72 |

## Learning experience

- Responsive right-to-left layout with eight subject colours.
- Bundled Jameel Noori Nastaleeq for Urdu and Amiri Regular/Bold for Arabic quotations; no external font requests. Noto is retained only as a fallback.
- Full-text Urdu search across questions and answers, with subject filtering and Arabic/Urdu letter normalization.
- Chapter outlines, previous/next navigation and distraction-free reading.
- Adjustable type size,  light/dark modes and optional term emphasis.
- Bookmarks, private notes, confidence tracking, daily goals and study history.
- Interview practice: randomized 5/10/20-question sessions, answer reveal, optional 90-second timer and self-assessment.
- Review list using confidence-based intervals. A review mark schedules one day; successive confident marks schedule 3, 7, 14 and 30 days. The review list also includes questions explicitly marked for review immediately.
- JSON backup/export and validated import for moving personal progress between devices.
- Offline study after a successful first online load; source links need connectivity. Offline support requires HTTPS or localhost. Browser storage can be cleared by the user or the browser.
- No sign-in, analytics, external runtime libraries or database.

## Publish on GitHub Pages

1. Create a GitHub repository with **main** as its default branch.
2. Upload the **contents of this folder**, including `dist`, `scripts` and `.github/workflows/pages.yml`, to the repository root. Do not upload only the ZIP file. If using Git, push the complete folder contents.
3. Open repository **Settings → Pages**. Under **Build and deployment → Source**, select **GitHub Actions**.
4. Open **Actions → Publish Al-Hayat to GitHub Pages → Run workflow**, or push a new commit to main.
5. When deployment succeeds, GitHub shows the published address in the Pages settings and workflow deployment.

The workflow publishes `dist/`. All links and assets are relative, so it works under a GitHub project path as well as a custom domain.

Official guide: [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Open locally

No installation is required. With Node.js 18 or newer:

```sh
npm run dev
```

Open **http://localhost:3000**. Alternatively, with Python installed:

```sh
python -m http.server 3000 --directory dist
```

For a quick offline inspection, `dist/index.html` can also be opened directly. Browser-local persistence varies for `file://` pages, and the service worker requires HTTP/HTTPS.

## Edit the educational content

1. Edit the corresponding original JSON file in `dist/data/`.
2. Run `python scripts/build.py` (or `python3` on systems using that command).
3. Run `npm run check`.
4. Commit the changed source JSON and generated `dist/data.js`. The GitHub workflow also regenerates and validates the browser data before publication.

The normalizer uses each question’s explicit `learning_id`. Preserve these IDs when reordering or editing. New questions need new, unique IDs; never reuse an existing ID for different content.

## Project layout

- `dist/index.html`: accessible application shell.
- `dist/style.css`: responsive layouts, typography and themes.
- `dist/app.js`: study modes, search, notes and local progress.
- `dist/data.js`: generated, bundled browser content.
- `dist/data/`: the eight original content JSON files.
- `dist/assets/fonts/`: bundled fonts and SIL Open Font License notices.
- `scripts/build.py`: data normalizer.
- `scripts/validate.py`: checks source fidelity and required assets.
- `scripts/serve.mjs`: dependency-free local server.
- `.github/workflows/pages.yml`: GitHub Pages deployment.

Keyboard shortcuts: **Ctrl/Cmd K** opens search; **B** bookmarks the current reading question; **←** opens the next question and **→** the previous question. Shortcuts are inactive while typing.

## Privacy and credits

Study records remain in the visitor's browser. No automatic cross-device sync or recording is performed. Export a backup before clearing browser data. Links to sources and the author website open external websites only when selected.

Font notices and the applicable open-font licenses are supplied in `dist/assets/fonts/`. The educational content retains its supplied authorship and source attributions. No blanket third-party content license is implied.

## Editorial revision 2.0

See `CONTENT_REVIEW.md` for the focused content and usability changes. Arabic quotations use explicit `arabic_spans` metadata, keeping Urdu prose in Jameel rather than guessing the language from a shared alphabet.

### Revision 3

Adds contextual Arabic evidence with Urdu translations to 29 answers and worked examples to 12 further answers. Reading controls are more compact, next-question navigation follows the answer directly, and highlighting preserves complete Urdu words. See CONTENT_REVIEW.md and CONTENT_ENRICHMENT.json for the scope of the revision.

The root index.html redirects branch-based GitHub Pages hosting to dist/. Upload the complete project contents when replacing the earlier repository; the separate dist/ directory remains the deployed app. Run npm run build and npm run check after content edits.
