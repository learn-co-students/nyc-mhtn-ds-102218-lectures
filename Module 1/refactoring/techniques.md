1. How would we apply this to the real world
2. Break that into steps, and write out the comments
3. Lean on preprocessing
  a. rejection - remove the information
  b. coercion -
4. turn the variable names into methods
A. Code smells
  1. Getting rid of for loops
  titles = []
  for item in items:
    titles.append(item['title'])

  2. tu
  list(map(lambda item: item['title'],items))
