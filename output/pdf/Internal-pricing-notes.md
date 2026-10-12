# Internal only - Astra 45% margin pricing, 16 September 2026

Do not send internal cost and margin notes to leads.

## Service margin model

Target: 45% operating profit before income tax on Astra service revenue only. Labour remains INR 400/hour, with 15% of service fees allocated to sales, tools, administration and rework. These are assumptions, not guaranteed results.

Price = labour cost / (1 - 0.15 - 0.45) = labour cost / 0.40.

| Package | Price | Labour | Overhead | Operating profit | Margin |
|---|---:|---:|---:|---:|---:|
| Launch | 12,000 | 4,800 | 1,800 | 5,400 | 45% |
| Business | 24,000 | 9,600 | 3,600 | 10,800 | 45% |
| Managed | 42,000 | 16,800 | 6,300 | 18,900 | 45% |

Monthly maintenance: INR 500 / 1,000 / 2,000 for 0.5 / 1 / 2 hours. Labour costs are INR 200 / 400 / 800; overhead is INR 75 / 150 / 300; profit is INR 225 / 450 / 900 (45% each). All monitoring, checks and support consume that allowance.
Additional work is INR 1,000/hour (INR 400 labour + INR 150 overhead + INR 450 operating profit). Additional standard pages start at INR 2,000, assuming no more than two hours. Re-quote more complex work.
Build hours must cover delivery, testing and expected warranty support. Discounting or exceeding these costs reduces the margin below 45%. After-income-tax profit requires the applicable effective tax rate. Provider charges are pass-through and excluded from service-margin percentages.

## Provider calculation - Render backend plus MongoDB database

Corrected scope: Render Starter hosts the backend; MongoDB Atlas Flex is the database. Both apply to package 03. They are complementary services, not competing database options. No Render PostgreSQL charge is included. No frontend hosting subscription charge is included. This is a brochure update only; no live service has been migrated, cancelled or purchased.

Planning conversion: INR 90/USD (not a live FX rate). Render Starter USD 7/month = INR 630/month or INR 7,560/year. MongoDB Atlas Flex starts at USD 8/month = INR 720/month or INR 8,640/year at base usage; the Flex cluster fee scales with usage to USD 30/month and is billed hourly. Domain allowance INR 2,000/year; exact registration/renewal quote required. SSL setup included.

| Package | Build | Domain/year | Render backend/year | MongoDB base/year | Optional care/year | Year 1 with care | Renewal with care |
|---|---:|---:|---:|---:|---:|---:|---:|
| Launch | 12,000 | 2,000 | 0 | 0 | 6,000 | 20,000 | 8,000 |
| Business | 24,000 | 2,000 | 0 | 0 | 12,000 | 38,000 | 14,000 |
| Managed | 42,000 | 2,000 | 7,560 | 8,640 | 24,000 | 84,200 | 42,200 |

Without care, first-year totals are INR 14,000 / 26,000 / 60,200; renewals are INR 2,000 / 2,000 / 18,200. Managed-content backend plus database is INR 1,350/month at base usage. Provider bills are pass-through costs carrying no profit. Estimates exclude frontend hosting, taxes, FX/card fees and additional usage; assume unchanged rates. Hosting fee removal does not eliminate actual provider costs. Agree frontend hosting and who pays before launch; if Astra absorbs costs, recalculate the 45% service margin. Confirm sizing for actual workload.

Sources:
- https://render.com/pricing (checked 15 September 2026)
- https://render.com/articles/render-vs-railway (Starter backend USD 7/month)
- https://www.mongodb.com/docs/atlas/billing/atlas-flex-costs/ (checked 16 September 2026)
- https://www.godaddy.com/en-in/domains (exact quote required)
