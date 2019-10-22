from selenium import webdriver

browser = webdriver.Firefox()

# Edith has head about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures).

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item on a to-do list.

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (She is very methodical).

# The page updates again, and now both items are shown on her list.

# Edith wonders if the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits the URL - her to-do list is still there.

# Satisfied, she goes back to sleep.

browser.quit()