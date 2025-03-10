/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',  // Added darkMode from the second config
  content: [
    "./src/**/*.{html,ts}",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {}
  },
  variants: {},
  plugins: [
    require('flowbite/plugin'),
  ],
}
