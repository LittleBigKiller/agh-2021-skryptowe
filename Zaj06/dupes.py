import sys
import re

print(*list(map(lambda x: list(x.group()), re.finditer(r'(.)\1*', "".join("".join(list(map(lambda x: x.rstrip(), sys.argv[1:]))).split(","))))))

