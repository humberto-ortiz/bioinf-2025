def PatternCount(text, pattern):
  count = 0
  for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
      count = count + 1
  return count

def FrequentWords(text, k):
  FrequentPatterns = set()
  count = [0] * (len(text)-k+1)
  for i in range(len(text) - k + 1):
    Pattern = text[i:i+k]
    count[i] = PatternCount(text, Pattern)
  print(count)
  maxCount = max(count) 
  for i in range(len(text) - k):
    if count[i] == maxCount:
       FrequentPatterns.add(text[i:i+k])
  return FrequentPatterns 

def FrequencyTable(Text, k):
  freqMap = {}
  n = len(Text)
  for i in range(n-k+1):
    Pattern = Text[i:i+k]
    if Pattern not in freqMap:
      freqMap[Pattern] = 1
    else:
      freqMap[Pattern] += 1

  return freqMap

def BetterFrequentWords(Text, k):
  FrequentPatterns = []
  freqMap = FrequencyTable(Text, k)
  maxValue = max(freqMap.values())
  for Pattern in freqMap.keys():
    if maxValue is freqMap[Pattern]:
      FrequentPatterns.append(Pattern)

  return FrequentPatterns
