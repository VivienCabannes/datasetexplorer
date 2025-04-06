document.querySelectorAll('.tag').forEach(tag => {
  let tooltipDiv;

  tag.addEventListener('mouseenter', () => {
    const text = tag.getAttribute('data-tooltip');
    if (!text) return;

    tooltipDiv = document.createElement('div');
    tooltipDiv.className = 'custom-tooltip';
    tooltipDiv.innerText = text;
    document.body.appendChild(tooltipDiv);

    // Position the tooltip
    const rect = tag.getBoundingClientRect();
    const tooltipRect = tooltipDiv.getBoundingClientRect();

    let top = rect.bottom + window.scrollY + 5;
    let left = rect.left + window.scrollX + (rect.width - tooltipRect.width) / 2;

    if (left + tooltipRect.width > window.innerWidth) {
      left = window.innerWidth - tooltipRect.width - 5;
    }
    if (left < 0) {
      left = 5;
    }
    if (top + tooltipRect.height > window.innerHeight + window.scrollY) {
      top = rect.top + window.scrollY - tooltipRect.height - 5;
    }

    tooltipDiv.style.top = `${top}px`;
    tooltipDiv.style.left = `${left}px`;
  });

  tag.addEventListener('mouseleave', () => {
    if (tooltipDiv) {
      tooltipDiv.remove();
      tooltipDiv = null;
    }
  });
});
