# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/cases_3.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseCases3(HttpRunner):

    config = Config("Entry Task 'HTTP module API' test cases").base_url(
        "http://127.0.0.1:5000"
    )

    teststeps = [
        Step(
            RunRequest("Negative case：POST request")
            .post("/shopee/test")
            .with_params(**{"a": 1, "b": "nihao"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 11)
            .assert_equal("body.error_message", "system error")
            .assert_equal("body.reference", "System Error")
        ),
        Step(
            RunRequest("Positive case：parameter 'b' is JS code snippet")
            .get("/shopee/test")
            .with_params(**{"a": 1, "b": "</h1><script>alert('xss');</script></h1>"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 0)
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "success")
        ),
        Step(
            RunRequest("Positive case：parameter 'b' is html code snippet")
            .get("/shopee/test")
            .with_params(**{"a": 1, "b": "alert('warning');"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 0)
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "success")
        ),
        Step(
            RunRequest("Positive case：extra parameter")
            .get("/shopee/test")
            .with_params(**{"a": 1, "b": "nihao", "c": "extra"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 0)
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "success")
        ),
        Step(
            RunRequest("Negative case：wrong parameter name")
            .get("/shopee/test")
            .with_params(**{"a_wrong": 1, "b": "nihao"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 21)
            .assert_equal("body.error_message", "empty or wrong params")
            .assert_equal("body.reference", "Parameters Missing a")
        ),
        Step(
            RunRequest("Negative case：parameter 'a' includes '/'")
            .get("/shopee/test")
            .with_params(**{"a": "1/", "b": "nihao"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 21)
            .assert_equal("body.error_message", "empty or wrong params")
            .assert_equal(
                "body.reference", "Parameter Illegal Parameter 'a' needs to be int type"
            )
        ),
        Step(
            RunRequest("Positive case：parameter 'b' contains '\n'")
            .get("/shopee/test")
            .with_params(**{"a": 1, "b": "nihao\n"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.error_code", 0)
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseCases3().test_start()
