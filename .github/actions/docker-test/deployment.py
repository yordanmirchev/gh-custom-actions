import os
def run():
    user_input = os.environ['INPUT_USER-INPUT']
    # user_input = "foo"

    # As a next step we can save this as an output.
    # print(os.environ)

    result = "in: " + user_input + "\nenv: " + str(os.environ.values())

    # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'action_result={result}', file=gh_output)

    print(f'result is: \n{result}')

if __name__ == '__main__':
    run()
