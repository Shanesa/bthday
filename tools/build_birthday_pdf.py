from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'output/pdf/happy-birthday-king.pdf'
URL = 'https://shanesa.github.io/bthday/'
for name, file in [('Serif','/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'),('Italic','/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf'),('Sans','/usr/share/fonts/truetype/lato/Lato-Regular.ttf'),('Bold','/usr/share/fonts/truetype/lato/Lato-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,file))
INK=HexColor('#102e35'); PAPER=HexColor('#f8f6ef'); MINT=HexColor('#c7dcca'); GOLD=HexColor('#c6a775'); MUTED=HexColor('#5f6b64')
c=canvas.Canvas(str(DEST), pagesize=(600,900), pageCompression=1)
c.setTitle('Happy Birthday, Dear King')
c.setAuthor('A little birthday love')
c.setSubject('A birthday keepsake with a link to the interactive card')
c.setFillColor(INK); c.rect(0,0,600,900,fill=1,stroke=0)
c.setStrokeColor(GOLD); c.setLineWidth(.5); c.rect(17,17,566,866)

def text(x,y,s,font,size,color):
    c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,s)
def center(y,s,font,size,color):
    c.setFillColor(color);c.setFont(font,size);c.drawCentredString(300,y,s)
def tracking(x,y,s,size=8,color=MINT,spacing=1.8):
    c.saveState();t=c.beginText(x,y);t.setFont('Sans',size);t.setFillColor(color);t.setCharSpace(spacing);t.textLine(s);c.drawText(t);c.restoreState()
def para(s,x,top,width,size=13,leading=19,color=MUTED,font='Sans'):
    p=Paragraph(s,ParagraphStyle('body',fontName=font,fontSize=size,leading=leading,textColor=color))
    _,h=p.wrap(width,600);p.drawOn(c,x,top-h);return top-h

def heart(x,y,size,color):
    c.saveState();c.translate(x,y);c.scale(size/24,size/24);c.setStrokeColor(color);c.setLineWidth(1)
    p=c.beginPath();p.moveTo(12,2);p.curveTo(-6,13,1,25,12,17);p.curveTo(23,25,30,13,12,2);c.drawPath(p);c.restoreState()

tracking(45,850,'A LITTLE BIRTHDAY LOVE',9,MINT,2.3)
heart(535,844,19,GOLD)
c.setStrokeColor(Color(.78,.86,.79,.25));c.line(45,829,555,829)
# A restrained crown for the birthday king.
c.setStrokeColor(GOLD);c.setLineWidth(1.3)
p=c.beginPath();p.moveTo(48,783);p.lineTo(44,802);p.lineTo(58,793);p.lineTo(70,809);p.lineTo(82,793);p.lineTo(96,802);p.lineTo(92,783);p.close();c.drawPath(p);c.line(48,777,92,777)
text(44,719,'Happy','Serif',55,PAPER)
text(44,661,'Birthday,','Serif',55,PAPER)
text(46,609,'dear king.','Italic',41,MINT)
text(47,571,'Doctor to the world.','Sans',11,PAPER)
text(47,551,'A king with a heart of gold.','Sans',11,PAPER)
# Preserve the supplied photograph, with a simple keepsake frame.
c.saveState();c.translate(434,679);c.rotate(3)
c.setFillColor(Color(0,0,0,.15));c.rect(-108,-151,220,282,fill=1,stroke=0)
c.setFillColor(PAPER);c.rect(-113,-145,220,282,fill=1,stroke=0)
c.drawImage(str(ROOT/'assets/brother.png'),-105,-107,width=204,height=236,preserveAspectRatio=True,anchor='c',mask='auto')
tracking(-86,-130,'ONE OF A KIND',7,INK,2)
heart(70,-134,15,GOLD)
c.restoreState()
# ECG accent and celebratory line.
c.setStrokeColor(GOLD);c.setLineWidth(1)
p=c.beginPath();p.moveTo(47,512)
for x,y in [(80,512),(87,519),(95,499),(105,530),(115,507),(122,512),(154,512)]:p.lineTo(x,y)
c.drawPath(p)
center(477,'A GOOD HEART. A GREAT DOCTOR. A TRUE KING.','Sans',9,MINT)
# The message has its own generous, quiet paper panel.
c.setFillColor(PAPER);c.roundRect(29,29,542,420,5,fill=1,stroke=0)
tracking(54,419,'SOME THINGS DESERVE TO BE SAID',7,MUTED,1.6)
text(54,384,'My king. My guide. My second father.','Italic',25,INK)
text(54,348,'Dear king,','Italic',19,INK)
y=para('To the world, you are a doctor. To me, you are a king with a heart of gold - a second father, a guiding hand, and someone I know I can always count on.',54,328,490)
y=para('Thank you for looking out for me, believing in me, and making me feel that I never have to face life alone. Today, I hope all the love you give finds its way back to you.',54,y-13,490)
y=para('May this next chapter bring you good health, quiet joy, dreams coming true, and every reason to smile.',54,y-13,490)
assert y>165, y
text(54,164,'So lucky to have you in my life.','Italic',17,INK)
# A real PDF link, plus a scan-friendly vector QR.
c.setStrokeColor(HexColor('#d9dfd4'));c.setLineWidth(.5);c.line(54,146,546,146)
c.setFillColor(INK);c.roundRect(54,88,343,39,3,fill=1,stroke=0)
c.setFillColor(PAPER);c.setFont('Bold',12);c.drawCentredString(225.5,102,'Open your digital birthday surprise')
c.linkURL(URL,(54,88,397,127),relative=0,thickness=0)
text(54,69,'shanesa.github.io/bthday/','Sans',10,MUTED)
c.linkURL(URL,(54,64,225,80),relative=0,thickness=0)
text(54,49,'Happy birthday. Always cheering for you.','Italic',11,INK)
heart(253,46,12,INK)
qr=QrCodeWidget(URL,barFillColor=INK,barBorder=4)
x0,y0,x1,y1=qr.getBounds();size=92
d=Drawing(size,size,transform=[size/(x1-x0),0,0,size/(y1-y0),0,0]);d.add(qr);renderPDF.draw(d,c,448,49)
c.linkURL(URL,(448,49,540,141),relative=0,thickness=0)
c.showPage();c.save()
print(DEST)
