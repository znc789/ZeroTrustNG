import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Zero Trust Network Guardian',
  description: 'AI-powered adaptive zero trust security framework',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
