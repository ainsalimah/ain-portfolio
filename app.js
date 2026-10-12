const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
const toggle = document.querySelector('#motion-toggle');
let paused = preference.matches;
let observer;
const animations = new Set();
const revealed = new WeakSet();
let heroPlayed = false;

function animate(element, frames, options) {
  if (paused || !element?.animate) return;
  const animation = element.animate(frames, options);
  animations.add(animation);
  animation.finished.catch(() => {}).finally(() => animations.delete(animation));
}

function applyMotionState() {
  document.body.classList.toggle('motion-paused', paused);
  document.body.classList.toggle('motion-enabled', !paused);
  toggle?.setAttribute('aria-pressed', String(paused));
  if (toggle) toggle.textContent = paused ? 'Aktifkan animasi' : 'Jeda animasi';
  if (paused) {
    animations.forEach(animation => animation.cancel());
    observer?.disconnect();
  } else {
    playHero();
    observeSections();
  }
}

function playHero() {
  if (heroPlayed) return;
  heroPlayed = true;
  document.querySelectorAll('.hero-intro, h1 > span, .hero-description, .hero-actions').forEach((element, index) => {
    animate(element, [
      { transform: 'translateY(44px)', opacity: .15 },
      { transform: 'translateY(0)', opacity: 1 }
    ], { duration: 1100, delay: index * 90, easing: 'cubic-bezier(.16,1,.3,1)' });
  });
  animate(document.querySelector('.hero-art'), [
    { transform: 'translateY(24px) scale(.9)', opacity: .15 },
    { transform: 'translateY(0) scale(1)', opacity: 1 }
  ], { duration: 1500, easing: 'cubic-bezier(.16,1,.3,1)' });
}

function observeSections() {
  if (!('IntersectionObserver' in window)) return;
  observer?.disconnect();
  observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      revealed.add(entry.target);
      animate(entry.target, [{ opacity: .2, transform: 'translateY(42px)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 1000, easing: 'cubic-bezier(.16,1,.3,1)' });
      observer.unobserve(entry.target);
    });
  }, { threshold: .16 });
  document.querySelectorAll('.reveal:not(.project), .project-top, .project-visual, .project-copy').forEach(element => {
    if (!revealed.has(element)) observer.observe(element);
  });
}

if (toggle) toggle.hidden = false;
toggle?.addEventListener('click', () => { paused = !paused; applyMotionState(); });
preference.addEventListener('change', event => { paused = event.matches; applyMotionState(); });
applyMotionState();

// A gentle visual response without scroll interception or layout measurements.
const art = document.querySelector('.orbit-art');
let scheduled = false;
window.addEventListener('scroll', () => {
  if (scheduled || paused) return;
  scheduled = true;
  requestAnimationFrame(() => {
    if (art && !paused) art.style.transform = `translateY(${Math.min(window.scrollY, 700) * .035}px)`;
    scheduled = false;
  });
}, { passive: true });
preference.addEventListener('change', () => { if (art) art.style.transform = ''; });
toggle?.addEventListener('click', () => { if (paused && art) art.style.transform = ''; });

// Native details work without JS. With JS, case studies can also be deep-linked.
document.querySelectorAll('.case-study').forEach(details => {
  details.addEventListener('toggle', () => {
    if (details.open) {
      const url = new URL(window.location.href);
      url.searchParams.set('studi', details.closest('article').id);
      history.replaceState(null, '', url);
    } else {
      const url = new URL(window.location.href);
      if (url.searchParams.get('studi') === details.closest('article').id) {
        url.searchParams.delete('studi');
        history.replaceState(null, '', url);
      }
    }
  });
});
const selected = new URLSearchParams(window.location.search).get('studi');
const selectedArticle = [...document.querySelectorAll('.project')].find(article => article.id === selected);
if (selectedArticle) selectedArticle.querySelector('details').open = true;
