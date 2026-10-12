from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PDF = OUT / 'Astra-Automation-US-Web-Development-Pricing.pdf'
pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold')
pdfmetrics.registerFont(TTFont('Rupee', '/Users/sudarshan/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/fonts/DejaVuSans.ttf'))
W,H = 595.28,841.89
NAVY='#0B1424'; INK='#1B293E'; MUTED='#56647A'; RED='#8B2146'; BLUE='#1D6388'; LIGHT='#F1F5FA'
c=canvas.Canvas(str(PDF),pagesize=(W,H))
c.setTitle('Astra Automation | US Web Development Packages | USD')
c.setAuthor('Astra Automation')

def box(x,y,w,h,color,r=10):
    c.setFillColor(HexColor(color)); c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=0)
def txt(s,x,y,size=12,color=INK,bold=False):
    family='ArialBold' if bold else 'Arial'
    c.setFillColor(HexColor(color))
    for run in re.split('(₹)',s):
        f='Rupee' if run=='₹' else family
        c.setFont(f,size);c.drawString(x,H-y-size,run);x+=pdfmetrics.stringWidth(run,f,size)
def para(s,x,y,w=507,size=11.2,color=INK,leading=None):
    s=s.replace('₹','<font name="Rupee">₹</font>')
    p=Paragraph(s,ParagraphStyle('p',fontName='Arial',fontSize=size,leading=leading or size*1.38,textColor=HexColor(color)))
    _,height=p.wrap(w,800);p.drawOn(c,x,H-y-height)
    assert y+height<805,(s,y,height)
    return height
def line(y):
    c.setStrokeColor(HexColor('#DCE3ED'));c.line(44,H-y,W-44,H-y)
def base(page,kicker,title):
    c.setFillColor(white);c.rect(0,0,W,H,fill=1,stroke=0)
    box(0,0,W,130,NAVY,0)
    box(40,25,44,44,'#FFFFFF',8)
    c.drawImage(str(ROOT/'public/astra-mark.png'),44,H-64,36,36,mask='auto')
    txt('ASTRA AUTOMATION',97,26,18,'#FFFFFF',True)
    txt('WE BUILD YOUR GROWTH ONLINE',98,52,8.5,'#B4C9DF')
    txt(kicker,44,87,10,'#92C9EA',True)
    txt(title,44,151,26,NAVY,True)
    line(795)
    txt('Astra Automation  /  Web development only',44,808,8.2,MUTED)
    txt(f'September 2026  |  {page}/3',425,808,8.2,MUTED)
def package(y,name,price,maintenance,summary,features,timing):
    box(44,y,507,155,LIGHT)
    box(44,y,5,155,RED,0)
    txt(name,61,y+10,16,NAVY,True)
    para(summary,61,y+34,469,10.2,MUTED)
    para(features,61,y+54,469,10.5)
    txt(timing,61,y+90,9.8,BLUE,True)
    box(57,y+109,481,40,'#E4EBF3',5)
    c.setStrokeColor(HexColor('#C7D1DF'));c.line(298,H-y-115,298,H-y-144)
    txt('Website development (one-time)',67,y+114,9,MUTED)
    txt(price,67,y+127,16,RED,True)
    txt('Maintenance (optional, billed separately)',310,y+114,9,MUTED)
    txt(maintenance+' / month',310,y+127,16,BLUE,True)

base(1,'US CLIENT PRICING  /  ALL PRICES IN USD','A website built for your business.')
para('Clear scope. Mobile-friendly design. Transparent build and running costs.',44,191,507,12,MUTED)
package(218,'01  Launch page','US$399','US$14','For one offer, a new launch or a professional introduction.',
        '1 scrolling page, up to 6 sections • Email and click-to-call buttons<br/>Social links • Search-engine setup • Developer-managed content',
        'Delivery: 5-7 working days  |  2 revision rounds')
package(379,'02  Business website','US$799','US$28','For service businesses that need a complete online presence.',
        'Up to 5 pages • Contact form to one email inbox • Map embed<br/>Service/gallery sections • Search-engine setup • Developer-managed content',
        'Delivery: 10-15 working days  |  2 revision rounds')
package(540,'03  Managed-content website','US$1,299','US$56','For businesses that want to update their own content.',
        'Up to 10 public pages • 1 admin login • Edit service and blog entries<br/>Store inquiries and export CSV • Up to 20 initial entries • Database setup',
        'Delivery: 15-25 working days  |  3 revision rounds')
para('<b>Every package includes:</b> responsive layouts using your branding and content, image optimization, page titles/meta descriptions, sitemap, SSL/domain connection, launch testing and 30-day bug-fix support.',44,711,507,11)
para('Optional maintenance, backend hosting, database, domain and applicable taxes are separate from the build price. Your written quote confirms the full scope and any frontend hosting arrangements.',44,767,507,9.4,MUTED)
c.showPage()

base(2,'PLAN WITH CONFIDENCE','Your website. A clear cost plan.')
para('All prices in USD, before applicable taxes. Providers bill separately at actual cost.',44,192,507,11.5,MUTED)
cols=[44,285,422]; widths=[241,137,129]
box(44,228,507,30,NAVY,5)
for x,s in zip(cols,['Running cost','Monthly','Annual']):txt(s,x+12,235,10.7,'#FFFFFF',True)
rows=[('Render Starter backend - package 03','$7','$84'),('MongoDB Atlas Flex DB - package 03','From ~$8','From ~$96'),('Standard domain - budget allowance','Annual billing','$25'),('SSL certificate / HTTPS','Included','$0')]
for i,row in enumerate(rows):
    yy=258+i*34
    if i%2==0:box(44,yy,507,34,LIGHT,0)
    for x,s in zip(cols,row):txt(s,x+12,yy+9,10.3,INK,i==0)
