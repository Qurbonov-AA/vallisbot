Token = "2055853816:AAFP99lG-PeNwKnvJ2LhjxKqIC0E3nQuBtY"

cat_url = "http://feruzbackend.backoffice.uz/api/product/category-list/"

pro_by_car_url = "http://feruzbackend.backoffice.uz/api/product/category-product/"

pro_buy_price_url = "http://feruzbackend.backoffice.uz/api/product/product-detail/"

client_url    = "http://feruzbackend.backoffice.uz/api/client/client-list/"

order_post_url = "http://feruzbackend.backoffice.uz/api/order/sell-order-list-bot/"

order_get_url = "http://feruzbackend.backoffice.uz/api/order/get-client-order/"


main_btn = [ 'Kategoriyani tanlang', 'Savatcha', "Buyurtmalar tarixi",'Hisob kitob','Info' ] 

storys = ["Kunlik","Haftalik","Oylik","Yillik"] 

pag_btn  = [1,2,3,4,5,6,7,8,9,10] 

orders = [] 

prices = [
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/0iswgkniect31-UZ/image;s=1000x700',
    'Maxsulot' : 'Gidra',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '100 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/e2637thdfs7g3-UZ/image;s=1000x700',
    'Maxsulot' : 'Truba',
    'Omborda mavjud miqdor' : '1000 m',
    'Narxi' : '1.5 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/wktkn0rihxib2-UZ/image;s=1000x700',
    'Maxsulot' : 'Konalizatsiya trubasi',
    'Omborda mavjud miqdor' : '2000 m',
    'Narxi' : '15 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://tovar.uz/images/company/989/tovar/53210/o_1_5fb797b4e0ece.png',
    'Maxsulot' : 'Ariston',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '19 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/kebq88fivp1q2-UZ/image;s=1000x700',
    'Maxsulot' : 'Vanna',
    'Omborda mavjud miqdor' : 50,
    'Narxi' : '30 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://images.app.goo.gl/CmQwkX34SvwdHjCn6',
    'Maxsulot' : 'macbook',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '1500$',
    'Skidka' : '90%'
    },
    {
    'img' : 'https://images.app.goo.gl/Co7qMJBTN1zkrCd57',
    'Maxsulot' : 'mac pro',
    'Omborda mavjud miqdor' : 5,
    'Narxi' : '5000$',
    'Skidka' : '5%'
    },
    {
    'img' : 'https://images.app.goo.gl/sTfXyUiNoLVe99V77',
    'Maxsulot' : 'imac 27',
    'Omborda mavjud miqdor' : 20,
    'Narxi' : '1800$',
    'Skidka' : '40%'
    },
    {
    'img' : "https:\\ireland.apollo.olxcdn.com\v1\files\q9b42extxhf12-UA\image;s=644x461",
    'Maxsulot' : "Переоборудование под насос дозатор МТЗ-80/82 ЮМЗ Т25/40/150 блокировка",
    'Omborda mavjud miqdor' : 10,
    'Narxi' : "39$" ,
    'Skidka' : '5%'
    },
    {
    'img' : "https://apollo-olx.cdnvideo.ru/v1/files/vyrz3e8vw3wp3-UZ/image;s=644x461",
    'Maxsulot' : "DXN енергия плюс сув филтри",
    'Omborda mavjud miqdor' : 15,
    'Narxi' :"7$" ,
    'Skidka' : '3%'
    },
    {
    'img' : "https://ireland.apollo.olxcdn.com/v1/files/ily8fjyi1jhn2-UA/image;s=644x461",
    'Maxsulot' : "Комплект переоборудования под дозатор МТЗ 80/82,ЮМЗ,Т40,Т25 Беларусь",
    'Omborda mavjud miqdor' : 1,
    'Narxi' : "160$" ,
    'Skidka' : '5%'
    },
    {
    'img' : "https://ireland.apollo.olxcdn.com/v1/files/37stako46xh13-UA/image;s=644x461",
    'Maxsulot' : "Муфта Elaflex SSB 16.1 поворотная разрывная на кран раздаточный",
    'Omborda mavjud miqdor' : 2,
    'Narxi' : "40$" ,
    'Skidka' : '0%'
    },
    {
    'img' : "https://ireland.apollo.olxcdn.com/v1/files/1joag99afu1q2-UA/image;s=644x461",
    'Maxsulot' : "Муфта на кран раздаточный",
    'Omborda mavjud miqdor' : 200,
    'Narxi' : "4$",
    'Skidka' : '0%'
    },
    {
    'img' : "https://ae04.alicdn.com/kf/H3a81894359d1492b9db920f4deecb2beD/1-5M-2M-3M-Stainless-Steel-Flexible-Bathtub-Shower-Head-Silicone-Hose-Hose-Washer-Bathroom-Accessories.jpg_220x220xzq55.jpg",
    'Maxsulot' : "Dush uchun nasadka",
    'Omborda mavjud miqdor':100,
    'Narxi' : "99000",
    'Skidka' : '2%'
    },
    {
    'img' : "https://ae04.alicdn.com/kf/H82e8b524210942eba666b6d36b9f3193P/-.jpg",
    'Maxsulot' : "Krasovka",
    'Omborda mavjud miqdor' : 250,
    'Narxi' : "250000",
    'Skidka' : '3%'
    },
    {
    'img' : "https://ae04.alicdn.com/kf/Hdbfb7a37f5eb420ea87a011d53c1a8dbS/-.jpg",
    'Maxsulot' : "Noutbook uchun patstavka",
    'Omborda mavjud miqdor': 50,
    'Narxi' : "150000",
    'Skidka' : '5%'
    },
    {
    'img' : "https://ae04.alicdn.com/kf/H2d8e9454177d42bf9a9ab557e5877addo/IP-1080P-PTZ-Wi-Fi-4.jpg",
    'Maxsulot' : "IP-kamera",
    'Omborda mavjud miqdor' :200,
    'Narxi' : "550000",
    'Skidka' : '4%'
    },
    {
    'img' : "https://ae04.alicdn.com/kf/Hefe0534bbce049c09008fdf51cbe1472n/Voteer-USB-Type-C-Micro-Lightning-iPhone-Android.jpg",
    'Maxsulot' : "Magnit adapter USB Type-C/Micro/Lightning",
    'Omborda mavjud miqdor' :500,
    'Narxi' : "30000",
    'Skidka' : '4%'
    },
    {
    'img' : 'https://images.app.goo.gl/vNGivYy6z1vQFfCn9',
    'Maxsulot' : 'iphone 13 pro max',
    'Omborda mavjud miqdor' : 100,
    'Narxi' : '1000$',
    'Skidka' : '60%'
    },
    {
    'img' : 'https://images.app.goo.gl/DGe49kcNU9QEMXuJ7',
    'Maxsulot' : 'Samsung A21',
    'Omborda mavjud miqdor' : 200,
    'Narxi' : '700$',
    'Skidka' : '95%'
    },
    {
    'img' : "https://images.app.goo.gl/CWnHhhTGHCe6Kxcv5",
    'Maxsulot' : "smistitel",
    'Omborda mavjud miqdor' : 5,
    'Narxi' : "100000",
    'Skidka' : '6%'
    },
    {
    'img': "0j16&client=ms-android-xiaomi&sourceid=chrome-mobile&ie=UTF-8#imgrc=bo7RmTDPEHeerM", 
    'Maxsulot' :"unitaz",
    'Omborda mavjud miqdor' : 58,
    'Narxi' : "800000",
    'Skidka' : '6%'
    },
    {
    'img' :'https://images.app.goo.gl/gPUkW3QLKxvpTE5E7',
    'Maxsulot' :"unitaz zs",
    'Omborda mavjud miqdor' : 8,
    'Narxi' : "50000",
    'Skidka' : '6%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/0iswgkniect31-UZ/image;s=1000x700',
    'Maxsulot' : 'Gidra',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '100 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/e2637thdfs7g3-UZ/image;s=1000x700',
    'Maxsulot' : 'Truba',
    'Omborda mavjud miqdor' : '1000 m',
    'Narxi' : '1.5 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/wktkn0rihxib2-UZ/image;s=1000x700',
    'Maxsulot' : 'Konalizatsiya trubasi',
    'Omborda mavjud miqdor' : '2000 m',
    'Narxi' : '15 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://tovar.uz/images/company/989/tovar/53210/o_1_5fb797b4e0ece.png',
    'Maxsulot' : 'Ariston',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '19 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://apollo-olx.cdnvideo.ru/v1/files/kebq88fivp1q2-UZ/image;s=1000x700',
    'Maxsulot' : 'Vanna',
    'Omborda mavjud miqdor' : 50,
    'Narxi' : '30 $',
    'Skidka' : '2%'
    },
    {
    'img' : 'https://images.app.goo.gl/96gJfi3e4M5LXvTF7',
    'Maxsulot' : 'путниковая антена',
    'Omborda mavjud miqdor' : 3,
    'Narxi' : '1000000$',
    'Skidka' : '0%'
    },
    {
    'img' : 'https://images.app.goo.gl/Z3T9nkwdtuwQZbYXA',
    'Maxsulot' : 'Вертолет',
    'Omborda mavjud miqdor' : 18,
    'Narxi' : '5000000$',
    'Skidka' : '100%'
    },
    {
    'img' : 'https://images.app.goo.gl/uZkiSzvt4czGMahJ6',
    'Maxsulot' : 'Частный самолет',
    'Omborda mavjud miqdor' : 13,
    'Narxi' : '100000$',
    'Skidka' : '1%'
    },
    {
    'img' : 'https://images.app.goo.gl/7KYxXkiMUbHsvnwX6',
    'Maxsulot' : 'Ройс ролс',
    'Omborda mavjud miqdor' : 1,
    'Narxi' : '500000$',
    'Skidka' : '10%'
    },
    {
    'img' : 'https://images.app.goo.gl/opp15s9JPBqyaHNu6',
    'Maxsulot' : 'МЕРСЕДЕС АВАТАР',
    'Omborda mavjud miqdor' : 1,
    'Narxi' : '5000000$',
    'Skidka' : '15%'
    },
    {
    'img' : 'https://images.app.goo.gl/jB62rFSuuP49HrLz6',
    'Maxsulot' : 'картина монализы',
    'Omborda mavjud miqdor' : 1,
    'Narxi' : '5000000$',
    'Skidka' : '0%'
    },
    {
    'img' : 'https://images.app.goo.gl/ExCVD294E1sTYCce9',
    'Maxsulot' : 'tesla model s',
    'Omborda mavjud miqdor' : 100,
    'Narxi' : '3.2M$',
    'Skidka' : '18%'
    },
    {
    'img' : 'https://images.app.goo.gl/JgzfTW7vcM9WZwWa8',
    'Maxsulot' : 'tesla model x',
    'Omborda mavjud miqdor' : 191,
    'Narxi' : '135k$',
    'Skidka' : '20%'
    },
    {
    'img' : 'https://images.app.goo.gl/vpwPibcbVJZezWZi6',
    'Maxsulot' : 'Космическая ракета',
    'Omborda mavjud miqdor' : 10,
    'Narxi' : '150М$',
    'Skidka' : '7%'
    },
    {
    'img' : 'https://images.app.goo.gl/JZ43TnmhL7bow3Q17',
    'Maxsulot' : 'Планета Марс',
    'Omborda mavjud miqdor' : 1,
    'Narxi' : '100B$',
    'Skidka' : '4%'
    },
]