import type { MetadataRoute } from 'next';
export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://astra-automation.sudarshankillekar199.chatgpt.site/',
      changeFrequency: 'monthly',
      priority: 1,
    },
  ];
}
