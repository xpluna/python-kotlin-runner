import os

try:
	from colorama import init, Fore, Style

except ModuleNotFoundError:
	os.system("pip install colorama")
	from colorama import init, Fore, Style
	print("\n\nInstalled the missing module - colorama\n\n")

init()

for i in (l:=[f for f in os.listdir() if f.endswith(".kt")]):
	print(Fore.MAGENTA + Style.BRIGHT + f"[{l.index(i)+1}] {i}" + Fore.RED)

m=l[int(input("\n>>> "))-1]
j=m[:-1]+".jar"

print(Fore.CYAN + f'\n{"="*35} OUTPUT {"="*35}\n' + Fore.GREEN)

os.system(f'cd "{os.getcwd()}" && kotlinc {m} -include-runtime -d {j} && java -jar {j}')

print(Fore.CYAN + f'\n{"="*35} EXEC\'D {"="*35}\n' + Fore.GREEN)
input()
