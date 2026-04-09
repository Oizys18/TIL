// === Filter by category ===
const tags = document.querySelectorAll('.filter-tags .tag');
const cards = document.querySelectorAll('.card');
const searchInput = document.getElementById('searchInput');
const grid = document.getElementById('varietyGrid');

let activeFilter = 'all';
let searchQuery = '';

function applyFilters() {
  let visibleCount = 0;

  cards.forEach(card => {
    const category = card.dataset.category;
    const name = card.dataset.name.toLowerCase();

    const matchesFilter = activeFilter === 'all' || category === activeFilter;
    const matchesSearch = name.includes(searchQuery) ||
      card.querySelector('.desc').textContent.toLowerCase().includes(searchQuery);

    if (matchesFilter && matchesSearch) {
      card.classList.remove('hidden');
      visibleCount++;
    } else {
      card.classList.add('hidden');
    }
  });

  // Show "no results" message
  const existing = grid.querySelector('.no-result');
  if (visibleCount === 0) {
    if (!existing) {
      const msg = document.createElement('p');
      msg.className = 'no-result';
      msg.textContent = '검색 결과가 없습니다 🍅';
      grid.appendChild(msg);
    }
  } else {
    if (existing) existing.remove();
  }
}

tags.forEach(tag => {
  tag.addEventListener('click', () => {
    tags.forEach(t => t.classList.remove('active'));
    tag.classList.add('active');
    activeFilter = tag.dataset.filter;
    applyFilters();
  });
});

searchInput.addEventListener('input', (e) => {
  searchQuery = e.target.value.trim().toLowerCase();
  applyFilters();
});

// === Scroll-in animation ===
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

cards.forEach((card, i) => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(32px)';
  card.style.transition = `opacity 0.45s ease ${i * 0.06}s, transform 0.45s ease ${i * 0.06}s, box-shadow 0.25s ease`;
  observer.observe(card);
});

// Nutrition cards animation
document.querySelectorAll('.nut-card').forEach((card, i) => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(24px)';
  card.style.transition = `opacity 0.4s ease ${i * 0.07}s, transform 0.4s ease ${i * 0.07}s`;
  observer.observe(card);
});
