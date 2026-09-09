'use client';
import { useEffect, useState, type FormEvent } from 'react';
import {
  ArrowUpRight,
  ArrowRight,
  Check,
  Zap,
  Globe,
  ShoppingBag,
  Code2,
  Workflow,
  Utensils,
  Sparkles,
  Scissors,
  Gem,
  House,
  Shirt,
  Building2,
  Smartphone,
  Target,
  Layers,
  HeartHandshake,
  BarChart3,
  CircleCheck,
  Play,
  RotateCcw,
  LoaderCircle,
  MessageCircle,
  Minus,
  Users,
} from 'lucide-react';
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from '@/components/ui/select';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';
import {
  Table,
  TableHeader,
  TableBody,
  TableHead,
  TableCell,
  TableRow,
  TableCaption,
} from '@/components/ui/table';
import { CTA, Brand } from './page';
import { services, industries, needs, validateLead } from '@/lib/lead';
const serviceIcons = [Globe, ShoppingBag, Workflow, Code2, Users];
const industryIcons = [
  Utensils,
  Sparkles,
  ShoppingBag,
  Scissors,
  Gem,
  House,
  Shirt,
  Building2,
];
function Title({
  tag,
  children,
  description,
}: {
  tag: string;
  children: React.ReactNode;
  description?: string;
}) {
  return (
    <div className="section-title">
      <span className="eyebrow">{tag}</span>
      <h2>{children}</h2>
      {description && <p>{description}</p>}
    </div>
  );
}
function Tags({ items }: { items: string[] }) {
  return (
    <div className="tags">
      {items.map((t) => (
        <span key={t}>{t}</span>
      ))}
    </div>
  );
}
function Dashboard() {
  return (
    <div
      className="dashboard"
      aria-label="Illustrative restaurant dashboard with sample data"
    >
      <div className="browser-bar">
        <span>● ● ●</span>
        <span>DineFlo / Overview</span>
        <span>↗</span>
      </div>
      <div className="dash-body">
        <aside>
          <b>◈ DineFlo</b>
          <span className="selected">Overview</span>
          <span>Live orders</span>
          <span>Tables</span>
          <span>Digital menu</span>
          <span>Inventory</span>
          <span>Analytics</span>
        </aside>
        <div className="dash-main">
          <div className="dash-heading">
            <strong>Good things are on the menu.</strong>
            <small>
              <i /> Restaurant overview
            </small>
          </div>
          <div className="stats">
            <div>
              <small>Today's sales</small>
              <b>₹24,850</b>
              <em>Sample revenue</em>
            </div>
            <div>
              <small>Orders</small>
              <b>86</b>
              <em>Sample activity</em>
            </div>
            <div>
              <small>Tables active</small>
              <b>12 / 18</b>
              <em>Sample occupancy</em>
            </div>
          </div>
          <div className="chart">
            <small>Sales overview</small>
            <div className="bars">
              {[30, 45, 38, 60, 52, 70, 62, 80, 69, 85, 78, 98].map((h, i) => (
                <span key={i} style={{ height: h + '%' }} />
              ))}
            </div>
          </div>
          <div className="order-row">
            <span>
              <i /> #DF-1086 · Table 04
            </span>
            <span className="status">Preparing</span>
          </div>
          <div className="order-row">
            <span>
              <i /> #DF-1085 · Table 12
            </span>
            <span className="status">Ready to serve</span>
          </div>
        </div>
      </div>
    </div>
  );
}
function CommerceMockup() {
  return (
    <div className="commerce-mockup">
      <div className="browser-bar">
        <span>● ● ●</span>
        <span>Gulabi Threads / Store operations</span>
        <ShoppingBag size={13} />
      </div>
      <div className="commerce-inside">
        <span className="commerce-wordmark">Gulabi Threads</span>
        <small>HANDCRAFTED WITH LOVE. CONNECTED BY TECHNOLOGY.</small>
        <div className="commerce-summary">
          <div>
            <ShoppingBag size={32} />
            <h4>
              From collection
              <br />
              to checkout.
            </h4>
            <p>A complete commerce experience.</p>
          </div>
          <div className="commerce-order">
            <b>Order management</b>
            <span>
              Order received <Check size={14} />
            </span>
            <span>
              Payment confirmed <Check size={14} />
            </span>
            <span>
              Inventory updated <Check size={14} />
            </span>
            <span className="pink-status">
              Ready to fulfil <ArrowRight size={14} />
            </span>
          </div>
        </div>
        <div className="commerce-pills">
          <span>Catalogue</span>
          <span>Customers</span>
          <span>Payments</span>
          <span>Inventory</span>
        </div>
      </div>
      <div className="phone-mini">
        <ShoppingBag size={24} />
        <b>
          Gulabi
          <br />
          Threads
        </b>
        <span>
          Your order
          <br />
          is confirmed
        </span>
        <CircleCheck size={26} />
      </div>
    </div>
  );
}
function BeautyMockup() {
  return (
    <div className="beauty-mockup">
      <span className="eyebrow">
        A DIGITAL SPACE, AS DISTINCTIVE AS YOUR WORK.
      </span>
      <div className="beauty-type">
        Make an
        <br />
        <em>impression.</em>
      </div>
      <div className="beauty-bottom">
        <span>Bridal · Beauty · Artistry</span>
        <a href="#contact">
          Enquire about a date <ArrowUpRight size={16} />
        </a>
      </div>
      <span className="mockup-note">Illustrative beauty website direction</span>
    </div>
  );
}
const workflowText = {
  Restaurant: [
    'Customer',
    'QR / digital menu',
    'Table order',
    'Automation engine',
    'Payment · kitchen · inventory · CRM',
    'Restaurant dashboard',
    'Sales analytics',
  ],
  Retail: [
    'Customer',
    'E-commerce website',
    'Online order',
    'Automation engine',
    'Payment · notification · inventory · CRM',
    'Business dashboard',
    'Sales analytics',
  ],
  Services: [
    'Customer',
    'Website / application',
    'Booking / enquiry',
    'Automation engine',
    'Payment · notification · calendar · CRM',
    'Business dashboard',
    'Enquiry analytics',
  ],
};
function Automation() {
  const [mode, setMode] = useState<keyof typeof workflowText>('Restaurant');
  const [step, setStep] = useState(-1);
  const [running, setRunning] = useState(false);
  useEffect(() => {
    if (!running) return;
    const t = setInterval(
      () =>
        setStep((s) => {
          if (s >= 6) {
            setRunning(false);
            return 6;
          }
          return s + 1;
        }),
      800,
    );
    return () => clearInterval(t);
  }, [running]);
  return (
    <section className="section automation-section" id="solutions">
      <div className="wrap">
        <Title
          tag="YOUR BUSINESS. IN SYNC."
          description="Explore how an everyday interaction becomes a connected workflow."
        >
          Imagine your business
          <br />
          running <span className="gradient">like this.</span>
        </Title>
        <Tabs
          value={mode}
          onValueChange={(v) => {
            setMode(v as keyof typeof workflowText);
            setStep(-1);
            setRunning(false);
          }}
        >
          <TabsList
            className="workflow-tabs"
            aria-label="Choose a business workflow"
          >
            {Object.keys(workflowText).map((m) => (
              <TabsTrigger key={m} value={m}>
                {m}
              </TabsTrigger>
            ))}
          </TabsList>
        </Tabs>
        <div className="workflow-layout">
          <div className="flow-track">
            {workflowText[mode].map((s, i) => (
              <div
                key={i}
                className={
                  'flow-item ' +
                  (i <= step ? 'lit ' : '') +
                  (i === 3 ? 'engine' : '')
                }
              >
                <span className="flow-number">0{i + 1}</span>
                {i === 3 && <Zap size={21} />}
                <span>{s}</span>
                {i <= step && <Check size={16} />}
              </div>
            ))}
          </div>
          <div className="workflow-explainer">
            <span className="eyebrow">ONE ACTION. EVERYTHING CONNECTED.</span>
            <h3>
              Less chasing.
              <br />
              More doing.
            </h3>
            <p>
              When a customer takes action, your systems move with them.
              Information reaches the right people, routine tasks happen
              automatically, and you see the whole picture.
            </p>
            <button
              className="button primary"
              onClick={() => {
                setStep(-1);
                setRunning(true);
              }}
              disabled={running}
            >
              {running ? (
                <LoaderCircle className="spin" size={16} />
              ) : step === 6 ? (
                <RotateCcw size={16} />
              ) : (
                <Play size={16} />
              )}{' '}
              {running
                ? 'Running example…'
                : step === 6
                  ? 'Replay workflow'
                  : 'Run an example'}
            </button>
            <p className="flow-result" aria-live="polite">
              {step === 6
                ? 'Workflow complete. Your customer, team and dashboard are in sync.'
                : step >= 0
                  ? 'Example: ' + workflowText[mode][step]
                  : 'An interactive example — no real orders or payments.'}
            </p>
          </div>
        </div>
        <div className="outcomes">
          <span>Less manual work.</span>
          <span>Fewer errors.</span>
          <span>Faster operations.</span>
          <span className="gradient">More growth.</span>
        </div>
      </div>
    </section>
  );
}
function ContactForm() {
  const [need, setNeed] = useState('Not Sure — Help Me Decide');
  const [industry, setIndustry] = useState('Small & Medium Businesses');
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState('');
  const [success, setSuccess] = useState(false);
  async function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (busy) return;
    const form = e.currentTarget;
    const data = { ...Object.fromEntries(new FormData(form)), need, industry };
    const error = validateLead(data);
    if (error) {
      setResult(error);
      setSuccess(false);
      return;
    }
    setBusy(true);
    setResult('');
    try {
      const response = await fetch('/api/enquiries', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      const value = (await response.json()) as {
        error?: string;
        reference?: string;
      };
      if (!response.ok)
        throw new Error(
          value.error || 'Your enquiry could not be saved. Please try again.',
        );
      setSuccess(true);
      setResult(
        'Thank you. Your enquiry has been received. Reference: ' +
          value.reference,
      );
      form.reset();
    } catch (error) {
      setSuccess(false);
      setResult(
        error instanceof Error
          ? error.message
          : 'Unable to connect. Please try again.',
      );
    } finally {
      setBusy(false);
    }
  }
  return (
    <form onSubmit={submit} className="contact-form">
      <div className="form-grid">
        {[
          ['name', 'Your name', 'text', 'name'],
          ['business', 'Business name', 'text', 'organization'],
          ['phone', 'Phone / WhatsApp', 'tel', 'tel'],
          ['email', 'Email address', 'email', 'email'],
        ].map(([name, label, type, auto]) => (
          <label key={name}>
            {label}
            <input
              name={name}
              type={type}
              autoComplete={auto}
              required
              maxLength={name === 'phone' ? 24 : 160}
              placeholder={label}
            />
          </label>
        ))}
        <label>
          Business type
          <Select value={industry} onValueChange={(v) => v && setIndustry(v)}>
            <SelectTrigger className="form-select" aria-label="Business type">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {industries.map((i) => (
                <SelectItem key={i} value={i}>
                  {i}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </label>
        <label>
          What are you looking for?
          <Select value={need} onValueChange={(v) => v && setNeed(v)}>
            <SelectTrigger
              className="form-select"
              aria-label="What are you looking for?"
            >
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {needs.map((i) => (
                <SelectItem key={i} value={i}>
                  {i}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </label>
      </div>
      <label>
        Tell us about your business
        <textarea
          required
          name="message"
          rows={4}
          minLength={10}
          maxLength={4000}
          placeholder="What do you do? What would you love to make simpler?"
        />
      </label>
      <div className="honeypot" aria-hidden="true">
        <label>
          Leave this empty
          <input name="website" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
      <p className="form-note">
        We’ll use these details to respond to your enquiry.
      </p>
      <button className="button primary" disabled={busy} type="submit">
        {busy ? (
          <>
            <LoaderCircle size={18} className="spin" />
            Sending your enquiry…
          </>
        ) : (
          <>
            Let’s build something powerful <ArrowUpRight size={18} />
          </>
        )}
      </button>
      {result && (
        <p
          className={'form-result ' + (success ? 'success' : 'error')}
          role={success ? 'status' : 'alert'}
        >
          {result}
        </p>
      )}
    </form>
  );
}
export default function Content() {
  useEffect(() => {
    const elements = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('is-visible');
            observer.unobserve(e.target);
          }
        }),
      { threshold: 0.08 },
    );
    elements.forEach((e) => observer.observe(e));
    return () => observer.disconnect();
  }, []);
  return (
    <>
      <section className="section wrap reveal" id="problems">
        <div className="split-heading">
          <Title tag="FROM FRICTION TO FLOW">
            Your business shouldn’t
            <br />
            depend on manual work.
          </Title>
          <p>
            Great businesses deserve better than disconnected tools and
            repetitive tasks. Let’s give yours room to grow.
          </p>
        </div>
        <div className="problem-grid">
          {[
            'Taking orders manually',
            'Customers scattered across spreadsheets',
            'No professional website',
            'Manual billing and follow-ups',
            'No online selling system',
            'Repetitive administrative work',
            'Limited business analytics',
          ].map((p, i) => (
            <div key={p}>
              <span>0{i + 1}</span>
              <p>{p}</p>
              <Minus size={17} />
            </div>
          ))}
        </div>
        <div className="problem-answer">
          <Zap />
          <div>
            <h3>We turn these problems into automated digital systems.</h3>
            <p>Website → Customer → Order → Payment → Operations → Analytics</p>
          </div>
          <a href="#solutions" aria-label="Explore connected solutions">
            <ArrowUpRight />
          </a>
        </div>
      </section>
      <section className="section service-section" id="services">
        <div className="wrap reveal">
          <div className="split-heading">
            <Title tag="WHAT WE BUILD">
              Everything your business
              <br />
              needs to <span className="gradient">go digital.</span>
            </Title>
            <p>
              Two core strengths. One connected approach.
              <br />
              Web development + business automation.
            </p>
          </div>
          <div className="services-grid">
            {services.map((s, i) => {
              const Icon = serviceIcons[i];
              return (
                <article className={'service-card service-' + i} key={s.name}>
                  <div className="service-top">
                    <span className="icon-box">
                      <Icon size={24} />
                    </span>
                    <span>0{i + 1}</span>
                  </div>
                  <h3>{s.name}</h3>
                  <p>{s.description}</p>
                  <ul>
                    {s.features.map((f) => (
                      <li key={f}>
                        <Check size={14} />
                        {f}
                      </li>
                    ))}
                  </ul>
                  <a href="#contact">
                    {s.cta}
                    <ArrowUpRight size={18} />
                  </a>
                </article>
              );
            })}
          </div>
        </div>
      </section>
      <section className="section wrap" id="work">
        <div className="split-heading reveal">
          <Title tag="SELECTED WORK">
            Ideas we’ve turned
            <br />
            into <span className="gradient">products.</span>
          </Title>
          <p>
            Customer-facing experiences.
            <br />
            Powerful systems behind the scenes.
          </p>
        </div>
        <article className="project project-dine reveal">
          <div className="project-copy">
            <span className="eyebrow">
              01 / RESTAURANT TECHNOLOGY & AUTOMATION
            </span>
            <h3>
              DineFlo<span>Less waiting. Better dining.</span>
            </h3>
            <p>
              A digital restaurant ordering and operations platform designed to
              reduce manual work and modernize restaurant operations.
            </p>
            <Tags
              items={[
                'QR table ordering',
                'Digital menu',
                'Kitchen orders',
                'Billing',
                'Cash / UPI / card workflows',
                'Dashboard',
                'Sales analytics',
                'Table management',
                'Inventory capabilities',
                'Customer reviews',
              ]}
            />
            <a
              className="project-link"
              href="https://dineflo.info/"
              target="_blank"
              rel="noopener noreferrer"
            >
              Explore DineFlo <ArrowUpRight size={19} />
            </a>
          </div>
          <div className="project-visual">
            <Dashboard />
            <small className="preview-label">
              Illustrative product preview · sample data
            </small>
          </div>
          <div className="project-flow">
            <span>SCAN QR</span>
            <ArrowRight aria-hidden="true" />
            <span>BROWSE MENU</span>
            <ArrowRight aria-hidden="true" />
            <span>ORDER</span>
            <ArrowRight aria-hidden="true" />
            <span>KITCHEN</span>
            <ArrowRight aria-hidden="true" />
            <span>BILLING</span>
            <ArrowRight aria-hidden="true" />
            <span>ANALYTICS</span>
          </div>
        </article>
        <article className="project project-gulabi reveal">
          <div className="project-copy">
            <span className="eyebrow">02 / E-COMMERCE PLATFORM</span>
            <h3>
              Gulabi Threads<span>Handcrafted meets digital.</span>
            </h3>
            <p>
              A complete digital commerce experience built for a handcrafted
              products brand — from discovering a collection to managing the
              next order.
            </p>
            <Tags
              items={[
                'Product catalogue',
                'Categories',
                'Shopping cart',
                'Customer login',
                'Online payments',
                'Order management',
                'Admin dashboard',
                'Inventory management',
              ]}
            />
            <a
              className="project-link"
              href="https://www.gulabitreads.com/"
              target="_blank"
              rel="noopener noreferrer"
            >
              View project <ArrowUpRight size={19} />
            </a>
          </div>
          <div className="project-visual">
            <CommerceMockup />
            <small className="preview-label">
              Illustrative desktop and mobile commerce workflow
            </small>
          </div>
        </article>
        <article className="project project-beauty reveal">
          <div className="project-copy">
            <span className="eyebrow">
              03 / WEBSITES FOR BEAUTY PROFESSIONALS
            </span>
            <h3>
              Beauty, with a presence.
              <span>Turn your craft into enquiries.</span>
            </h3>
            <p>
              Premium portfolio and lead-generation websites for beauticians and
              makeup artists who want to showcase their work and convert
              visitors into clients.
            </p>
            <Tags
              items={[
                'Service catalogue',
                'Portfolio gallery',
                'Bridal / makeup packages',
                'Pricing',
                'WhatsApp enquiries',
                'Appointment enquiries',
                'Google Maps',
                'Instagram',
                'SEO-friendly pages',
              ]}
            />
            <a className="project-link" href="#contact">
              Build my beauty website <ArrowUpRight size={19} />
            </a>
          </div>
          <div className="project-visual">
            <BeautyMockup />
          </div>
        </article>
      </section>
      <section className="section industries-section" id="industries">
        <div className="wrap reveal">
          <Title
            tag="BUILT FOR YOUR WORLD"
            description="Every industry works differently. Your technology should understand that."
          >
            Technology built
            <br />
            around your business.
          </Title>
          <div className="industry-grid">
            {industries.map((industry, i) => {
              const Icon = industryIcons[i];
              return (
                <a href="#contact" key={industry}>
                  <Icon />
                  <span>{industry}</span>
                  <ArrowUpRight size={16} />
                </a>
              );
            })}
          </div>
          <div className="industry-more">
            <p>
              <strong>Don’t see your industry?</strong> We build custom
              solutions around your workflow.
            </p>
            <a href="#contact">
              Tell us about your business <ArrowUpRight size={16} />
            </a>
          </div>
        </div>
      </section>
      <section className="section wrap reveal" id="process">
        <Title tag="A CLEAR PATH FORWARD">
          From your first idea
          <br />
          to your next stage of growth.
        </Title>
        <div className="timeline">
          {[
            [
              'Understand',
              'We understand your business, customers and current workflow.',
            ],
            [
              'Design',
              'We design the customer experience and system architecture.',
            ],
            ['Build', 'We develop your website, application or automation.'],
            ['Launch', 'We test, optimize and deploy the solution.'],
            [
              'Grow & automate',
              'We keep improving the system as your business grows.',
            ],
          ].map(([t, d], i) => (
            <div key={t}>
              <span className="step-number">0{i + 1}</span>
              <h3>{t}</h3>
              <p>{d}</p>
            </div>
          ))}
        </div>
      </section>
      <Automation />
      <section className="section wrap reveal" id="why-astra">
        <Title tag="THE ASTRA APPROACH">
          We don’t just build websites.
          <br />
          We build <span className="gradient">business systems.</span>
        </Title>
        <div className="why-grid">
          {[
            [
              Zap,
              'Automation first',
              'We identify repetitive work that technology can handle.',
            ],
            [
              Target,
              'Business focused',
              'Technology should solve an actual business problem.',
            ],
            [
              Smartphone,
              'Mobile first',
              'Every solution works beautifully across devices.',
            ],
            [
              Layers,
              'Custom solutions',
              'Solutions designed around your workflow.',
            ],
            [
              BarChart3,
              'Built to scale',
              'Technology capable of growing alongside your business.',
            ],
            [
              HeartHandshake,
              'Long-term support',
              'We help you continue improving after launch.',
            ],
          ].map(([Icon, title, desc]) => {
            const I = Icon as typeof Zap;
            return (
              <div key={String(title)}>
                <I />
                <h3>{String(title)}</h3>
                <p>{String(desc)}</p>
              </div>
            );
          })}
        </div>
      </section>
      <section className="section comparison-section">
        <div className="wrap comparison-layout reveal">
          <Title
            tag="A BIGGER PICTURE"
            description="Your website is the starting point. We connect it to the systems that help you sell, serve customers and operate every day."
          >
            More than
            <br />a website agency.
          </Title>
          <Table className="comparison">
            <TableCaption>
              Illustrative scope comparison; individual agency offerings vary.
            </TableCaption>
            <TableHeader>
              <TableRow>
                <TableHead>Capability</TableHead>
                <TableHead>Traditional agency</TableHead>
                <TableHead>Astra Automation</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {[
                'Website & design',
                'Hosting & launch',
                'E-commerce',
                'Business automation',
                'Custom applications',
                'Ordering systems',
                'Dashboards',
                'Inventory integration',
                'Analytics',
                'Workflow automation',
              ].map((v, i) => (
                <TableRow key={v}>
                  <TableCell>{v}</TableCell>
                  <TableCell>
                    {i < 2 ? (
                      <Check size={17} aria-label="Included" />
                    ) : (
                      <Minus size={17} aria-label="Varies" />
                    )}
                  </TableCell>
                  <TableCell>
                    <Check size={17} aria-label="Included" />
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </section>
      <section className="section wrap">
        <div className="big-cta reveal">
          <span className="eyebrow">LET’S BUILD WHAT’S NEXT</span>
          <h2>
            Have a business?
            <br />
            Let’s find what we can <span className="gradient">automate.</span>
          </h2>
          <p>
            Tell us how your business currently operates. We’ll explore how
            websites, software and automation can help you save time and grow.
          </p>
          <div className="actions">
            <CTA>Get a free business consultation</CTA>
          </div>
          <div className="whatsapp-pending">
            <MessageCircle size={16} />
            <span>Prefer WhatsApp? Include your number in the form below.</span>
          </div>
        </div>
      </section>
      <section className="section wrap contact-section reveal" id="contact">
        <div>
          <Title tag="START A CONVERSATION">
            Your next chapter
            <br />
            starts here.
          </Title>
          <p>
            Tell us about your business, your idea, or the tasks taking up too
            much of your day. We’ll help you find a practical way forward.
          </p>
          <div className="contact-points">
            <span>
              <Check />
              Business-first advice
            </span>
            <span>
              <Check />
              Solutions built around you
            </span>
            <span>
              <Check />A clear path from idea to launch
            </span>
          </div>
        </div>
        <ContactForm />
      </section>
      <footer>
        <div className="wrap footer-top">
          <div>
            <Brand />
            <p>
              Web Development · Business Automation
              <br />
              Custom Software
            </p>
            <span className="footer-tag">
              Built for businesses ready to evolve.
            </span>
          </div>
          <div>
            <h3>Explore</h3>
            {[
              ['Services', 'services'],
              ['Projects', 'work'],
              ['Industries', 'industries'],
              ['About', 'why-astra'],
              ['Contact', 'contact'],
            ].map(([t, id]) => (
              <a key={id} href={'#' + id}>
                {t}
              </a>
            ))}
          </div>
          <div>
            <h3>Connect</h3>
            <span className="pending-social">
              Instagram <small>Coming soon</small>
            </span>
            <span className="pending-social">
              LinkedIn <small>Coming soon</small>
            </span>
            <a href="#contact">
              WhatsApp enquiry <ArrowUpRight size={13} />
            </a>
          </div>
        </div>
        <div className="wrap footer-bottom">
          <span>© 2026 Astra Automation. All Rights Reserved.</span>
          <a href="#home">Back to top ↑</a>
        </div>
      </footer>
    </>
  );
}
