###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20

for tasks_ok in [20, 11, 10, 9, 0]:
    test_passed = False

    if tasks_ok >= total_tasks * 0.5:
        test_passed = True

    if test_passed:
        print(f'Congratulations! You passed the test with {tasks_ok} correct tasks.')
    else:
        print(f'Unfortunately, you failed the test with {tasks_ok} correct tasks.')
