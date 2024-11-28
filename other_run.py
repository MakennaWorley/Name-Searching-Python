import os

os.system("python other.py -algorithm BruteForce -name Mexican -length 5")
os.system("python other.py -algorithm BruteForce -name Mexican -length 8")
os.system("python other.py -algorithm BruteForce -name Chinese -length 5")
os.system("python other.py -algorithm BruteForce -name Arabic -length 7")
os.system("python other.py -algorithm BruteForce -name Arabic -length 8")

print()

os.system("python other.py -algorithm Horspool -name Mexican -length 5")
os.system("python other.py -algorithm Horspool -name Mexican -length 8")
os.system("python other.py -algorithm Horspool -name Chinese -length 5")
os.system("python other.py -algorithm Horspool -name Arabic -length 7")
os.system("python other.py -algorithm Horspool -name Arabic -length 8")