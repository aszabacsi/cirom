browser_history = []

def visit_url(url):
  print(f"Visiting: {url}")
  browser_history.append(url)
  print(f"Current history: {browser_history}")

def back():
  print("Going back")
  if browser_history:
    browser_history.pop()
  print(f"Current history: {browser_history}")


visit_url("https://example.com")
visit_url("https://openai.com")
back()
