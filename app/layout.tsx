import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = {
  title: 'Astra Automation — Web Development & Business Automation',
  description:
    'Build smarter. Automate faster. Grow further. Custom websites, e-commerce, web applications and automation built around your business.',
  metadataBase: new URL(
    'https://astra-automation.sudarshankillekar199.chatgpt.site',
  ),
  icons: { icon: '/favicon-theme.png', apple: '/favicon-theme.png' },
  openGraph: {
    title: 'Astra Automation — Digital systems for business growth',
    description:
      'Web development, e-commerce and business automation. Build smarter. Automate faster. Grow further.',
    type: 'website',
  },
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className="dark">
      <body>{children}</body>
    </html>
  );
}
