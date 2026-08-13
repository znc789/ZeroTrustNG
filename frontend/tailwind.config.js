/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './lib/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        cyber: {
          950: '#060b16',
          900: '#0b1220',
          800: '#111b2d',
          700: '#1d2f4d',
          600: '#2b5b83',
          500: '#4ac5ff',
          400: '#7ef9ff',
          300: '#9bd4ff',
          200: '#d6eefb',
        },
      },
      boxShadow: {
        glow: '0 0 24px rgba(74, 197, 255, 0.35)',
      },
    },
  },
  plugins: [],
};
