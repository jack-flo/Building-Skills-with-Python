# Check amount writing (digits to full sentences of the same number 100 -> one hundred)

oneToTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tensWords = ["twenty", "thirty", "foury", "fifty",
             "sixty", "seventy", "eighty", "ninety"]
scaleWords = ["", "thousand", "million", "billion", "trillion"]


chunkResult = ""
resultChunks = []
chunkIndex = 0
number = 180920

while number > 0:
    chunkResult = ""
    digits = number % 1000  # Last three digits of the number
    number //= 1000
    # Get the hundreds
    hundred = digits // 100
    if hundred > 0:
        chunkResult += f"{oneToTwenty[hundred]} hundred and "
    # Get the 10s
    teens = digits % 100
    tensDigit = teens // 10
    onesDigit = teens % 10
    if teens > 0:
        if teens <= 19:
            chunkResult += f"{oneToTwenty[teens]}"
        else:
            chunkResult += f"{tensWords[tensDigit - 2]} {oneToTwenty[onesDigit]}"
    if chunkResult.strip() != "":
        chunkResult += f" {scaleWords[chunkIndex]}"
        resultChunks.append(chunkResult.strip())
    chunkIndex += 1

# Reverse the list then turn it into a string using "".join
result = " ".join(reversed(resultChunks))
# Get rid of any double spaces
result = " ".join(result.split())
print(result)
