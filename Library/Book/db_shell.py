
###### ORM Queries #####


'''

from Book.models import Book

# to run python file into db_shell - copy-paste below command ;
# exec(open('C:\\Django_ Practice\\Library\\Book\\db_shell.py').read())


# all data(read);
b = Book.objects.all()
print(b)
print("--" * 50)

# single data(read);
sid = 1
b2 = Book.objects.get(id=sid)
print(b2)
print("--" * 50)


# create data;
b3 = Book.objects.create(name="Oracle", author="Gandhi", qty=2, price=150)
print(b3)
print("--" * 50)


# update data;
sid = 4
b4 = Book.objects.get(id=sid)
b4.name = "LAMP"
b4.author = "Zen"
b4.qty = 75
b4.save()
print("--" * 50)


# # delete data;
# sid = 5
# b5 = Book.objects.get(sid)
# b5.delete()


all_data = Book.objects.all()   # len(all_data)
print(all_data)


'''

#------------------------------------------------------------------------------------------------------------------------------------------

# Django_ORM CookBook queries;

# exec(open('C:\\Django_ Practice\\Library\\Book\\db_shell.py').read())

# from Book.models import Book

'''

# 1. filter()

books = Book.objects.filter(id__lt=2).values("id", "name")       # __gte = greater than equal to &  __lte = less than equal to
# for i in books:
#     print(i)

print(books)



# 2. order_by()

# books = Book.objects.all().order_by("name")
# print(books)


# b1 = Book.objects.all().count()     # len or count functions can provide us total data in database
# print(b1)


# b1 = Book.objects.all()[5]      # indexing for fetching particular id/data
# print(b1)


#--------------------------------------------------------------------------------------

# 3. bulk_create()

# bulk_create into database;

b1 = Book.objects.bulk_create([Book(name="Java", author="G yfalskjf", qty=17, price=784),
Book(name="Java",  author="G yfalskjf", qty=17, price=784),                          
Book(name="Java1", author="B yfalskjf", qty=5, price=333),
Book(name="Java2", author="C yfalskjf", qty=10, price=550),
Book(name="Java3", author="D yfalskjf", qty=1, price=700),
Book(name="Java4", author="E yfalskjf", qty=20, price=1000),
Book(name="Java5", author="F yfalskjf", qty=30, price=450),
])

print(b1)


'''


#------------------------------------------------------------------------------------------------------------------------------------------



























