# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 16:39:51 2018

@author: ibm
"""

#Create a fictitious data file with following fields
#personal id - e.g. ssn
#first name
#last name
#sex
#age - 2 digit integer
#salary
#DOB
#avg spending per month


from faker import Faker
fake = Faker()    #Default usage

#%% - create data
#fake.ssn() from faker.providers.ssn
print fake.ssn()  
print fake.name()

my_word_list = ['python','anaconda','custom','bit','default','may','copyright','type','credits','license','more','information']

print fake.sentence(ext_word_list=my_word_list)


#%% - Using FactoryBoy
import factory
from myapp.models import Book

class BookFactory (factory.Factory):
    class Meta:
        model = Book
    
    title = factory.Faker('sentence', nb_words=4)
    author_name = factory.Faker('name')

#How to use it ???
    
#%% - All the fields for en_GB and hi_HI

fake = Faker('en_GB')    #Default usage

#for faker.providers.address
print fake.city()
# 'Port Natalie'

print fake.geo_coordinate(center=None, radius=0.001)
# Decimal('-112.433299')

print fake.building_number()
# '250'

print fake.street_name()
# 'Kyle shoals'

print fake.address()
# '370 Todd club\nKayleighland\nLS1 0DT'

print fake.postcode()
# 'N3C 7AQ'

print fake.country_code()
# 'FR'

print fake.city_prefix()
# 'West'

print fake.latitude()
# Decimal('19.441471')

print fake.country()
# 'Bulgaria'

print fake.secondary_address()
# 'Studio 23'

print fake.street_suffix()
# 'gardens'

print fake.city_suffix()
# 'mouth'

print fake.longitude()
# Decimal('75.823840')

print fake.street_address()
# 'Studio 05\nStephen viaduct'

#for faker.providers.automotive
print fake.license_plate()
# 'NK82EFC'

#for faker.providers.bank

print fake.bban()
# 'MOYM6466229621705'

print fake.iban()
# 'GB79WFLS9112316260568'

print fake.bank_country()
# 'GB'

#for faker.providers.barcode

print fake.ean8()
# '12888665'

print fake.ean(length=13)
# '1893724632508'

print fake.ean13()
# '4834903539987'

#for faker.providers.color

print fake.hex_color()
# '#d65252'

print fake.color_name()
# 'DarkSeaGreen'

print fake.safe_color_name()
# 'white'

print fake.rgb_color()
# '135,209,120'

print fake.safe_hex_color()
# '#cc7700'

print fake.rgb_css_color()
# 'rgb(77,235,14)'

#for faker.providers.company
print fake.bs()
# 'transition integrated networks'

print fake.company()
# 'Graham, Edwards and Parry'

print fake.catch_phrase()
# 'Synergistic optimal neural-net'

print fake.company_suffix()
# 'PLC'

#for faker.providers.credit_card

print fake.credit_card_provider(card_type=None)
# 'Discover'

print fake.credit_card_number(card_type=None)
# '4474271364439055'

print fake.credit_card_security_code(card_type=None)
# '967'

print fake.credit_card_full(card_type=None)
# 'Maestro\nJohn Fisher\n569454134333 01/23\nCVV: 643\n'

print fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
# '10/27'

#for faker.providers.currency

print fake.cryptocurrency_code()
# 'DASH'

print fake.currency_name()
# 'CFP franc'

print fake.cryptocurrency()
# ('ZCL', 'Zclassic')

print fake.currency()
# ('JEP', 'Jersey pound')

print fake.cryptocurrency_name()
# 'Litecoin'

print fake.currency_code()
# 'TND'

#for faker.providers.date_time

print fake.date_this_year(before_today=True, after_today=False)
# datetime.date(2018, 5, 28)

print fake.timezone()
# 'Asia/Pyongyang'

print fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2018, 6, 3, 17, 32, 8)

print fake.past_date(start_date="-30d", tzinfo=None)
# datetime.date(2018, 5, 19)

print fake.month_name()
# 'December'

print fake.time_delta(end_datetime=None)
# datetime.timedelta(55, 14579)

print fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)
# datetime.datetime(1997, 7, 4, 18, 7, 41)

print fake.am_pm()
# 'PM'

print fake.day_of_month()
# '02'

print fake.date_this_century(before_today=True, after_today=False)
# datetime.date(2007, 1, 5)

print fake.iso8601(tzinfo=None, end_datetime=None)
# '1983-07-25T20:30:23'

print fake.date(pattern="%Y-%m-%d", end_datetime=None)
# '2003-07-05'

print fake.month()
# '02'

print fake.time(pattern="%H:%M:%S", end_datetime=None)
# '05:47:42'

print fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2018, 4, 29, 12, 49, 33)

print fake.date_time(tzinfo=None, end_datetime=None)
# datetime.datetime(1983, 9, 21, 18, 38, 41)

print fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2015, 9, 18, 12, 18, 5)

print fake.year()
# '2018'

print fake.century()
# 'XII'

print fake.date_between_dates(date_start=None, date_end=None)
# datetime.date(2018, 6, 11)

print fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
# <generator object time_series at 0x7f9d8e0f0af0>

print fake.date_object(end_datetime=None)
# datetime.date(1975, 5, 5)

print fake.unix_time(end_datetime=None)
# 1127938424

print fake.day_of_week()
# 'Sunday'

print fake.future_datetime(end_date="+30d", tzinfo=None)
# datetime.datetime(2018, 6, 16, 12, 18, 32)

print fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)
# datetime.datetime(2001, 6, 26, 6, 18, 17)

print fake.past_datetime(start_date="-30d", tzinfo=None)
# datetime.datetime(2018, 6, 6, 13, 34, 15)

print fake.future_date(end_date="+30d", tzinfo=None)
# datetime.date(2018, 6, 28)

print fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)
# datetime.datetime(2018, 6, 11, 14, 41, 1)

print fake.date_this_month(before_today=True, after_today=False)
# datetime.date(2018, 6, 1)

print fake.time_object(end_datetime=None)
# datetime.time(19, 45, 37)

print fake.date_between(start_date="-30y", end_date="today")
# datetime.date(2001, 3, 3)

print fake.date_time_ad(tzinfo=None, end_datetime=None)
# datetime.datetime(1242, 12, 11, 23, 48, 40)

print fake.date_this_decade(before_today=True, after_today=False)
# datetime.date(2011, 7, 2)

#for faker.providers.file

print fake.unix_partition(prefix=None)
# '/dev/vdh1'

print fake.file_name(category=None, extension=None)
# 'aliquam.mp3'

print fake.unix_device(prefix=None)
# '/dev/vdr'

print fake.file_path(depth=1, category=None, extension=None)
# '/harum/est.key'

print fake.file_extension(category=None)
# 'key'

print fake.mime_type(category=None)
# 'text/csv'

#for faker.providers.internet

print fake.ipv4(network=False, address_class=None, private=None)
# '32.188.150.144'

#print fake.free_email_domain(*args, **kwargs)
# 'hotmail.com'

#print fake.domain_name(*args, **kwargs)
# 'bray.com'

print fake.uri()
# 'http://www.stokes.com/main/wp-content/post.asp'

print fake.uri_path(deep=None)
# 'search/wp-content/blog'

print fake.uri_extension()
# '.php'

#print fake.ascii_company_email(*args, **kwargs)
# 'tmcdonald@owen.com'

print fake.url(schemes=None)
# 'https://scott.org/'

#print fake.ascii_safe_email(*args, **kwargs)
# 'thomascheryl@example.net'

print fake.ipv4_network_class()
# 'b'

#for fake.slug(*args, **kwargs)
# 'accusamus'

print fake.image_url(width=None, height=None)
# 'https://dummyimage.com/375x818'

#for fake.safe_email(*args, **kwargs)
# 'david86@example.org'

print fake.ipv6(network=False)
# '878:8c1a:29d7:dfcb:3c84:e6eb:c245:fecd'

#print fake.user_name(*args, **kwargs)
# 'donnasinclair'

print fake.tld()
# 'org'

#print fake.free_email(*args, **kwargs)
# 'eileenleach@hotmail.com'

print fake.ipv4_private(network=False, address_class=None)
# '172.25.54.185'

#print fake.domain_word(*args, **kwargs)
# 'wells'

#print fake.email(*args, **kwargs)
# 'davispatrick@hotmail.com'

#print fake.company_email(*args, **kwargs)
# 'bullmegan@mclean-nash.com'

#print fake.ascii_free_email(*args, **kwargs)
# 'norman57@gmail.com'

print fake.uri_page()
# 'index'

print fake.mac_address()
# '82:37:c4:bc:5b:58'

#print fake.ascii_email(*args, **kwargs)
# 'anthony49@connor.net'

print fake.ipv4_public(network=False, address_class=None)
# '209.164.70.141'

#for faker.providers.isbn

print fake.isbn13(separator="-")
# '978-0-8389-0421-3'

print fake.isbn10(separator="-")
# '0-588-44275-5'

#for faker.providers.job

print fake.job()
# 'Airline pilot'

#for faker.providers.lorem

print fake.word(ext_word_list=None)
# 'libero'

print fake.text(max_nb_chars=200, ext_word_list=None)
# ('Quos mollitia eos nulla. Dolorum hic fugiat autem accusantium earum ut.\n'
#  'Esse facere necessitatibus necessitatibus voluptate. Dolorem vel illum '
#  'assumenda.')

print fake.sentences(nb=3, ext_word_list=None)
# [   'Iusto dicta dignissimos laudantium accusantium ducimus.',
#     'Quidem quae earum sed.',
#     'Ut ea accusantium ea facere at.']

print fake.paragraphs(nb=3, ext_word_list=None)
# [   'Animi laboriosam dolorem dolore. Reiciendis dolores debitis ut blanditiis '
#     'in quam exercitationem.',
#     'Minus illum minima rem magni. Dolorem possimus natus provident.',
#     'Impedit consequuntur recusandae. Laboriosam iure ratione sequi deleniti '
#     'itaque animi provident. Ipsa magni vero nostrum quas.']

print fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
# 'Eos quidem consectetur ratione.'

print fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
# ('Error officia necessitatibus ducimus ut dolores omnis tenetur. In voluptatum '
#  'voluptas ipsa velit adipisci est. Cum repellendus ex optio.')

print fake.words(nb=3, ext_word_list=None)
# ['cumque', 'vitae', 'nihil']

#for faker.providers.misc

print fake.language_code()
# 'ht'

print fake.uuid4()
# '9354f85e-6cf7-dd8e-cb25-227765c7d8aa'

print fake.binary(length=1048576)
# (b'\xa7vS\x1b\xeeF\x98\xd3\x98W\x0e%\xc6?Q\x87|\x18\xb6\r:\xdeC\xaa\xd9-\xe8"'
#  b'\xa4\x83\xf2@\xfb\x19\xaf8M\xfb\xc8\xe5li\xfb\xf4\x9f\x11\xe3/\x0e\t\xb9\xb1'
#  b'\xd7\xb5m\xae\xaf\x998\x12]J\x01?V\xa9\xa4\x99C\xca\xf5\x19\xb3K\xd6J'
#  b'St\xff\x04z\xd4\xf5\x7f\xff\x07\x15\x8d\x827\x1d\xaa>C\\\xa0a\xc8\xe5\x89'
#  b'T\xa8\xe5\x9d{\xb7#\r>\xe6\xfa?\xc8\xd7\xb0\xe1S0\xac\xbe\x17\xe5\xebJ'
#  b'\x18\xd8\xa8\xb6-\xd9#M\n\x1a\xe1\xf6\xc9\xd3jG\xce2\xe5+y\xcfo\t'
#  b'0\xa5\xcf\x97e;\x15\xe2\x90+t\xc5\xc0\xa5\xd9\x11Qsd|M~\xe7\xf4\x0c\xf9\x94a'
#  b'\x08\xda\xf9\xc0\xa2\xa3\x8d\x06K\x1dp\xb8\x93\xd3\x975;\xdc)x\x9fTE5'
#  b'\x8c\xa8\xb9\xd7A\xd6\xcc\x02\xdb\xc3\xe7\xb45\xd8\xa2\x7fL\xc8<\xef'
#  b",-\x14\xc2\xa6lta\xfa\x01\x95\xbb\x92\x90\x08'\x0ej!\xa4\xb0\xaaa\xf7"
#  b'\xed\x90\xe3\xc3\rXE\xcf9\xc8\xe9Ch\xfe\xcf\xad\x8a\x15\x81\x80\x9aw\xabT'
#  b'0m1\xcb\x07\x97\x9f\x95\xad3\x9f\x11>\xae5N\xab\x85\x06\xc5\x90c<\x96'
#  b'\xf1\xca\x02\xb4\x9c\xe9\xb9k\x1b\x86\xc3\xae\xfd\x12\x07\xfd'
#  b"\x1c\xf7\xc3\xe4L\xf3#'wO\x15\xcb\xde\xb4\x1f*\x93p\x03f\xe1\xfd@\xfb"
#  b'9\xb7\x93\xdc\x87\xea?\x87<\x92\xb1\xb8\xe2cx)\xbb<\x08X}\xc6\x96\x0f'
#  b'\xdb\x9dJ\xd3E3\xc0\x94({s\x80&j8$q!\xba\xf8%\x82\x1d\x1d\xa9\xd1\xec\xf9'
#  b'\xd5$H\xa5,c\xceZq\x1c\x91/\xd8s\x0e\x14k\xbe\xd4r\xc9\xbfd{t\x99\xd44'
#  b'=\xed\x8dX\x11\xc0\xfa\xc0\x86\xe3>\xc6+\xd9\xf6)\x96\xe9\xde\x16'
#  b'\\\x08\xf6\xff\xdc\x9fS\x01\x8b\xae\x12\xc2\xb3\xc5\xe0\xcd-\x86W\xba'
#  b'Q\xb0X\xc3\x01\xf7M\xce5;\xf08\xe1\xd2X\xd1jp8p\x93|\xef\x9b)\xb8J='
#  b'\xd0\x0e\xf7\xc5k?NNz\x1a\\\xeb\xe9\xd5\xeb\xcf\xe8\xc7pw&\xc6\xcbE'
#  b'0\xf2\xa5\xc2k\xcb~$\x07:\x19\xca\xa5\x15\xad\x12C\r\xa3\xadH\xfc+\xbd'
#  b':\x96\xbah\xc4\xe1\xbfIQ\xf1\x1f9\xe0+\xdf\x04\xc7\xfd\xe2\x11'
#  b'\x05\xfe\xbe\x0b3\xbb{\x02\x08\x144S\xc5:`\n$g\xd1\xccT<\x85\nZ>\xb41'
#  b'\x81\xd4\xf4\xdb\xbd6E\xfd5\xbaP(\x86\xd6\xf8V\xfa\xb9&\xc6\x00\xa7\xcf\xc4'
#  b'\xc3\xb3.\x9fIJ\xabE\xea\xa5\xc4I\\\xab\xbcr\x1e\x99Scm\x16\x9b\n\xa2\xe8K1'
#  b'\xbed\x0fNX\x13a\xe4\xe1-\x9eoB\xbb\\\x97b~\x90\x1eg\xe3\x1e\x91'
#  b'\x8a\xfcj\xbd\xcc\x8b\x8bD\xfe\x93\x98\x0cP@P\x90\xccQ\xbdYH\x04`\xb8'
#  b'\x9e\xf9\r\x96\x03\x8b\x0b\\\xae\x0f\xa9C1O\xc04$\xa8\xf7\x117~\x06i'
#  b"\x90\x07\x87\x13\xcb\xaep\x8b\x9ek\x15Nn\t\x88#'x\xaa\xf7\x062V\xdb"
#  b'\x03K\xb1\xd4\xbbz\xdc\x95\x18\xb6\xe4\x9c\x04&g\x91\xcf;vzUa\xc1\x13'
#  b'\xab\x1c\x96\xd9\x11\x92\xd7\xba\x15\xb8\x93\xa4\x1dY\xf7dQ\x14\xf6\x89'
#  b'\x07>\xe5s=\x17\xadm\x0e\x0c\xac\xf1\xb3\x1d\x90\xc0\x94s\x9e\x9fmD\x12\xe3'
#  b'>2\x90=\x05m=|N\x1aB\xaewQ\xff\xc801\x16h\xbf\xf4\x03\xda\x1c\xa6g\xed'
#  b'1\xb6\xfb]a\x92\xa6\x8c\x161\xfa\xd6\xccx\x06i\xa3\x0bEV\xd3\xd0"\xf9'
#  b'I\x16\x06\xdb\xb6\x07\xd6\xeaZ\x18\x9d\xf2\xe3\xb10\xe9U\\?j\x830u/J\xc5BZ'
#  b'\xdd\x19\xc7P\xe3\xa8*>\xab\x9cz\xb1\xd96\xe5\xc6l\x18\xd5\x9c\x8bG\x00\x7f'
#  b'\x91,\xef\x10r\xe9Va\xab\x0c\xee\xefy\xee\xffw\x1fC\x14,\\R\xbb\x1d'
#  b"\xdc\x80\xffa\x06\x19^!x\x17U(\xa7\xbb\x1b'\xd8\x8d\xcd\xb4\x18\x81\xa70"
#  b'\xf1\xe0\xf6\xccw8\xa0\x0b\xcb\xa0l0\x94~o2\xf1\n?\xe9\x85\xb0\xf3-_b\xb3&'
#  b'\xcb\xa8\rv\xf02\r\x87\x93\xf7\x1aeQ3\xe6\x1e\xea9\xabsr\xa3/2\xa8\x0fX\t'
#  b'\xb4t1\xcf\xcb\xbb\x8c_\xaf\x81OW\x01)\xd2M\xc9\x8f\xa8\x86\xf0\x9fK\xb5')

print fake.boolean(chance_of_getting_true=50)
# False

print fake.null_boolean()
# None

print fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
# 'j3DN1Lhb)!'

print fake.md5(raw_output=False)
# '3475f1ae3544ce92b35643a6ff36c090'

print fake.locale()
# 'da_DK'

print fake.sha256(raw_output=False)
# 'eaff1652f257fb9bc79820c02b57264ceb10959a8bf3ca33e86cd79019d8359e'

print fake.sha1(raw_output=False)
# '8fa475528643616e2428cb412c941c52b10b3520'

#for faker.providers.person

print fake.first_name()
# 'Paul'

print fake.prefix_female()
# 'Dr.'

print fake.name()
# 'Mrs. Julia White'

print fake.name_male()
# 'Leah Ward'

print fake.last_name_male()
# 'Smith'

print fake.suffix_female()
# ''

print fake.suffix()
# ''

print fake.prefix()
# 'Miss'

print fake.prefix_male()
# 'Dr.'

print fake.last_name()
# 'Ross'

print fake.suffix_male()
# ''

print fake.first_name_male()
# 'Mohammad'

print fake.name_female()
# 'Terry Holloway'

print fake.first_name_female()
# 'Eileen'

print fake.last_name_female()
# 'Brooks'

#for faker.providers.phone_number

print fake.msisdn()
# '8685026419913'

print fake.phone_number()
# '+44(0)1514960559'

print fake.cellphone_number()
# '07700900744'

#for faker.providers.profile

print fake.profile(fields=None, sex=None)
# {   'address': 'Studio 8\nMaureen junction\nJunetown\nEH8A 7DS',
#     'birthdate': '1999-02-28',
#     'blood_group': 'B-',
#     'company': 'Williams-Scott',
#     'current_location': (Decimal('40.968151'), Decimal('-175.518615')),
#     'job': 'Multimedia specialist',
#     'mail': 'hopkinsmohammad@hotmail.com',
#     'name': 'Mrs. Teresa Thomas',
#     'residence': '3 Terence islands\nNorth Elizabeth\nLS2W 8RT',
#     'sex': 'M',
#     'ssn': 'ZZ 69 35 62 T',
#     'username': 'guygriffiths',
#     'website': [   'https://www.bell.com/',
#                    'http://lee-smith.info/',
#                    'http://www.smith.com/']}

print fake.simple_profile(sex=None)
# {   'address': '048 Stephen estates\nNew Dennisland\nM6 9RJ',
#     'birthdate': '1972-05-23',
#     'mail': 'naomi02@gmail.com',
#     'name': 'Damian Smith',
#     'sex': 'M',
#     'username': 'eking'}

#for faker.providers.python

#for fake.pylist(nb_elements=10, variable_nb_elements=True, *value_types)
# [   Decimal('-9.0'),
#     Decimal('753.4992644'),
#     'dorothyhall@yahoo.com',
#     2545,
#     'qTBatzSyEOHcbGqhrLjS',
#     'colinstephenson@gmail.com',
#     Decimal('422394334906.31'),
#     'KzKZElBxuBIqCcjLeDnF',
#     'https://www.russell.info/',
#     7046,
#     -704.409327901,
#     'JYzpBOpCyvlsPAkplgjA',
#     -41062723485150.0]

print fake.pybool()
# True

#print fake.pydict(nb_elements=10, variable_nb_elements=True, *value_types)
# {   'dolor': 4943,
#     'dolorum': Decimal('-457404461.53'),
#     'exercitationem': datetime.datetime(1978, 3, 17, 10, 42, 42),
#     'labore': 1322,
#     'temporibus': -96119044.0}

#print fake.pyset(nb_elements=10, variable_nb_elements=True, *value_types)
# {7744, 'eFdzbLSIzcehvJgYzrBx', 7718, 'bWPPyHHHvWTCJjLleYkl', 'FasvHOSGwLDKhtXyvmpU', -501.2574, 'swlTlupmpneUbMXuMrmt', 'MiaiHanQJAaIAcvnlRwZ', datetime.datetime(1979, 8, 15, 22, 25, 10), 'TyUehHHkjbsplQVXiaLv'}

#print fake.pyiterable(nb_elements=10, variable_nb_elements=True, *value_types)
# [   'YoGjhwxGjFFrgCjXWWYk',
#     'YMWGIFzBjhpDAknBIKtY',
#     'UKjcIsSSpBDyBmgZeAHN',
#     'http://allen.info/',
#     -8481.57723931,
#     'TzKSynIDgWMmPoMbYcff',
#     -7.29961478,
#     'http://mitchell-reid.com/tags/index.htm']

print fake.pyint()
# 5215

#print fake.pystruct(count=10, *value_types)
# (   [   datetime.datetime(1982, 10, 12, 9, 34, 6),
#         'VLgBbtFDewnQgWffuQOn',
#         8126,
#         'OseKwNvXtTbrfzqScgjI',
#         'flihFSFwIrXNtSHmnpOe',
#         'JxVjKEhcTjLJjSYRIxYY',
#         9870,
#         'TSeCXzhAExxnQvcDzWcX',
#         'jDvapNEKUqiFoNYRkTlk',
#         Decimal('7097070489933.1')],
#     {   'deleniti': 'PhWtifDadBYmOKHVcxOe',
#         'fugit': datetime.datetime(1995, 4, 1, 5, 13, 5),
#         'ipsum': -9918248127.11,
#         'magni': 963,
#         'molestiae': 5655.32438442443,
#         'nam': 'aIzuWVjJHgyFcPGRynlt',
#         'omnis': 'https://www.griffiths.com/faq.php',
#         'pariatur': 'yrqEkSBmwamraQGvikhw',
#         'reprehenderit': -470851194.482,
#         'tempore': 'DbRJBTpfYCsARXNaNPCM'},
#     {   'aperiam': {   0: 'robinsoneileen@yahoo.com',
#                        1: [   'https://www.watkins-price.com/category.php',
#                               Decimal('3.673'),
#                               'https://www.webster.net/main/'],
#                        2: {   0: 'kuXpdAKaXOylwLoaaKni',
#                               1: -33463752.0,
#                               2: ['UkQrvJzHiaeOGULqrjVm', 5439]}},
#         'dolorem': {   8: 'https://cox-collins.biz/home.php',
#                        9: [   'murphyolivia@yahoo.com',
#                               'gWKFFLNxeRQdGfDvSlVZ',
#                               Decimal('62167344116.0')],
#                        10: {   8: Decimal('97712764.6'),
#                                9: Decimal('-53260334.148596'),
#                                10: [7128, 58132.3]}},
#         'doloribus': {   1: 'fosterjoan@watson.org',
#                          2: [   'qXJhPZJQibDTQkQsRTSn',
#                                 'MVcHzuyPkqbQfXYGjZJh',
#                                 1.827633373845],
#                          3: {   1: 'rdVcUjQRodVpoMNxhDhf',
#                                 2: 'GBaTgrOzIqNoCfpSjkgE',
#                                 3: [   Decimal('-76081912.77747'),
#                                        'GMvufAmSXEmZHmJWBDrs']}},
#         'iusto': {   5: Decimal('-154136407.6902'),
#                      6: [   'ZEYcPJSfrRXlWhwJMzKS',
#                             Decimal('7360.4265731429'),
#                             datetime.datetime(2003, 12, 28, 20, 27, 49)],
#                      7: {   5: 'JXveOygCYBLCVINEgqVV',
#                             6: Decimal('-56813304.37275'),
#                             7: ['louis57@gmail.com', Decimal('-781589637.0')]}},
#         'magnam': {   6: 'http://ford.com/app/homepage/',
#                       7: [   -410.0,
#                              'nHhtzQQcruigmpppqDxl',
#                              'https://kelly.com/categories/homepage.php'],
#                       8: {   6: 'uCjWDqYDHcZqsynbXPDf',
#                              7: 'RbdXpzMlXEvTukagpKLp',
#                              8: [   'sdlJGcEvTMxjTSzCNvVI',
#                                     'ZGWeKXblCwIXaqsWUDvD']}},
#         'molestiae': {   9: datetime.datetime(1992, 4, 15, 18, 16, 7),
#                          10: [   'teresacox@ellis.com',
#                                  'jlCNSvfqeATEnVCRgYxL',
#                                  'SWHcxUmNztoEAZXTcvEV'],
#                          11: {   9: -9365889345.0,
#                                  10: Decimal('-165586.2845'),
#                                  11: [   -7612.485868065,
#                                          datetime.datetime(1989, 2, 2, 23, 44, 20)]}},
#         'officiis': {   4: 'FlqGQWVmlwXvevJFpaHV',
#                         5: [   1200,
#                                datetime.datetime(1975, 8, 18, 20, 36, 54),
#                                Decimal('6316594.2715')],
#                         6: {   4: datetime.datetime(2003, 12, 15, 15, 56, 58),
#                                5: 'rgivZeJNUbdcGEjUakho',
#                                6: [   'yLXisBtYaNZpJsadrptx',
#                                       'https://www.brooks-welch.net/']}},
#         'optio': {   2: 'http://chapman.com/posts/about/',
#                      3: [3361, datetime.datetime(1970, 11, 2, 6, 1, 22), 4704],
#                      4: {   2: 3621349.64699,
#                             3: 'https://www.allen-thomas.com/about/',
#                             4: ['kfmFANOYeUvcsMyjykut', 7001]}},
#         'pariatur': {   7: datetime.datetime(2016, 5, 14, 19, 34, 3),
#                         8: ['tony98@yahoo.com', 7688, 'emmaanderson@day.com'],
#                         9: {   7: 'jgjakjnRTfeajJCcwUqw',
#                                8: Decimal('3.402723'),
#                                9: [   datetime.datetime(1990, 7, 7, 11, 6, 43),
#                                       'YcmnqeVsVmWmCDYUXMwv']}},
#         'praesentium': {   3: 'phillipreeves@hotmail.com',
#                            4: [   Decimal('-7620328980504.0'),
#                                   6390,
#                                   Decimal('8164136.5592')],
#                            5: {   3: datetime.datetime(1989, 4, 15, 2, 12, 43),
#                                   4: 'http://cole.net/',
#                                   5: [4049, 'PaDCAujCxjwSeCfQjShJ']}}})

print fake.pydecimal(left_digits=None, right_digits=None, positive=False)
# Decimal('393098.4841')

print fake.pyfloat(left_digits=None, right_digits=None, positive=False)
# 4947993087601.62

#print fake.pytuple(nb_elements=10, variable_nb_elements=True, *value_types)
# (   'zPgRNQuExdjqiGNWiNNG',
#     'http://www.douglas.info/privacy/',
#     'klXiJhGbxImleLoYvZby',
#     Decimal('443.271078611872'),
#     'eCFbJWDSfjgmIaZEwxdo',
#     'RzeRknXLFrCFJnEuMhBE',
#     511)

print fake.pystr(min_chars=None, max_chars=20)
# 'hfBZATYPstScxCBlhnal'

# for faker.providers.ssn

print fake.ssn()
# 'ZZ 24 68 26 T'

#for faker.providers.user_agent

print fake.user_agent()
# 'Opera/8.29.(Windows NT 4.0; et-EE) Presto/2.9.169 Version/12.00'

print fake.windows_platform_token()
# 'Windows NT 5.0'

print fake.safari()
# ('Mozilla/5.0 (iPod; U; CPU iPhone OS 4_2 like Mac OS X; apn-IN) '
#  'AppleWebKit/534.10.5 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 '
#  'Safari/6534.10.5')

print fake.firefox()
# ('Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_4; rv:1.9.6.20) '
#  'Gecko/2015-04-08 01:54:15 Firefox/3.8')

print fake.mac_processor()
# 'PPC'

print fake.linux_processor()
# 'x86_64'

print fake.opera()
# 'Opera/8.91.(Windows NT 5.1; dv-MV) Presto/2.9.184 Version/11.00'

print fake.mac_platform_token()
# 'Macintosh; U; PPC Mac OS X 10_11_8'

print fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)
# ('Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_6) AppleWebKit/5332 (KHTML, like '
#  'Gecko) Chrome/43.0.858.0 Safari/5332')

print fake.internet_explorer()
# 'Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.2; Trident/3.0)'

print fake.linux_platform_token()
# 'X11; Linux i686'    
