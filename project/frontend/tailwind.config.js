/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../apps/**/*.html',
    '../apps/**/*.js',
    '../apps/**/*.py',
  ],
  theme: {
    extend: {
      fontFamily: {
        yekan: ['yekan'], // اینو اینجا اضافه کن
      },
    },
  },
  plugins: [],
}

