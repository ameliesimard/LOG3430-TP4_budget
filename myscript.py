import os
os.system("git bisect start 7b9bb2055ec37243ccf6955561842283daac2969 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
os.system("git bisect run python manage.py test")
