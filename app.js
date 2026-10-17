const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
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

preference.addEventListener('change', event => { paused = event.matches; applyMotionState(); });
applyMotionState();

// Existing study links still land on the right project; the full case is now visible.
const selected = new URLSearchParams(window.location.search).get('studi');
const selectedArticle = [...document.querySelectorAll('.project')].find(article => article.id === selected);
if (selectedArticle) selectedArticle.scrollIntoView();
