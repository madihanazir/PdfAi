module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pinkBg: "#ffdde1",
        pinkAccent: "#ff69b4",
      },
      boxShadow: {
        kawaii: "5px 5px 15px rgba(255, 182, 193, 0.5)",
      },
    },
  },
  plugins: [],
};
