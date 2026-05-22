from pathlib import Path

import pytest
import allure
from playwright.sync_api import sync_playwright

BASE_URL = (Path(__file__).parent / "app" / "login.html").resolve().as_uri()

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screenshot_path = screenshot_dir / f"{request.node.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)

            allure.attach.file(
                str(screenshot_path),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        context.close()
        browser.close()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_"+ report.when, report)