para('<b>Cost basis:</b> Render Starter hosts the backend. MongoDB Atlas Flex is the database: $8 base per 30 days with 5 GB, scaling with usage to $30 per 30 days; billed hourly. <b>Both apply to package 03.</b> Annual figures use 12 monthly estimates. Domain is a $25 planning allowance, not a provider quote. Frontend hosting is outside these totals.',44,404,507,10.1,MUTED)

txt('Optional monthly care',44,493,17,NAVY,True)
para('<b>Launch US$14</b> (30 minutes)  •  <b>Business US$28</b> (1 hour)  •  <b>Managed US$56</b> (2 hours)',44,522,507,10.5)
para('Monthly health check, dependency review and minor text/image edits within your monthly allowance (unused time expires each month). Managed care adds a monthly database export and quarterly restore check. Further work is agreed with you at US$28/hour.',44,548,507,10.4,MUTED)
box(44,609,507,31,NAVY,5)
for x,s in zip([56,261,373,460],['Package','Year 1*','Renewal/year*','Optional care/mo']):txt(s,x,618,8.7,'#FFFFFF',True)
build=[399,799,1299]; care=[14,28,56]; totals=[]
for i,name in enumerate(['Launch page','Business website','Managed-content']):
    annual=25+12*care[i]+(84+96 if i==2 else 0)
    total=annual+build[i];totals.append({'package':name,'build':build[i],'annual_including_care':annual,'first_year_including_care':total})
    yy=640+i*32;box(44,yy,507,32,LIGHT if i%2==0 else '#FFFFFF',0)
    for x,s in zip([56,261,373,460],[name,f'${total:,}',f'${annual:,}',f'${care[i]:,}']):txt(s,x,yy+8,10.3,INK)
para('*Includes build (year 1 only), domain, Render backend + MongoDB database for package 03, and 12 months of optional care. Without care, deduct $168 / $336 / $672 respectively. Excludes frontend hosting, taxes and additional usage. Provider estimates assume base usage and unchanged rates.',44,749,507,9.4,MUTED)
c.showPage()

base(3,'WORKING TOGETHER','Your project, step by step.')
terms=[
('Comfortable payment milestones','Reserve your project with 50%, pay 30% once you approve the design, and the final 20% before launch and source handover. Domain and provider costs are paid upfront or directly to the provider. Your written quotation is valid for 15 days.'),
('Design shaped by your feedback','Each package covers one language and one agreed design direction. A revision round brings your feedback together in one list within that scope. Additional standard pages start at US$28; further revisions are US$14/hour. We agree estimates for additions before proceeding.'),
('Planning your launch together','Please share your final text, brand assets, images and required access. Delivery starts once the advance and these inputs are ready. Feedback within 3 working days helps keep the schedule; if more time is needed, we adjust the launch date together. Copywriting and migration are separate services.'),
('Your backend, database and domain','We recommend keeping billing accounts in your name. Package 03 uses Render Starter for backend hosting and MongoDB Atlas Flex for the database; both appear in its running-cost totals. Packages 01/02 have no dedicated backend or paid database charge. Domain renewals are at actual cost.'),
('Choosing supporting services','Frontend hosting arrangements and any cost responsibility are agreed before launch; no frontend hosting subscription is included in these totals. Backend and database charges depend on provider usage and rates. Email, mailboxes, paid media and external APIs are additional at actual cost.'),
('Support after your launch','Enjoy 30 days of bug fixes within the delivered scope. Optional care is paid monthly in advance and may be canceled before the next cycle. Support is Mon-Fri, 10am-6pm IST, excluding holidays, with a first response within 2 working days. Resolution time depends on the issue; redesigns and new features are quoted separately.'),
('Your website and flexibility','After full payment, you receive the source files and agreed admin access. Third-party licenses continue to apply. If plans change, we settle completed work and non-recoverable provider costs, refund the unused advance and hand over the work paid for.'),
('A shared understanding','Checkout, payments, customer accounts, booking engines, automation and marketing are separate services. Rankings, inquiry volumes and uninterrupted availability are not guaranteed. Before launch, you approve content and privacy/consent text and confirm rights to supplied materials. Applicable taxes are shown on the invoice.')]
y=200
for title,body in terms:
    txt(title,44,y,10.5,BLUE,True)
    ht=para(body,44,y+16,507,9.7,INK,12.6);y+=ht+26
assert y<747,y
para('<b>Let us bring your ideas online.</b> Share your preferred package, required pages and reference websites. Visit <link href="https://astra-automation.vercel.app/" color="#1D6388">astra-automation.vercel.app</link> to start a conversation and request a written quote.',44,739,507,10.1)
para('Pricing checked Sep 2026: <link href="https://render.com/pricing" color="#1D6388">Render</link> • <link href="https://www.mongodb.com/docs/atlas/billing/atlas-flex-costs/" color="#1D6388">MongoDB Atlas Flex</link> • <link href="https://www.godaddy.com/domains" color="#1D6388">Confirm domain quote</link>',44,779,507,7.6,MUTED)
c.save()
(OUT/'us-pricing-calculations.json').write_text(json.dumps(totals,indent=2))
r=PdfReader(str(PDF));assert len(r.pages)==3
assert all('Astra Automation' in p.extract_text() for p in r.pages)
print(PDF);print(json.dumps(totals));print('3 pages; text checks passed')
