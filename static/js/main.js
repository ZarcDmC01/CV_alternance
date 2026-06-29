// Demo modal
function openDemo(url, title) {
  document.getElementById('demoFrame').src = url;
  document.getElementById('demoModalTitle').textContent = title;
  document.getElementById('demoModal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeDemo() {
  document.getElementById('demoModal').classList.remove('open');
  document.getElementById('demoFrame').src = '';
  document.body.style.overflow = '';
}
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDemo(); });

// Fade-in on scroll
const observer = new IntersectionObserver(
  entries => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
  { threshold: 0.1 }
);
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Active nav link highlight
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav ul a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => { if (window.scrollY >= s.offsetTop - 80) current = s.id; });
  navLinks.forEach(a => {
    const isActive = a.getAttribute('href') === '#' + current;
    a.classList.toggle('active', isActive);
  });
});
