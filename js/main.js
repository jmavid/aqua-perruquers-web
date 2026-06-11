// Menú móvil
const toggle = document.querySelector('.menu-toggle');
const mobileNav = document.getElementById('mobile-nav');

if (toggle && mobileNav) {
  toggle.addEventListener('click', () => {
    const open = !mobileNav.hidden;
    mobileNav.hidden = open;
    toggle.setAttribute('aria-expanded', String(!open));
    toggle.textContent = open ? '☰' : '✕';
  });
  mobileNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      mobileNav.hidden = true;
      toggle.setAttribute('aria-expanded', 'false');
      toggle.textContent = '☰';
    });
  });
}

// Formulario de reserva → WhatsApp
const form = document.getElementById('form-reserva');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    let msg = 'Hola! Quiero reservar una cita:\n\n';
    msg += `Nombre: ${data.get('name')}\n`;
    msg += `Teléfono: ${data.get('phone')}\n`;
    if (data.get('service')) msg += `Servicio: ${data.get('service')}\n`;
    if (data.get('message')) msg += `Mensaje: ${data.get('message')}\n`;
    window.open(`https://wa.me/34692039950?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
  });
}
