import qrcode
import base64
import tinyurl
import csv

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

PATH = "/Users/oluwasemilore/projects/ubaqrcode/uba/%s/"

result = ['abiodun_lateef', 'chinye_nwabuzor', 'olutayo_patience', 'odianosen_ewah', 'ogochukwu_amaefunah', 'ogochukwu_chigbo']
#result = ['Jeremiah_Essien', 'Adetokunbo_Alegbejo',  'Ali_Wali', 'Abiodun_Agoro', 'Veronica_Nwosisi']
#name = "abiodun_lateef"
#URL = "https://scannerqr.herokuapp.com/advertapp/?influencer=%s"
#URL = "http://download.airtel.ng/checkinfluencer/?anchor=%s&app=airteltv"
URL = "http://127.0.0.1:8000/checkinfluencer/?anchor=%s&app=ubamobile"
app = []


def create_qr(app, path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # name = 'Lagos_A%s' % i
    # print name
    # # final = URL % name
    # # print(final)
    # # #result = base64.b64encode(b'tunde_instagram')
    # result = base64.b64encode(name)
    # final = URL % result
    name, url =  app.split(",")
    print(url)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save(path + "%s.png" % name)


def new():
    #LOCATION = ['NE', 'NW', 'SOUTH', 'WEST']
    #app = []
    #for loc in LOCATION:
    app = []
    #loc = 'NE'
    LOCATION = ['HQ']
    #path = PATH % loc
    print("initiated")
    #[app.append("%s, %s" % ('%s_A%s' % (loc, i), tinyurl.create_one(URL % base64.b64encode('%s_A%s' % (loc, i))))) for i in range(1, 501)]

    for loc in LOCATION:
        path = PATH % loc
        for i in range(1, 2):
            print(i)
            app.append("%s, %s" % ('%s_ubaM_%s' % (loc, i), tinyurl.create_one(URL % base64.b64encode('%s_A%s' % (loc, i)))))

        with open(PATH % loc + '%sA500.csv' % loc, mode='w') as a500:
            new_csv = csv.writer(a500, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for ap in app:
                new_csv.writerow([ap])
                create_qr(ap, path)
        app = []


print("Starting")
new()
print("Completed")

#
# for i in range(501):
#     try:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         name = 'Lagos_A%s' % i
#         print name
#         #final = URL % name
#         #print(final)
#         # #result = base64.b64encode(b'tunde_instagram')
#         result = base64.b64encode(name)
#         final = URL % result
#         print(final)
#         qr.add_data(final)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color="black", back_color="white")
#         img.save(PATH % "%s.png" % i)
#     except  Exception, ex:
#         print(ex)
#         pass
#
#

name = "uba"
url = tinyurl.create_one(URL % name)
print(url)
#URL = "http://airtel.com.ng/HBB/?influencer=%s"
#result = base64.b64encode(b'tunde_instagram')
result = base64.b64encode(name)
final = URL % str(result, 'utf-8')
print(final)
qr.add_data(final)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
#base64.b64encode(b'data to be encoded')
#base64.b64decode(red)
img.save("%s.png" % str(name, 'utf-8'))
# import qrcode
# img = qrcode_new.make('Some data here')