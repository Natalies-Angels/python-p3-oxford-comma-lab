def oxford_comma(items):
   if len(items) == 1:
      return items[0]
   elif len(items) == 2:
      return ' and '.join(items)
   else:
        comma_separated = ", ".join(items[:-1])
        return f"{comma_separated}, and {items[-1]}"

    
print(oxford_comma(["Matcha", "Bobba", "Latte"]))