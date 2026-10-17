# A little birthday love

A personal digital birthday card for a wonderful doctor and a king with a heart of gold. Designed in midnight blue, warm ivory and soft mint, with a portrait, a sister's letter, a playful birthday prescription and an interactive birthday candle.

## Publish on GitHub Pages

In this repository, open **Settings → Pages**, choose **Deploy from a branch**, select **main** and **/ (root)**, then save.

No build step, package installation, API keys or external JavaScript dependencies are needed. All assets use relative paths so the card works under the `/bthday/` project URL. Google Fonts is optional; local serif and sans-serif fallbacks are provided.

## Preview locally

Run `python3 -m http.server 8080` inside this folder and open `http://localhost:8080`.

## Edit

- Text and layout: `index.html`
- Colours and responsive styles: `style.css`
- Card opening, candle and confetti: `script.js`
- Supplied portrait: `assets/brother.png`

Supports keyboard interaction, reduced motion preferences, and a readable card when JavaScript is disabled. No analytics or visitor data collection.
