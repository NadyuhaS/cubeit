from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/113-index.html"

def test_cube(page:Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    input_field.fill("5")

    btn = page.get_by_role("button", name="Cube")
    btn.click()

    result_field = page.locator("css=p#result")
    expect(result_field).to_contain_text(f"{5 ** 3}")

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    input_field.fill("")

    btn = page.get_by_role("button", name="Cube")
    btn.click()

    result_field = page.locator("css=p#result")
    expect(result_field).to_contain_text(f"Enter something!")
