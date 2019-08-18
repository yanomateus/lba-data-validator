
def authors_view(request):
    contributors = [{"name": "Mateus",
                    "last_name": "Yano",
                    "age": 26,
                    "occupation": "Developer"},
                    {"name": "Rodolpho",
                    "last_name": "Santos",
                    "age": 26,
                    "occupation": "Date Scientist"},
                    {"name": "Moises",
                     "last_name": "Oliveira",
                     "age": 32,
                    "occupation": "Date Analyst"}]
    return contributors