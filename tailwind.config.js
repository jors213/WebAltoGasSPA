/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './core/templates/**/*.html',
  ],

  // Safelist: clases generadas dinámicamente desde views.py
  // que el purger no puede detectar en los templates.
  safelist: [
    // Bordes de tarjetas de servicios (service.border_color)
    'border-green-600',
    'border-blue-600',
    'border-orange-500',
    // Iconos (service.icon_color)
    'text-green-600',
    'text-blue-600',
    'text-orange-600',
    // Fondos de icono (service.bg_color)
    'bg-green-100',
    'bg-blue-100',
    'bg-orange-100',
    // Colores de expertise_areas en asesoria_online
    'text-purple-600',
    'bg-purple-100',
    'text-red-600',
    'bg-red-100',
    'text-slate-600',
    'bg-slate-100',
  ],

  theme: {
    extend: {},
  },

  plugins: [],
};
