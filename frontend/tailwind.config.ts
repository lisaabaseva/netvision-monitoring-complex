import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors : {
        'netvision-bg-dark': '#14191d',
        'netvision-gradient-start': '#545C62',
        'netvision-gradient-end': '#414851',
        'netvision-gradient2-start': '#343C42',
        'netvision-gradient2-end': '#212831',
      },
    },
  },
  plugins: [],
};
export default config;
