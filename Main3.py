class Kenya:
    def capital(self):
        print("Capital: Nairobi.")
    def language(self):
        print("Official Language: Swahili and English.")
    def country_type(self):
        print("Type: Developing Country")
class Japan:
    def capital(self):
        print("Capital: Tokyo.")
    def language(self):
        print("Official Language: Japanese.")
    def country_type(self):
        print("Type: Developed Country")
def show_country_info(country):
    country.capital()
    country.language()
    country.country_type()
# Driver code
k = Kenya()
j = Japan()
print("Kenya Info:")
show_country_info(k)
print("\nJapan Info:")
show_country_info(j)
