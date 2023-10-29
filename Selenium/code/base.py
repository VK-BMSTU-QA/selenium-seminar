import pytest
from _pytest.fixtures import FixtureRequest

CLICK_RETRY = 3


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        if self.authorize:
            cookies = request.getfixturevalue('cookies')

            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()

        self.logger.debug('Initial setup completed')
