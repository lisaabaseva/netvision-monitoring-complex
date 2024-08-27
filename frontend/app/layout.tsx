import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import 'bootstrap/dist/css/bootstrap.min.css';
import { store } from "@/state/store";
import { Providers } from "@/state/Providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Monitoring",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <Providers store={store}>
        <body className={`${inter.className} bg-netvision-bg-dark min-h-screen text-white`}>
          <Header/>
          {children}
        </body>
      </Providers>
    </html>
  );
}
