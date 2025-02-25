module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pinkBg: "#ffe4e1",
        pinkAccent: "#ff69b4",
        whiteGlass: "rgba(255, 255, 255, 0.3)",
      },
      boxShadow: {
        kawaii: "5px 5px 15px rgba(255, 182, 193, 0.5)",
        glass: "0 4px 30px rgba(0, 0, 0, 0.1)",
      },
      backdropBlur: {
        glass: "10px",
      },
      borderRadius: {
        glass: "20px",
      },
    },
  },
  plugins: [],
};
