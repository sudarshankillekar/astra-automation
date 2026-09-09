'use client';
import {
  ArrowUpRight,
  ArrowRight,
  Check,
  Zap,
  Globe,
  ShoppingBag,
  Users,
  CreditCard,
  BarChart3,
  Workflow,
  Menu,
  X,
} from 'lucide-react';
import { useState } from 'react';
import Content from './content';
const links = [
  ['Home', 'home'],
  ['Services', 'services'],
  ['Solutions', 'solutions'],
  ['Our Work', 'work'],
  ['Industries', 'industries'],
  ['Why Astra', 'why-astra'],
  ['Contact', 'contact'],
];
export function Brand() {
  return (
    <a href="#home" className="brand" aria-label="Astra Automation home">
      <img
        src="/astra-mark.png"
        alt=""
        aria-hidden="true"
        width="512"
        height="512"
      />
      <span className="brand-copy">
        <strong>Astra Automation</strong>
        <small>WE BUILD YOUR GROWTH ONLINE</small>
      </span>
    </a>
  );
}
export function CTA({
  children,
  href = '#contact',
  secondary = false,
}: {
  children: React.ReactNode;
  href?: string;
  secondary?: boolean;
}) {
  return (
    <a
      className={'button ' + (secondary ? 'secondary' : 'primary')}
      href={href}
    >
      {children}
      <ArrowUpRight size={17} />
    </a>
  );
}
export function SystemVisual() {
  return (
    <div
      className="system-visual"
      aria-label="Website, orders, customers, payments and analytics connected through Astra Automation"
    >
      <div className="visual-top">
        <span>
          <i /> CONNECTED BUSINESS SYSTEM
        </span>
        <span>01 — 06</span>
      </div>
      <div className="orbit orbit-one" />
      <div className="orbit orbit-two" />
      <svg className="connections" viewBox="0 0 600 500" aria-hidden="true">
        <path d="M300 240L105 110M300 240L480 110M300 240L80 280M300 240L515 290M300 240L180 415M300 240L430 415" />
      </svg>
      <div className="core">
        <Zap size={38} />
        <strong>ASTRA</strong>
        <small>AUTOMATION ENGINE</small>
      </div>
      {[Globe, ShoppingBag, Users, CreditCard, BarChart3, Workflow].map(
        (Icon, i) => (
          <div key={i} className={'system-node node-' + i}>
            <Icon />
            <div>
              <strong>
                {
                  [
                    'Website',
                    'Orders',
                    'Customers',
                    'Payments',
                    'Analytics',
                    'Automation',
                  ][i]
                }
              </strong>
              <small>
                {
                  [
                    'Your digital storefront',
                    'Every order, connected',
                    'Relationships, organized',
                    'Seamless transactions',
                    'Clarity at a glance',
                    'Less work. More flow.',
                  ][i]
                }
              </small>
            </div>
            <i />
          </div>
        ),
      )}
      <div className="visual-bottom">
        <span>
          <i /> All systems connected
        </span>
        <span>
          Built to work together <ArrowRight size={14} />
        </span>
      </div>
    </div>
  );
}
export default function Home() {
  const [menu, setMenu] = useState(false);
  return (
    <>
      <a className="skip" href="#main">
        Skip to content
      </a>
      <header>
        <div className="nav wrap">
          <Brand />
          <nav aria-label="Main navigation" className={menu ? 'open' : ''}>
            {links.map(([label, id]) => (
              <a key={id} href={'#' + id} onClick={() => setMenu(false)}>
                {label}
              </a>
            ))}
          </nav>
          <a className="nav-cta" href="#contact">
            Free consultation <ArrowUpRight size={15} />
          </a>
          <button
            className="menu-toggle"
            onClick={() => setMenu(!menu)}
            aria-expanded={menu}
            aria-label="Toggle navigation"
          >
            {menu ? <X /> : <Menu />}
          </button>
        </div>
      </header>
      <main id="main">
        <section id="home" className="hero wrap">
          <div className="hero-copy">
            <div className="eyebrow badge">
              <Zap size={13} /> WEB DEVELOPMENT · BUSINESS AUTOMATION
            </div>
            <h1>
              We <span>build</span> digital
              <br />
              systems that
              <br />
              <span>grow</span> your business.
            </h1>
            <p>
              From high-performance websites and e-commerce to restaurant
              ordering and business automation. We transform manual businesses
              into modern digital operations.
            </p>
            <div className="actions">
              <CTA>Start your project</CTA>
              <CTA href="#work" secondary>
                Explore our work
              </CTA>
            </div>
            <div className="assurances">
              {[
                'Custom-built solutions',
                'Mobile responsive',
                'Business automation',
                'Scalable technology',
              ].map((t) => (
                <span key={t}>
                  <Check size={13} />
                  {t}
                </span>
              ))}
            </div>
          </div>
          <SystemVisual />
        </section>
        <div className="strap">
          <div className="wrap">
            <span>BUILD SMARTER.</span>
            <span>AUTOMATE FASTER.</span>
            <span>GROW FURTHER.</span>
            <span className="muted">One partner. A connected business.</span>
          </div>
        </div>
        <Content />
      </main>
    </>
  );
}
