'use strict';

const intro = document.getElementById('intro');
const card = document.getElementById('card');
const openButton = document.getElementById('openCard');
const wishButton = document.getElementById('wishButton');
const relightButton = document.getElementById('relightButton');
const flame = document.getElementById('flame');
const wishResult = document.getElementById('wishResult');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let celebrationFrame;
document.body.classList.add('sealed');

openButton.addEventListener('click', () => {
  card.hidden = false;
  card.classList.add('card-arrive');
  intro.classList.add('is-open');
  intro.inert = true;
  document.body.classList.remove('sealed');
  window.scrollTo({ top: 0, behavior: 'instant' });
  document.querySelector('.wordmark').focus({ preventScroll: true });
  celebrate(65);
});

document.getElementById('replay').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'instant' });
  card.hidden = true;
  card.classList.remove('card-arrive');
  intro.classList.remove('is-open');
  intro.inert = false;
  document.body.classList.add('sealed');
  resetCandle();
  openButton.focus({ preventScroll: true });
});

wishButton.addEventListener('click', () => {
  flame.classList.add('out');
  wishButton.disabled = true;
  wishButton.textContent = 'Your wish is on its way ♡';
  wishResult.textContent = 'More joy. More love. More beautiful days. All for you. ♡';
  relightButton.hidden = false;
  celebrate(150);
});

function resetCandle() {
  flame.classList.remove('out');
  wishButton.disabled = false;
  wishButton.innerHTML = 'Make a wish & blow out the candle <span aria-hidden="true">✧</span>';
  wishResult.textContent = 'May this be your happiest chapter yet.';
  relightButton.hidden = true;
}

relightButton.addEventListener('click', () => {
  resetCandle();
  wishButton.focus({ preventScroll: true });
});

function celebrate(count) {
  if (reducedMotion.matches) return;
  const canvas = document.getElementById('confetti');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  cancelAnimationFrame(celebrationFrame);
  const width = window.innerWidth;
  const height = window.innerHeight;
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = width * ratio;
  canvas.height = height * ratio;
  ctx.scale(ratio, ratio);
  const colours = ['#c7dcca', '#c6a775', '#e8d8bb', '#769985', '#f4ead3'];
  const pieces = Array.from({ length: count }, () => ({
    x: Math.random() * width, y: -Math.random() * height * .7 - 10,
    size: 4 + Math.random() * 5, speed: 1.7 + Math.random() * 2.8,
    drift: (Math.random() - .5) * 2, rotation: Math.random() * Math.PI,
    spin: (Math.random() - .5) * .06,
    colour: colours[Math.floor(Math.random() * colours.length)]
  }));
  const start = performance.now();
  let previous = start;
  function frame(now) {
    const elapsed = now - start;
    const step = Math.min((now - previous) / 16.67, 3);
    previous = now;
    ctx.clearRect(0, 0, width, height);
    for (const piece of pieces) {
      piece.y += piece.speed * step;
      piece.x += piece.drift * step;
      piece.rotation += piece.spin * step;
      ctx.save();
      ctx.globalAlpha = Math.min(1, Math.max(0, (6500 - elapsed) / 1200));
      ctx.translate(piece.x, piece.y);
      ctx.rotate(piece.rotation);
      ctx.fillStyle = piece.colour;
      ctx.fillRect(-piece.size / 2, -piece.size / 4, piece.size, piece.size / 2);
      ctx.restore();
    }
    if (elapsed < 6500) celebrationFrame = requestAnimationFrame(frame);
    else ctx.clearRect(0, 0, width, height);
  }
  celebrationFrame = requestAnimationFrame(frame);
}
