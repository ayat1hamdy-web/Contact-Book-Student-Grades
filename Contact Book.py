# -----------------------------
# Task 1: Contact Book
# -----------------------------

# 1. إنشاء قاموس جهات الاتصال
contacts = {
    "Ahmed": "01012345678",
    "Sara": "01198765432",
    "Mona": "0125556677"
}

# 2. طباعة كل الأسماء الموجودة
print("All contacts:")
for name in contacts.keys():
    print(name)

print("\n-----------------------")

# 3. البحث عن جهة اتصال
search_name = input("Enter the name you want to search for: ")

# التحقق من وجود الاسم في القاموس
if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("This name is not found in the contact book.")
