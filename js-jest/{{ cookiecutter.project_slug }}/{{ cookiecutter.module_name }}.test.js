const sum = require('./{{ cookiecutter.module_name }}');


test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
