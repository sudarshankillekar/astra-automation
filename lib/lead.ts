export const needs = [
  'Website',
  'E-Commerce Website',
  'Business Automation',
  'Custom Software',
  'Influencer Marketing',
  'Restaurant Solution',
  'Not Sure — Help Me Decide',
];
export const industries = [
  'Restaurants & Cafés',
  'Makeup Artists & Beauticians',
  'Retail & E-Commerce',
  'Salons',
  'Jewellery Brands',
  'Real Estate',
  'Fashion & Handcrafted Brands',
  'Small & Medium Businesses',
];
export const services = [
  {
    name: 'Website development',
    description:
      'Professional, fast and mobile-responsive websites designed around your business.',
    features: [
      'Business websites',
      'Portfolio websites',
      'Landing pages',
      'Service websites',
      'SEO-friendly development',
      'Mobile responsive design',
    ],
    cta: 'Build my website',
  },
  {
    name: 'E-commerce development',
    description:
      'Complete online stores that make it easy to sell directly to your customers.',
    features: [
      'Product catalogue',
      'Shopping cart',
      'Online payments',
      'Customer login',
      'Order management',
      'Admin dashboard',
      'Inventory integration',
    ],
    cta: 'Start selling online',
  },
  {
    name: 'Business automation',
    description:
      'Connect your operations. Reduce repetitive work. Make room for what comes next.',
    features: [
      'Order automation',
      'Billing workflows',
      'Customer management',
      'Inventory automation',
      'Notifications',
      'Reporting',
      'Internal approval workflows',
      'Custom business tools',
    ],
    cta: 'Automate my business',
  },
  {
    name: 'Custom web applications',
    description:
      'Software designed specifically around the way your company works.',
    features: [
      'Restaurant systems',
      'Booking systems',
      'Admin dashboards',
      'Inventory systems',
      'Customer portals',
      'Internal business applications',
    ],
    cta: 'Discuss your idea',
  },
  {
    name: 'Influencer marketing',
    description:
      'Creator-led campaigns that help your brand reach the right audience and turn attention into enquiries.',
    features: [
      'Influencer discovery',
      'Campaign strategy',
      'Content planning',
      'Brand collaborations',
      'Launch promotions',
      'Performance tracking',
      'Lead generation campaigns',
    ],
    cta: 'Plan my campaign',
  },
];
export function validateLead(data: Record<string, unknown>): string | null {
  for (const key of [
    'name',
    'business',
    'phone',
    'email',
    'industry',
    'need',
    'message',
  ])
    if (typeof data[key] !== 'string' || !(data[key] as string).trim())
      return 'Please complete all fields.';
  for (const key of ['name', 'business', 'email'])
    if ((data[key] as string).length > 160)
      return 'Please keep your name, business name and email under 160 characters.';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email as string))
    return 'Please enter a valid email address.';
  if (
    !/^[+\d\s().-]{7,24}$/.test(data.phone as string) ||
    (data.phone as string).replace(/\D/g, '').length < 7
  )
    return 'Please enter a valid phone number, including your country code.';
  if (
    !needs.includes(data.need as string) ||
    !industries.includes(data.industry as string)
  )
    return 'Please select a valid service and business type.';
  if (
    (data.message as string).trim().length < 10 ||
    (data.message as string).length > 4000
  )
    return 'Please write a message between 10 and 4,000 characters.';
  return null;
}
