from django.shortcuts import render, HttpResponse
from reportlab.pdfgen import canvas
from django.core.mail import EmailMessage

def web_page(request):
    print "WOW"
    if request.method =="POST":
        detail = request.POST
        detail_currency =detail.get('currency')
        detail_payment = detail.get('payment')
        detail_name =  detail.get('name')
        detail_email = detail.get('email')
        money_in_inr = 0
        print detail
        if detail_currency == "pound":
            money_in_inr = int(detail_payment)*99.59
            print money_in_inr

        elif detail_currency == "dollar":
            money_in_inr = int(detail_payment)*65.03
            print money_in_inr

        elif detail_currency == "euro":
            money_in_inr = int(detail_payment)*71.63
            print money_in_inr

        elif detail_currency == "yen":
            money_in_inr = int(detail_payment)*0.54
            print money_in_inr


        print money_in_inr
        c = canvas.Canvas("invoice.pdf")
        c.drawString(100,650,"Name : " +  detail_name)
        c.drawString(100,600,"Currency Type : " + detail_currency)
        c.drawString(100,550,"Amount in INR : " +  str(money_in_inr))
        c.drawString(100,500,"Email Id : " + detail_email)
        c.save()
        msg = EmailMessage("INVOICE!","Hey, Please find attached the Invoice! :D ",'aishwarya.khanna@st.niituniverisity.in',[detail_email])
        attachment = open('invoice.pdf','rb')
        msg.attach('invoice.pdf',attachment.read())
        msg.send()
        return HttpResponse("Hello we will email you shortly")
    else:
        return render(request, "webpage.html")




